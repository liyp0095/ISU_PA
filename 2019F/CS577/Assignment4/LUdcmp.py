#!/bin/python
#-*- coding: utf8 -*-

import math
import numpy as np

def LUdcmp(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    P = np.identity(n)
    for j in range(n):
        for i in range(n):
            if i == j:
                ulist = []
                for t in range(i, n):
                    ulist.append(abs(A[t,j] - sum([(L[t, k]*U[k,j]) for k in range(i)])))
                max_index = ulist.index(max(ulist)) + i
                # print(i, max_index, ulist)
                A[[i, max_index]] = A[[max_index, i]]
                P[[i, max_index]] = P[[max_index, i]]
                L[[i, max_index]] = L[[max_index, i]]  # this is very important
                U[i, j] = A[i, j] - sum([(L[i, k]*U[k,j]) for k in range(i)])
                # print(U[i,j])
                L[i, j] = 1
            elif i > j:
                U[i, j] = 0
                L[i, j] = (A[i, j] - sum([(L[i, k]*U[k,j]) for k in range(j)])) / U[j, j]
            else:
                U[i, j] = A[i, j] - sum([(L[i, k]*U[k,j]) for k in range(i)])
                L[i, j] = 0
    # for i in range(n):
    #     D[i, i] = U[i, i]
    #     U[i, i] = 1.0
    return P, L, U

def main():
    A = np.array([
        [11, 2, -5, 6, 48],
        [1, 0, 17, 29, -21],
        [-3, 4, 55, -61, 0],
        [41, 97, -32, 47, 23],
        [-6, 9, -4, -8, 50]
    ])
    # A = np.array([
    #     [2, -7, 6, 5],
    #     [4, 8, -10, 3],
    #     [9, -6, -4, 2],
    #     [5, 1, 3, 3]
    # ])

    P,L,U = LUdcmp(A)

    print("========================= PA = LU ============================")
    print("============================ A ===============================")
    print(A)
    print("============================ L ===============================")
    print(L)
    # print("============================ D ===============================")
    # print(D)
    print("============================ U ===============================")
    print(U)
    print("============================ P ===============================")
    print(P)
    # print(np.dot(np.linalg.inv(P),np.dot(L, U)))

if __name__ == "__main__":
    main()
