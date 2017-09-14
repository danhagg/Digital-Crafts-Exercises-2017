#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:28:32 2017
@author: danielhaggerty

"""

import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 1:
        return 1
    else:
        return -1

xs = list(range(-5, 5))

ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()