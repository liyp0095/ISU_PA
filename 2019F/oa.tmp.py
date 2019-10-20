#!/bin/python
# -*- coding: utf8 -*-

def reverse(s):
    return s[::-1]

def palin():
    num = 0
    for i in range(1000, 10000):
        if i % 11 == 0:
            rev = reverse(str(i))
            # print(rev)
            if rev != str(i):
                num += 1
    print(num)

def numStudent():
    num = 0
    for i in range(1, 121):
        if i % 2 == 0:
            continue
        if i % 5 == 0:
            continue
        if i % 7 == 0:
            continue
        num += 1
    print(num)


def lengthBinaryNumber():
    num = 10000000000
    b = bin(num)
    print(b)
    print(len(b))


def maxDivisor(a, b):
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def travelisfun(n, g, ori, des):
    res = []
    for i in range(n):
        if maxDivisor(ori[i], des[i]) > g:
            res.append(1)
        else:
            res.append(0)
    return res


def main():
    # palin()
    # numStudent()
    # print(maxDivisor(12, 6))
    print(travelisfun(3, 2, [1,2,3], [4,5,6]))
    lengthBinaryNumber()
    pass


if __name__ == "__main__":
    main()
