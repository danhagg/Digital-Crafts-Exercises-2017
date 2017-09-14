#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:32:05 2017
@author: danielhaggerty

"""

sentence = input("Give me a phrase: ")

vowel5 = {
        "A" : "AAAAA",
        "E" : "EEEEE",
        "I" : "IIIII",
        "O" : "OOOOO",
        "U" : "UUUUU",
        }

message = sentence.upper()

for x, y in vowel5.items():
    message = message.replace(x, y)
    
print("Changes phrase equals ", message)
    