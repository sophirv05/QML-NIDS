import numpy as np

# Load the saved files
betti_X = np.load("betti_X.npy")
betti_y = np.load("betti_y.npy")

# Print shapes
print("betti_X shape:", betti_X.shape)  # e.g., (100, 3)
print("betti_y shape:", betti_y.shape)  # e.g., (100,)

# View first few entries
for i in range(len(betti_X)):
    print(f"Sample {i}: Betti = {betti_X[i]}, Label = {betti_y[i]}")
