# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:46:44 2020

@author: Christina
"""

animals = ["Lion","Zebra","Dolphin","Monkey"]
chars=0
for animal in animals:
    chars+=len(animal)
    print("Total characters:{},Average length :{}".format(chars,chars/len(animals)))
    