#include "Eigen/Eigen"
#include <iostream>
#include <iomanip>

#define M_PI 3.1415926
#define M_PI_3 (M_PI / 3.0)
#define M_PI_6 (M_PI / 6.0)

using pencil_t = struct {
    Eigen::Vector3d pos; // position
    Eigen::Quaterniond orientation; // orientation in quaternion
    Eigen::Vector3d vel; // velocity
    Eigen::Vector3d omega; // angular velocity
    Eigen::Matrix3d inertia; // principal inertia
};

Eigen::Vector3d rotate(
    Eigen::Vector3d p,
    Eigen::Quaterniond quat) {
    // convert a 3D vector to a quaternion
    Eigen::Quaterniond p_quat;
    p_quat.w() = 0.0;
    p_quat.vec() = p;
    quat.normalize();
    Eigen::Quaterniond rotated_p_quat = quat * p_quat * quat.inverse();
    Eigen::Vector3d rotated_p = rotated_p_quat.vec();
    return rotated_p;
}

void tumble(
    const pencil_t& init,
    const double T,
    const size_t iteration,
    const double output_step,
    std::vector<pencil_t>& results)
    {
        double t = 0.0;
        const double dt = abs(T) / iteration;
        const size_t output_index_step = output_step / dt;
        const Eigen::Vector3d g = { 0.0, 0.0, -9.8 };
        Eigen::Vector3d omega_body = init.omega;
        Eigen::Matrix3d Q = init.inertia;
        Eigen::Quaterniond q_body_to_world = init.orientation;
        Eigen::Vector3d vel, pos;
        for (size_t i = 0; i < iteration + 1; i++) {
        const Eigen::Vector3d omega_world = rotate(omega_body, q_body_to_world);
        const Eigen::Vector3d rotate_axis_world = omega_world / omega_world.norm();
        const double d_angle = (T > 0) ?
        omega_world.norm() * dt :
        -omega_world.norm() * dt;
        Eigen::Quaterniond q_inc;
        q_inc.w() = cos(d_angle / 2.0);
        q_inc.vec() = sin(d_angle / 2.0) * rotate_axis_world;
        q_body_to_world = q_inc * q_body_to_world;
        if (T > 0) {
            vel = init.vel + g * dt * i;
            omega_body -= dt * (Q.inverse() * omega_body.cross(Q * omega_body));
            t = i * dt;
        } else {
            vel = init.vel - g * dt * i;
            omega_body += dt * (Q.inverse() * omega_body.cross(Q * omega_body));
            t = -(i * dt);
        }
        pos = init.pos + init.vel * t + 0.5 * g * t * t;
        if (i % output_index_step == 0) {
            pencil_t state;
            state.pos = pos;
            state.vel = vel;
            state.omega = omega_body;
            results.push_back(state);
        }
    }
}

int main(int argc, char const *argv[])
{
    const double m = 1.0; // pencil mass
    const double r = 0.5; // pencil radius
    const double h1 = 3.0; // height of cone
    const double h2 = 0.5; // height of cylinder
    const double h = // mass center, distance(o2->op)
    (6.0*h1*h1 + 12.0*h1*h2 + 3.0*h2*h2) / (12.0*h1 + 4.0*h2);
    const double l = h1 / 2 + h2 - h; // distance(op->o1)
    Eigen::Matrix3d Q; // principal inertia
    const double Q11 =
        m / (h1 + h2 / 3.0) * (h1 * ((3.0*r*r + h1*h1) / 12 + l*l)
        + h2 * (0.2 * (r*r / 4.0 + h2*h2) + h*h / 3.0));
    const double Q22 = Q11;
    const double Q33 = 93.0*m*r*r / 190.0;
    std::cout << Q11 << std::endl;
    std::cout << Q33 << std::endl;
    Q << Q11, 0.0, 0.0,
        0.0, Q22, 0.0,
        0.0, 0.0, Q33;
    Eigen::Quaterniond q_body_to_world;
    const Eigen::Vector3d u = { 0.0, 1.0, 0.0 };
    const double theta = M_PI_6;
    q_body_to_world.w() = cos(theta / 2.0);
    q_body_to_world.vec() = sin(theta / 2.0) * u;
    std::vector<pencil_t> results;

    // simulation phase 1 (before impact)
    pencil_t state_before_impact;
    state_before_impact.inertia = Q;
    state_before_impact.orientation = q_body_to_world;
    state_before_impact.pos = { h*cos(M_PI_3), 0.0, h*sin(M_PI_3) };
    state_before_impact.vel = { -5.0*cos(M_PI_6), 0.0, -5.0*sin(M_PI_6) };
    state_before_impact.omega = { 1.0, 5.0, 0.5 };
    tumble(state_before_impact, -0.4, 40000, 0.1, results);
    std::reverse(results.begin(), results.end());
    // simulation phase 2 (after impact)

    pencil_t state_after_impact;
    state_after_impact.inertia = Q;
    state_after_impact.orientation = q_body_to_world;
    state_after_impact.pos = { h*cos(M_PI_3), 0.0, h*sin(M_PI_3) };
    state_after_impact.vel = { -1.80954, -0.546988, 1.2076 };
    state_after_impact.omega = { 0.09957, -0.04174, 0.5 };
    tumble(state_after_impact, +0.4, 40000, 0.1, results);
    std::cout << std::setprecision(4) << std::fixed << std::showpos;
    const Eigen::IOFormat cleanfmt(Eigen::StreamPrecision, 0, ", ", "\n", "[", "]");
    const std::vector<std::string> labels =
            { "0.0", "0.1", "0.2", "0.3", "0.4-", "0.4+", "0.5", "0.6", "0.7", "0.8" };
    auto label = labels.cbegin();
    std::cout << "t\t\tvelocity\t\t\tomega\t\t\t\tposition\n";
    for (auto& result : results)
    {
        std::cout << (*label++) << " \t" <<
        result.vel.transpose().format(cleanfmt) << "\t" <<
        result.omega.transpose().format(cleanfmt) << "\t" <<
        result.pos.transpose().format(cleanfmt) << "\n";
    }
    return 0;
}
