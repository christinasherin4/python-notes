number = 5
try:
    print(number)
except NameError as ne:
    print(ne)
else:
    print("correct code")
finally:
    print("Always run")