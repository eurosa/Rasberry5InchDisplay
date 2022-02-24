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
from MessageBox import AutoCloseMessageBox
import sys
from Database import database
from Database.dataModel import DataModel
from PyQt5.QtSql import QSqlQueryModel
from virtual_keyboard import *
# This gets the Qt stuff
import PyQt5
import mainwindow_auto
import setPointDialog
import patientDetailsForm
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

    # cQLineEdit(self.patientWindowForm.patientIdLineEdit, "", self.dataModel, "patientIdLineEdit")
    def delete_previous_in_patientForm(self, text):
        try:
            if self.startNew_form:
                self.patientWindowForm.patientIdLineEdit.setText(text[-1])
                self.startNew_form = 0
        except:
            return

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
            print("89798 " + self.dataModel.get_form_patient_name())
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
