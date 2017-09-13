#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:31:35 2017
@author: danielhaggerty

"""
rows = int(input("Give me the number of triangle rows: "))
stars = 1
rowCount = rows -1
for i in range(1, rows + 1):
    print(rowCount*" " + stars*"*")
    stars += 2
    rowCount -= 1
