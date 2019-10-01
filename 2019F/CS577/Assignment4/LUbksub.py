#!/bin/python
#-*- coding: utf8 -*-

import math
import numpy as np

import LUdcmp


def forward_substitution(L, pb):
    n = len(pb)
    y = [0] * n
    for i in range(n):
        y[i] = pb[i] - sum([(L[i,j]*y[j]) for j in range(i)])
    return np.array(y)


def backward_substitution(U, y):
    n = len(y)
    x = [0] * n
    for i in range(n):
        i = n - i - 1
        x[i] = (y[i] - sum([(U[i,j]*x[j]) for j in range(i, n)])) / U[i, i]
    return np.array(x)


def LUbksub(A, b):
    P, L, U = LUdcmp.LUdcmp(A)
    pb = np.dot(P, b)
    xx = np.dot(np.linalg.inv(U), np.dot(np.linalg.inv(L), pb))
    y = forward_substitution(L, pb)
    x = backward_substitution(U, y)
    return x


def main():
    b1 = np.array([4, 0, -7, -2, -11])
    b2 = np.array([2, 77, -1003, -7, 10])
    A = np.array([
        [11, 2, -5, 6, 48],
        [1, 0, 17, 29, -21],
        [-3, 4, 55, -61, 0],
        [41, 97, -32, 47, 23],
        [-6, 9, -4, -8, 50]
    ])
    T = np.array(A)
    x1 = LUbksub(A, b1)
    x2 = LUbksub(A, b2)
    print("========== b1 ===========")
    print(b1)
    print("x = ")
    print(x1)
    print("========== b2 ===========")
    print(b2)
    print("x = ")
    print(x2)

    # print(T)
    # their = np.dot(np.linalg.inv(T), b1)
    # print(their)
    # print(T)
    # print(np.dot(T, x1))
    # print(np.dot(T, their))



if __name__ == "__main__":
    main()
