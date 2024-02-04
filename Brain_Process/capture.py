import time
import argparse
import numpy as np
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


# BoardShim.enable_dev_board_logger()

parser = argparse.ArgumentParser()
# parser.add_argument('--serial-port', type=str,
#         help='serial port', required=False, default='/dev/ttyUSB0')
parser.add_argument('--board-id', type=int,
        help='board id, check docs to get a list of supported boards', required=False, default=0) ## Cyton board ID = 0)
args = parser.parse_args()


# params = BrainFlowInputParams()
# params.ip_port = "192.168.4.1"
# params.serial_port = args.serial_port
# params.mac_address = args.mac_address
# params.other_info = args.other_info
# params.serial_number = args.serial_number
# params.ip_address = args.ip_address
# params.ip_protocol = args.ip_protocol
# params.timeout = args.timeout
# params.file = args.file
# params.master_board = args.master_board

#INI BUAT PORT SM ADDRESS CYTON + WIFI SHIELD
params = BrainFlowInputParams()
params.ip_port = 6987
params.ip_address = "192.168.4.1"
board = BoardShim(BoardIds.CYTON_WIFI_BOARD, params)
print(BoardIds.CYTON_WIFI_BOARD)
board.prepare_session()
board.start_stream()
t = 5 #WAKTU CAPTURE
time.sleep(t)
# timestamps = board.get_timestamps() #dapet data waktu
data = board.get_board_data(250*t) ## (250 Hz @ t sec) ## #SAMPLING RATE
board.stop_stream()
board.release_session()

eeg_channels = BoardShim.get_eeg_channels(args.board_id)
# eeg_names = BoardShim.get_eeg_names(args.board_id) #8-channel EEG config: Fp1, Fp2, C1, C2, P7, P8, O1 and O2
print(eeg_channels)
df = pd.DataFrame(np.transpose(data[:,1:]))
df_eeg = df[eeg_channels]
# df_eeg.columns = eeg_names
df_eeg.to_csv('braindimas.csv', sep=',', index = False) #Setiap buat data nama jangan sama
print(df_eeg)
