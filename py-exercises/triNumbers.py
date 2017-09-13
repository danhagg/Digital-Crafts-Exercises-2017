#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:57:53 2017
@author: danielhaggerty

"""
n = int(input("Give me a number between 1 and 100: "))
x = n *(n+1)/2
print("The triangle number for {} is {}".format(n, int(x)))