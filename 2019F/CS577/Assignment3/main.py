#!/bin/python
#-*- coding: utf8 -*-

import math
import numpy as np

from quaternion import Quaternion
from vector import Vector3

output_dict = {}

def tumble(p, q, v, omega, T, Q):
    g = Vector3(0, 0, -9.8)
    t = 0
    if T > 0:
        dt = 0.00001
    else:
        dt = -0.00001
    output_dict = {}
    while abs(t) <= abs(T):
        cap_omega = q._act(omega)
        # print(cap_omega.length())
        unit_cap_omega = cap_omega / cap_omega.length()
        # print(unit_cap_omega)
        dphi = cap_omega.length() * dt
        # print(dphi)
        r = Quaternion(math.cos(dphi/2), math.sin(dphi/2)*unit_cap_omega)
        # print(q)
        q = r * q
        # print(q)
        # print(omega.length())
        v = v + g*dt
        omega = omega + Vector3(dt*(np.linalg.inv(Q).dot(omega.cross(Vector3(
                    Q.dot(omega.to_column()))).to_column())))
        t = t + dt
        p = p + v*dt + 0.5*g*(dt**2)
        # print(omega.length())
        # print(p)
        if (abs(t)/abs(dt)) % (0.1/abs(dt)) < 1:
            print(output_dict)
            output_dict[round(t, 1) + 0.4] = (p, v, omega)
        # break

def main():
    # input
    m = 1
    r = 0.5
    h1 = 3
    h2 = 0.5
    t1 = 0.4
    t2 = 0.8

    h = (6*h1**2 + 12*h1*h2 + 3*h2**2) / (12*h1 + 4*h2)
    # print(h)
    l = h1/2 + h2 - h
    v1 = r**2 * h1
    v2 = 1/3 * r**2 * h2
    m1 = v1 / (v1 + v2) * m
    m2 = v2 / (v1 + v2) * m
    # print(m1, m2)

    p1 = h * Vector3(math.cos(math.pi/3), 0, math.sin(math.pi/3))
    v1_neg = -5 * Vector3(math.cos(math.pi/6), 0, math.sin(math.pi/6))
    w1_neg = Vector3(1.0, 5, 0.5)
    v1_pos = Vector3(-1.80954, -0.546988, 1.2076)
    w1_pos = Vector3(0.09957, -0.04174, 0.5)
    q1 = Quaternion(math.cos(math.pi/12), math.sin(math.pi/12)*Vector3(0,1,0))

    Q11 = m / (h1 + h2/3) * (h1*((3*r**2 + h**2)/12+l**2) +
            h2/3*(3/5*(r**2/4 + h2**2) + h**2))
    Q22 = Q11
    Q33 = (1/2*m1 + 3/10*m2)*r**2

    Q = np.array([[Q11,0,0], [0,Q22,0], [0,0,Q33]])
    # print(np.linalg.inv(Q))
    # return 0

    # simulation
    tumble(p1, q1, v1_neg, w1_neg, -t1, Q)
    tumble(p1, q1, v1_pos, w1_pos, t2-t1, Q)

    # output
    for (key, item) in sorted(output_dict.items(), key=lambda x:x[0]):
        print(key, item)


if __name__ == "__main__":
    main()
