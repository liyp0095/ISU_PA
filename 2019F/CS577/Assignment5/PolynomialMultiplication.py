#!/bin/python
#-*- coding: utf8 -*-

import cmath


def DFT(a, flag = 1):
    if len(a) == 1:
        return a
    n = len(a)
    wn = cmath.exp(flag*complex(0, 1) * cmath.pi * 2 / n)
    w = 1
    # // is int division operator
    a0 = [a[2*i] for i in range(n//2)]
    a1 = [a[2*i+1] for i in range(n//2)]
    ahat0 = DFT(a0, flag = flag)
    ahat1 = DFT(a1, flag = flag)
    ahat = [complex(0, 0)] * n
    for k in range(n//2):
        ahat[k] = ahat0[k] + w*ahat1[k]
        ahat[k+n//2] = ahat0[k] - w*ahat1[k]
        w = w*wn
        # print(w)
    return ahat


def IDFT(ahat):
    return [d/len(ahat) for d in DFT(ahat, flag = -1)]


def multiplyPolys(a, b):
    a = list(a)
    b = list(b)
    n = max(len(a), len(b))
    m = len(a) + len(b) - 1
    length_align = 1
    while length_align < 2*n:
        length_align *= 2
    a.extend([0]*(length_align - len(a)))
    b.extend([0]*(length_align - len(b)))

    a_hat = DFT(a)
    b_hat = DFT(b)
    c_hat = [a_hat[i] * b_hat[i] for i in range(length_align)]
    c = IDFT(c_hat)

    return [round(t.real, 2) for t in c[:m]]


def printPoly(a):
    for i in range(len(a)):
        print("x^" + str(i) + "\t" + str(a[i]))


def main():
    # a = [float(i) for i in range(4)]
    # print(DFT(a))
    # print(IDFT(DFT(a)))
    # a = [1,2]
    # b = [1,2]
    # print(multiplyPolys(a, b))
    p = [-6.8, 10.8, -10.8, 7.4, -3.7, 2.4, -70.1, 1]
    q = [51200, 0, -39712, 104.2, 7392, 0.614, -170, 0, 1]
    res = multiplyPolys(p, q)
    print("==== p ====")
    printPoly(p)
    print("==== q ====")
    printPoly(q)
    print("=== p*q ===")
    printPoly(res)


if __name__ == '__main__':
    main()
