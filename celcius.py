# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:59:47 2020

@author: Christina
"""

def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x,to_celcius(x))
    