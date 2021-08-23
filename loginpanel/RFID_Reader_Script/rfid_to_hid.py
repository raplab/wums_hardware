#SERIAL TO HID INTERFACE 🐍
#CODE BY: TAO, RAPLAB V1.1, 28.08.2021
#-------------------------------------------------------
# pip install pyserial
# pip install pynput
#-------------------------------------------------------

import serial
import time
from pynput.keyboard import Controller

def checkRFID():
    keyboard = Controller()

    ser = serial.Serial('/dev/serial0', 9600, timeout=1)

    time.sleep(0.5)
    ser.write(b'pon') #init reader
    time.sleep(0.5)
    ser.write(b'c') #switch reader to continous mode
    ser.flushInput()
    time.sleep(0.5)
    print("RFID reader configured and ready!")

    while True:
        serial_stream = ser.readline()
        if len(serial_stream) == 16 :
            ser.write(b'.') #abort continous read
            ser.write(b's') #read single card
            serial_msg = ser.readline()
            rfid_str = serial_msg.decode("utf-8")
            rfid_str = rfid_str.rstrip()
            rfid_str += "\r"

            keyboard.type(cleanmessage)

            time.sleep(2)

            ser.flushInput()
            ser.write(b'c') #continue with continous mode!


if __name__ == "__main__":
    checkRFID()
