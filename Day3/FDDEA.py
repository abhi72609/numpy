import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

result = array_2d + scalar
print("Array:\n", array_2d)
print("---"* 10)

print("adding Scalar:", scalar)
print("---"* 10)

print("Result after broadcasting:\n", result)


# Case 2: if one array is 1D and other is higher-dimensional , Broadcasting will expand the 1D array
# Broadcasting a 1D array to a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([10, 20, 30])

result = array_2d + array_1d

print(f"{array_2d} + {array_1d} =")
print("---"* 10)
print(result)



# Case 3: Column and Row Matrices
# Column matrix (3x1) and row matrix (1x3)
col_matrix = np.array([[1], [2], [3]])
row_matrix = np.array([[10, 20, 30]])

result = col_matrix + row_matrix

print(f"{col_matrix} + {row_matrix} =")
print("---"* 10)
print(result)