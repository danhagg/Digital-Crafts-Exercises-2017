#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:27:33 2017
@author: danielhaggerty

"""

import matplotlib.pyplot as plot

def f(x):
    return x ** 2

xs = list(range(-3, 4))

ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()