import serial.tools.list_ports
import time

# Get the list of available ports
ports = serial.tools.list_ports.comports()

# Print the available ports
for port in ports:
    print(str(port))

# Select the port (you can modify this based on your requirements)
port_var = input('Select Port: ')

# Create a serial instance
serial_inst = serial.Serial(port=port_var, baudrate=9600, timeout=1)

# Wait for a moment to ensure the Arduino is ready
time.sleep(2)

# Send data to Arduino indefinitely
while True:
    data_to_send = "Hello, Arduino!\n"
    serial_inst.write(data_to_send.encode())
    time.sleep(2)
