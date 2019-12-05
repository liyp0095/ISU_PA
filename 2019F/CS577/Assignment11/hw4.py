#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Linear Least Squares
Auther: Yuepei Li
Date: 2019-12-05
'''

import math
import numpy as np


def solve(phi_1, phi_2, phi_3, f):
    A = np.array([phi_1, phi_2, phi_3]).T
    F = np.array([f]).T
    # A = A.T
    U, s, V = np.linalg.svd(A)
    r, c = A.shape
    # print(np.zeros((8,3)))
    S = np.row_stack((np.diag(1/s), np.zeros((r-3,3))))
    # S = np.r_[np.diag(1/s), np.zeros((8,3))]
    # d = U.T.dot(F)
    # d = S.T.dot(d)
    # d = V.T.dot(d)
    # d = np.multiply(S, d)
    r = V.T.dot(S.T).dot(U.T).dot(F)
    return r[0][0], r[1][0], r[2][0]


def main():
    x = [i for i in range(1,12,1)]
    f = [0.0, 0.6, 1.77, 1.92, 3.31, 3.52, 4.59, 5.31, 5.79, 7.06, 7.17]
    print(x)
    phi_1 = [1] * len(x)
    phi_2 = [i for i in x]
    phi_3 = [math.sin(123*(i-1)) for i in x]

    # x = [i/2 for i in range(-2,5,1)]
    # print(x)
    # f = [4.1, 2.3, 1.05, 0.20, .05, .26, .9]
    # phi_1 = [1] * len(x)
    # phi_2 = [i for i in x]
    # phi_3 = [i*i for i in x]
    c1, c2, c3 = solve(phi_1, phi_2, phi_3, f)
    print(c1, c2, c3)


if __name__ == "__main__":
    main()
