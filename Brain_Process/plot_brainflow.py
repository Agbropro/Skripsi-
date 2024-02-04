import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import butter, filtfilt
import numpy as np
#Frequency Sampling OpenBCI = 250 Hz data diambil waktu 5 detik jadi data diambil tiap 0.02 detik
#time sleep x, x nya ga masuk jadi data yang dicapture
# Load data from the provided text file
file_path = r"C:\Users\Lenovo\OneDrive - UGM 365\Skripsi Training\braindimas.csv"  # Replace with the actual path to your file
df = pd.read_csv(file_path)
# print(len(np.arange(0,5,0.02)))
df['Index'] = np.arange(0,4.996,0.004)#range(len(df))
df['1'] = df['1']/10**6
# print(df['Index'])
print(len(df['1']))
# Plotting the data with 1 and 2 columns as x and the default integer index as y
plt.figure(figsize=(10, 6))
plt.plot(df['Index'],df['1'])
# plt.plot(df[2], df.index, label='Column 2', marker='o')

# Adding labels and title
plt.xlabel('Indexes')
plt.ylabel('Values')
plt.title('Plot for Columns 1 and 2')
plt.legend()

# Display the plot
plt.show()


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

# Set filter parameters
lowcut_delta, highcut_delta = 1.0, 4.0  # Delta waves (1-4 Hz)
lowcut_theta, highcut_theta = 4.0, 8.0  # Theta waves (4-8 Hz)
lowcut_alpha, highcut_alpha = 8.0, 13.0  # Alpha waves (8-13 Hz)
lowcut_beta, highcut_beta = 13.0, 30.0   # Beta waves (13-30 Hz)

# Apply bandpass filters to extract specific frequency bands
delta_wave = butter_bandpass_filter(df['1'], lowcut_delta, highcut_delta, fs=250, order=5)
theta_wave = butter_bandpass_filter(df['1'], lowcut_theta, highcut_theta, fs=250, order=5)
alpha_wave = butter_bandpass_filter(df['1'], lowcut_alpha, highcut_alpha, fs=250, order=5)
beta_wave = butter_bandpass_filter(df['1'], lowcut_beta, highcut_beta, fs=250, order=5)

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 16), sharex=True)

# Plot each brain wave band on a separate subplot
axs[0].plot(df['Index'], delta_wave, label='Delta Waves')
axs[1].plot(df['Index'], theta_wave, label='Theta Waves')
axs[2].plot(df['Index'], alpha_wave, label='Alpha Waves')
axs[3].plot(df['Index'], beta_wave, label='Beta Waves')

# Set titles and labels
axs[0].set_title('Delta Waves (1-4 Hz)')
axs[1].set_title('Theta Waves (4-8 Hz)')
axs[2].set_title('Alpha Waves (8-13 Hz)')
axs[3].set_title('Beta Waves (13-30 Hz)')

plt.xlabel('Time (s)')
# plt.ylim(-0.08,0.08)
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()