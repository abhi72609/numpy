import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

result = array_2d + scalar
print("Array:\n", array_2d)
print("---"* 10)

print("adding Scalar:", scalar)
print("---"* 10)

print("Result after broadcasting:\n", result)