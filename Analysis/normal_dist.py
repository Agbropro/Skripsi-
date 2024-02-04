import numpy as np
import matplotlib.pyplot as plt

# Generate random numbers from normal distributions with different scales
random_numbers_small_scale = np.random.normal(loc=0, scale=0.5, size=1000)
random_numbers_large_scale = np.random.normal(loc=0, scale=2, size=1000)
'''
loc: Mean (center) of the distribution.
scale: Standard deviation (spread or width) of the distribution. The standard deviation is a measure of the amount of variation or dispersion in a set of values.
size: Number of random samples to generate.'''
# Plot histograms
plt.hist(random_numbers_small_scale, bins=30, density=True, alpha=0.7, color='blue', label='LOW SD')
plt.hist(random_numbers_large_scale, bins=30, density=True, alpha=0.7, color='orange', label='LARGE SD')

plt.title('Effect of Scale on Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()

