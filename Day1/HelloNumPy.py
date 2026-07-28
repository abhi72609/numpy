import numpy as np
print("Hello NumPy")

import numpy as np
votes = np.array([ 775,  787,  918,   88,  166,  286, 2556,  324,  504,  402])

# Note: intentionally messy data
costs = np.array(["'800.0'" ,"'800.0'", "'800.0'", "'300.0'", "'600.0'", "'600.0'", "'600.0'", "'700.0'" ,"'550.0'", "'500.0'"])

print("Votes (Array):", votes)
print("Costs (Array):", costs)
print(type(votes))


votes * 2


# Dimensions & Shape
print("Votes array shape:", votes.shape)
print("Votes array dimensions:", votes.ndim)
print("Votes array size:", votes.size)

print("Costs array shape:", costs.shape)
print("Costs array dimensions:", costs.ndim)
print("Costs array size:", costs.size)