import numpy as np

a = 0
b = 0
c = 0
array = np.arange(1,11)
print(array)

choice = input("what sort of expression do you want to to evaluate?\n1) Linear (ax+b)\n2) Quadratic (ax^2+bx+c)\n")
print("")
if choice == "1":
    a = int(input("a? "))
    b = int(input("b? "))
    array = a*array+b
    print(array)
elif choice == "2":
    a = int(input("a? "))
    b = int(input("b? "))
    c = int(input("c? "))
    array = a*array^2+b*array+c
    print(array)