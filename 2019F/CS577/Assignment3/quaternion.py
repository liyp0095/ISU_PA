#!/bin/python
#-*- coding: utf8 -*-

import numpy as np
from vector import Vector3
import math

class Quaternion:
    def __init__(self, q0, v):
        self.q0 = q0
        self.v = v

    def __str__(self):
        return "[%s, %s]" % (self.q0, self.v)

    def _act(self, v):
        return ((math.pow(self.q0, 2) - self.v.length_square())*v
                + 2*(self.v*v)*self.v + 2*self.q0*self.v.cross(v))

    def __add__(self, q):
        return Quaternion(self.q0 + q.q0, self.v + q.v)


    def __mul__(self, q):
        return Quaternion(self.q0*q.q0 - self.v*q.v,
                self.q0*q.v + q.q0*self.v + self.v.cross(q.v))



if __name__ == "__main__":
    q = Quaternion(1/2, Vector3(1/2,1/2,1/2))
    v = Vector3(1,0,0)
    print(q._act(v))
