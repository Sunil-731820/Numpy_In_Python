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

