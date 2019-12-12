#!/bin/python
# -*- coding: utf8 -*-

'''
Description: inplementation of 2-d fft
Auther: Yuepei Li
Date: 2019-12-11
'''

import numpy as np
from fft import  DFT, IDFT


def fft2(m1):
    m = m1.copy()
    tmp = []
    for i in range(m.shape[0]):
        m[i,:] = DFT(m[i,:])
    for i in range(m.shape[1]):
        m[:,i] = DFT(m[:,i])
    print(m)
    return m


def ifft2(m1):
    m = m1.copy()
    tmp = []
    for i in range(m.shape[0]):
        m[i,:] = IDFT(m[i,:])
    for i in range(m.shape[1]):
        m[:,i] = IDFT(m[:,i])
    print(m)


def main():
    m = np.array([[1+0j,3+0j],[2+0j,3+0j]])
    m = fft2(m)
    ifft2(m)
    # print(np.fft.fft2(m))

    # a = [1,2,3,4]
    # print(np.fft.fft(a))
    # print(DFT(a))
    pass


if __name__ == "__main__":
    main()
