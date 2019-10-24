#!/bin/python
# -*- coding: utf8 -*-

'''
Description: give the derivative function in question 6
Auther: Yuepei Li
Date: 2019-10-24
'''

from math import sin, cos

def t1(a, phi):
    "des: help calculate h3prime, a = -1/4 or -361/400"
    return 2*a*cos(2*phi) + 2*a**2*cos(2*phi)*sin(phi)**2 - 1/2 * a**2 * sin(2*phi)**2


def t2(a, phi):
    "des: help calculate h3prime, same as t1"
    return (1+a*sin(phi)**2)**(3/2.0)


def t1prime(a, phi):
    "des: help calculate h3prime, a = -1/4 or -361/400"
    return -2*a*sin(2*phi)*2 - 2*a**2*sin(2*phi)*2*sin(phi)**2 #+ 2*a**2*cos(2*phi)*sin(2*phi) - a**2*sin(4*phi)


def t2prime(a, phi):
    "des: help calculate h3prime, same as t1"
    return 3/2.0 * ((1+a*sin(phi)**2)**(1/2.0)) * a*sin(2*phi)


def h1prime(a, phi):
    "des: help calculate rho 1st derivative, a = -1/4 or -361/400"
    return 1/2 * (a*sin(2*phi))/((1+a*sin(phi)**2)**(1/2.0))


def h2prime(a, phi):
    "des: help calculate rho 2nd derivative"
    return 1/2 * (t1(a, phi) / t2(a, phi))


def h3prime(a, phi):
    "des: help calcute rho 3rd derivative"
    tt1 = t1(a, phi)
    tt2 = t2(a, phi)
    tt1prime = t1prime(a, phi)
    tt2prime = t2prime(a, phi)
    return 1/2*(tt1prime*tt2 - tt2prime*tt1) / (tt2**2)


def rho(phi):
    return cos(phi) + (1-1/4.0*sin(phi)**2)**(1/2.0) + (1-361/400.0*sin(phi)**2)**(1/2.0)


def rho1prime(phi):
    "des: rho derivative"
    return -sin(phi) + h1prime(-1/4.0, phi) + h1prime(-361/400.0, phi)


def rho2prime(phi):
    "des: rho derivative"
    return -cos(phi) + h2prime(-1/4.0, phi) + h2prime(-361/400.0, phi)


def rho3prime(phi):
    "des: rho derivative"
    return sin(phi) + h3prime(-1/4.0, phi) + h3prime(-361/400.0, phi)


def k(phi):
    "des: return curvature"
    v_rho = rho(phi)
    v_rho1prime = rho1prime(phi)
    v_rho2prime = rho2prime(phi)
    return (v_rho**2 + 2*v_rho1prime**2 - v_rho*v_rho2prime) / (v_rho ** 2 + v_rho1prime**2)**(3/2.0)


def k1prime(phi):
    "des: return derivative of curvature"
    rhoo = rho(phi)
    rho1 = rho1prime(phi)
    rho2 = rho2prime(phi)
    rho3 = rho3prime(phi)

    s1 = (2*rhoo*rho1 + 4*rho1*rho2 - rhoo*rho3 - rho1*rho2)*(rhoo**2+rho1**2)
    s2 = 3/2.0 * (2*rhoo*rho1 + 2*rho1*rho2) * (rhoo**2+2*rho1**2-rhoo*rho2)
    s3 = (rhoo**2 + rho1**2)**(5/2.0)

    return (s1 - s2) / s3


def angTest(ang):
    print("======== angTest =========")
    print("ang = ", ang)
    print()
    print("p = ", rho(ang))
    print("p' = ", rho1prime(ang))
    print("p'' = ", rho2prime(ang))
    print("p'' = ", rho3prime(ang))
    print()
    print("k = ", k(ang))
    print("k' = ", k1prime(ang))


def main():
    angTest(0.5)


if __name__ == "__main__":
    main()
