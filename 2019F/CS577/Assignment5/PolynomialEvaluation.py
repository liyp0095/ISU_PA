#!/bin/python
#-*- coding: utf8 -*-


def evalPoly(a, t, reverse = False):
    if reverse:
        a = list(a)
        a.reverse()
    n = len(a) - 1
    b = [0.0] * len(a)
    c = [0.0] * len(a)
    b[-1] = a[-1]
    c[-1] = b[-1]
    for k in range(n-1, 0, -1):
        b[k] = a[k] + t*b[k+1]
        c[k] = b[k] + t*c[k+1]
    b[0] = a[0] + t*b[1]
    return b[0], c[1]


def evaluate(a, t, reverse = False):
    return evalPoly(a, t, reverse=reverse)[0]


def main():
    p1 = 1.414214
    p2 = complex(1, 2)
    a = [51200, 0, -39712, 0, 7392, 0, -170, 0, 1]
    print("evaluation at " + str(p1))
    print(evalPoly(a, p1))
    print("evaluation at " + str(p2))
    print(evalPoly(a, p2))


if __name__ == '__main__':
    main()
