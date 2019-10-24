#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Calculate simple inflections and vertices
Auther: Yuepei Li
Date: 2019-10-24
'''

from SolutionOfNonlinear import Bisection
from Derivative import k, k1prime, rho
import math


def CalInflections(step):
    "des: find where k == 0 in [0, 2pi]"
    t = 0
    s = [0]
    res = []
    while s[-1] < math.pi * 2:
        t += 1
        s.append(t*step)
    t = 0
    for i in s:
        if k(t)*k(i) < 0:
            res.append(Bisection(k, (t, i)))
        t = i
    return res


def CalVertices(step):
    "des: find where k1prime == 0 in [0, 2pi]"
    t = 0
    s = [0.001]
    res = []
    while s[-1] < math.pi * 2:
        t += 1
        s.append(t*step)
    t = 0
    for i in s:
        if k1prime(t)*k1prime(i) <= 0:
            res.append(Bisection(k1prime, (t, i)))
        t = i
    return res


def main():
    dicimal = 4
    print("================= Bisection ==================")
    print("  phi \t  x \t  y")
    for phi in CalInflections(0.1):
        r = rho(phi)
        x = math.cos(phi)*r
        y = math.sin(phi)*r
        print('\t'.join([str(round(i,dicimal)) for i in [phi,x,y]]))
    print()
    print("================== Vertices ==================")
    print("  phi \t  x \t  y")
    for phi in CalVertices(0.1):
        r = rho(phi)
        x = math.cos(phi)*r
        y = math.sin(phi)*r
        print('\t'.join([str(round(i,dicimal)) for i in [phi,x,y]]))
    pass


if __name__ == "__main__":
    main()
