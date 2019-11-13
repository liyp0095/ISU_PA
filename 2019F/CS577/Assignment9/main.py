#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Use steepest descent and ascent to find the minima and maxima of
            f(x1, x2) = x1^3/3 + x2^2*x1 - 3*x1
Auther: Yuepei Li
Date: 2019-11-12
'''

accuracy = 10 ** (-6)

def getT(x1, x2):
    f_x1 = x1**2 + x2**2 - 3
    f_x2 = 2*x1*x2
    a = 3*(-f_x2**2*f_x1 - (1/3.0)*f_x1**3)
    b = 2*(f_x1**2*x1 + f_x2**2*x1 + 4*x1*x2**2*f_x1)
    c = -f_x1 * x1**2 - f_x2**2 - x2**2 * f_x1 + 3*f_x1

    delta = b**2 - 4*a*c
    t1 = (-b + delta ** (1/2.0)) / 2 / a
    t2 = (-b - delta ** (1/2.0)) / 2 / a

    return (t1, t2)


def f(x1, x2):
    return x1**3/3.0 + x2**2 * x1 - 3*x1


def fd(x1, x2):
    return (x1**2 + x2**2 - 3, 2*x1*x2)


def findExtremum(x1, x2, s = 1):
    d = 1
    fv = f(x1, x2)
    while abs(d) > accuracy:
        t = getT(x1, x2)
        print(x1, x2)
        print(t)
        gradient = fd(x1, x2)
        if s == 1:
            x1 -= t[0] * gradient[0]
            x2 -= t[0] * gradient[1]
        else:
            x1 -= t[1] * gradient[0]
            x2 -= t[1] * gradient[1]
        d = fv - f(x1, x2)
        fv = f(x1, x2)
        print(fv)
        print()


def main():
    findExtremum(0,0, s = -1)
    print(getT(1,1))
    # pass()


if __name__ == "__main__":
    main()
