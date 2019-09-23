#!/bin/python
#-*- coding: utf8 -*-

import numpy as np
import math
import logging

class Vector3:
    def __init__(self, *args):
        if len(args) == 1:
            a = args[0]
            if a.shape == (3,):
                self.x = a[0]
                self.y = a[1]
                self.z = a[2]
            elif a.shape == (1, 3):
                self.x = a[0][0]
                self.y = a[0][1]
                self.z = a[0][2]
            elif a.shape == (3, 1):
                self.x = a[0][0]
                self.y = a[1][0]
                self.z = a[2][0]
        elif len(args) == 3:
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])


    def __repr__(self):
        return "<%s, %s, %s>" % (self.x, self.y, self.z)

    def __str__(self):
        return "<%s, %s, %s>" % (self.x, self.y, self.z)

    def __add__(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __mul__(self, v):
        types = (int, float)
        if isinstance(v, types):
            return Vector3(self.x*v, self.y*v, self.z*v)
        return self.x * v.x + self.y * v.y + self.z * v.z

    def __rmul__(self, v):
        return self.__mul__(v)

    def __truediv__(self, v):
        types = (int, float)
        if isinstance(v, types):
            return Vector3(self.x/v, self.y/v, self.z/v)
        return self.x / v.x + self.y / v.y + self.z / v.z

    def cross(self, v):
        return Vector3(self.y*v.z - self.z*v.y, self.z*v.x
                - self.x*v.z, self.x*v.y - self.y*v.x)

    def length_square(self):
        return self.x**2 + self.y**2 + self.z**2

    def length(self):
        return math.sqrt(self.length_square())

    def to_row(self):
        return np.array([self.x, self.y, self.z])

    def to_column(self):
        return np.array([[self.x], [self.y], [self.z]])


if __name__ == "__main__":
    v1 = Vector3(1,2,3)
    v2 = Vector3(1,1,1)
    '''
    v3 = v1.to_column()
    m = np.array([[1,2,3],[4,5,6],[7,8,9]])
    v3 = np.dot(m, v3)
    '''
    a = v1.to_column()
    vn = Vector3(a)
    vm = v1 * v2
    print(vm)
