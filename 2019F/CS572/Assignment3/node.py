#!/bin/python
#-*- coding: utf8 -*-

class Node:
    def __init__(self, index, six_tuple):
        self.index = index
        self.six_tuple = six_tuple
        self.c1, self.m1, self.b1, self.c2, self.m2, self.b2 = six_tuple


    def valid(self):
        # check if this node is valid
        if self.c1 < 0 or self.c2 < 0 or self.m1 < 0 or self.m2 < 0:
            return False
        if self.c1 > self.m1:
            return False
        if self.c2 > self.m2:
            return False
        if self.b1 not in [0, 1]:
            return False
        if self.b2 not in [0, 1]:
            return False
        return True


    def successors(self):
        # return a list of six integer tuple
        res = []
        actions = [[0,1], [1,0], [1,1], [2,0], [0,2]]
        if self.b1 == 1:
            for a in actions:
                res.append((self.c1 - a[0], self.m1 - a[1], 0, self.c2 + a[0], self.m2 + a[1], 1))
        if self.b1 == 0:
            for a in actions:
                res.append((self.c1 + a[0], self.m1 + a[1], 1, self.c2 - a[0], self.m2 - a[1], 0))
        return res
