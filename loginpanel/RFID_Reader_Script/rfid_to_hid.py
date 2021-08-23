#SERIAL TO HID INTERFACE
#CODE BY: TAO, RAPLAB V1.0, 12.09.2019
#------------------------------------------------
# pip install pyserial
# pip install pynput


import serial
import time
from pynput.keyboard import Controller

keyboard = Controller() #configure the keyboard

ser = serial.Serial('/dev/serial0') #init serial in linux '/dev/tty...'

print("RFID reader Init...")

time.sleep(0.5) #add timeout to ensure a propper handshake and avoid stalling
ser.write(b'pon')
time.sleep(0.5) #add timeout to ensure a propper handshake and avoid stalling
ser.write(b'c')
ser.flushInput() 
time.sleep(0.5) #timeout to avoid stalling of the port

print("RFID reader configured and ready!")

while True: #running the loop
    sermessage = ser.readline()
    if len(sermessage)==16:
	ser.write(b'.') #abort continous read
	time.sleep(0.1)
	ser.write(b's') #read single card
	smsg = ser.readline()
        messagestring = smsg.decode("utf-8")
        cleanmessage = messagestring.rstrip()
        cleanmessage += "\r" #this enables auto enter
	print(cleanmessage)
        keyboard.type(cleanmessage) #use the hid-keyboard to virtually type the result
        time.sleep(10) #wait in seconds - the user is turing on a machine or doing something else
	ser.flushInput()
	ser.write(b'c') #continue with continous mode!
