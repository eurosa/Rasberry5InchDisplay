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
from past.builtins import unicode
from past.types import long

import configVariables
import timerCounter
from MessageBox import AutoCloseMessageBox
import sys
from Database import database
from Database.dataModel import DataModel
from PyQt5.QtSql import QSqlQueryModel

from StringBuilder import StringBuilder
from serialDataTXRX import SerialWrapper
from virtual_keyboard import *
# This gets the Qt stuff
import PyQt5
import mainwindow_auto
import setPointDialog
import patientDetailsForm
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
        self.ui.unitChangeToolButton.clicked.connect(self.changeUnit)
        self.ui.muteToolButton.clicked.connect(self.muteControl)

        self.patientWindow = QMainWindow()
        self.patientWindowForm = patientDetailsForm.Ui_patientFormWindow()
        self.patientWindowForm.setupUi(self.patientWindow)
        self.patientWindowForm.cancelToolButton.clicked.connect(self.closePatientForm)

        self.ui.setPointBtn.clicked.connect(self.setPointDialogBox)
        self.setPointDialog = setPointDialog.Ui_setPointForm()
        self.setDialog = QMainWindow()
        self.setPointDialog.setupUi(self.setDialog)

        self.setPointDialog.okBtn.clicked.connect(self.updateSetPointData)
        self.setPointDialog.cancelBtn.clicked.connect(self.closeSetPointDialog)
        # self.setStyleSheet("background-color: yellow;")
        self.skin_temp = float(self.dataModel.get_skin_temp())
        self.air_temp = float(self.dataModel.get_air_temp())
        self.setPointDialog.tempLabel1.setNum(self.skin_temp)
        self.setPointDialog.tempLabel2.setNum(self.air_temp)

        self.ui.setLabelSkinTemp.setNum(self.skin_temp)
        self.ui.setLabelAirTemp.setNum(self.air_temp)

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

        self.serialWrapper = SerialWrapper('/dev/ttyUSB0', self)
        print("starting... Repeater Timer to send data in terminal")
        self.rt = RepeatedTimer(2, self.serialWrapper.sendDataToSerialPort)  # it auto-starts, no need of rt.start()

        self.chronosObject3 = timerCounter.TimerCounter(self.ui)
        # self.changeUnit()
        self.ui.unitChangeToolButton.setText("°C")  # °C/°F
        configVariables.unitFlag = True

    def changeUnit(self):
        if configVariables.unitFlag:
            self.ui.unitChangeToolButton.setText("°F")  # °C/°F
            configVariables.unitFlag = False
        else:
            self.ui.unitChangeToolButton.setText("°C")  # °C/°F
            configVariables.unitFlag = True

        # T(°C) = (T(°F) - 32) × 5 / 9

    def muteControl(self):
        configVariables.checkSendReceive = False
        sert = str(configVariables.heatMode14)
        res = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in sert)
        print(chr(configVariables.hex_string[13]))
        # printing result
        print("The unicode converted String : " + str(res) + " " + str(configVariables.heatMode14))

        if configVariables.mute15:
            # timerOnValue ="\u0000"
            muteValue = chr(0)  # "\u0000"   # self.hexToAscii("0")
        else:
            # timerOnValue ="\u0001"
            muteValue = chr(1)  # "\u0001"  # self.hexToAscii("1")
        # data = str.encode("$I0W" +str(configVariables.hex_string[12]) + str(configVariables.hex_string[13]) + str(
        # configVariables.heatMode14) + str(muteValue) + str( configVariables.hex_string[16]) + str(
        # configVariables.hex_string[17]) + ";")
        # data = str.encode("$I0W" + "\u0001" + "\u0079" + "\u0001" + muteValue + "0" + "0" + ";")
        data = str.encode("$I0W" + chr(configVariables.hex_string[12]) + chr(configVariables.hex_string[13]) + chr(
            configVariables.hex_string[14]) + muteValue + chr(configVariables.hex_string[16]) + chr(
            configVariables.hex_string[17]) + ";")
        # stringData = "$I0W" + str(configVariables.hex_string[12]) + str(configVariables.hex_string[13]) + str(
        # configVariables.hex_string[14]) + str(configVariables.hex_string[15]) + str(configVariables.hex_string[16])
        # + str(timerOnValue) + ";"
        print(data)
        # self.hexToAscii("1")
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
            configVariables.hex_string[16]) + chr(configVariables.hex_string[17]) + ";")
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
        self.ui.setLabelSkinTemp.setNum(self.dataModel.get_skin_temp())
        self.ui.setLabelAirTemp.setNum(self.dataModel.get_air_temp())
        self.decimalToHex(int(self.dataModel.get_skin_temp() * 10))
        self.setDialog.close()

    def closeSetPointDialog(self):
        self.setDialog.close()

    def decSkinTemp(self):
        if self.skin_temp > 32:
            self.skin_temp = self.skin_temp - 0.1
            self.setPointDialog.tempLabel1.setNum(self.skin_temp)

    def incSkinTemp(self):
        if 32 <= self.skin_temp < 38:
            self.skin_temp = self.skin_temp + 0.1
            self.setPointDialog.tempLabel1.setNum(self.skin_temp)

    def decAirTemp(self):
        if self.air_temp > 30:
            self.air_temp = self.air_temp - 0.1
            self.setPointDialog.tempLabel2.setNum(self.air_temp)

    def incAirTemp(self):
        if 30 <= self.air_temp < 39:
            self.air_temp = self.air_temp + 0.1
            self.setPointDialog.tempLabel2.setNum(self.air_temp)
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
        self.setDialog.showFullScreen()

    def getGeneralData(self):
        self.database_manage.queryGeneralSettingsData(self.dataModel)
        self.skin_temp = float(self.dataModel.get_skin_temp())
        self.air_temp = float(self.dataModel.get_air_temp())
        self.setPointDialog.tempLabel1.setNum(self.skin_temp)
        self.setPointDialog.tempLabel2.setNum(self.air_temp)


# I feel better having one of these
def main():
    # a new app instance
    import time
    app = QApplication(sys.argv)
    app.setStyle("QtCurve")  # dataModel.get_power_on_image_path()
    form = MainWindow()
    form.showFullScreen()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
