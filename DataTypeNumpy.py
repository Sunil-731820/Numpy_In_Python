import numpy as np
a = np.array([1,2,3,4,5,6])
print("the numpy array is ")
print(a)
#the use of the empty() in the numpy array
arr = np.empty((3,2),dtype=int)
print("the uninitialised array is ")
print(arr)
#the use of the zero() in numpy array
arr1 = np.zeros((3,2))
print("the array is ")
print(arr1)
#the use of the ones() in numpy array
arr2 = np.ones((3,2),dtype="complex")
print("the array is ")
print(arr2)
#creating the numpy array using list
list1 = [1,23,4,5,6,7]
arr3 = np.asarray(list1)
print("before converting numpy array is ")
print(list1)
print("the numpy array is")
print(arr3)
#creating numpy array using more than one list
list2 = [[1,2,3,4],[5,6,7,8]]
print("the list before converting into the numpy array ")
print(list2)
arr4 = np.asarray(list2)
print("the numpy array is ")
print(arr4)
#the use of the full() in numpy array
d = np.full((3,6),6,dtype="complex")
print("the numpy array is ")
print(d)
#creating the random array in numpy 
import random
e = np.random.random((2,3))
print("the random array is ")
print(e)
#creating the sequence of the numpy array with steps
f = np.arange(0,30,31)
print("the array is")
print(f)
#use of linspace() in numpy array
g = np.linspace(0,5,10)
print("the numpy array is ")
print(g)
#reshaping the 3x4 array into 2x2x3 array using reshape() in numpy 
h = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("the array is")
print(h)
newArray = h.reshape(2,2,3)
print("after reshaping the new array is ")
print(newArray)
newArray1 = h.reshape(4,3)
print("the new array is ")
print(newArray1)
#the use of the flatten array 
i = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("the array is")
print(i)
newArray2 = i.flatten()
print("the new Array is")
print(newArray2)

#again converting the multi-dimensional array into single dimensional array
j = np.array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
])
print("the numpy array is ")
print(j)
newArray3 = j.reshape(2,2,3)
print("the new Array is ")
print(newArray3)
afterArray = newArray3.flatten()
print("the new Array is ") 
print(afterArray)

#Indexing in numpy array

arr = np.array([
   [-1, 2, 0, 4],
    [4, -0.5, 6, 0],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2.0]
])
print("the array is ")
print(arr)
print("after indexing the new array is ")
temp = (arr[:2,::2])
print(temp)

#Integer array Indexing Examples
arr = np.array([
    [-1,2,0,4],
    [4,-0.5,6,0],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2.0]
])

print("the array is ")
print(arr)

index1 = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("the numpy array is ")
print(index1)

#boolean array indexing problems
cond = arr>=0
temp = arr[cond]
print("the boolean array is ")
print(temp)

#again boolean array is 

cond1 = arr>4
temp1 = arr[cond1]
print("the array is ")
print(temp1)

#Basic Single Operation in the Array
a = np.array([1,2,5,3])
print("the first array is ")
print(a)
print("adding 1 to every element in the array")
print(a+1)

print("subtracting 2 to every element in the array")
print(a-2)

print("multiply each element by 10")
print(a*10)

print("squaring every element by given number ")
print(a**10)

print("squaring by 100 as given number by the users")
print(a**12)

#the tranpose of the array is 
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [8,9,10,11]
])
print("the array is")
print(arr)
modifyArray = arr.T
print("the transpose of the array is ")
print(modifyArray)


#unary Operations Perform on Numpy Array is 

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
print("the array is ")
print(arr)
print("the maximum value of the array is " , arr.max())
print("the row wise maximum value is " , arr.max(axis=1))
print("the column wise maximum values is " , arr.max(axis=0))

#the use of sum() in unary operation in the numpy array
print("the sum of the numpy array is ")
print(arr.sum())


#find the sum of the numpy array if the dimension of the array is multi-dimensions
arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("the array is ")
print(arr)
#First Reshaping the array 
newArray4 = arr.reshape(2,2,3)
print("the new array after the reshaping is ")
print(newArray4)
#the sum of the array is 
print(arr.sum())

#commutative sum of each row is
print(arr.cumsum(axis=1))

#Binary Operations In Numpy Array

a = np.array([[1,2],
[3,4]])
b = np.array([[4,3],
[2,1]])
print("the first Array is ")
print(a)
print("the second array ")
print(b)
print("the sum of the array is ")
print(a+b)
print("thesubtraction of the two array i ")
print(a-b)
print("the product(elementwise multiply) of the two array is ")
print(a*b)
print("the dot product of the two matrix is")
print(a.dot(b))


#the universal function in numpy 
a = np.array([0,np.pi/2,np.pi])
print("the array is")
print(a)

#Create the array of the sin values
a = np.array([])

#the exponential value of the array using universal function is 

b = np.array([0,1,2,3,4])
exp1 = np.exp(b)
print("the exponential of the array is ")
print(exp1)

#the sin of the array is 
a = np.array([1,2,3,4,5])
sin1 = np.sin(a)
print("the sin of the array is ")
print(sin1)

#Square roo of the array value is 
squareRoot = np.array([1,2,3,4,5,6,7,8,9])
root1 = np.sqrt(squareRoot)
print("the square roo of the each element is ")
print(root1)


#Sorting the array using np.sort()

a = np.array([1,2,13,4])
sort1 = np.sort(a)
print("sorting the single dimension array ")
print(sort1)

a = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]]
)
sort2 = np.sort(a)
print("the sorted array of the two dimension is ")
print(sort2)

#now sorting the array along the row wise of the array
print("after the row wise sorting the array is ", np.sort(a,axis=1))

#now sorting the array by specifying the algorithms name

print("after using merge sort the sorted array is " , np.sort(a,kind="mergesort"))

#sorting the array according to the column wise of the array 
a = np.array([
                 [1, 4, 2],
                 [3, 4, 6],
                 [0, -1, 5]
])
print("the array is ",a)
print("after the array is ", np.sort(a,axis=0))

#Example to show the sorting of the structured array 

dtype = [('name','S10'),('grad_year',int),('cgpa',float)]
values = [("sunil",2022,9),("harish",2024,8.9),("arti",2026,9.6)]
#now creating the array
arr = np.array(values,dtype=dtype)
print("the array is ")
print(arr)

print("sorting the array according to name wise")
print(np.sort(arr,order="name"))

print("again sorting the array according to graduation year and cgpa ")
print(np.sort(arr,order=["grad_year","cgpa"]))