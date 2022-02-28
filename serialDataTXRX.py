import binascii
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
                skinTemp = self.joinHex(self.s[4], self.s[5])
                airTemp = self.joinHex(self.s[6], self.s[7])
                # air_pressure_data_read_hex = self.joinHex(self.s[9], self.s[10])
                # shifts decimal place left
                skinTempValue = int(hex(skinTemp), 16) / 10
                airTempValue = int(hex(airTemp), 16) / 10
                setSkinTemp = self.joinHex(self.s[12], self.s[13])

                timer8 = int(hex(self.s[8]), 16)
                heaterValue = int(hex(self.s[9]), 16)
                setTempValue = int(hex(setSkinTemp), 16) / 10
                # shifts decimal place left
                # hum_data_read = int(hex(hum_data_read_hex), 16) / 10
                # air_pressure_data_read = int(hex(air_pressure_data_read_hex), 16)

                # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++
                self.ui.ui.tempLabel3.setText(str(skinTempValue))
                self.ui.ui.tempLabel4.setText(str(airTempValue))
                self.ui.ui.timerShowLabel.setText(str(timer8))
                self.ui.ui.heaterLabelShow.setText(str(heaterValue))
                self.ui.ui.setLabelSkinTemp.setText(str(setTempValue))
                # self.ui.ui.humidityShow.setText(str(hum_data_read))
                # self.ui.ui.differentialPressureShow.setText(str(air_pressure_data_read))

                heatMode14 = int(hex(self.s[14]), 16)

                mute15 = int(hex(self.s[15]), 16)

                unitValue16 = int(hex(self.s[16]), 16)

                timerON = int(hex(self.s[17]), 16)

                if heatMode14 == 0:
                    configVariables.heatModeString = "SERVO"
                elif heatMode14 == 1:
                    configVariables.heatModeString = "MANUAL"
                elif heatMode14 == 2:
                    configVariables.heatModeString = "ACCIDENTAL"
                elif heatMode14 == 3:
                    configVariables.heatModeString = "PREHEAT"

                print("Binary String: " + format(self.s[18], '08b'))

                bin1 = format(self.s[18], '08b')  # "{0:b}".format(self.s[19])  # bin(self.s[18])
                CF = bin1[7]
                highTMP = bin1[6]
                lowTMP = bin1[5]
                tmerON = bin1[4]
                systemF = bin1[3]
                probeF = bin1[2]

                bin2 = format(self.s[19], '08b')
                SET = bin2[0]
                htrON = bin2[1]
                htrFAIL = bin2[2]
                serVO = bin2[3]
                manUAL = bin2[4]
                CF2 = bin2[5]
                mutE = bin2[6]
                amtTIME = bin2[7]

                if probeF == '1':
                    self.ui.probeIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.probeIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")

                if highTMP == '1':
                    self.ui.tempHighIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.tempHighIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")
                if lowTMP == '1':
                    self.ui.tempLowIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.tempLowIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")

                if systemF == '1':
                    self.ui.systemIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.systemIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")

                if htrFAIL == '1':
                    self.ui.heaterIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.heaterIconLabel.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")

                if tmerON == '1':
                    self.ui.timerButton.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:#FF0000")
                else:
                    self.ui.timerButton.setStyleSheet("border-style: outset; padding:2px;border-radius:4px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:#00FF00")
                '''if CF == '1':
                    unitFarhenheit()
                else:
                    unitCelCius()'''

                #  String bin1 = HexToBinary(arrayHex[18]);
                self.ui.ui.heaterLabelMode.setText(str(configVariables.heatModeString))
                # configVariables.temp_read_value = temp_data_read
                # configVariables.hum_read_value = hum_data_read
                # configVariables.air_pressure_value = air_pressure_data_read
                # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++
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
