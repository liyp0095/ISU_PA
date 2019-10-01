#!/bin/python
#-*- coding: utf8 -*-

import math


N = 500000
delta = 0.00000000000005

def func(x):
    return math.exp(x) - math.sin(2*x)


def d_func(x):
    return math.exp(x) - math.cos(2*x) * 2


def Bisection(f, interval):
    (a, b) = interval
    if f(a)*f(b) > 0:
        print("invalid interval")
        return

    for i in range(N):
        m = (a+b) / 2
        if f(a)*f(m) <= 0:
            b = m
        else:
            a = m
        print(i, (a, b))
        if abs(a - b) < delta:
            return a


def MRF(f, interval):
    (a, b) = interval
    F, G, w = f(a), f(b), a
    for i in range(N):
        w_next = (G*a - F*b)/(G-F)
        if f(a)*f(w_next) <=0:
            b = w_next
            G = f(w_next)
            if f(w)*f(w_next) > 0:
                F = F/2
        else:
            a = w_next
            F = f(w_next)
            if f(w)*f(w_next) > 0:
                G = G/2
        if abs(a - b) < delta:
            return a


def Secant(f, interval):
    (x0, x1) = interval
    for i in range(N):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x2
        if abs(x0 - x1) < delta:
            return x1


def Newton(f, df, interval):
    x = interval[0]
    for i in range(N):
        x_n = x - f(x) / df(x)
        if abs(x_n - x) < delta:
            return x_n
        x = x_n


def main():
    a = Bisection(func, (-2, 2))
    a = MRF(func, (-2, 2))
    a = Secant(func, (-2, 2))
    a = Newton(func, d_func, (-2, 2))
    print(a, func(-2), func(2))


if __name__ == "__main__":
    main()
