#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:59:11 2017
@author: danielhaggerty

"""

import matplotlib.pyplot as plt

c = int(input("Gimme a temp in celsius "))

def conv(c):
    return (1.8 * c) + 32

f = conv(c)

plt.plot(c, f, 'go')
plt.show()