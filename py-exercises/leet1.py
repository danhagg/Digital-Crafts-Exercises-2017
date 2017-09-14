#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:36:27 2017
@author: danielhaggerty

"""


leetA = 'AEGIOST'
leetB = '4361057'

word1 = "Enter a sentence to be converted using leet: "

leetmsg1 = word1.upper()

for i in leetmsg1:
    for ch in leetA:
        if ch in leetmsg1:
            leetmsg1[i] = leetB[ch]
            
print(leetmsg1)
