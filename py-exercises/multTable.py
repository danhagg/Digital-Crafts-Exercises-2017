#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:48:34 2017
@author: danielhaggerty

"""

# i included both ways of printing

for i in range(1,11):
    print(str(i) + " * " + str(i) + " equals " + str(i*i))
    
for i in range(1,11):
    print("{} * {} equals {}".format(i, i, i*i))