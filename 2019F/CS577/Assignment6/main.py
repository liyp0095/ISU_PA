#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Calculate sample inflections and vertices
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
    while s[-1] < math.pi * 2:
        t += 1
        s.append(t*step)
    t = 0
    for i in s:
        if k(t)*k(i) < 0:
            print(Bisection(k, (t, i)))
        t = i


def CalVertices(step):
    "des: find where k1prime == 0 in [0, 2pi]"
    t = 0
    s = [0.001]
    while s[-1] < math.pi * 2:
        t += 1
        s.append(t*step)
    t = 0
    for i in s:
        if k1prime(t)*k1prime(i) <= 0:
            phi = Bisection(k1prime, (t, i))
            r = rho(phi)
            x = math.cos(phi)*r
            y = math.sin(phi)*r
            print(round(phi, 4), round(x,4), round(y,4))
        t = i


def main():
    CalInflections(0.1)
    print()
    CalVertices(0.1)
    pass


if __name__ == "__main__":
    main()
