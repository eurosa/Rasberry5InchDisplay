# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patientFormWindow(object):
    def setupUi(self, patientFormWindow):
        patientFormWindow.setObjectName("patientFormWindow")
        patientFormWindow.resize(800, 480)
        patientFormWindow.setMinimumSize(QtCore.QSize(800, 480))
        patientFormWindow.setMaximumSize(QtCore.QSize(800, 480))
        patientFormWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        patientFormWindow.setStyleSheet("QMainWindow{background-color:blue ;}")
        self.centralwidget = QtWidgets.QWidget(patientFormWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okCal = QtWidgets.QToolButton(self.centralwidget)
        self.okCal.setGeometry(QtCore.QRect(360, 390, 72, 72))
        self.okCal.setMinimumSize(QtCore.QSize(72, 72))
        self.okCal.setMaximumSize(QtCore.QSize(72, 72))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.okCal.setFont(font)
        self.okCal.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 18px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed { \n"
"    background-color:#535353;\n"
"    border-style: inset;\n"
"}")
        self.okCal.setObjectName("okCal")
        self.cancelCal = QtWidgets.QToolButton(self.centralwidget)
        self.cancelCal.setGeometry(QtCore.QRect(460, 390, 72, 72))
        self.cancelCal.setMinimumSize(QtCore.QSize(72, 72))
        self.cancelCal.setMaximumSize(QtCore.QSize(72, 72))
        self.cancelCal.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 18px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: #535353;\n"
"    border-style: inset;\n"
"}")
        self.cancelCal.setObjectName("cancelCal")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 250, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 240, 101, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 90, 151, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(471, 311, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 310, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.airLowEditLine = QtWidgets.QLineEdit(self.centralwidget)
        self.airLowEditLine.setGeometry(QtCore.QRect(290, 310, 101, 31))
        self.airLowEditLine.setObjectName("airLowEditLine")
        self.airHighEditLine = QtWidgets.QLineEdit(self.centralwidget)
        self.airHighEditLine.setGeometry(QtCore.QRect(580, 307, 101, 31))
        self.airHighEditLine.setObjectName("airHighEditLine")
        self.skinHighEditLine = QtWidgets.QLineEdit(self.centralwidget)
        self.skinHighEditLine.setGeometry(QtCore.QRect(580, 240, 101, 31))
        self.skinHighEditLine.setObjectName("skinHighEditLine")
        self.skinLowEditLine = QtWidgets.QLineEdit(self.centralwidget)
        self.skinLowEditLine.setGeometry(QtCore.QRect(290, 240, 101, 31))
        self.skinLowEditLine.setObjectName("skinLowEditLine")
        self.skinCalUpToolBtn1 = QtWidgets.QToolButton(self.centralwidget)
        self.skinCalUpToolBtn1.setGeometry(QtCore.QRect(550, 50, 72, 72))
        self.skinCalUpToolBtn1.setMinimumSize(QtCore.QSize(72, 72))
        self.skinCalUpToolBtn1.setMaximumSize(QtCore.QSize(72, 72))
        self.skinCalUpToolBtn1.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF ;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/plus-sign-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skinCalUpToolBtn1.setIcon(icon)
        self.skinCalUpToolBtn1.setIconSize(QtCore.QSize(42, 40))
        self.skinCalUpToolBtn1.setObjectName("skinCalUpToolBtn1")
        self.airCalDownToolBtn2 = QtWidgets.QToolButton(self.centralwidget)
        self.airCalDownToolBtn2.setGeometry(QtCore.QRect(340, 150, 72, 72))
        self.airCalDownToolBtn2.setMinimumSize(QtCore.QSize(72, 72))
        self.airCalDownToolBtn2.setMaximumSize(QtCore.QSize(72, 72))
        self.airCalDownToolBtn2.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/minus_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.airCalDownToolBtn2.setIcon(icon1)
        self.airCalDownToolBtn2.setIconSize(QtCore.QSize(42, 42))
        self.airCalDownToolBtn2.setObjectName("airCalDownToolBtn2")
        self.skinCalLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.skinCalLabel1.setGeometry(QtCore.QRect(420, 70, 120, 40))
        self.skinCalLabel1.setMinimumSize(QtCore.QSize(120, 40))
        self.skinCalLabel1.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.skinCalLabel1.setFont(font)
        self.skinCalLabel1.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.skinCalLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.skinCalLabel1.setObjectName("skinCalLabel1")
        self.airCalUpToolBtn2 = QtWidgets.QToolButton(self.centralwidget)
        self.airCalUpToolBtn2.setGeometry(QtCore.QRect(550, 150, 72, 72))
        self.airCalUpToolBtn2.setMinimumSize(QtCore.QSize(72, 72))
        self.airCalUpToolBtn2.setMaximumSize(QtCore.QSize(72, 72))
        self.airCalUpToolBtn2.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.airCalUpToolBtn2.setIcon(icon)
        self.airCalUpToolBtn2.setIconSize(QtCore.QSize(42, 42))
        self.airCalUpToolBtn2.setObjectName("airCalUpToolBtn2")
        self.airCalLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.airCalLabel2.setGeometry(QtCore.QRect(420, 170, 120, 40))
        self.airCalLabel2.setMinimumSize(QtCore.QSize(120, 40))
        self.airCalLabel2.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.airCalLabel2.setFont(font)
        self.airCalLabel2.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.airCalLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.airCalLabel2.setObjectName("airCalLabel2")
        self.skinCalDownToolBtn1 = QtWidgets.QToolButton(self.centralwidget)
        self.skinCalDownToolBtn1.setGeometry(QtCore.QRect(340, 50, 72, 72))
        self.skinCalDownToolBtn1.setMinimumSize(QtCore.QSize(72, 72))
        self.skinCalDownToolBtn1.setMaximumSize(QtCore.QSize(72, 72))
        self.skinCalDownToolBtn1.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00A36C ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.skinCalDownToolBtn1.setIcon(icon1)
        self.skinCalDownToolBtn1.setIconSize(QtCore.QSize(42, 42))
        self.skinCalDownToolBtn1.setObjectName("skinCalDownToolBtn1")
        patientFormWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(patientFormWindow)
        QtCore.QMetaObject.connectSlotsByName(patientFormWindow)
        patientFormWindow.setTabOrder(self.okCal, self.cancelCal)

    def retranslateUi(self, patientFormWindow):
        _translate = QtCore.QCoreApplication.translate
        patientFormWindow.setWindowTitle(_translate("patientFormWindow", "Settings Window"))
        self.okCal.setText(_translate("patientFormWindow", "Ok"))
        self.cancelCal.setText(_translate("patientFormWindow", "Cancel"))
        self.label_2.setText(_translate("patientFormWindow", "Air Calibration"))
        self.label_3.setText(_translate("patientFormWindow", "Skin High"))
        self.label_4.setText(_translate("patientFormWindow", "Skin Low"))
        self.label.setText(_translate("patientFormWindow", "Skin Calibration"))
        self.label_6.setText(_translate("patientFormWindow", "Air High"))
        self.label_7.setText(_translate("patientFormWindow", "Air Low"))
        self.skinCalUpToolBtn1.setText(_translate("patientFormWindow", "..."))
        self.airCalDownToolBtn2.setText(_translate("patientFormWindow", "..."))
        self.skinCalLabel1.setText(_translate("patientFormWindow", "1.0"))
        self.airCalUpToolBtn2.setText(_translate("patientFormWindow", "..."))
        self.airCalLabel2.setText(_translate("patientFormWindow", "1.0"))
        self.skinCalDownToolBtn1.setText(_translate("patientFormWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientFormWindow = QtWidgets.QMainWindow()
    ui = Ui_patientFormWindow()
    ui.setupUi(patientFormWindow)
    patientFormWindow.show()
    sys.exit(app.exec_())
