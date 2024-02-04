import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset with outliers
np.random.seed(42)
data = np.concatenate([np.random.normal(0, 1, 50), np.random.normal(8, 1, 10)])

# Plot the data points
plt.scatter(range(len(data)), data, label='Data Points', color='blue')

# Plot the mean line
mean_line = np.full_like(data, np.mean(data))
plt.plot(mean_line, label='Mean', linestyle='--', color='red')

# Highlight outliers
outliers = np.abs(data - np.mean(data)) > 2 * np.std(data)  # Using a threshold of 2 standard deviations
plt.scatter(np.where(outliers)[0], data[outliers], label='Outliers', color='red', marker='x')

# Plot the box plot
plt.boxplot(data, vert=False, widths=0.7, patch_artist=True, medianprops={'color': 'orange'})

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Data Points')
plt.title('Visualization of Outliers, Mean, and Box Plot')
plt.legend()

# Show the plot
plt.show()
