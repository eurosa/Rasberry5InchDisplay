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
        if configVariables.checkSendReceive:
            try:
                self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
                try:
                    self.ser1.write(serial.to_bytes(self.my_str_as_bytes))
                    self.s = self.ser1.read(21)
                except Exception as e:
                    print("--- abnormal read and write from port serialDataTXRX---：", e)
                    print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")
                self.receiveData()
                time.sleep(0.5)  # Sleep for 3 seconds
                self.ser1.close()
            except Exception as e:
                print(e)

    def receiveData(self):
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

        if self.s:
            skinTemp1 = int(hex(self.s[4]), 16)
            skinTemp2 = int(hex(self.s[5]), 16)
            tempValue = (skinTemp1 << 8) | skinTemp2

            airTemp1 = int(hex(self.s[6]), 16)
            airTemp2 = int(hex(self.s[7]), 16)
            airValue = (airTemp1 << 8) | airTemp2

            # skinTemp = self.joinHex(self.s[4], self.s[5])
            # airTemp = self.joinHex(self.s[6], self.s[7])
            # air_pressure_data_read_hex = self.joinHex(self.s[9], self.s[10])
            # shifts decimal place left
            # skinTempValue = int(hex(skinTemp), 16) / 10
            # airTempValue = int(hex(airTemp), 16) / 10
            setSkinTemp = self.joinHex(self.s[12], self.s[13])
            timer8 = int(hex(self.s[8]), 16)
            heaterValue = int(hex(self.s[9]), 16)
            setTempValue = int(hex(setSkinTemp), 16) / 10
            # shifts decimal place left
            # hum_data_read = int(hex(hum_data_read_hex), 16) / 10
            # air_pressure_data_read = int(hex(air_pressure_data_read_hex), 16)

            # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++
            self.ui.ui.tempLabel3.setText(str(tempValue / 10))
            self.ui.ui.tempLabel4.setText(str(airValue / 10))
            #  self.ui.ui.timerShowLabel.setText(str(timer8))
            self.ui.ui.heaterLabelShow.setText(str(heaterValue))
            self.ui.ui.setLabelSkinTemp.setText(str(setTempValue))
            # self.ui.ui.humidityShow.setText(str(hum_data_read))
            # self.ui.ui.differentialPressureShow.setText(str(air_pressure_data_read))

            configVariables.heatMode14 = int(hex(self.s[14]), 16)
            configVariables.setTempLow = int(hex(self.s[12]), 16)
            configVariables.setTempHigh = int(hex(self.s[13]), 16)

            configVariables.mute15 = int(hex(self.s[15]), 16)

            unitValue16 = int(hex(self.s[16]), 16)

            timerON = int(hex(self.s[17]), 16)

            if configVariables.heatMode14 == 0:
                configVariables.heatModeString = "SERVO"
            elif configVariables.heatMode14 == 1:
                configVariables.heatModeString = "MANUAL"
            elif configVariables.heatMode14 == 2:
                configVariables.heatModeString = "ACCIDENTAL"
            elif configVariables.heatMode14 == 3:
                configVariables.heatModeString = "PREHEAT"
            binLowSkinTemp = bin(int(format(self.s[4])))  # int result = (first << 4) | second;
            binHighSkinTemp = bin(int(format(self.s[5])))  # int result = (first << 4) | second;

            result = int(f'0b{self.s[4]:08b}', 2) << 4 | int(f'0b{self.s[5]:08b}', 2)
            # "{0:b}".format(configVariables.hex_string[4])#   print("Binary String1: " + f'0b{self.s[18]:08b}')

            print(result)  # "{0:b}".format(configVariables.hex_string[4])

            bin1 = f'{self.s[18]:08b}'  # format(self.s[18], '08b')  # "{0:b}".format(self.s[19])  # bin(self.s[18])

            highTMP = bin1[6]
            lowTMP = bin1[5]
            configVariables.tmerON = bin1[4]
            systemF = bin1[2]
            probeF = bin1[1]
            CF = bin1[0]

            bin2 = f'0b{self.s[19]:08b}'
            print(str(highTMP))
            print(str(lowTMP))
            print(str(systemF))
            print("Mute value: "+str(configVariables.mute15))
            print(str(probeF))
            print(str(CF))
            print("Binary String1: " + f'{self.s[18]:08b}')  # "{0:b}".format(configVariables.hex_string[4])
            print("Binary String2: " + f'0b{self.s[19]:08b}')  # "{0:b}".format(configVariables.hex_string[4])
            # bin2 = format(self.s[19], '08b')
            SET = bin2[0]
            htrON = bin2[1]
            htrFAIL = bin2[2]
            serVO = bin2[3]
            manUAL = bin2[4]
            CF2 = bin2[5]
            mutE = bin2[6]
            amtTIME = bin2[7]

            x7 = bin(0b10000000)
            x6 = bin(0b01000000)
            x5 = bin(0b00100000)
            x4 = bin(0b00010000)
            x3 = bin(0b00001000)
            x2 = bin(0b00000100)
            x1 = bin(0b00000010)
            x0 = bin(0b00000001)
            x8 = bin(0b00000100)
            x9 = bin(0b0010)
            x10 = bin(0b0100)
            x11 = bin(0b1000)
            x12 = bin(0b00100000)  # 100000
            x13 = bin(0b00010000)  # 100000

            bit7 = bool(int(bin1, 2) & int(x7, 2))
            bit5 = bool(int(bin1, 2) & int(x5, 2))  # highTMP = bin1[5]
            bit4 = bool(int(bin1, 2) & int(x4, 2))  # lowTMP = bin1[4]
            bit3 = bool(int(bin1, 2) & int(x3, 2))  # tmerON = bin1[3]
            bit2 = bool(int(bin1, 2) & int(x2, 2))  # systemF = bin1[2]
            bit1 = bool(int(bin1, 2) & int(x1, 2))  # probeF = bin1[1]
            bit0 = bool(int(bin1, 2) & int(x0, 2))  # CF = bin1[0]
            bit8 = bool(int(bin2, 2) & int(x2, 2))  # htrFAIL = bin2[2]

            if bit1:
                self.ui.ui.probeIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#FF0000; "
                    "border-color:beige}")
            else:
                self.ui.ui.probeIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px; border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#00A36C; "
                    "border-color:beige}")

            if bit2:
                self.ui.ui.systemIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")
            else:
                self.ui.ui.systemIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#00FF00; "
                    "border-color:beige}")
            if bit3:
                self.ui.ui.timerButton.setStyleSheet("QToolButton{border-style: outset; border-width: "
                                                     "1px;border-radius:10px; font: bold 14px; "
                                                     "border-width: 2px; background-color:#FF0000; "
                                                     "border-color:beige}")
            else:
                self.ui.ui.timerButton.setStyleSheet("QToolButton{border-style: outset; border-width: "
                                                     "1px;border-radius:10px; font: bold 14px; "
                                                     "border-width: 2px; background-color:#00FF00; "
                                                     "border-color:beige}")
            if bit4:
                self.ui.ui.tempLowIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                          "1px;border-radius:10px; font: bold 14px; "
                                                          "border-width: 2px; background-color:#FF0000; "
                                                          "border-color:beige}")
            else:
                self.ui.ui.tempLowIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#00FF00; "
                    "border-color:beige}")

            if bit5:
                self.ui.ui.tempHighIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                           "1px;border-radius:10px; font: bold 14px; "
                                                           "border-width: 2px; background-color:#FF0000; "
                                                           "border-color:beige}")
            else:
                self.ui.ui.tempHighIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                           "1px;border-radius:10px; font: bold 14px; "
                                                           "border-width: 2px; background-color:#00FF00; "
                                                           "border-color:beige}")

            if bit8:
                self.ui.ui.heaterIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")
            else:
                self.ui.ui.heaterIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:beige}")

            print(self.append_hex(self.s[4], self.s[5]))
            if bit0:
                pass
                # unitFarhenheit()
            else:
                pass
                # unitCelCius()

            self.ui.ui.heaterLabelMode.setText(str(configVariables.heatModeString))


            # time.sleep(0.5)



    def decimalToBinary(self, n):
        return bin(n).replace("0b", "")

    def append_hex(self, a, b):
        sizeof_b = 0

        # get size of b in bits
        while (b >> sizeof_b) > 0:
            sizeof_b += 1

        # align answer to nearest 4 bits (hex digit)
        sizeof_b += sizeof_b % 4

        return int(str((a << sizeof_b) | b), 16)

    def eightBitBinary(self, value):
        bnr = bin(value)
        x = bnr[::-1]  # this reverses an array
        while len(x) < 8:
            x += '0'
        bnr = x[::-1]
        print(bnr)

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
        print(int(hex_data, 16))
        return int(hex_data, 16)

    def bytes1(self, num):
        return hex(num >> 8), hex(num & 0xFF)


def main():
    SerialWrapper('/dev/ttyUSB0')
    # ser = SerialWrapper('/dev/ttyUSB0')
    # ser1 = serial.Serial("COM5", 9600)

    # sudo usermod -a -G dialout $USER
