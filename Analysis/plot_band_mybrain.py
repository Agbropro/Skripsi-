import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import butter, filtfilt

# Function to design a bandpass filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

# Load data from the provided text file
file_path = r"C:\Users\Lenovo\Documents\OpenBCI_GUI\Recordings\OpenBCISession_2024-01-31_14-34-33\OpenBCI-RAW-2024-01-31_14-37-14.txt"
data = pd.read_csv(file_path, skiprows=4)

# Extract relevant columns
time = data['Sample Index']
channel_0 = data[' EXG Channel 0'] / 10**6

# Set filter parameters
lowcut_delta, highcut_delta = 1.0, 4.0  # Delta waves (1-4 Hz)
lowcut_theta, highcut_theta = 4.0, 8.0  # Theta waves (4-8 Hz)
lowcut_alpha, highcut_alpha = 8.0, 13.0  # Alpha waves (8-13 Hz)
lowcut_beta, highcut_beta = 13.0, 30.0   # Beta waves (13-30 Hz)

# Apply bandpass filters to extract specific frequency bands
delta_wave = butter_bandpass_filter(channel_0, lowcut_delta, highcut_delta, fs=200, order=9)
theta_wave = butter_bandpass_filter(channel_0, lowcut_theta, highcut_theta, fs=200, order=9)
alpha_wave = butter_bandpass_filter(channel_0, lowcut_alpha, highcut_alpha, fs=200, order=9)
beta_wave = butter_bandpass_filter(channel_0, lowcut_beta, highcut_beta, fs=350, order=9)

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# Plot each brain wave band on a separate subplot
axs[0].plot(time, delta_wave, label='Delta Waves')
axs[1].plot(time, theta_wave, label='Theta Waves')
axs[2].plot(time, alpha_wave, label='Alpha Waves')
axs[3].plot(time, beta_wave, label='Beta Waves')

# Set titles and labels
axs[0].set_title('Delta Waves (1-4 Hz)')
axs[1].set_title('Theta Waves (4-8 Hz)')
axs[2].set_title('Alpha Waves (8-13 Hz)')
axs[3].set_title('Beta Waves (13-30 Hz)')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
