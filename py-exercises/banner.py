#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:53:46 2017
@author: danielhaggerty

"""

message = "My name is Dan"


height = 3
width = len(message)+2
print (width * "*")
print ((height-2)*("*" + message + "*\n"),end="")
print (width * "*")