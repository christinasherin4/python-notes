# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 01:44:10 2020

@author: Christina
"""

'''class student(object):
    def __init__(self,name,Regno):
        self.name=name
        self.Regno=Regno
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setRegno(self,Regno):
        self.Regno=Regno
    def getRegno(self):
        return self.Regno
    
student1=student("David",178)
print("Name:",student1.getName())
print("Regno:",student1.getRegno())
student1.setName("John")
student1.setRegno(150)
print("Name:",student1.getName())
print("Regno:",student1.getRegno())'''

'''class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __str__(self):
        return "Feet:{},Inches:{}".format(self.feet,self.inches)
    def __add__(self,ob):
        return Distance(self.feet+ob.feet,self.inches+ob.inches)
d1=Distance(10,5)
d2=Distance(7,4)
d3=d1+d2
print(d3)'''

'''class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def ___eq__(self,ob):
        return self.feet==ob.feet and self.inches==ob.inches
d1=Distance(10,5)
d2=Distance(7,4)
print(d1==d2)'''

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getArea(self):
        return self.length*self.breadth
    def __lt__(self,ob):
        return self.getArea()<ob.getArea()
r1=Rectangle(20,10)
r2=Rectangle(7,4)
print(r1<r2)