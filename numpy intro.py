import numpy as np

list1 = [2,4,5,2]
print(list1)
print(type(list1))

array1 = np.array(list1) # returns an array (original list is unchanged)
print(array1)
print(type(array1))

for i in range(len(list1)):
    list1[i] = i*2
print(list1)

print(array1*2)

# create an array of zeros
zeros1 = np.zeros(5,dtype=int) # each is float by default
print(zeros1)
print(zeros1+1)

# create an array of ones
ones1 = np.ones(5)
print(ones1)

# 2 dimensional array
zeros2 = np.zeros((4,5)) # 4 arrays, each have 5 items.
print(zeros2)

# how to find the dimension of an array
print(zeros1.ndim)
print(ones1.ndim)
print(zeros2.ndim)

# how to find shape (how many rows and columns)
print(zeros1.shape)
print(ones1.shape)
print(zeros2.shape)

# create array with numbers in a range
range1 = np.arange(1,7,2,dtype=int) # start, end (not included), step, datatype 
print(range1)

# items with linear spacing
linspace1 = np.linspace(1,10,5) # divides range a-b (both included) into c equal parts, defaults to float
print(linspace1)

# reshape
range2 = np.arange(1,11)
reshaped2 = range2.reshape(2,5) # if number of items (a*b) doesn't match original array's length, returns error
print(range2)
print(reshaped2) # same values, but arrangement changes

# permutation (like the shuffle function)
print(np.random.permutation(range2))
print(np.random.permutation(range2))
print(np.random.permutation(range2))

# creating arrays with random numbers
random1 = np.random.randint(1,50,15)
print(random1)
random2 = np.random.randint(1,10,(8,10))
print(random2)

# sorting an array
print(np.sort(random1))

# slicing
print("")
print(random1)
print(random1[3:10]) # b isnt included
print(random1[:10])
print(random1[10:])
print(random1[::2])
print(random1[::-1])

# select multiple indexes
print(random1[[1,2,3,7]])

# conditional slicing
print(random1[random1>20]) # returns array with all items more than 20
print(random1[random1%2==0]) # returns array with all even items

# slicing 2 dimensional array
print(random2)
print(random2[2:4,5:8]) # doesnt include ending indexes!!!!!

# mathematical operations
print("")
l = np.random.randint(10,31,5)
w = np.random.randint(5,21,5)
area = l*w
print(l)
print(w)
print(area)
perimeter = 2*(l+w)
print(perimeter)

# comparing speeds
print("")
import time

start = time.time()
comparison_list = [i for i in range(0,1000001)]
end = time.time()
print(end-start)

start = time.time()
comparison_array = np.arange(0,1000001)
end = time.time()
print(end-start)