#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:50:33 2017
@author: danielhaggerty

"""

# plots the X,Y data. 
# Exchange JSON data with others to test your program more thoroughly.


import json
import matplotlib.pyplot as plt


d = {"data" : [[1, 1],[2, 2],[3, 3],[4, 4]]}

with open('d.json', 'w') as fh:
  json.dump(d, fh)
with open('d.json', 'r') as fh:
  data = json.load(fh)
  print(d)

plt