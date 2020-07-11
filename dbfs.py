#error handling
#handling multiple errorss


try:
 x=5
 print(x)#nameerror
 a=10/1#zzero division error
 b=10+"ten"#type error
except NameError as ne:
     print(ne)
except ZeroDivisionError as zde:
    print(zde)
except TypeError as te:
    print(te)
else:
    print("Code is fine")
finally:
    print("Always run")
print("program ends")