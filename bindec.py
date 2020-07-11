# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:09:56 2020

@author: Christina
"""

binary = input("Enter the binary number:")
exponent = len(binary)-1
decimal=0
for digit in binary:
    decimal = decimal+int(digit)*2**exponent
    exponent=exponent-1
print("The decimal number is:",decimal)