import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform PCA with 2 components (for visualization purposes)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

# Scatter plot the data in the new coordinate system
plt.figure(figsize=(8, 6))
colors = ['blue', 'red', 'green']

for i in range(len(iris.target_names)):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=iris.target_names[i], color=colors[i])

plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1 (Explained Variance: {:.2f}%)'.format(explained_variance_ratio[0] * 100))
plt.ylabel('Principal Component 2 (Explained Variance: {:.2f}%)'.format(explained_variance_ratio[1] * 100))
plt.legend()
plt.show()
