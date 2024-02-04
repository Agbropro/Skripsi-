import argparse
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
import time
def main():
    # Set parameters
    desired_sampling_frequency = 250  # Adjust this to your desired sampling frequency
    num_data_points = 100  # Adjust this to your desired number of data points

    # Calculate the duration needed based on the desired number of data points and sampling frequency
    duration_seconds = num_data_points / desired_sampling_frequency

    # Use synthetic board for demo
    params = BrainFlowInputParams()
    board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)
    board.prepare_session()
    board.start_stream()

    BoardShim.log_message(LogLevels.LEVEL_INFO.value, f'Capturing {num_data_points} data points at {desired_sampling_frequency} Hz')
    time.sleep(duration_seconds)

    # Get the specified number of latest data points without removing them from the internal buffer
    data = board.get_current_board_data(num_data_points)

    board.stop_stream()
    board.release_session()

    # Get EEG channels data (columns 1 to 8)
    eeg_data = data[:, 1:9]

    print("EEG Data:")
    print(eeg_data)

if __name__ == "__main__":
    main()
