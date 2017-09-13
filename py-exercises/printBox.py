#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:16:46 2017
@author: danielhaggerty

"""

height = int(input("Give me the height of a box: "))
width = int(input("Give me the width of a box: "))
print (width * "*")
print ((height-2)*("*" + (width-2)*" " + "*\n"),end="")
print (width * "*")