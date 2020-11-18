from sklearn.neighbors import NearestNeighbors as nn
import numpy as np

# Data set
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

# Query set
Y = np.array([[0, 1], [2, 3]])

nbrs = nn(n_neighbors=2, algorithm='ball_tree').fit(X)
distances, indices = nbrs.kneighbors(Y)

print(indices)
print(distances)
