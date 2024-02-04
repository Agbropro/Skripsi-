import matplotlib.pyplot as plt
import pandas as pd

# Load data from the provided text file
file_path = r"C:\Users\Lenovo\Documents\OpenBCI_GUI\Recordings\OpenBCISession_2024-01-31_14-34-33\OpenBCI-RAW-2024-01-31_14-37-14.txt"  # Replace with the actual path to your file
data = pd.read_csv(file_path, skiprows=4)
# print(data.columns)
# Extract relevant columns
time = data['Sample Index']
channel_0 = data[' EXG Channel 0']/10**6
channel_1 = data[' EXG Channel 1']/10**6
channel_2 = data[' EXG Channel 2']/10**6
channel_3 = data[' EXG Channel 3']/10**6
# channel_4 = data[' EXG Channel 4']
# channel_5 = data[' EXG Channel 5']
# channel_6 = data[' EXG Channel 6']
# channel_7 = data[' EXG Channel 7']
# print(channel_0)
# # Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# Plot each channel on a separate subplot
axs[0].plot(time, channel_0, label='Channel 0')
axs[1].plot(time, channel_1, label='Channel 1')
axs[2].plot(time, channel_2, label='Channel 2')
axs[3].plot(time, channel_3, label='Channel 3')

# Set titles and labels
axs[0].set_title('Channel 0')
axs[1].set_title('Channel 1')
axs[2].set_title('Channel 2')
axs[3].set_title('Channel 3')

plt.xlabel('freq')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()


## Customize the plot
# plt.title('OpenBCI Raw EXG Data')
# plt.xlabel('Sample Index')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.grid(True)
# plt.show()
