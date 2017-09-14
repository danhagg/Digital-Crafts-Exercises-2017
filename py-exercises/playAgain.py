#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:38:21 2017
@author: danielhaggerty

"""

def playAg():
    isTrue = 0
    while (isTrue == 0):
        answer = input("Play a game (y or n)").upper()     
        if answer == 'Y':
            isTrue = 1
            return True        
        elif answer == 'N':
            isTrue = 1
            return False
        else:
            print("invalid input")
            

playAg()    