#!/bin/python
# -*- coding: utf8 -*-

'''
Description: Line Fitting
Auther: Yuepei Li
Date: 2019-12-05
'''

import numpy as np


def main():
    x = [i for i in range(10)]
    y = [0.905877, 1.21214, 0.744417, -0.099021, -0.268071, -1.035455, -1.28139, -1.36631, -1.80558, -2.13389]
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    print("x_mean\n", x_mean)
    print("y_mean\n", y_mean)
    M = np.array([[i-x_mean for i in x], [i-y_mean for i in y]]).T
    print("M=\n", M)
    A = M.T.dot(M)
    print("A = \n", A)
    eigenvalue,featurevector=np.linalg.eig(A)
    print("eigenvalue=\n",eigenvalue)
    print("featurevector=\n",featurevector)

    if eigenvalue[0] > eigenvalue[1]:
        # print(featurevector[1])
        a, b = featurevector.T[1]
    if eigenvalue[0] < eigenvalue[0]:
        a, b = featurevector.T[0]
    print(a,b)
    print(a*a + b*b)
    d = a*x_mean + b*y_mean
    print("d = ", d)

    print(np.polyfit(x, y, 1))



if __name__ == "__main__":
    main()
