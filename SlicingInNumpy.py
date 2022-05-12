from xmlrpc.client import Boolean
import numpy as np
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]
#you can not multiply two list
# print(list1*list2)
#converting into the array first then multiply
a = np.array(list1)
b = np.array(list2)
print("the multiplication of the two matrix is ")
print(a*b)
#  the use of index in the numpy np.array
a = np.arange(10,1,-2)
print("the array is ")
print(a)

#index are specified into the numpy array
newArray = a[np.array([3, 1, 2])]
print("the new Array is ")
print(newArray)

#indexes can be negative 
a = np.array([1,2,3,4,5,6,7,8,9])
print("the array is ")
print(a)
print("the index of the array is when i give negative index ")
print(a[np.array([1,3,-3])])


#Some Basic slicing in the numpy array
a = np.arange(20)
print("the array is ")
print(a)
print("the first slice of the array is")
print(a[-8:17:1])

print("again applying the slicing in the array")
print(a[10:])
print("reversing the array is ")
print(a[::-1])

#creating the 3 dimensional array
a = np.array([[
    [1,2,3,4],
    [4,5,6,7]],
    [[1,2,3,4],[5,6,7,8]]
    ])
print("the numpy array is ")
print(a)
print("the use of equaivalent method in the numpy array")
print(a[...,1])
print(b[...,1]) #Equivalent to b[: ,: ,1 ]


#The use of the advance index in numpy array
a = np.array([[1 ,2 ],[3 ,4 ],[5 ,6 ]])
print("the array is ")
print(a)
print("the array after indexing is ")
print(a[[0,1,2],[0,0,1]])
# the Boolean indexing is 
a = np.array([100,200,300,1,2,3,4,500])
print("the array after applying the boolean conditions in the array")
print(a[a>50])
print("again applying the conditions in the array")
print(a[a>1200])
# find the sqaure of the multiple of 40 
a = np.array([10, 40, 80, 50, 100])
print("the array is ")
print(a)
print(a[a%40==0]**2)

b = np.array([1,2,3,4,5,6,7,8,9,10])
print("the array b is ")
print(b)
print(b[b%2==0]**10)

# print the list whose sum of the row is a multiple of 10
b = np.array([[5, 5],[4, 5],[16, 4]])
sumrow = b.sum(-1)
print("the list of the array is ")
print(b[sumrow%10==0])