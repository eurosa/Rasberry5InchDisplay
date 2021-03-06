import binascii
import datetime
import math
import threading
import time
from multiprocessing.pool import ThreadPool

import serial
from PyQt5 import QtGui

import configVariables


class SerialWrapper:
    def __init__(self, device, ui, dataModel):
        self.s = None
        self.port = device
        self.ui = ui
        self.model = dataModel
        self.ser1 = ""
        self.skinV = 0
        self.airV = 0
        self.my_str_as_bytes = str.encode("$I0R;")
        self.time_count = 0
        self.heaterValue = 0
        self.setTempValue = 0
        self.air_cal_point = 0
        self.skin_cal_point = 0
        self.set_temp_skin = 0
        self.skin_cal_check = 0
        self.air_cal_check = 0
        self.oldTime = time.time()

    # def sendDataToSerialPort(self, hex_code):
    def setRepeater(self, repeater):
        self.repeater = repeater

    def getRepeater(self):
        return self.repeater

    def sendDataToSerialPort(self):
        # time.sleep(1)  # Sleep for 3 seconds
        print(configVariables.receiveFlag)
        if configVariables.checkSendReceive:

            try:
                self.ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600,
                                          write_timeout=1)
                # print("**************************First reading received data ***********************************")
                try:
                    self.ser1.write(serial.to_bytes(self.my_str_as_bytes))
                    configVariables.hex_string = self.ser1.read(21)
                except Exception as e:
                    self.time_count = self.time_count + 1
                    print("--- abnormal read and write from port serialDataTXRX---：", e)
                    # print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")
                # self.receiveData()
                time.sleep(0.5)  # Sleep for 3 seconds
                self.time_count = 0
                self.ser1.close()
                configVariables.receiveFlag = True
            except Exception as e:
                self.time_count = self.time_count + 1
                self.ui.ui.systemLabelFail.setText("System Fail")
                self.ui.ui.systemIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")
                print("--- usb port serialDataTXRX---：", e)

    def receiveData(self):
        if configVariables.hex_string:
            skinTemp1 = int(hex(configVariables.hex_string[4]), 16)
            skinTemp2 = int(hex(configVariables.hex_string[5]), 16)
            tempValue = (skinTemp1 << 8) | skinTemp2

            airTemp1 = int(hex(configVariables.hex_string[6]), 16)
            airTemp2 = int(hex(configVariables.hex_string[7]), 16)
            airValue = (airTemp1 << 8) | airTemp2

            # skinTemp = self.joinHex(self.s[4], self.s[5])
            # airTemp = self.joinHex(self.s[6], self.s[7])
            # air_pressure_data_read_hex = self.joinHex(self.s[9], self.s[10])
            # shifts decimal place left
            # skinTempValue = int(hex(skinTemp), 16) / 10
            # airTempValue = int(hex(airTemp), 16) / 10

            bin1 = f'{configVariables.hex_string[18]:08b}'  # format(self.s[18], '08b')  # "{0:b}".format(self.s[19])
            # bin(self.s[18])

            CF = bin1[0]
            highTMP = bin1[1]
            lowTMP = bin1[2]
            configVariables.tmerON = bin1[3]
            systemF = bin1[4]
            probeF = bin1[5]

            bin2 = f'0b{configVariables.hex_string[19]:08b}'

            print(
                "Binary String1: " + f'{configVariables.hex_string[18]:08b}')  # "{0:b}".format(configVariables.hex_string[4])
            print(
                "Binary String2: " + f'{configVariables.hex_string[19]:08b}')  # "{0:b}".format(configVariables.hex_string[4])"Binary String2: " + f'0b{configVariables.hex_string[19]:08b}')
            self.time_count = 0
            self.ui.ui.systemLabelFail.setText("System Ok")
            self.ui.ui.systemIconLabel.setStyleSheet(
                "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                "border-width: 2px; background-color:#00FF00; "
                "border-color:beige}")

            # bin2 = format(self.s[19], '08b')

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
            bit5 = bool(int(bin1, 2) & int(x5, 2))  # probeF = bin1[5]
            bit4 = bool(int(bin1, 2) & int(x4, 2))  # systemF = bin1[4]
            bit3 = bool(int(bin1, 2) & int(x3, 2))  # tmerON = bin1[3]
            bit2 = bool(int(bin1, 2) & int(x2, 2))  # lowTMP = bin1[2]
            bit1 = bool(int(bin1, 2) & int(x1, 2))  # highTMP = bin1[1]
            bit0 = bool(int(bin1, 2) & int(x0, 2))  # CF = bin1[0]
            amtTIME = bool(int(bin2, 2) & int(x7, 2))  # htrFAIL = bin2[2]
            mutE = bool(int(bin2, 2) & int(x6, 2))  # htrFAIL = bin2[2]
            CF2 = bool(int(bin2, 2) & int(x5, 2))  # htrFAIL = bin2[2]
            manUAL = bool(int(bin2, 2) & int(x4, 2))  # htrFAIL = bin2[2]
            serVO = bool(int(bin2, 2) & int(x3, 2))  # htrFAIL = bin2[2]
            htrFAIL = bool(int(bin2, 2) & int(x2, 2))  # htrFAIL = bin2[2]
            htrON = bool(int(bin2, 2) & int(x1, 2))  # htrFAIL = bin2[2]
            fanFAIL = bool(int(bin2, 2) & int(x0, 2))  # htrFAIL = bin2[2]

            # setSkinTemp = self.joinHex(configVariables.hex_string[12], configVariables.hex_string[13])
            setTemp1 = int(hex(configVariables.hex_string[12]), 16)
            setTemp2 = int(hex(configVariables.hex_string[13]), 16)
            setSkinTemp = (setTemp1 << 8) | setTemp2

            timer8 = int(hex(configVariables.hex_string[8]), 16)
            self.heaterValue = int(hex(configVariables.hex_string[9]), 16)
            self.setTempValue = int(hex(setSkinTemp), 16) / 10
            self.set_temp_skin = int(hex(setSkinTemp), 16)
            # shifts decimal place left
            # hum_data_read = int(hex(hum_data_read_hex), 16) / 10
            # air_pressure_data_read = int(hex(air_pressure_data_read_hex), 16)

            # ++++++++++++++++++++ Temp , Humidity, Pressure UI update +++++++++++++++++++
            tempValue = tempValue / 10
            airValue = airValue / 10
            if bit0:
                self.ui.ui.skinTempUnit.setText("°F")
                self.ui.ui.airTempUnit.setText("°F")
                self.ui.ui.unitChangeToolButton.setText("°C")
                self.skinV = (5 / 9) * (tempValue - 32)
                self.airV = (5 / 9) * (airValue - 32)  # Celcius °C
                self.air_cal_point = ((9 / 5) * (float(self.model.get_air_cal_point()) / 10))
                self.skin_cal_point = ((9 / 5) * (float(self.model.get_skin_cal_point()) / 10))
                self.skin_cal_check = float(self.model.get_skin_cal_point()) / 10
                self.air_cal_check = float(self.model.get_air_cal_point()) / 10

            else:
                self.ui.ui.skinTempUnit.setText("°C")
                self.ui.ui.airTempUnit.setText("°C")
                self.ui.ui.unitChangeToolButton.setText("°F")
                self.skinV = tempValue
                self.airV = airValue
                self.air_cal_point = (float(self.model.get_air_cal_point()) / 10)
                self.skin_cal_point = (float(self.model.get_skin_cal_point()) / 10)
                self.skin_cal_check = float(self.model.get_skin_cal_point()) / 10
                self.air_cal_check = float(self.model.get_air_cal_point()) / 10

            # print(" Air Temp:" + str(airValue - float(self.model.get_air_temp()) / 10) + " Skin temp: " + str(
            #   tempValue - float(self.model.get_skin_temp()) / 10))

            if self.skinV + self.skin_cal_check < float(self.model.get_skin_temp()) / 10 - 1.0:
                self.ui.ui.tempHighLabel.setText("Skin Low")
                self.ui.ui.tempHighIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                           "1px;border-radius:10px; font: bold 14px; "
                                                           "border-width: 2px; background-color:#FF0000; "
                                                           "border-color:beige}")
            elif float(self.model.get_skin_temp()) / 10 + 1.0 < self.skinV + self.skin_cal_check:
                self.ui.ui.tempHighLabel.setText("Skin High")
                self.ui.ui.tempHighIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                           "1px;border-radius:10px; font: bold 14px; "
                                                           "border-width: 2px; background-color:#FF0000; "
                                                           "border-color:beige}")
            else:
                self.ui.ui.tempHighLabel.setText("Skin Ok")
                self.ui.ui.tempHighIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                           "1px;border-radius:10px; font: bold 14px; "
                                                           "border-width: 2px; background-color:#00FF00; "
                                                           "border-color:beige}")

            if self.airV + self.air_cal_check < float(self.model.get_air_temp()) / 10 - 1.0:
                self.ui.ui.tempLowLabel.setText("Air Low")
                self.ui.ui.tempLowIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                          "1px;border-radius:10px; font: bold 14px; "
                                                          "border-width: 2px; background-color:#FF0000; "
                                                          "border-color:beige}")
            elif float(self.model.get_air_temp()) / 10 + 1.0 < self.airV + self.air_cal_check:
                self.ui.ui.tempLowLabel.setText("Air High")
                self.ui.ui.tempLowIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                          "1px;border-radius:10px; font: bold 14px; "
                                                          "border-width: 2px; background-color:#FF0000; "
                                                          "border-color:beige}")
            else:
                self.ui.ui.tempLowLabel.setText("Air Ok")
                self.ui.ui.tempLowIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                          "1px;border-radius:10px; font: bold 14px; "
                                                          "border-width: 2px; background-color:#00FF00; "
                                                          "border-color:beige}")

            if 10 < self.skinV < 50:
                self.ui.ui.tempLabel3.setText(str("{:.1f}".format(tempValue + self.skin_cal_point)))

            else:
                self.ui.ui.probeIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                        "1px;border-radius:10px; font: bold 14px; "
                                                        "border-width: 2px; background-color:#FF0000; "
                                                        "border-color:beige}")
                self.ui.ui.tempLabel3.setText("Error")

            if 10 < self.airV < 50:
                self.ui.ui.tempLabel4.setText(str("{:.1f}".format(airValue + self.air_cal_point)))

            else:
                self.ui.ui.probeIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                        "1px;border-radius:10px; font: bold 14px; "
                                                        "border-width: 2px; background-color:#FF0000; "
                                                        "border-color:beige}")
                self.ui.ui.tempLabel4.setText("Error")

            if 10 < self.skinV < 50:
                if 10 < self.airV < 50:
                    self.ui.ui.probeIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                            "1px;border-radius:10px; font: bold 14px; "
                                                            "border-width: 2px; background-color:#00FF00; "
                                                            "border-color:beige}")

            #  self.ui.ui.timerShowLabel.setText(str(timer8))

            # self.ui.ui.humidityShow.setText(str(hum_data_read))
            # self.ui.ui.differentialPressureShow.setText(str(air_pressure_data_read))

            configVariables.heatMode14 = int(hex(configVariables.hex_string[14]), 16)
            configVariables.setTempLow = int(hex(configVariables.hex_string[12]), 16)
            configVariables.setTempHigh = int(hex(configVariables.hex_string[13]), 16)

            configVariables.mute15 = int(hex(configVariables.hex_string[15]), 16)

            configVariables.unitValue = int(hex(configVariables.hex_string[16]), 16)

            timerON = int(hex(configVariables.hex_string[17]), 16)
            set_temp_database = int(float(self.model.get_skin_temp()))
            db_heater_value = int(float(self.model.get_heater_output()))
            print("Heater_database: " + str(db_heater_value) + " CI=ircuit " + str(self.heaterValue) + " " + str(
                configVariables.hex_string[9]))
            print("$I0W" + str(configVariables.hex_string[12]) + " " + str(configVariables.hex_string[13]) + " " + str(
                configVariables.hex_string[14]) + " " + str(configVariables.hex_string[15]) + " " + str(
                configVariables.hex_string[16]) + " " + str(configVariables.hex_string[17]) + " " + str(
                configVariables.hex_string[9]) + ";")
            if self.set_temp_skin != set_temp_database:
                try:
                    self.decimalToHex(int(float(self.model.get_skin_temp())))
                except Exception as e:
                    print(e)

            if configVariables.heatMode14 == 0:
                configVariables.heatModeString = "SERVO"
            elif configVariables.heatMode14 == 1:
                configVariables.heatModeString = "MANUAL"
                if (configVariables.hex_string[9] != int(float(self.model.get_heater_output()))) and \
                        configVariables.hex_string[9] != 0:
                    try:
                        self.heater_set(db_heater_value)
                    except Exception as e:
                        print(e)
            elif configVariables.heatMode14 == 2:
                configVariables.heatModeString = "ACCIDENTAL"
            elif configVariables.heatMode14 == 3:
                configVariables.heatModeString = "PREHEAT"
            # binLowSkinTemp = bin(int(format(configVariables.hex_string[4])))  # int result = (first << 4) | second;
            # binHighSkinTemp = bin(int(format(configVariables.hex_string[5])))  # int result = (first << 4) | second;

            # result = int(f'0b{configVariables.hex_string[4]:08b}', 2) << 4 | int(
            #   f'0b{configVariables.hex_string[5]:08b}', 2)
            # "{0:b}".format(configVariables.hex_string[4])#   print("Binary String1: " + f'0b{self.s[18]:08b}')

            # print(result)  # "{0:b}".format(configVariables.hex_string[4])

            if configVariables.mute15:
                icon9 = QtGui.QIcon()
                icon9.addPixmap(QtGui.QPixmap("/home/pi/icon/speaker-off-white.png"), QtGui.QIcon.Normal,
                                QtGui.QIcon.On)
                self.ui.ui.muteToolButton.setIcon(icon9)
            else:
                icon9 = QtGui.QIcon()
                icon9.addPixmap(QtGui.QPixmap("/home/pi/icon/speaker-on-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.ui.ui.muteToolButton.setIcon(icon9)

            if bit5:
                self.ui.ui.probeIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#FF0000; "
                    "border-color:beige}")
            else:
                self.ui.ui.probeIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px; border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#00FF00; "
                    "border-color:beige}")

            """
            if bit4:
                self.ui.ui.systemIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")
            else:
                self.ui.ui.systemIconLabel.setStyleSheet(
                    "QLabel{border-style: outset; border-width: 1px;border-radius:10px; font: bold 14px; "
                    "border-width: 2px; background-color:#00FF00; "
                    "border-color:beige}")
            """

            if htrFAIL:
                self.ui.ui.heaterIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")
            else:
                self.ui.ui.heaterIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#00FF00; "
                                                         "border-color:beige}")
            if htrON:
                self.ui.ui.powerLabelFail.setText("Heater On")
                self.ui.ui.powerIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                        "1px;border-radius:10px; font: bold 14px; "
                                                        "border-width: 2px; background-color:#00FF00; "
                                                        "border-color:beige}")
            else:
                self.ui.ui.powerLabelFail.setText("Heater Off")
                self.heaterValue = 0
                self.ui.ui.powerIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                        "1px;border-radius:10px; font: bold 14px; "
                                                        "border-width: 2px; background-color:#FF0000; "
                                                        "border-color:beige}")
            if fanFAIL:
                self.ui.ui.fanFailLabel.setText("Fan Fail")
                self.ui.ui.fanFailIcon.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                     "1px;border-radius:10px; font: bold 14px; "
                                                     "border-width: 2px; background-color:#FF0000; "
                                                     "border-color:beige}")
            else:
                self.ui.ui.fanFailLabel.setText("Fan Ok")
                self.ui.ui.fanFailIcon.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                     "1px;border-radius:10px; font: bold 14px; "
                                                     "border-width: 2px; background-color:#00FF00; "
                                                     "border-color:beige}")

            # print(self.append_hex(configVariables.hex_string[4], configVariables.hex_string[5]))

            self.ui.ui.heaterLabelMode.setText(str(configVariables.heatModeString))
        else:
            print("No Data received")
            """self.time_count = self.time_count + 1
            if self.time_count > 5:
                self.ui.ui.systemLabelFail.setText("System Fail")
                self.ui.ui.systemIconLabel.setStyleSheet("QLabel{border-style: outset; border-width: "
                                                         "1px;border-radius:10px; font: bold 14px; "
                                                         "border-width: 2px; background-color:#FF0000; "
                                                         "border-color:beige}")"""
        self.ui.ui.heaterLabelShow.setText(str(self.heaterValue))
        self.ui.ui.setLabelSkinTemp.setText("{:.1f}".format(self.setTempValue))

        # check
        if configVariables.heatMode14 == 1:
            if self.heaterValue > 60:
                if configVariables.heatMode14 == 1:
                    print(
                        str(self.heaterValue) + "++++++++++++++++++++++++++++++++++++++++++++")
                    if time.time() - self.oldTime > 600:
                        self.heaterOnOffServoMode()
                        print(
                            "------------------------------------------------------------it's been a "
                            "minute-----------------------------------------------------------------------------------")
        else:
            self.oldTime = time.time()
            # time.sleep(0.5)

    def decimalToHex(self, value):
        hexValue = int(hex(value), 16)
        firstPart = hexValue >> 8
        secondPart = hexValue & 0xFF
        self.setPoint(firstPart, secondPart)
        skinTemp1 = int(hex(firstPart), 16)
        skinTemp2 = int(hex(secondPart), 16)
        tempValue = (skinTemp1 << 8) | skinTemp2

    def setPoint(self, firstPart, secondPart):
        configVariables.checkSendReceive = False
        data = str.encode("$I0W" + chr(firstPart) + chr(secondPart) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + chr(
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + chr(
            configVariables.hex_string[9]) + ";")

        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                                      write_timeout=1, timeout=0)
            try:
                self.ser1.write(serial.to_bytes(data))
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")
            # time.sleep(0.5)  # Sleep for 3 seconds
            self.ser1.close()
        except Exception as e:
            print(e)
        configVariables.checkSendReceive = True

    def heaterOnOffServoMode(self):
        configVariables.checkSendReceive = False
        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + chr(
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + chr(0) + ";")

        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                                      write_timeout=1, timeout=0)
            try:
                self.ser1.write(serial.to_bytes(data))
                configVariables.hex_string = self.ser1.read(21)
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")
            # time.sleep(0.5)  # Sleep for 3 seconds
            self.ser1.close()
        except Exception as e:
            print(e)
        configVariables.checkSendReceive = True

    def heater_set(self, value):
        configVariables.checkSendReceive = False
        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + chr(
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + chr(value) + ";")

        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                                      write_timeout=1, timeout=0)
            try:
                self.ser1.write(serial.to_bytes(data))
                configVariables.hex_string = self.ser1.read(21)
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")
            # time.sleep(0.5)  # Sleep for 3 seconds
            self.ser1.close()
        except Exception as e:
            print(e)
        configVariables.checkSendReceive = True

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
        # print(bnr)

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
        # print(str(hex_data))
        # print(int(hex_data, 16))
        return int(hex_data, 16)

    def bytes1(self, num):
        return hex(num >> 8), hex(num & 0xFF)


def main():
    SerialWrapper('/dev/ttyUSB0')
    # ser = SerialWrapper('/dev/ttyUSB0')
    # ser1 = serial.Serial("COM5", 9600)

    # sudo usermod -a -G dialout $USER
