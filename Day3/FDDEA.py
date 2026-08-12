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


# Broadcasting in 2D Arrays
# Example: Compatible shapes
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[10], [20]])

# Broadcasting works
result = array1 + array2

print("Array 1:\n", array1)
print("---"* 10)

print("Array 2:\n", array2)
print("---"* 10)

print("Result:\n", result)

# Example: Incompatible shapes
# This is expected to fail!
# array1 = np.array([[1, 2, 3], [4, 5, 6]])
# array2 = np.array([[10, 20]])

# result = array1 + array2
# result


# Using np.tile()
# Example: Explicit broadcasting with np.tile
array1 = np.array([[1, 2, 3]])
array2 = np.array([[10], [20], [30]])

# Use np.tile to match shapes
array1_tiled = np.tile(array1, (3, 1))
print(array1_tiled)

# Perform addition
result = array1_tiled + array2
print("Result:\n", result)


# Vectorization


# When working with arrays, applying a Python function directly to a NumPy array often leads to errors.
# Example: Apply a custom function to the 'rate' column
def categorize_rating(rating):
    "Categorize ratings into high or low."""
    if rating >= 4.0:
        return "High"
    else:
        return "Low"
# Attempt to apply the function directly
# This is expected to fail!
# categorized_ratings = categorize_rating(numeric_data[:, 0])  # 'rate' column
# print(categorized_ratings)


# Vectorize the categorize_rating function
vectorized_categorize_rating = np.vectorize(categorize_rating)
# print(vectorized_categorize_rating)
# Apply the vectorized function to the 'rate' column
# numeric_data
numeric_data = np.arange(11,20).reshape(3,3)
categorized_ratings = vectorized_categorize_rating(numeric_data[:, 0])

# Display a sample of the categorized ratings
print("Categorized Ratings (sample):", categorized_ratings[:10])

# Define a function to calculate the discounted cost
def discount_cost(rate, cost):
    "Apply a 10% discount if the rating is 4.0 or higher."""
    if rate >= 4.0:
        return cost * 0.9
    else:
        return cost

# Vectorize the discount_cost function
vectorized_discount_cost = np.vectorize(discount_cost)

# Apply the vectorized function to 'rate' and 'approx_cost(for two people).'
discounted_costs = vectorized_discount_cost(numeric_data[:, 0], numeric_data[:, 2])

# Display a sample of the discounted costs
print("Discounted Costs (sample):", discounted_costs[:10])



# Split

# 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])

# Split into 3 sections
split_1d = np.split(array_1d, 3)

print("Original Array:", array_1d)
print("Splits:", split_1d)