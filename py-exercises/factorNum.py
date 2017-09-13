#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:08:28 2017
@author: danielhaggerty

"""

x = 24
xList = [i for i in range(1, x+1)]
factorsList = []
for j in xList:
    if x % j == 0:
        factorsList.append(j)
 






       
newFactors = [k for k in range(1, x+1) if x % k == 0]
        