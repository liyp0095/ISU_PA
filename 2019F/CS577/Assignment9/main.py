#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Use steepest descent and ascent to find the minima and maxima of
            f(x1, x2) = x1^3/3 + x2^2*x1 - 3*x1
Auther: Yuepei Li
Date: 2019-11-12
'''

accuracy = 10 ** (-6)
decimal_accuracy = 4

def getT(x1, x2):
    "return t1, t2 that make gradient of t equal 0"
    f_x1 = x1**2 + x2**2 - 3
    f_x2 = 2*x1*x2
    a = 3*(-f_x2**2*f_x1 - (1/3.0)*f_x1**3)
    b = 2*(f_x1**2*x1 + f_x2**2*x1 + 4*x1*x2**2*f_x1)
    c = -f_x1 * x1**2 - f_x2**2 - x2**2 * f_x1 + 3*f_x1
    # print(a, b, c)
    delta = b**2 - 4*a*c
    t1 = (-b + delta ** (1/2.0)) / 2 / a
    t2 = (-b - delta ** (1/2.0)) / 2 / a

    return (t1, t2)


def f(x1, x2):
    "function f"
    return x1**3/3.0 + x2**2 * x1 - 3*x1


def fd(x1, x2):
    "gradient of function f"
    return (x1**2 + x2**2 - 3, 2*x1*x2)


def findExtremum(x1, x2, s = 1):
    "steepest gradient method"
    d = 1
    fv = f(x1, x2)
    steps = []
    while abs(d) > accuracy:
        details = {}
        t = getT(x1, x2)
        gradient = fd(x1, x2)
        # print(gradient)
        if s == 1:
            "minima"
            x1 -= t[0] * gradient[0]
            x2 -= t[0] * gradient[1]
            details["t"] = t[0]
        else:
            "maxima"
            x1 -= t[1] * gradient[0]
            x2 -= t[1] * gradient[1]
            details["t"] = t[1]
        d = fv - f(x1, x2)
        fv = f(x1, x2)
        details["accuracy"] = d
        details["f_value"] = fv
        details["position"] = (x1, x2)
        steps.append(details)

    return steps


def show_steps(steps):
    for i, s in enumerate(steps):
        print(str(i+1) + " th iteration: ")
        print(" * t: " + str(round(s["t"], decimal_accuracy)))
        print(" * position: (%s, %s)" % (str(round(s["position"][0], decimal_accuracy)), str(round(s["position"][1], decimal_accuracy))))
        print(" * f_value: " + str(round(s["f_value"], decimal_accuracy)))
        print(" * accuracy: " + str(round(s["accuracy"], decimal_accuracy)))


def main():
    x1, x2 = 1, 1
    print("================= minima ==================")
    print("starts at (%f, %f)" % (x1, x2))
    steps_min = findExtremum(x1, x2, s = 1)
    show_steps(steps_min)
    print("================= maxima ==================")
    print("starts at (%f, %f)" % (x1, x2))
    steps_max = findExtremum(x1, x2, s = -1)
    show_steps(steps_max)
    # print(getT(1,1))
    # pass()


if __name__ == "__main__":
    main()
