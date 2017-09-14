#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:30:54 2017
@author: danielhaggerty

"""

import matplotlib.pyplot as plot
import math
import numpy as np

def f(x):
    return math.sin(x)

xs = np.linspace(-5, 5, 100)

ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()