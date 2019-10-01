#!/bin/python
#-*- coding: utf8 -*-

import numpy as np
import math

class Matrix:
    def __init__(self, *args):
        self.m = []
        for r in args[0]:
            row = []
            for i in r:
                row.append(i)
            self.m.append(row)
