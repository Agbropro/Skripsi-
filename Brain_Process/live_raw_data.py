import time
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

# BoardShim.enable_dev_board_logger()

parser = argparse.ArgumentParser()
parser.add_argument('--board-id', type=int,
                    help='board id, check docs to get a list of supported boards', required=False, default=0)
args = parser.parse_args()

params = BrainFlowInputParams()
params.ip_port = 6987
params.ip_address = "192.168.4.1"
board = BoardShim(BoardIds.CYTON_WIFI_BOARD, params)
board.prepare_session()
board.start_stream()

eeg_channels = BoardShim.get_eeg_channels(args.board_id)
eeg_names = BoardShim.get_eeg_names(args.board_id)

# Set up the plot
plt.ion()
fig, ax = plt.subplots()
lines, = ax.plot([], [])

def init():
    lines.set_xdata(np.arange(250))
    lines.set_ydata(np.zeros((len(eeg_channels), 250)))
    ax.set_xlim(0, 250)
    ax.set_ylim(-500, 500)  # Update the y-axis limits based on your EEG data range
    return lines,

def update(frame):
    data = board.get_current_board_data(250)
    df = pd.DataFrame(np.transpose(data[:, 1:]))
    df_eeg = df[eeg_channels]
    lines.set_ydata(df_eeg.values)
    return lines,

ani = FuncAnimation(fig, update, init_func=init, blit=True)

try:
    plt.show()
    plt.pause(10)  # Pause for 10 seconds (or adjust as needed)
except KeyboardInterrupt:
    board.stop_stream()
    board.release_session()
    plt.ioff()
