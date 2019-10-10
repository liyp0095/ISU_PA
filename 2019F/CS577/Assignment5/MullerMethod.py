#!/bin/python
#-*- coding: utf8 -*-

import numpy
from PolynomialRoots import quartics
from PolynomialRoots import cubics
from PolynomialEvalution import evalPoly, evaluate

accuracy = 0.0000001


def polyDivision(a, b):
    a = numpy.array(a)
    b = numpy.array(b)
    return numpy.polydiv(a, b)[0].tolist()


def deg(a):
    return len(a) - 1


def roundc(a, c):
    return complex(round(a.real, c), round(a.imag, c))


def mullerRoot(p0):
    p = list(p0)
    # radius
    n = len(p) - 1
    a0 = p[0]
    a1 = p[1] + 0.00000001
    an = p[-1]
    radius = min(n*abs(a0/a1), (abs(a0/an))**(1./n))
    # generate three root estimates
    r = [0.0] * 3
    r[0] = radius * 0.25
    r[1] = radius * 0.5
    r[2] = radius
    # find one root
    while abs(r[-1] - r[-2]) > accuracy:
        p_reverse = list(p)
        p_reverse.reverse()
        c = evaluate(p_reverse, r[-1])
        f23 = (evaluate(p_reverse, r[-1]) - evaluate(p_reverse, r[-2])) / (r[-1] - r[-2])
        f12 = (evaluate(p_reverse, r[-2]) - evaluate(p_reverse, r[-3])) / (r[-2] - r[-3])
        f13 = (f12 - f23) / (r[-3] - r[-1])
        b = f23 + f13*(r[-1] - r[-2])
        a = f13
        x1 = -2*c / (b + (b**2 - 4*a*c)**(1./2))
        x2 = -2*c / (b - (b**2 - 4*a*c)**(1./2))
        if (abs(x1) > abs(x2)):
            res = x2 + r[-1]
        else:
            res = x1 + r[-1]
        r.append(res)
    return r[-1]


def Newton(a, r):
    v = evalPoly(a, r, reverse=True)
    rn = r - v[0]/v[1]
    while abs(rn - r) > accuracy:
        r = rn
        v = evalPoly(a, r, reverse=True)
        rn = r - v[0]/v[1]
    return rn


def mullerMethod(a):
    r = []
    if deg(a) == 4:
        r.extend(quartics(a[0], a[1], a[2], a[3], a[4]))
    elif deg(a) == 3:
        r.extend(cubics(a[0], a[1], a[2], a[3]))
    elif deg(a) > 4:
        p0 = list(a)
        p1 = list(a)
        l = 0
        while deg(p1) > 4:
            # r[l] =
            r.append(complex(mullerRoot(p1)))
            if abs(r[l].imag) < accuracy:
                # r[l] = complex(r[l].real, 0)
                p1 = polyDivision(p0, [1, -r[l]])
                p0 = p1
                l = l + 1
                while abs(evaluate(p1, r[l-1], reverse=True)) < accuracy:
                    r.append(r[l-1])
                    p1 = polyDivision(p0, [1, -r[l]])
                    p0 = p1
                    l = l + 1
            else:
                conjugate_r = r[l].conjugate()
                r.append(conjugate_r)
                p1 = polyDivision(p0, [1, -2*r[l].real, r[l].real**2 + r[l].imag**2])
                p0 = p1
                # print(p1)
                l = l + 2
                while abs(evaluate(p1, r[l-1], reverse=True)) < accuracy:
                    r.append(r[l-2])
                    r.append(r[l-2])
                    p1 = polyDivision(p0, [1, -2*r[l].real, r[l].real**2 + r[l].imag**2])
                    p0 = p1
                    l = l + 2
        if deg(p1) == 4:
            r.extend(quartics(p1[0], p1[1], p1[2], p1[3], p1[4]))
        elif deg(p1) == 3:
            r.extend(cubics(p1[0], p1[1], p1[2], p1[3]))

    r_final = []
    for i in r:
        r_final.append(roundc(Newton(a, i),8))
    # for i in range(len(r_final)):
    #     if abs(r_final[i].real) < accuracy:
    #         r_final[i] = complex(0, r_final[i].imag)
    #     if abs(r_final[i].imag) < accuracy:
    #         r_final[i] = complex(r_final[i].real, 0)

    return r_final


def main():
    # a = [1, 0, -1]
    # b = [1, 1]
    # print(polyDivision(a, br))
    # pass
    # p = [1, 0, -1, -1]
    # print(mullerRoot(p))
    # p = [1,0,0,0,0,0,1]
    p = [1, -3.7, 7.4, -10.8, 10.8, -6.8]
    q = [1, -0.843121, -8.35979, 10.1887, 14.6196, -25.7634, 9.15636, -0.360995, -0.180591, 0.00787276]
    print(mullerMethod(p))
    print(mullerMethod(q))
    print(evaluate(q, complex(0.258139, 0), reverse = True))


if __name__ == '__main__':
    main()
