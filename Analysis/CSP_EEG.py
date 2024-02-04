import numpy as np
import matplotlib.pyplot as plt
import mne
from mne.datasets import sample
from mne import Epochs, pick_types, events_from_annotations
from mne.decoding import CSP
import os
# Specify the desired custom path to save the dataset
custom_path = r'C:\Users\Lenovo\OneDrive - UGM 365\Skripsi Training\MNE_data'

# Download the sample dataset to the custom path
mne.datasets.sample.data_path(path=custom_path)

# Check the downloaded files in the specified path
downloaded_files = os.listdir(custom_path)
print("Downloaded files:")
for file in downloaded_files:
    print(os.path.join(custom_path, file))

# Rest of the code remains the same...

# print(data_path)
raw = mne.io.read_raw_fif(custom_path + '/MEG/sample/sample_audvis_raw.fif', preload=True)

# Bandpass filter the raw EEG data
raw.filter(7., 30., fir_design='firwin', skip_by_annotation='edge')

# Create epochs
events, _ = events_from_annotations(raw)
picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude='bads')
epochs = Epochs(raw, events, event_id=None, tmin=1., tmax=3., picks=picks, baseline=None, preload=True)

# Extract data and labels
X = epochs.get_data()
y = epochs.events[:, -1]

# Apply CSP
csp = CSP(n_components=4, reg=None, log=True, norm_trace=False)
X_csp = csp.fit_transform(X, y)

# Plot the CSP patterns
csp.plot_patterns(epochs.info)

# Show the plot
plt.show()
