import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170
# seed for guassian blobs, default centers = 3, default features = 2
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# y_predarrayof indicesof eachsampleto eachcluster
# Incorrect number of clusters, should be n_clusters = 3
# random_state is the seed for Kmeans initialization
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

# arrays for each feature of the samples
# c for color from cluster index
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Incorrect number of blobs")
plt.show()
