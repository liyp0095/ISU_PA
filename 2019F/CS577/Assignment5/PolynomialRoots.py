#!/bin/python
#-*- coding: utf8 -*-

import math

def cbrt(x):
    if x == 0:
        return 0
    return x/abs(x) * (abs(x) ** (1./ 3.))

def cubics(*args):
    if len(args) == 4:
        a3 = args[0]
        a2 = args[1]
        a1 = args[2]
        a0 = args[3]
        p = float(a2) / a3
        q = float(a1) / a3
        r = float(a0) / a3
        a = 1/3 * (3*q - p**2)
        b = 1/27 * (2*p**3 - 9*p*q + 27*r)
        CapitalA = cbrt((-b/2 + (b**2/4 + a**3/27)**(1./2)))
        CapitalB = cbrt((-b/2 - (b**2/4 + a**3/27)**(1./2)))
    elif len(args) == 3:
        p = args[0]
        q = args[1]
        r = args[2]
        a = 1/3 * (3*q - p**2)
        b = 1/27 * (2*p**3 - 9*p*q + 27*r)
        CapitalA = cbrt((-b/2 + (b**2/4 + a**3/27)**(1./2)))
        CapitalB = cbrt((-b/2 - (b**2/4 + a**3/27)**(1./2)))
    elif len(args) == 2:
        p = q = 0
        a = args[0]
        b = args[1]
        CapitalA = cbrt((-b/2 + (b**2/4 + a**3/27)**(1./2)))
        CapitalB = cbrt((-b/2 - (b**2/4 + a**3/27)**(1./2)))
    else:
        print("error")

    # print(p, q, r)
    # print(a, b)
    # print(CapitalA)
    # print(CapitalB)
    print("p = ", p)
    print("q = ", q)
    print("r = ", r)
    print("a = ", r)
    print("b = ", r)
    print("CapitalA = ", CapitalA)
    print("CapitalB = ", CapitalB)
    y1 = CapitalA + CapitalB
    y2 = complex(-1/2*(CapitalA + CapitalB), 3**(1/2)/2 * (CapitalA - CapitalB))
    y3 = complex(-1/2*(CapitalA + CapitalB), -3**(1/2)/2 * (CapitalA - CapitalB))

    return y1 - p/3, y2 - p/3, y3 - p/3


def quartics(*args):
    if len(args) == 5:
        a4 = args[0]
        a3 = args[1]
        a2 = args[2]
        a1 = args[3]
        a0 = args[4]
        p = float(a3) / a4
        q = float(a2) / a4
        r = float(a1) / a4
        s = float(a0) / a4
        # a = 1/3 * (3*q - p**2)
        # b = 1/27 * (2*p**3 - 9*p*q + 27*r)
        # CapitalA = cbrt((-b/2 + (b**2/4 + a**3/27)**(1./2)))
        # CapitalB = cbrt((-b/2 - (b**2/4 + a**3/27)**(1./2)))
    elif len(args) == 4:
        p = args[0]
        q = args[1]
        r = args[2]
        s = args[3]
        # a = 1/3 * (3*q - p**2)
        # b = 1/27 * (2*p**3 - 9*p*q + 27*r)
        # CapitalA = cbrt((-b/2 + (b**2/4 + a**3/27)**(1./2)))
        # CapitalB = cbrt((-b/2 - (b**2/4 + a**3/27)**(1./2)))
    else:
        print("error")
    a = q - 3*p**2/8
    b = r + p**3/8 - p*q/2
    c = s - 3*p**4/256 + p**2*q/16 - p*r/4

    # real root of resolvent cubic
    rr = cubics(-q, p*r - 4*s, 4*q*s - r**2 - p**2*s)[0]

    R = (1/4*p**2 - q + rr)**(1./2)
    if R == 0:
        D = (3/4*p**2 - 2*q + 2*(rr**2 - 4*s)**(1./2))**(1./2)
        E = (3/4*p**2 - 2*q - 2*(rr**2 - 4*s)**(1./2))**(1./2)
    else:
        D = (3/4*p**2 - R**2 - 2*q + 1/4*(4*p*q - 8*r - p**3)/R)**(1./2)
        E = (3/4*p**2 - R**2 - 2*q - 1/4*(4*p*q - 8*r - p**3)/R)**(1./2)

    x1 = -p/4 + 1/2 * (R + D)
    x2 = -p/4 + 1/2 * (R - D)
    x3 = -p/4 - 1/2 * (R - E)
    x4 = -p/4 - 1/2 * (R + E)

    return x1, x2, x3, x4


def main():
    # a, b, c, d = 110, -23, 87, 4
    # print(a, b, c, d)
    # print(cubics(110, -23, 87, 4))
    print(cubics(1, 1, 1, 1))
    # print(cubics(1, 0, 0, 8))
    # print(quartics(43, 1.34, -7, 0, -3400))


if __name__ == '__main__':
    main()
