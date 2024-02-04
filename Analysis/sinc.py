import matplotlib.pyplot as plt

def plot_10_20_system():
    # Define electrode positions for the 10-20 system
    electrode_positions = {
        'Fp1': (0, 1),
        'Fp2': (0, -1),
        'F7': (-1, 0.5),
        'F8': (-1, -0.5),
        'T7': (-1, 0),
        'T8': (-1, 0),
        'F3': (-0.5, 1),
        'F4': (-0.5, -1),
        'C3': (0, 0.5),
        'C4': (0, -0.5),
        'P3': (0.5, 1),
        'P4': (0.5, -1),
        'O1': (1, 0.5),
        'O2': (1, -0.5),
    }

    # Plot electrode positions
    for electrode, (x, y) in electrode_positions.items():
        plt.scatter(x, y, color='black', s=100)
        plt.text(x, y, electrode, fontsize=8, ha='center', va='center')

    # Set plot limits and labels
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Left ← → Right')
    plt.ylabel('Anterior ↑ ↓ Posterior')
    plt.title('10-20 EEG System')

    # Display the plot
    plt.show()

# Call the function to plot the 10-20 system
plot_10_20_system()
