import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
print("the array is")
print(A)
print("the rank of the matrix is ")
print(np.linalg.matrix_rank(A))
print("the determinant of the array is")
print(np.linalg.det(A))
print("the inverse of the array is ")
print(np.linalg.inv(A))
print("the power of the matrix is ")
print(np.linalg.matrix_power(A,3))
print("the trace of the given matrix is")
#trace() is used to find the sum of the diagonal elements
print(np.trace(A))


#solving the linear equations
a = np.array([[1,2],[3,4]])
b = np.array([8,18])
print("the solutions of the linear equations is ")
print(np.linalg.solve(a,b))

