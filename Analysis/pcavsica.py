import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FastICA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data for PCA and ICA
X_standardized = StandardScaler().fit_transform(X)
# y_standarized = StandardScaler().fit_transform(y)
# Normal Visualization
print(X_standardized[:, 0])
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.scatter(X_standardized[:, 0], X_standardized[:, 1], c=y, cmap='viridis') #Mengambil 2 fitur dari X iris dataset buat divisualisasi
plt.title('Normal Visualization')

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_standardized)

plt.subplot(132)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('PCA')

# Apply ICA
ica = FastICA(n_components=2, random_state=42)
X_ica = ica.fit_transform(X_standardized)

plt.subplot(133)
plt.scatter(X_ica[:, 0], X_ica[:, 1], c=y, cmap='viridis')
plt.title('ICA')

plt.tight_layout()
plt.show()
