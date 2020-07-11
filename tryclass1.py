class student(object):
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setregno(self,regno):
        self.getregno=regno
    def gretregno(self):
        return self.regno
student1=student("David",128)
print("name",student1.getname())
print("regno",student1.regno)
student1.setname("john")
student1.setregno(678)
print("name",student1.name)
print("regno",student1.regno)