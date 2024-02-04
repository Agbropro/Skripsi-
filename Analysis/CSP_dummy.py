import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.preprocessing import LabelEncoder
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.covariance import EmpiricalCovariance
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from mne.decoding import CSP
from mne.filter import filter_data
import serial
import serial.tools.list_ports
import time
import keyboard

# Generate synthetic EEG data
np.random.seed(42)
n_samples = 200
n_channels = 4
n_timepoints = 1000
X = np.random.randn(n_samples, n_channels, n_timepoints)
#In a 3D array with shape (depth, rows, columns), the "depth" dimension corresponds to the layers, and it is the first dimension. The "rows" and "columns" dimensions follow.
#np.random.randn is a NumPy function that generates random samples from a standard normal distribution (mean=0, standard deviation=1). The shape of the generated array is specified by (n_samples, n_channels, n_timepoints).
# Create labels (two classes)
y = np.array(['Left', 'Right'] * (n_samples // 2))
# print(X,y)
from sklearn.preprocessing import LabelEncoder

# Create label encoder
label_encoder = LabelEncoder()

# Fit and transform the labels
y = label_encoder.fit_transform(y)
# Apply Butterworth filter for motor imagery
sfreq = 250  # Set your sampling frequency
freqs = [8, 30]  # Define your frequency band for motor imagery (adjust as needed)

X_filtered = np.zeros_like(X)
for i in range(n_samples):
    for j in range(n_channels):
        X_filtered[i, j, :] = filter_data(X[i, j, :], sfreq, freqs[0], freqs[1], method='iir', verbose=False)

# Flatten the filtered data for CSP
X_flat = X_filtered.reshape((n_samples, -1))

# Apply CSP
csp = CSP(n_components=2, reg=None, log=True, norm_trace=False)
X_csp = csp.fit_transform(X_filtered, y)

# # Plot CSP components
# plt.figure()
# for class_label in np.unique(y):
#     mask = (y == class_label)
#     plt.scatter(X_csp[mask, 0], X_csp[mask, 1], label=class_label)

# plt.title('CSP Components')
# plt.xlabel('CSP Component 1')
# plt.ylabel('CSP Component 2')
# plt.legend()
# plt.show()

from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_csp, y, test_size=0.2, random_state=42)

# Create an SVM classifier
classifier = SVC(kernel='linear')

# Train the classifier on the training set
classifier.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = classifier.predict(X_test)

# Evaluate the classifier's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Plot the decision boundary (if 2D)
if X_csp.shape[1] == 2:
    # Plot decision regions
    h = .02  # step size in the mesh
    x_min, x_max = X_csp[:, 0].min() - 1, X_csp[:, 0].max() + 1
    y_min, y_max = X_csp[:, 1].min() - 1, X_csp[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    # plt.scatter(X_csp[:, 0], X_csp[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    # plt.title('SVM Decision Boundary')
    # plt.xlabel('CSP Component 1')
    # plt.ylabel('CSP Component 2')
    # plt.show()

# New input data for classification
new_input = np.random.randn(1, n_channels, n_timepoints)

# Apply the same Butterworth filter to the new input
new_input_filtered = np.zeros_like(new_input) #shape 1 4 1000
for j in range(n_channels):
    new_input_filtered[0, j, :] = filter_data(new_input[0, j, :], sfreq, freqs[0], freqs[1], method='iir', verbose=False)

import matplotlib.pyplot as plt

# Plot the filtered EEG data for the new input
# Create subplots
fig, ax = plt.subplots(2, n_channels, figsize=(15, 6))

# Plot the original EEG data for the new input
for i in range(n_channels):
    ax[0, i].plot(new_input[0, i, :], label=f'Channel {i+1}')
    ax[0, i].set_title(f'Original EEG Channel {i+1}')
    ax[0, i].set_xlabel('Time')
    ax[0, i].set_ylabel('Amplitude')
    ax[0, i].legend()
    plt.show()
    # ax[1, i].plot(new_input_filtered[0, i, :], label=f'Channel {i+1}')
    # ax[1, i].set_title(f'Filtered EEG Channel {i+1}')
    # ax[1, i].set_xlabel('Time')
    # ax[1, i].set_ylabel('Amplitude')
    # ax[1, i].legend()
    # plt.show()
# Flatten the filtered new input data for CSP
# Flatten the filtered new input data for CSP
# new_input_flat = new_input_filtered.reshape((1, -1))
# print(new_input.shape, new_input_filtered.shape, new_input_flat.shape)
# # Reshape to match the expected input shape for CSP
# new_input_flat_reshaped = new_input_flat.reshape((1, -1, n_timepoints))  # Assuming n_timepoints is the length of the time dimension
# print(new_input_flat_reshaped.shape)
# Use the trained classifier to predict the class label for the new input
predicted_class = classifier.predict(csp.transform(new_input_filtered))

# Print the predicted class
print(f"Predicted Class: {label_encoder.inverse_transform(predicted_class)}") #inverse_transform balikin dari encoding 0 1 ke left right

print(label_encoder.inverse_transform(predicted_class)[0])


# ARDUINO COMMUNICATION
# Map predicted class to Arduino command
if label_encoder.inverse_transform(predicted_class)[0] == 'Right':
    arduino_command = 'ON'
elif label_encoder.inverse_transform(predicted_class)[0] == 'Left':
    arduino_command = 'OFF'
else:
    arduino_command = 'UNKNOWN'

# Open a serial connection to Arduino
ports = serial.tools.list_ports.comports()
ports_list = [str(port) for port in ports]
print("Available Ports:")
for port in ports_list:
    print(port)

val : str = input('Select Port: COM')
port_var = f'COM{val}'

serial_inst = serial.Serial(port=port_var, baudrate=9600, timeout=1)
time.sleep(2)  # Wait for Arduino to be ready
print(arduino_command)
# Send the Arduino command
def stop_code():
    print("Stopping the code...")
    serial_inst.close()
    exit()
# while True:
serial_inst.write(arduino_command.encode('utf-8'))

    # # Close the serial connection
    # keyboard.add_hotkey('enter', stop_code)
serial_inst.close()