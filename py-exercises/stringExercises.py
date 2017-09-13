#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:42:27 2017
@author: danielhaggerty

"""

stringOne = "hello, dan. how you doing?"
print(stringOne.upper())
print(stringOne.capitalize())


stringRev = stringOne[::-1]
print(stringRev[::-1])

# leetspeak
leetDict = {
        'A' : '4',
        'E' : '3',
        'G' : '6',
        'I' : '1',
        'O' : '0',
        'S' : '5',
        'T' : '7',
        }

for key, value in leetDict.items():
    print("\nKey: " + key)
    print("Value: " + value)
    
stringTwo = []

for i in stringOne:
    if i not in leetDict.keys()
        stringTwo.append(i)