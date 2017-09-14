#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:14:45 2017
@author: danielhaggerty

"""

import string

alphabet = string.ascii_lowercase

alphaDict = dict.fromkeys(alphabet)

listA = [ch for ch in alphabet]
listB = [ord(ch1)+13 for ch1 in alphabet]
listC = []
for ch2 in listB:
    if ch2 > 122:
        ch2 = ch2 - 26
    else:
        ch2 = ch2
    listC.append(ch2)
listD = [chr(i) for i in listC] 

keys = listA
values = listD
leet = dict(zip(keys, values))
print(leet)

word = input("Enter a sentence to be converted using leet")
leetmsg = word.lower()
for x, y in leet.items():
        leetmsg = leetmsg.replace(x, y)
print ("Translated Message: ", leetmsg.lower())
