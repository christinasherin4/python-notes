'''class distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __str__(self):
        return "feet{},inches:{}".format(self.feet,self.inches)
    def __add__(self,ob):
        return(self.feet+ob.feet,self.inches+ob.inches)
d1=distance(4,5)
d2=distance(8,9)
d3=d1+d2
print(d3)'''

'''class distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __eq__(self,ob):
        return self.feet==ob.feet and self.inches==ob.inches
d1=distance(7,8)
d2=distance(3,4)
print(d1==d2)'''

'''class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def getarea(self):
        return self.length*self.breadth
    
    def __lt__(self,ob):
        return self.getarea()<ob.getarea()


r1=rectangle(10,20)
r2=rectangle(50,40)
print(r1<r2)'''

class student(object):
    def __init__(self,name,regno):
        self.__name=name
        self.__regno=regno
        
s1=student("raj",1230)
print(s1.name)
print(s1.regno)