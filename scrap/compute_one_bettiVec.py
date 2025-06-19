import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import gudhi

# Load data
X = np.load("X.npy")   # shape (N, d)
y = np.load("y.npy")   # shape (N,)

# Normalize
X_scaled = StandardScaler().fit_transform(X)

# Build kNN model
k = 10
nbrs = NearestNeighbors(n_neighbors=k).fit(X_scaled)

# Store Betti vectors and labels
betti_vectors = []
betti_labels = []

for i, label in enumerate(y):
    if label != 1:
        continue  # Only collect for anomalies (or change this to include both)

    indices = nbrs.kneighbors(X_scaled[i:i+1], return_distance=False)[0]
    cloud = X_scaled[indices]

    rips = gudhi.RipsComplex(points=cloud, max_edge_length=1.5)
    st = rips.create_simplex_tree(max_dimension=2)
    st.compute_persistence()
    betti = st.betti_numbers()
    betti += [0] * (3 - len(betti))  # pad to [β0, β1, β2]
    
    betti_vectors.append(betti)
    betti_labels.append(label)  # this will be +1

# Optionally sample benigns too
# (repeat above loop for randomly chosen benign points)

# Save output
np.save("betti_X.npy", np.array(betti_vectors))
np.save("betti_y.npy", np.array(betti_labels))
