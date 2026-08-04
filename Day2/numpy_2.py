import numpy as np

# Creating IDs for 1000 customers
ids = np.arange(1, 1001)
print(ids)

print(np.arange(1,3,0.2))



# Fancy Indexing and Boolean Masking
votes = np.array([ 775,  787,  918,   88,  166,  286, 2556,  324,  504,  402])
costs = np.array(["'800.0'" ,"'800.0'", "'800.0'", "'300.0'", "'600.0'", "'600.0'", "'600.0'", "'700.0'" ,"'550.0'", "'500.0'"])
print(votes >= 500)

# Get only values where votes >= 500
high_votes = votes[votes >= 500]
print(high_votes)

# Or pass a list of specific indices
print(votes[[1, -1]]) # Gets index 1 and the last element (Fancy Indexing)

costs[votes>=500] # the cost where rating are greater than 500 votes



# 2D Matrices and the Reshape Function
# Take a sample of 50 restaurants
sample_votes = np.array([775, 787, 918, 88, 166, 286, 2556, 324, 504, 402, 150, 164, 424, 918, 90, 133, 144, 93, 62, 180, 62, 148, 219, 506, 172, 415, 230, 1647, 4884, 133, 286, 540, 2556, 36, 244, 804, 679, 245, 345, 618, 1047, 627, 354, 244, 163, 808, 1720, 868, 520, 299])
sample_costs = np.array([800.0, 800.0, 800.0, 300.0, 600.0, 600.0, 600.0, 700.0, 550.0, 500.0, 600.0, 500.0, 450.0, 800.0, 650.0, 800.0, 700.0, 300.0, 400.0, 500.0, 600.0, 550.0, 600.0, 500.0, 750.0, 500.0, 650.0, 600.0, 750.0, 200.0, 500.0, 800.0, 600.0, 400.0, 300.0, 450.0, 850.0, 300.0, 400.0, 750.0, 450.0, 450.0, 800.0, 800.0, 800.0, 850.0, 400.0, 1200.0, 300.0, 300.0])

# Create a 2D array: rows = restaurants, columns = [votes, costs]
restaurants_data = np.column_stack((sample_votes, sample_costs))

print("2D Array (votes, costs):\n", restaurants_data)
print("Shape:", restaurants_data.shape)
print("Dimensions:", restaurants_data.ndim)  # 2D


# Creating a 1D array and reshaping to 2D
arr = np.arange(10, 100, 10).reshape(3, 3)
print(arr)




# Aggregate Functions and Transformation
# Total votes of these 10 restaurants
total_votes = np.sum(restaurants_data[:, 0])

# Average cost for these 10 restaurants
avg_cost = np.mean(restaurants_data[:, 1])

# Max votes, Min cost
max_votes = np.max(restaurants_data[:, 0])
min_cost = np.min(restaurants_data[:, 1])

print("Total Votes:", total_votes)
print("Average Cost:", avg_cost)
print("Max Votes:", max_votes)
print("Min Cost:", min_cost)


# Logical Operations
# any
costs = np.array([800.0 ,800.0, 800.0, 300.0, 600.0, 600.0, 600.0, 700.0 ,550.0, 500.0])
any_above_3000 = np.any(costs > 3000)
print("Any cost above 3000?", any_above_3000)

# all
all_below_5000 = np.all(costs < 5000)
print("All cost below 5000?", all_below_5000)

# where
# Syntax: np.where(condition, value_if_true, value_if_false)
ratings = np.array([4.9, 4.1, 4.8])
# Labeling sessions
labels = np.where(ratings >= 4.2, "Green Flag", "Red Flag")
print(labels)


high_cost_indices = np.where(costs > 1000)
print("Indices with cost > 1000:", high_cost_indices)

selected_costs = costs[np.where((costs > 500) & (costs < 1000))]
print("Costs between 500 and 1000:", selected_costs)





# Sort
# Sorting a 1D Array

# Sorting Ascending:
sorted_votes = np.sort(votes)       # Sort the votes
print("Sorted Votes:", sorted_votes[:10])  # Display the first 10 sorted values

# Sorting Descending:
print("Votes sorted in descending order:", np.sort(votes)[::-1][:10])  # Display the first 10 sorted values in descending order

sorted_indices = np.argsort(votes)  # Indices that would sort the votes
print("Indices for Sorting:", sorted_indices[:10])