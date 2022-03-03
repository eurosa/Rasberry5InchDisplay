# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(870, 550))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("QMainWindow{background-color:blue ;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heaterLabelMode = QtWidgets.QToolButton(self.centralwidget)
        self.heaterLabelMode.setGeometry(QtCore.QRect(690, 60, 101, 41))
        self.heaterLabelMode.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
" QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.heaterLabelMode.setText("")
        self.heaterLabelMode.setIconSize(QtCore.QSize(42, 42))
        self.heaterLabelMode.setObjectName("heaterLabelMode")
        self.timerButton = QtWidgets.QToolButton(self.centralwidget)
        self.timerButton.setGeometry(QtCore.QRect(720, 140, 72, 61))
        self.timerButton.setMinimumSize(QtCore.QSize(72, 61))
        self.timerButton.setMaximumSize(QtCore.QSize(72, 61))
        self.timerButton.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.timerButton.setIconSize(QtCore.QSize(42, 42))
        self.timerButton.setObjectName("timerButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 366, 801, 1))
        self.line.setStyleSheet("Line{\n"
"\n"
" \n"
"    border-width: 1px;\n"
" \n"
"    border-color: beige; \n"
"  \n"
" \n"
"    background-color:#aa0000;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.muteToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.muteToolButton.setGeometry(QtCore.QRect(540, 250, 72, 61))
        self.muteToolButton.setMinimumSize(QtCore.QSize(72, 61))
        self.muteToolButton.setMaximumSize(QtCore.QSize(72, 61))
        self.muteToolButton.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.muteToolButton.setIconSize(QtCore.QSize(42, 42))
        self.muteToolButton.setObjectName("muteToolButton")
        self.setPointBtn = QtWidgets.QToolButton(self.centralwidget)
        self.setPointBtn.setGeometry(QtCore.QRect(440, 250, 72, 61))
        self.setPointBtn.setMinimumSize(QtCore.QSize(72, 61))
        self.setPointBtn.setMaximumSize(QtCore.QSize(72, 61))
        self.setPointBtn.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;;\n"
"    border-style: inset;\n"
"}")
        self.setPointBtn.setIconSize(QtCore.QSize(42, 42))
        self.setPointBtn.setObjectName("setPointBtn")
        self.unitChangeToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.unitChangeToolButton.setGeometry(QtCore.QRect(630, 250, 72, 61))
        self.unitChangeToolButton.setMinimumSize(QtCore.QSize(72, 61))
        self.unitChangeToolButton.setMaximumSize(QtCore.QSize(72, 61))
        self.unitChangeToolButton.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.unitChangeToolButton.setIconSize(QtCore.QSize(42, 42))
        self.unitChangeToolButton.setObjectName("unitChangeToolButton")
        self.tempDownToolBtn2_9 = QtWidgets.QToolButton(self.centralwidget)
        self.tempDownToolBtn2_9.setGeometry(QtCore.QRect(720, 250, 72, 61))
        self.tempDownToolBtn2_9.setMinimumSize(QtCore.QSize(72, 61))
        self.tempDownToolBtn2_9.setMaximumSize(QtCore.QSize(72, 61))
        self.tempDownToolBtn2_9.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempDownToolBtn2_9.setIconSize(QtCore.QSize(42, 42))
        self.tempDownToolBtn2_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tempDownToolBtn2_9.setObjectName("tempDownToolBtn2_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(540, 40, 60, 60))
        self.label_10.setMinimumSize(QtCore.QSize(60, 60))
        self.label_10.setMaximumSize(QtCore.QSize(60, 60))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../.designer/backup/icon/heater_white_60_60.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 50, 60, 60))
        self.label_9.setMinimumSize(QtCore.QSize(60, 60))
        self.label_9.setMaximumSize(QtCore.QSize(60, 60))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../.designer/backup/icon/thermometer_60_60.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.tempLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.tempLabel4.setGeometry(QtCore.QRect(350, 40, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(55)
        font.setBold(True)
        font.setWeight(75)
        self.tempLabel4.setFont(font)
        self.tempLabel4.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempLabel4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tempLabel4.setObjectName("tempLabel4")
        self.setLabelAirTemp = QtWidgets.QLabel(self.centralwidget)
        self.setLabelAirTemp.setGeometry(QtCore.QRect(380, 140, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.setLabelAirTemp.setFont(font)
        self.setLabelAirTemp.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setLabelAirTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.setLabelAirTemp.setObjectName("setLabelAirTemp")
        self.setTitleLabel4 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel4.setGeometry(QtCore.QRect(290, 10, 51, 20))
        self.setTitleLabel4.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel4.setFont(font)
        self.setTitleLabel4.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel4.setObjectName("setTitleLabel4")
        self.setTitleLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel2.setGeometry(QtCore.QRect(250, 150, 160, 20))
        self.setTitleLabel2.setMinimumSize(QtCore.QSize(160, 20))
        self.setTitleLabel2.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel2.setFont(font)
        self.setTitleLabel2.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel2.setObjectName("setTitleLabel2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 60, 60))
        self.label_8.setMinimumSize(QtCore.QSize(60, 60))
        self.label_8.setMaximumSize(QtCore.QSize(60, 60))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../.designer/backup/icon/thermometer_60_60.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.setTitleLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel1.setGeometry(QtCore.QRect(-30, 150, 160, 20))
        self.setTitleLabel1.setMinimumSize(QtCore.QSize(160, 20))
        self.setTitleLabel1.setMaximumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel1.setFont(font)
        self.setTitleLabel1.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel1.setObjectName("setTitleLabel1")
        self.setTitleLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel3.setGeometry(QtCore.QRect(20, 10, 61, 20))
        self.setTitleLabel3.setMaximumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel3.setFont(font)
        self.setTitleLabel3.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel3.setObjectName("setTitleLabel3")
        self.tempLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.tempLabel3.setGeometry(QtCore.QRect(90, 40, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(55)
        font.setBold(True)
        font.setWeight(75)
        self.tempLabel3.setFont(font)
        self.tempLabel3.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel3.setObjectName("tempLabel3")
        self.setLabelSkinTemp = QtWidgets.QLabel(self.centralwidget)
        self.setLabelSkinTemp.setGeometry(QtCore.QRect(100, 140, 160, 40))
        self.setLabelSkinTemp.setMinimumSize(QtCore.QSize(160, 40))
        self.setLabelSkinTemp.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.setLabelSkinTemp.setFont(font)
        self.setLabelSkinTemp.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setLabelSkinTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.setLabelSkinTemp.setObjectName("setLabelSkinTemp")
        self.setTitleLabel2_2 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel2_2.setGeometry(QtCore.QRect(710, 10, 91, 20))
        self.setTitleLabel2_2.setMaximumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel2_2.setFont(font)
        self.setTitleLabel2_2.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel2_2.setObjectName("setTitleLabel2_2")
        self.setTitleLabel4_2 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel4_2.setGeometry(QtCore.QRect(550, 10, 101, 20))
        self.setTitleLabel4_2.setMaximumSize(QtCore.QSize(160, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel4_2.setFont(font)
        self.setTitleLabel4_2.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setTitleLabel4_2.setWordWrap(True)
        self.setTitleLabel4_2.setObjectName("setTitleLabel4_2")
        self.heaterLabelShow = QtWidgets.QLabel(self.centralwidget)
        self.heaterLabelShow.setGeometry(QtCore.QRect(560, 60, 81, 40))
        self.heaterLabelShow.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.heaterLabelShow.setFont(font)
        self.heaterLabelShow.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.heaterLabelShow.setAlignment(QtCore.Qt.AlignCenter)
        self.heaterLabelShow.setObjectName("heaterLabelShow")
        self.patientDetailsToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.patientDetailsToolButton.setGeometry(QtCore.QRect(320, 250, 72, 61))
        self.patientDetailsToolButton.setMinimumSize(QtCore.QSize(72, 61))
        self.patientDetailsToolButton.setMaximumSize(QtCore.QSize(72, 61))
        self.patientDetailsToolButton.setStyleSheet("QToolButton{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.patientDetailsToolButton.setIconSize(QtCore.QSize(42, 42))
        self.patientDetailsToolButton.setObjectName("patientDetailsToolButton")
        self.setTitleLabel2_4 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel2_4.setGeometry(QtCore.QRect(10, 270, 100, 40))
        self.setTitleLabel2_4.setMinimumSize(QtCore.QSize(100, 40))
        self.setTitleLabel2_4.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel2_4.setFont(font)
        self.setTitleLabel2_4.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel2_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setTitleLabel2_4.setObjectName("setTitleLabel2_4")
        self.patientIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.patientIdLineEdit.setGeometry(QtCore.QRect(150, 280, 150, 31))
        self.patientIdLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.patientIdLineEdit.setMaximumSize(QtCore.QSize(150, 40))
        self.patientIdLineEdit.setObjectName("patientIdLineEdit")
        self.patientNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.patientNameLineEdit.setGeometry(QtCore.QRect(150, 240, 150, 31))
        self.patientNameLineEdit.setMaximumSize(QtCore.QSize(150, 40))
        self.patientNameLineEdit.setObjectName("patientNameLineEdit")
        self.setTitleLabel2_3 = QtWidgets.QLabel(self.centralwidget)
        self.setTitleLabel2_3.setGeometry(QtCore.QRect(10, 230, 131, 40))
        self.setTitleLabel2_3.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setTitleLabel2_3.setFont(font)
        self.setTitleLabel2_3.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.setTitleLabel2_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setTitleLabel2_3.setObjectName("setTitleLabel2_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 380, 100, 20))
        self.label_7.setMinimumSize(QtCore.QSize(100, 20))
        self.label_7.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
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
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.timerShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerShowLabel.setGeometry(QtCore.QRect(610, 140, 100, 40))
        self.timerShowLabel.setMinimumSize(QtCore.QSize(100, 40))
        self.timerShowLabel.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.timerShowLabel.setFont(font)
        self.timerShowLabel.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.timerShowLabel.setMidLineWidth(100)
        self.timerShowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerShowLabel.setObjectName("timerShowLabel")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 150, 100, 20))
        self.label_11.setMinimumSize(QtCore.QSize(100, 20))
        self.label_11.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 410, 680, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.probeLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.probeLabel.setFont(font)
        self.probeLabel.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.probeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.probeLabel.setObjectName("probeLabel")
        self.verticalLayout_6.addWidget(self.probeLabel)
        self.probeIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.probeIconLabel.setMinimumSize(QtCore.QSize(30, 15))
        self.probeIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.probeIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.probeIconLabel.setText("")
        self.probeIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.probeIconLabel.setObjectName("probeIconLabel")
        self.verticalLayout_6.addWidget(self.probeIconLabel)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tempHighLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tempHighLabel.setFont(font)
        self.tempHighLabel.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempHighLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempHighLabel.setObjectName("tempHighLabel")
        self.verticalLayout_8.addWidget(self.tempHighLabel)
        self.tempHighIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.tempHighIconLabel.setMinimumSize(QtCore.QSize(30, 15))
        self.tempHighIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tempHighIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempHighIconLabel.setText("")
        self.tempHighIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempHighIconLabel.setObjectName("tempHighIconLabel")
        self.verticalLayout_8.addWidget(self.tempHighIconLabel)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tempLowLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tempLowLabel.setFont(font)
        self.tempLowLabel.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempLowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLowLabel.setObjectName("tempLowLabel")
        self.verticalLayout_9.addWidget(self.tempLowLabel)
        self.tempLowIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.tempLowIconLabel.setMinimumSize(QtCore.QSize(30, 15))
        self.tempLowIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tempLowIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.tempLowIconLabel.setText("")
        self.tempLowIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLowIconLabel.setObjectName("tempLowIconLabel")
        self.verticalLayout_9.addWidget(self.tempLowIconLabel)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.heaterLabelFail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.heaterLabelFail.setFont(font)
        self.heaterLabelFail.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.heaterLabelFail.setAlignment(QtCore.Qt.AlignCenter)
        self.heaterLabelFail.setObjectName("heaterLabelFail")
        self.verticalLayout_3.addWidget(self.heaterLabelFail)
        self.heaterIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.heaterIconLabel.setMinimumSize(QtCore.QSize(40, 15))
        self.heaterIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.heaterIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.heaterIconLabel.setText("")
        self.heaterIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.heaterIconLabel.setObjectName("heaterIconLabel")
        self.verticalLayout_3.addWidget(self.heaterIconLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.powerLabelFail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.powerLabelFail.setFont(font)
        self.powerLabelFail.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.powerLabelFail.setAlignment(QtCore.Qt.AlignCenter)
        self.powerLabelFail.setObjectName("powerLabelFail")
        self.verticalLayout_2.addWidget(self.powerLabelFail)
        self.powerIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.powerIconLabel.setMinimumSize(QtCore.QSize(40, 15))
        self.powerIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.powerIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.powerIconLabel.setText("")
        self.powerIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.powerIconLabel.setObjectName("powerIconLabel")
        self.verticalLayout_2.addWidget(self.powerIconLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 9, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.systemLabelFail = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.systemLabelFail.setFont(font)
        self.systemLabelFail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.systemLabelFail.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.systemLabelFail.setScaledContents(False)
        self.systemLabelFail.setAlignment(QtCore.Qt.AlignCenter)
        self.systemLabelFail.setObjectName("systemLabelFail")
        self.verticalLayout.addWidget(self.systemLabelFail)
        self.systemIconLabel = QtWidgets.QLabel(self.layoutWidget)
        self.systemIconLabel.setMinimumSize(QtCore.QSize(40, 15))
        self.systemIconLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.systemIconLabel.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.systemIconLabel.setText("")
        self.systemIconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.systemIconLabel.setObjectName("systemIconLabel")
        self.verticalLayout.addWidget(self.systemIconLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 10, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 11, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setStyleSheet("QLabel{\n"
"  \n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(40, 15))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_19.setStyleSheet("QLabel{\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
" \n"
"    padding: 6px;\n"
"    background-color: #00FF00 ;\n"
"    color:#FFFFFF;\n"
"}\n"
"QLabel:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}")
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 12, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 400, 67, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/medical-logo-plus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.patientIdLineEdit, self.patientDetailsToolButton)
        MainWindow.setTabOrder(self.patientDetailsToolButton, self.setPointBtn)
        MainWindow.setTabOrder(self.setPointBtn, self.muteToolButton)
        MainWindow.setTabOrder(self.muteToolButton, self.unitChangeToolButton)
        MainWindow.setTabOrder(self.unitChangeToolButton, self.tempDownToolBtn2_9)
        MainWindow.setTabOrder(self.tempDownToolBtn2_9, self.timerButton)
        MainWindow.setTabOrder(self.timerButton, self.heaterLabelMode)
        MainWindow.setTabOrder(self.heaterLabelMode, self.patientNameLineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timerButton.setText(_translate("MainWindow", "Start"))
        self.muteToolButton.setText(_translate("MainWindow", "MUTE"))
        self.setPointBtn.setText(_translate("MainWindow", "SET"))
        self.unitChangeToolButton.setText(_translate("MainWindow", "°C/°F"))
        self.tempDownToolBtn2_9.setText(_translate("MainWindow", "Start \n"
"System"))
        self.tempLabel4.setText(_translate("MainWindow", "36.6"))
        self.setLabelAirTemp.setText(_translate("MainWindow", "36.6"))
        self.setTitleLabel4.setText(_translate("MainWindow", "AIR"))
        self.setTitleLabel2.setText(_translate("MainWindow", "SET"))
        self.setTitleLabel1.setText(_translate("MainWindow", "SET"))
        self.setTitleLabel3.setText(_translate("MainWindow", "SKIN"))
        self.tempLabel3.setText(_translate("MainWindow", "36.6"))
        self.setLabelSkinTemp.setText(_translate("MainWindow", "36.6"))
        self.setTitleLabel2_2.setText(_translate("MainWindow", "MODE"))
        self.setTitleLabel4_2.setText(_translate("MainWindow", "HEATER"))
        self.heaterLabelShow.setText(_translate("MainWindow", "36.6"))
        self.patientDetailsToolButton.setText(_translate("MainWindow", "Patient \n"
"Details"))
        self.setTitleLabel2_4.setText(_translate("MainWindow", "Patient ID:"))
        self.setTitleLabel2_3.setText(_translate("MainWindow", "Patient Name:"))
        self.label_7.setText(_translate("MainWindow", "Alarms"))
        self.timerShowLabel.setText(_translate("MainWindow", "00"))
        self.label_11.setText(_translate("MainWindow", "TIMER"))
        self.probeLabel.setText(_translate("MainWindow", "Probe Fail"))
        self.tempHighLabel.setText(_translate("MainWindow", "Temp High"))
        self.tempLowLabel.setText(_translate("MainWindow", "Temp Low"))
        self.heaterLabelFail.setText(_translate("MainWindow", "Heater Fail"))
        self.powerLabelFail.setText(_translate("MainWindow", "Power Fail"))
        self.systemLabelFail.setText(_translate("MainWindow", "System Fail"))
        self.label_18.setText(_translate("MainWindow", "Probe Fail"))
        self.label_2.setText(_translate("MainWindow", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
