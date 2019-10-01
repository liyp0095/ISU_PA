#!/bin/python
#-*- coding: utf8 -*-

import math


N = 5000
delta = 0.00005

def func(x):
    return math.exp(x) - math.sin(2*x)


def d_func(x):
    return math.exp(x) - math.cos(2*x) * 2


def Bisection(f, interval, flag = 0):
    (a, b) = interval
    if f(a)*f(b) > 0:
        print("invalid interval")
        return

    if flag:
        print("iterations \t f(x) \t interval")
    for i in range(N):
        m = (a+b) / 2
        if f(a)*f(m) <= 0:
            b = m
        else:
            a = m
        if flag:
            print(i, f(a), (a, b))
        if abs(a - b) < delta:
            return a


def MRF(f, interval, flag = 0):
    (a, b) = interval
    F, G, w = f(a), f(b), a
    if flag:
        print("iterations \t f(x) \t interval")
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
        if flag:
            print(i, f(a), (a, b))
        if abs(a - b) < delta:
            return a


def Secant(f, interval, flag = 0):
    (x0, x1) = interval
    if flag:
        print("iterations \t f(x) \t x")
    for i in range(N):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x2
        if flag:
            print(i, f(x1), x1)
        if abs(x0 - x1) < delta:
            return x1


def Newton(f, df, interval, flag = 0):
    x = interval[0]
    if flag:
        print("iterations \t f(x) \t x")
    for i in range(N):
        x_n = x - f(x) / df(x)
        if flag:
            print(i, f(x_n), x_n)
        if abs(x_n - x) < delta:
            return x_n
        x = x_n


def main():
    print("accuracy: " + str(delta))
    print("max_iterations: " + str(N))
    print("============== Bisection ==============")
    Bisection(func, (-2, 2), 1)
    print("================= MRF =================")
    MRF(func, (-2, 2), 1)
    print("=============== Secant ================")
    Secant(func, (-2, 2), 1)
    print("=============== Newton ================")
    Newton(func, d_func, (-2, 2), 1)


if __name__ == "__main__":
    main()
