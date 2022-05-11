import  numpy as np
a = [1,2,3,4,5]
print(a)
# this is the example of single dimension array
b = np.array([1,2,3,4,5,6,7,8,9,10])
print("the numpy array is ")
print(b)

# Now i am going to make multi dimension array
c = np.array([[1,2,3,4],[5,6,7,8]])
print("the multi dimension array is ")
print(c)

# printing the numpy array with given data type here

d = np.array([12,13,14],complex)
print("printin the complex data type here")
print(d)

# finding the dimension of the array
print(d.ndim)
print(c.ndim)

# printing the size of each element of the array

a = np.array([1,2,3,4])
print("size of each element is ",a.itemsize,"bytes")

# finding the data type of each array

a = np.array([1,2,3,4])
print("the datatype of array is ",a.dtype)

# printing the shape and size of the array

a = np.array([1,2,3,4,5])
print("the size of the array",a.size)
print("the shape of the array is " , a.shape)


# Reshaping the array of multi dimensional array

a = np.array([[1,2,3],[4,5,6]])
print("the original array without reshaping is " , a)
a = a.reshape(3,2)
print("the array after reshaping is " , a)

# Slicing in the array as performed in the list of the python array

a = np.array([[1,2],[3,4],[5,600]])
print("the original array is " , a)
print("the array after the slicing is ")
print(a[0,1])
print(a[2,0])
# the use of the linspace in python Numpy

# Suppose i am wanting the 10 values between 5 and 15
a = np.linspace(5,15,10)
print("the 10 values between 5 and 15 is " , a)

# finding the max(), min() and sum() in the array
a = np.array([1,2,3,4,5,6,7,8,9])
print("the maximum values is", a.max())
print("the minimum value is ", a.min())
print("the sum of the array is ",a.sum())


# finding the maximum values in the array
a = np.array([[100,2,3,4],[5,6,7,8]])
print("the original array is ", a)
print("the maximum element in the column array is ", a.max(axis=0))
print("the minimum  values in the column array is ", a.min(axis=0))

print("the original array is ",a)
print("the maximum values in the row array is " , a.max(axis=1))
print("the mimimum values in the row is ",a.min(axis=1))

# How to find the square root and standard deviation of the numpy array

a = np.array([[1,2,30],[10,15,4]])
print("the original array is ",a)
print("the square root of the array is ", np.sqrt(a))
print("the standard deviation of the array is " , np.std(a))


# arithematic operation on the array is

a = np.array([1,2,3,4,5,6,7,8])
b = np.array([1,2,3,4,5,6,7,8])
print("the sum of the two array is " , a+b)
print("the subtraction of the two array is ", a-b)
print("the multiplication of the two array is " , a*b)


# vertical array concatenation
a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[1,2,3,4],[5,6,7,8]])
print("the vertical stack of the array  is " , np.vstack((a,b)))
print("the concatenation of the horizontal array is " , np.hstack((a,b)))
print("hello,Dhiraj")