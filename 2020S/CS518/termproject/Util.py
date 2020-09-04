#!/bin/python
# -*- coding: utf8 -*-

'''
Description:
Auther: Yuepei Li
Date: 2020-04-25
'''

import math

def find_intersect(pi, pj, ly):
    # https://codereview.stackexchange.com/questions/51011/calculating-the-point-of-intersection-of-two-parabolas
    xi = pi[0]
    yi = pi[1]
    xj = pj[0]
    yj = pj[1]

    a1 = 1/(2*(yi - ly))
    b1 = -2*xi / (2*(yi - ly))
    c1 = (xi*xi + yi*yi - ly*ly) / (2*(yi - ly))

    a2 = 1/(2*(yj - ly))
    b2 = -2*xj / (2*(yj - ly))
    c2 = (xj*xj + yj*yj - ly*ly) / (2*(yj - ly))

    a = a1-a2
    b = b1-b2
    c = c1-c2

    if a == 0:
        x = -c/b
        return (x, a1*x*x + b1*x + c)

    square = math.sqrt(b**2 - 4*a*c)
    double_a = 2*a
    answers = [(-b + square)/double_a, (-b - square)/double_a]

    # Using `set()` removes any possible duplicates.
    if xi > xj:
        x = max(answers)
        return (x, a1*x*x + b1*x + c)
    else:
        x = min(answers)
        return (x, a1*x*x + b1*x + c)


def point_cmp(p1, p2):
    # top to bottom, left to right
    if p1[1] > p2[1]:
        return True
    elif p1[1] < p2[1]:
        return False
    else:
        if p1[0] < p2[0]:
            return True
        else:
            return False

def main():
    print(find_intersect(0,1,0,2,-2))
    pass


if __name__ == "__main__":
    main()
