import serial
import keyboard
#######
#Code ini read apapun dari serial monitor kalo gaada juga tetep di print, sama time out nya ada error
# arduino = serial.Serial('COM3', 9600, timeout=.1)
# # while True:
# # 	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
# # 	print(data)
# def stop_code():
#     print("Stopping the code...")
#     arduino.close()
#     exit()

# keyboard.add_hotkey('enter', stop_code)


# while True:
#     data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
#     print(data)


try:
    arduino = serial.Serial('COM3', 9600, timeout=5)

    def stop_code():
        print("Stopping the code...")
        arduino.close()
        exit()

    keyboard.add_hotkey('enter', stop_code)

    while True:
        try:
            data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
            if data:
                print(data)
        except serial.SerialException as e:
            print(f"SerialException: {e}")
            break

except serial.SerialException as e:
    print(f"SerialException: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()