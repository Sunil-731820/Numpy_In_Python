import numpy as np
#Example of the vertical stacking in the numpy array

a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
print("the first array is ",a)
print("the second array is ",b)
print("the vertical stacking is ")
print(np.vstack((a,b)))

print("the horizontal array is ")
print(np.hstack((a,b)))

c = [5,6]
print("the use of the cloumn stacking is")
print(np.column_stack((a,c)))

print("concatening to the 2nd index of the array ")
print(np.concatenate((a,b),1))
print("the horizontal stack is ")
print(np.hstack((a,b)))
print("again concatening the array to the  1st index ")
print(np.concatenate((a,b),0))


#Spliting the numpy array
a = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])
print("the array is ")
print(a)

print("after spliting the array into the horizontal into 2 Parts ")
print(np.hsplit(a,2))
print("spliting the array into 2 parts vertically ")
print(np.vsplit(a,2))

