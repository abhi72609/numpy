import numpy as np

# Creating IDs for 1000 customers
ids = np.arange(1, 1001)
print(ids)

print(np.arange(1,3,0.2))



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