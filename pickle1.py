'''import pickle
class student:
     def __init__(self,name,marks):
         self.name=name
         self.marks=marks
s1=student("abc",80)
file = open("C:/Users/Christina/Desktop/pickle.pk1",'wb')
pickle.dump(s1,file)
print("student object is serialized")'''

'''import pickle
file = open("C:/Users/Christina/Desktop/pickle.pk1",'rb')
student=pickle.load(file)
print("student object deserialized")
print("name",student.name)
print("marks",student.marks)'''

import pickle
mylist=[1,2,3,4,5]
file=open("C:/Users/Christina/Desktop/pickle.pk1","wb")
pickle.dump(mylist,file)
print("list serialised")
file2=open("C:/Users/Christina/Desktop/pickle.pk1","rb")
data=pickle.load(file2)
print("list deserialisation")
print(data)