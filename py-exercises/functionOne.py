#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:55:18 2017
@author: danielhaggerty

"""


def f(x):
    return 2 * x + 1

def g(x):
    return x + 1

import matplotlib.pyplot as plt
fOutput = []
gOutput = []

xList = range(-3, 5)

for x in xList:
    fOutput.append(f(x))
    gOutput.append(g(x))

plt.plot(xList, fOutput, xList, gOutput)
plt.show()