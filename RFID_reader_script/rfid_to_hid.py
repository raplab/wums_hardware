# RFID-SERIAL TO HID INTERFACE
# CODE BY: TAO, RAPLAB V1.1, 12.01.2022
# ------------------------------------------------
# pip install pyserial
# pip install pynput

import serial
import time
from pynput.keyboard import Controller

# seconds the script waits after successfully reading a card...
delay = 10


def reformat_card(card):
    """
    Takes RFID-Number String and returns cleaned result
    """
    rfid = card.decode("utf-8")
    clean_card = rfid.rstrip()
    clean_card += "\r"
    return clean_card


def loop(ser, hid):
    """
    Checks for new cards and writes the results to a text field
    """
    while True:
        rfid_code_raw = ser.readline()
        if len(rfid_code_raw) == 16:
            ser.write(b'.')  # abort continues read
            time.sleep(0.1)
            ser.write(b's')  # read single card
            rfid_code = ser.readline()
            rfid_clean = reformat_card(rfid_code)
            hid.type(rfid_clean)  # use the hid-keyboard to virtually type the result
            time.sleep(delay)  # wait in seconds - the user is turing on a machine or doing something else
            ser.flushInput()
            ser.write(b'c')  # continue with continuous mode!


if __name__ == '__main__':
    # configure the keyboard
    keyboard = Controller()

    # init serial in linux '/dev/tty...'
    serial_connection = serial.Serial('/dev/serial0')

    print("RFID reader Init...")

    serial_connection.write(b'pon')
    time.sleep(0.5)
    serial_connection.write(b'c')
    serial_connection.flushInput()
    time.sleep(0.5)

    print("RFID reader configured and ready!")

    loop(serial_connection, hid)
