# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import enum
import os
import shlex
import signal
import subprocess
import threading
import time
import serial
# from past.builtins import unicode
# from past.types import long

import configVariables
import servoManualSetPointDialog
import timerCounter
from MessageBox import AutoCloseMessageBox
import sys
from Database import database
from Database.dataModel import DataModel
from PyQt5.QtSql import QSqlQueryModel

from StringBuilder import StringBuilder
from WorkerThread import Worker
from serialDataTXRX import SerialWrapper
from virtual_keyboard import *
# This gets the Qt stuff
import PyQt5
import mainwindow_auto
import setPointDialog
import patientDetailsForm
import settingWindow
from repeatedTimer import RepeatedTimer
import self as self
from PyQt5.QtCore import QTime, QTimer, Qt, QPoint, QAbstractListModel, pyqtSignal, QSize, QUrl, pyqtSlot, QEvent, QDate
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

dir_path = os.path.dirname(os.path.realpath(__file__))


class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    def ventilationOpen(self):
        pass

    def __init__(self):
        super(self.__class__, self).__init__()
        # ========================Start of Database Management===============================================
        self.dataModel = DataModel()
        self.database_manage = database.DataBaseManagement()
        self.database_manage.init('datafile', 'QSQLITE')
        self.database_manage.queryGeneralSettingsData(self.dataModel)
        self.ui = mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)  # gets defined in the UI file
        self.startNew = 1
        self.startNew_form = 1
        self.typing_timer = QtCore.QTimer()
        self.typing_timer.setSingleShot(True)
        self.typing_timer.timeout.connect(self.make_changes)

        self.typing_timer_2 = QtCore.QTimer()
        self.typing_timer_2.setSingleShot(True)
        self.typing_timer_2.timeout.connect(self.make_changes_patient_form)

        self.ui.patientDetailsToolButton.clicked.connect(self.patientDetailsDialogOpen)
        self.ui.patientIdLineEdit.textChanged.connect(self.start_typing_timer)
        self.ui.patientIdLineEdit.textChanged.connect(self.delete_previous)
        self.ui.unitChangeToolButton.clicked.connect(self.unitConverter)
        self.ui.muteToolButton.clicked.connect(self.muteControl)
        self.ui.heaterLabelMode.clicked.connect(self.servManControl)

        self.clickable(self.ui.heaterLabelShow).connect(self.servManSetDialog)
        self.servoManualDialog = servoManualSetPointDialog.Ui_servoManualSetPointForm()
        self.setServManDialog = QMainWindow()
        self.servoManualDialog.setupUi(self.setServManDialog)

        self.servoManualDialog.okHeaterBtn.clicked.connect(self.updateSetHeaterOutput)
        self.servoManualDialog.cancelHeaterBtn.clicked.connect(self.closeHeaterDialog)
        self.servoManualDialog.heaterUpToolBtn.clicked.connect(self.incHeaterOutput)
        self.servoManualDialog.heaterDownToolBtn.clicked.connect(self.decHeaterOutput)

        self.patientWindow = QMainWindow()
        self.patientWindowForm = patientDetailsForm.Ui_patientFormWindow()
        self.patientWindowForm.setupUi(self.patientWindow)
        self.patientWindowForm.cancelToolButton.clicked.connect(self.closePatientForm)

        self.ui.setPointBtn.clicked.connect(self.setPointDialogBox)
        self.setPointDialog = setPointDialog.Ui_setPointForm()
        self.setDialog = QMainWindow()
        self.setPointDialog.setupUi(self.setDialog)

        self.settingWindow = QMainWindow()
        self.settingWindowUi = settingWindow.Ui_patientFormWindow()
        self.settingWindowUi.setupUi(self.settingWindow)
        self.settingWindowUi.cancelCal.clicked.connect(self.closeSettingWindow)
        self.ui.openSettingDialog.clicked.connect(self.openSettingWindow)
        self.settingWindowUi.okCal.clicked.connect(self.saveSettingData)

        self.setPointDialog.okBtn.clicked.connect(self.updateSetPointData)
        self.setPointDialog.cancelBtn.clicked.connect(self.closeSetPointDialog)
        # self.setStyleSheet("background-color: yellow;")
        self.skin_temp = float(self.dataModel.get_skin_temp())
        self.air_temp = float(self.dataModel.get_air_temp())

        self.skin_low_temp = float(self.dataModel.get_skin_low_temp())
        self.skin_high_temp = float(self.dataModel.get_skin_high_temp())
        self.air_low_temp = float(self.dataModel.get_air_low_temp())
        self.air_high_temp = float(self.dataModel.get_air_high_temp())

        self.heater_output = float(self.dataModel.get_heater_output())
        self.setPointDialog.tempLabel1.setText("{:.1f}".format(self.skin_temp / 10))
        self.setPointDialog.tempLabel2.setText("{:.1f}".format(self.air_temp / 10))
        self.ui.heaterLabelShow.setNum(float(self.dataModel.get_heater_output()))
        self.ui.setLabelSkinTemp.setText("{:.1f}".format(self.skin_temp / 10))
        self.ui.setLabelAirTemp.setText("{:.1f}".format(self.air_temp / 10))

        self.setPointDialog.tempUpToolBtn1.pressed.connect(self.incSkinTemp)
        self.setPointDialog.tempDownToolBtn1.pressed.connect(self.decSkinTemp)
        self.setPointDialog.tempUpToolBtn2.pressed.connect(self.incAirTemp)
        self.setPointDialog.tempDownToolBtn2.pressed.connect(self.decAirTemp)

        self.setPointDialog.tempUpToolBtn1.setAutoRepeat(True)
        self.setPointDialog.tempDownToolBtn1.setAutoRepeat(True)
        self.setPointDialog.tempUpToolBtn2.setAutoRepeat(True)
        self.setPointDialog.tempDownToolBtn2.setAutoRepeat(True)

        self.patientWindowForm.saveToolButton.clicked.connect(self.savePatientDetails)
        self.patientWindowForm.nameLineEdit.textChanged.connect(self.patientName)
        self.patientWindowForm.sexLineEdit.textChanged.connect(self.patientSex)
        self.patientWindowForm.ageLineEdit.textChanged.connect(self.patientAge)
        self.patientWindowForm.patientIdLineEdit.textChanged.connect(self.patientId)
        self.patientWindowForm.patientIdLineEdit.textChanged.connect(self.delete_previous_in_patientForm)
        self.patientWindowForm.patientIdLineEdit.textChanged.connect(self.start_typing_timer_2)

        self.ui.patientNameLineEdit.setReadOnly(True)
        #  cQLineEdit(self.ui.patientNameLineEdit, "", self.dataModel, "patientNameLineEdit")
        self.nameLineEdit = cQLineEdit(self.patientWindowForm.nameLineEdit, "", self.dataModel, "nameLineEdit")
        self.ageLineEdit = cQLineEdit(self.patientWindowForm.ageLineEdit, "", self.dataModel, "ageLineEdit")
        self.sexLineEdit = cQLineEdit(self.patientWindowForm.sexLineEdit, "", self.dataModel, "sexLineEdit")

        self.serialWrapper = SerialWrapper('/dev/ttyUSB0', self, self.dataModel)
        print("Starting... Repeater Timer to send data in terminal")
        self.rt = RepeatedTimer(1, self.serialWrapper.sendDataToSerialPort)  # it auto-starts, no need of rt.start()

        self.chronosObject3 = timerCounter.TimerCounter(self.ui)
        # self.changeUnit()
        # self.ui.unitChangeToolButton.setText("°C")  # °C/°F
        configVariables.unitFlag = True
        # ****************************************************** Multithreading ********************************
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        self.counter = 0
        configVariables.checkSendReceive = True

    def clickable(self, widget):
        class Filter(QObject):

            clicked = pyqtSignal()

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

    def servManSetDialog(self):
        self.getGeneralData()
        self.servoManualDialog.heaterOutput.setNum(float(self.dataModel.get_heater_output()))
        self.setServManDialog.showFullScreen()

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        """ for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n * 100 / 4) """

        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        # Execute
        self.threadpool.start(worker)

    def recurring_timer(self):
        # print("******************************* reading received data ***************************************")
        if configVariables.receiveFlag:
            self.serialWrapper.receiveData()
        configVariables.receiveFlag = False
        # self.counter += 1
        # self.ui.setLabelAirTemp.setText("%d" % self.counter)

    # ****************************************************** Multithreading ********************************
    def servManControl(self):
        heaterValue = int(float((self.dataModel.get_heater_output())))
        if configVariables.hex_string[14]:
            data = str.encode(
                "$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(0) + chr(
                    configVariables.hex_string[15]) + chr(configVariables.hex_string[16]) + chr(
                    configVariables.hex_string[17]) + chr(configVariables.hex_string[9]) + ";")
            self.servoManual(data)  # "\u0000"   # self.hexToAscii("0"))
            self.ui.heaterLabelShow.setNum(heaterValue)

        else:
            data = str.encode(
                "$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(1) + chr(
                    configVariables.hex_string[15]) + chr(configVariables.hex_string[16]) + chr(
                    configVariables.hex_string[17]) + chr(heaterValue) + ";")
            self.servoManual(data)  # "\u0000"   # self.hexToAscii("0"))
            self.ui.heaterLabelShow.setNum(heaterValue)

    def unitConverter(self):
        configVariables.checkSendReceive = False

        if configVariables.unitValue:
            # timerOnValue ="\u0000"
            unitChangeValue = chr(0)  # "\u0000"   # self.hexToAscii("0")
        else:
            # timerOnValue ="\u0001"
            unitChangeValue = chr(1)  # "\u0001"  # self.hexToAscii("1")
        # data = str.encode("$I0W" +str(configVariables.hex_string[12]) + str(configVariables.hex_string[13]) + str(
        # configVariables.heatMode14) + str(muteValue) + str( configVariables.hex_string[16]) + str(
        # configVariables.hex_string[17]) + ";")
        # data = str.encode("$I0W" + "\u0001" + "\u0079" + "\u0001" + muteValue + "0" + "0" + ";")
        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + unitChangeValue + chr(
            configVariables.hex_string[17]) + chr(configVariables.hex_string[9]) + ";")
        # stringData = "$I0W" + str(configVariables.hex_string[12]) + str(configVariables.hex_string[13]) + str(
        # configVariables.hex_string[14]) + str(configVariables.hex_string[15]) + str(configVariables.hex_string[16])
        # + str(timerOnValue) + ";"
        print(data)
        # self.hexToAscii("1")
        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
            try:
                self.ser1.write(serial.to_bytes(data))
                # configVariables.hex_string = self.ser1.read(21)
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")

            # time.sleep(0.5)  # Sleep for 3 seconds
            self.ser1.close()
        except Exception as e:
            print(e)
        configVariables.checkSendReceive = True

    def changeUnit(self):
        if configVariables.unitFlag:
            self.ui.unitChangeToolButton.setText("°F")  # °C/°F
            configVariables.unitFlag = False
        else:
            self.ui.unitChangeToolButton.setText("°C")  # °C/°F
            configVariables.unitFlag = True

        # T(°C) = (T(°F) - 32) × 5 / 9

    def servoManual(self, data):
        configVariables.checkSendReceive = False

        # self.hexToAscii("1")
        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
            try:
                self.ser1.write(serial.to_bytes(data))
                configVariables.hex_string = self.ser1.read(21)
                print(str(configVariables.hex_string[0]) + " " +
                      str(configVariables.hex_string[1]) + " " +
                      str(configVariables.hex_string[2]) + " " +
                      str(configVariables.hex_string[3]) + " " +
                      str(configVariables.hex_string[4]) + " " +
                      str(configVariables.hex_string[5]) + " " +
                      str(configVariables.hex_string[6]) + " " +
                      str(configVariables.hex_string[7]) + " " +
                      str(configVariables.hex_string[8]) + " " +
                      str(configVariables.hex_string[9]) + " " +
                      str(configVariables.hex_string[10]) + " " +
                      str(configVariables.hex_string[11]) + " " +
                      str(configVariables.hex_string[12]) + " " +
                      str(configVariables.hex_string[13]) + " " +
                      str(configVariables.hex_string[14]) + " " +
                      str(configVariables.hex_string[15]) + " " +
                      str(configVariables.hex_string[16]) + " " +
                      str(configVariables.hex_string[17]) + " " +
                      str(configVariables.hex_string[18]) + " " +
                      str(configVariables.hex_string[19]) + " " +
                      str(configVariables.hex_string[20]))
            except Exception as e:
                print("--- abnormal read and write from port serialDataTXRX---：", e)
                print("++++++++++++++++++++++++++Exception is here occured++++++++++++++++++++++++++++++++++")

            # time.sleep(0.5)  # Sleep for 3 seconds
            self.ser1.close()
        except Exception as e:
            print(e)
        configVariables.checkSendReceive = True

    def muteControl(self):
        configVariables.checkSendReceive = False
        sert = str(configVariables.heatMode14)
        res = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in sert)
        print(chr(configVariables.hex_string[13]))
        # printing result
        print("The unicode converted String : " + str(res) + " " + str(configVariables.heatMode14))

        if configVariables.mute15:
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon/speaker-on-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            muteValue = chr(0)
        else:
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon/speaker-off-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            muteValue = chr(1)

        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + muteValue + chr(configVariables.hex_string[16]) + chr(
            configVariables.hex_string[17]) + chr(
            configVariables.hex_string[9]) + ";")

        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
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

    def heaterSetPoint(self, heatvalue):
        configVariables.checkSendReceive = False
        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + chr(
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + chr(heatvalue) + ";")
        print(data)
        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
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

    def setPoint(self, firstPart, secondPart):
        configVariables.checkSendReceive = False
        data = str.encode("$I0W" + chr(firstPart) + chr(secondPart) + chr(
            configVariables.hex_string[14]) + chr(configVariables.hex_string[15]) + chr(
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + chr(
            configVariables.hex_string[9]) + ";")
        print(data)
        try:
            self.ser1 = serial.Serial('/dev/ttyUSB0', 9600)
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

    def heatToHex(self, value):
        print("heater Value: " + str(value))
        hexValue = int(hex(value), 16)
        firstPart = hexValue >> 8
        secondPart = hexValue & 0xFF
        self.heaterSetPoint(value)
        skinTemp1 = int(hex(firstPart), 16)
        skinTemp2 = int(hex(secondPart), 16)
        tempValue = (skinTemp1 << 8) | skinTemp2
        print(
            "Temperature value original: " + str(tempValue) + " First Part: " + str(firstPart) + " Second Part: " + str(
                secondPart))

    def decimalToHex(self, value):
        print("Temperature Value: " + str(value))
        hexValue = int(hex(value), 16)
        firstPart = hexValue >> 8
        secondPart = hexValue & 0xFF
        self.setPoint(firstPart, secondPart)
        skinTemp1 = int(hex(firstPart), 16)
        skinTemp2 = int(hex(secondPart), 16)
        tempValue = (skinTemp1 << 8) | skinTemp2
        print(
            "Temperature value original: " + str(tempValue) + " First Part: " + str(firstPart) + " Second Part: " + str(
                secondPart))

    def hexToAscii(self, data):
        output = StringBuilder()
        for i in range(0, len(data), 1):
            str1 = data[i]
            output.Append(chr(int(str1, 16)))
        return str(output)

    # cQLineEdit(self.patientWindowForm.patientIdLineEdit, "", self.dataModel, "patientIdLineEdit")
    def delete_previous_in_patientForm(self, text):
        try:
            if self.startNew_form:
                self.patientWindowForm.patientIdLineEdit.setText(text[-1])
                self.startNew_form = 0
        except Exception as e:
            print(e)

    def make_changes_patient_form(self):
        txt = self.patientWindowForm.patientIdLineEdit.text()
        self.dataModel.set_find_by_patient_id(txt)
        self.database_manage.getPatientById(txt, self.dataModel)

        if len(self.dataModel.get_form_patient_name()) == 0:
            self.nameLineEdit.ex.text_box.clear()
            self.nameLineEdit.ex.currentTextBox.clear()
            self.ageLineEdit.ex.text_box.clear()
            self.ageLineEdit.ex.currentTextBox.clear()
            self.sexLineEdit.ex.text_box.clear()
            self.sexLineEdit.ex.currentTextBox.clear()
        else:
            self.nameLineEdit.ex.text_box.setText(self.dataModel.get_form_patient_name())
            self.nameLineEdit.ex.currentTextBox.setText(self.dataModel.get_form_patient_name())
            self.ageLineEdit.ex.text_box.setText(self.dataModel.get_patient_age())
            self.ageLineEdit.ex.currentTextBox.setText(self.dataModel.get_patient_age())
            self.sexLineEdit.ex.text_box.setText(self.dataModel.get_patient_sex())
            self.sexLineEdit.ex.currentTextBox.setText(self.dataModel.get_patient_sex())
            print("8979" + self.dataModel.get_form_patient_name())
            self.patientWindowForm.nameLineEdit.setText(self.dataModel.get_form_patient_name())
        # cQLineEdit(self.patientWindowForm.nameLineEdit, "89798", self.dataModel, "nameLineEdit")
        self.startNew_form = 1

    def delete_previous(self, text):
        try:
            if self.startNew:
                self.ui.patientIdLineEdit.setText(text[-1])
                self.startNew = 0
        except:
            return

    def start_typing_timer_2(self):
        """Wait until there are no changes for 24msec second before making changes."""
        self.typing_timer_2.start(24)

    def start_typing_timer(self):
        """Wait until there are no changes for 24msec second before making changes."""
        self.typing_timer.start(24)

    def make_changes(self):
        txt = self.ui.patientIdLineEdit.text()
        self.dataModel.set_find_by_patient_id(txt)
        self.database_manage.getPatientById(txt, self.dataModel)
        if len(self.dataModel.get_form_patient_name()) == 0:
            self.ui.patientNameLineEdit.setText("No record found !")
        else:
            self.ui.patientNameLineEdit.setText(self.dataModel.get_form_patient_name())
        self.startNew = 1
        # print(txt)
        # RUN SQL OR DO SOMETHING ELSE WITH THE TEXT HERE #

    def findPatientById(self, text):
        self.dataModel.set_find_by_patient_id(text)
        self.database_manage.getPatientById(self.dataModel)

    def updateSetPointData(self):
        self.dataModel.set_skin_temp(self.skin_temp)
        self.dataModel.set_air_temp(self.air_temp)
        self.database_manage.updateSkinTempValue(self.dataModel)
        self.database_manage.updateAirTempValue(self.dataModel)
        self.ui.setLabelSkinTemp.setText("{:.1f}".format(self.dataModel.get_skin_temp() / 10))
        self.ui.setLabelAirTemp.setText("{:.1f}".format(self.dataModel.get_air_temp() / 10))
        try:
            self.decimalToHex(int(self.dataModel.get_skin_temp()))
        except Exception as e:
            print(e)

        self.setDialog.close()

    def closeSetPointDialog(self):
        self.setDialog.close()

    def decHeaterOutput(self):
        if self.heater_output > 0:
            self.heater_output = self.heater_output - 1
            self.servoManualDialog.heaterOutput.setNum(self.heater_output)

    def incHeaterOutput(self):
        if 0 <= self.heater_output < 100:
            self.heater_output = self.heater_output + 1
            self.servoManualDialog.heaterOutput.setNum(self.heater_output)

    def updateSetHeaterOutput(self):
        self.dataModel.set_heater_output(self.heater_output)
        self.database_manage.updateHeaterOutput(self.dataModel)
        # self.ui.setLabelSkinTemp.setNum(self.dataModel.get_skin_temp())
        self.heatToHex(int(self.dataModel.get_heater_output()))
        self.setServManDialog.close()

    def closeHeaterDialog(self):
        self.setServManDialog.close()

    def decSkinTemp(self):
        print("Skin Temp dec: " + str(self.skin_temp))
        if self.skin_temp > self.skin_low_temp:
            self.skin_temp = self.skin_temp - 1
            self.setPointDialog.tempLabel1.setText("{:.1f}".format(self.skin_temp / 10))

    def incSkinTemp(self):
        print("Skin Temp inc: " + str(self.skin_temp))
        if self.skin_low_temp <= self.skin_temp < self.skin_high_temp:
            self.skin_temp = self.skin_temp + 1
            self.setPointDialog.tempLabel1.setText("{:.1f}".format(self.skin_temp / 10))

    def decAirTemp(self):
        if self.air_temp > self.air_low_temp:
            self.air_temp = self.air_temp - 1
            self.setPointDialog.tempLabel2.setText("{:.1f}".format(self.air_temp / 10))

    def incAirTemp(self):
        if self.air_low_temp <= self.air_temp < self.air_high_temp:
            self.air_temp = self.air_temp + 1
            self.setPointDialog.tempLabel2.setText("{:.1f}".format(self.air_temp / 10))
        self.dataModel.set_air_temp(self.air_temp)

    def patientName(self, text):
        self.dataModel.set_patient_name(text)

    def patientSex(self, text):
        self.dataModel.set_patient_sex(text)

    def patientAge(self, text):
        self.dataModel.set_patient_age(text)

    def patientId(self, text):
        self.dataModel.set_patient_id(text)

    def savePatientDetails(self):
        self.database_manage.insertPatientDetails(self.dataModel)
        AutoCloseMessageBox.showWithTimeout(1, "Record has been saved successfully", "Success", QMessageBox.Warning)

    def patientDetailsDialogOpen(self):
        #  if self.ui.patientDetailsToolButton.isChecked():
        self.patientWindow.showFullScreen()
        # else:
        # self.patientDialog.hide()
        # self.patientDialog.exec_()

    def openSettingWindow(self):
        self.settingWindow.showFullScreen()

    def saveSettingData(self):
        self.database_manage.updateSettingData(self.dataModel)
        self.settingWindow.close()

    def closeSettingWindow(self):
        self.settingWindow.close()

    # self.patientForm.exec_()
    def closePatientForm(self):
        self.patientWindow.clearFocus()
        self.nameLineEdit.ex.text_box.clear()
        self.nameLineEdit.ex.currentTextBox.clear()
        self.ageLineEdit.ex.text_box.clear()
        self.ageLineEdit.ex.currentTextBox.clear()
        self.sexLineEdit.ex.text_box.clear()
        self.sexLineEdit.ex.currentTextBox.clear()
        self.patientWindowForm.patientIdLineEdit.clear()
        self.ui.patientNameLineEdit.clear()
        self.ui.patientIdLineEdit.clear()
        self.showFullScreen()
        # self.ui.patientIdLineEdit.mouseDoubleClickEvent()
        self.patientWindow.close()
        # self.ui.patientIdLineEdit.setCursor(True)

    def setPointDialogBox(self):
        self.getGeneralData()
        self.setPointDialog.tempLabel1.setText("{:.1f}".format(self.skin_temp / 10))
        self.setPointDialog.tempLabel2.setText("{:.1f}".format(self.air_temp / 10))
        self.setDialog.showFullScreen()

    def getGeneralData(self):
        self.database_manage.queryGeneralSettingsData(self.dataModel)
        self.skin_temp = float(self.dataModel.get_skin_temp())
        self.air_temp = float(self.dataModel.get_air_temp())
        self.setPointDialog.tempLabel1.setText("{:.1f}".format(self.skin_temp / 10))
        self.setPointDialog.tempLabel2.setText("{:.1f}".format(self.air_temp / 10))


# I feel better having one of these
def main():
    # a new app instance
    import time
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")  # dataModel.get_power_on_image_path()

    splash_pix = QPixmap("icon/sstech-logo-plus.png")
    # -------------------------Splash screeen Image ----------------------------------------------------------
    # self.splash_pix = QPixmap(self.dataModel.get_power_on_image_path())
    # from.splash_pix
    # -------------------------Splash Screen Image ----------------------------------------------------------
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    # splash = QSplashScreen(splash_pix, Qt.WindowMinimizeButtonHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 20, splash_pix.width(), 20)

    splash.setMask(splash_pix.mask())

    splash.showFullScreen()
    splash.showMessage("<h1><font color='green'>Welcome to SS Technomed Pvt. Ltd!</font></h1>",
                       Qt.AlignBottom | Qt.AlignCenter, Qt.black)

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    # Simulate something that takes time
    time.sleep(1)

    form = MainWindow()
    form.showFullScreen()
    splash.finish(form)
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
