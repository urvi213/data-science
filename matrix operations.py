import numpy as np
rows = int(input("rows: "))
columns = int(input("columns: "))

list1 = []
for i in range(rows*columns):
    list1.append(int(input("matrix1 value {}: ".format(i))))
#print(list1)
matrix1 = np.array(list1)
matrix1 = np.reshape(matrix1,(rows,columns))
print(matrix1)

list2 = []
for i in range(rows*columns):
    list2.append(int(input("matrix2 value {}: ".format(i))))
#print(list1)
matrix2 = np.array(list2)
matrix2 = np.reshape(matrix2,(rows,columns))
print(matrix2)

operation = input("1) addition \n2) subtraction \n")
if operation == "1":
    print(matrix1+matrix2)
elif operation == "2":
    print(matrix1-matrix2)