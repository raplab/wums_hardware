
try:
  import usocket as socket
except:
  import socket

from machine import Pin
from time import sleep
import network
import esp

esp.osdebug(None)

import gc
gc.collect()

ssid = 'your-network'
password = 'your-password'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

pinmap = {
  "D0": 16,
  "D1": 5,
  "D2": 4,
  "D3": 0,
  "D4": 2,
  "D5": 14,
  "D6": 12,
  "D7": 13,
  "D8": 15
}

tool_00 = Pin(pinmap["D0"], Pin.OUT)
tool_01 = Pin(pinmap["D1"], Pin.OUT)
tool_02 = Pin(pinmap["D2"], Pin.OUT)
tool_03 = Pin(pinmap["D3"], Pin.OUT)
tool_04 = Pin(pinmap["D4"], Pin.OUT)
tool_05 = Pin(pinmap["D5"], Pin.OUT)
tool_06 = Pin(pinmap["D6"], Pin.OUT)
tool_07 = Pin(pinmap["D7"], Pin.OUT)
tool_08 = Pin(pinmap["D8"], Pin.OUT)

tool_00.value(1)
tool_01.value(1)
tool_02.value(1)
tool_03.value(1)
tool_04.value(1)
tool_05.value(1)
tool_06.value(1)
tool_07.value(1)
