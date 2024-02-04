import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the plot in each animation frame
def update(frame):
    x_data = np.linspace(0, 2*np.pi, 1000)
    y_data = np.sin(x_data + frame / 10.0)  # Update the sine wave with time
    line.set_ydata(y_data)
    return line,

# Create a figure and axis
fig, ax = plt.subplots()

# Plot an initial sine wave
x_init = np.linspace(0, 2*np.pi, 1000)
y_init = np.sin(x_init)
line, = ax.plot(x_init, y_init)

# Set up the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=1, blit=True)

# Show the animated plot
plt.show()
