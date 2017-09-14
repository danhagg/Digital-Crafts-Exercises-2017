#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:52:43 2017
@author: danielhaggerty

"""

# leetspeak

leet = {
        'A' : '4',
        'E' : '3',
        'G' : '6',
        'I' : '1',
        'O' : '0',
        'S' : '5',
        'T' : '7',
        }

word = input("Enter a sentence to be converted using leet")
leetmsg = word.upper()
for x, y in leet.items():
        leetmsg = leetmsg.replace(x, y)
print ("Translated Message: ", leetmsg.upper())

