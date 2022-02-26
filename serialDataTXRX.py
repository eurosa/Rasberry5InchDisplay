import datetime
import math
import threading
import time
from multiprocessing.pool import ThreadPool

import serial

import configVariables


class SerialWrapper:
    def __init__(self, device, ui):
        self.s = None
        self.port = device
        self.ui = ui
        self.ser1 = ""
        self.my_str_as_bytes = str.encode("$I0R;")

    # def sendDataToSerialPort(self, hex_code):
    def setRepeater(self, repeater):
        self.repeater = repeater

    def getRepeater(self):
        return self.repeater

    def sendDataToSerialPort(self):
        # time.sleep(1)  # Sleep for 3 seconds

        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)

            try:
                self.ser1.write(serial.to_bytes(self.my_str_as_bytes))
                self.s = self.ser1.read(21)
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")

            configVariables.hex_string = self.s

            if self.s:
                print(str(self.s[0]) + " " +
                      str(self.s[1]) + " " +
                      str(self.s[2]) + " " +
                      str(self.s[3]) + " " +
                      str(self.s[4]) + " " +
                      str(self.s[5]) + " " +
                      str(self.s[6]) + " " +
                      str(self.s[7]) + " " +
                      str(self.s[8]) + " " +
                      str(self.s[9]) + " " +
                      str(self.s[10]) + " " +
                      str(self.s[11]) + " " +
                      str(self.s[12]) + " " +
                      str(self.s[13]) + " " +
                      str(self.s[14]) + " " +
                      str(self.s[15]) + " " +
                      str(self.s[16]) + " " +
                      str(self.s[17]) + " " +
                      str(self.s[18]) + " " +
                      str(self.s[19]) + " " +
                      str(self.s[20]))

            if configVariables.hex_string:
                time.sleep(0.5)  # Sleep for 3 seconds
                self.ser1.close()
                # time.sleep(0.5)

        except:
            print("An Exception occurred /dev/ttyUSB0 not found")

    def joinHex(self, low, high):
        sizeof_high = 0
        # get size of b in bits
        while int(hex(high), 16) >> sizeof_high > 0:
            sizeof_high += 1

        # every position in hex in represented by 4 bits
        sizeof_high_hex = math.ceil(sizeof_high / 4) * 4
        low_data = int(hex(low), 16)
        high_data = int(hex(high), 16)
        hex_data = hex((low_data << sizeof_high_hex) | high_data)
        print(str(hex_data))
        return int(hex_data, 16)

    def bytes1(self, num):
        return hex(num >> 8), hex(num & 0xFF)


def main():
    SerialWrapper('/dev/ttyUSB0')
    # ser = SerialWrapper('/dev/ttyUSB0')
    # ser1 = serial.Serial("COM5", 9600)

    # sudo usermod -a -G dialout $USER
