#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:35:28 2017
@author: danielhaggerty

"""

import matplotlib.pyplot as plot
import numpy as np

def f(x):
    return (x * 1.8) + 32

xs = np.linspace(-100, 100, 200)

ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()