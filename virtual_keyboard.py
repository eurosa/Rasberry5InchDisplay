import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *


# from allDisplayAttributeColor import AllDisplayAttributeColor


class KeyboardWidget(QDialog):
    def __init__(self, dataModel, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = None
        self.dataModel = dataModel
        # self.obj = AllDisplayAttributeColor(self.dataModel)
        self.text_box_name = None
        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)

        self.initUI()

    @pyqtSlot()
    def do_caps(self):
        # self.timer.start()
        self.names = self.names_caps
        self.buttonAdd()
        self.cap_button.setText("Caps")
        self.cap_button.clicked.disconnect()
        self.cap_button.clicked.connect(self.do_small)

    @pyqtSlot()
    def do_small(self):
        # self.timer.stop()
        self.names = self.names_small
        self.buttonAdd()
        self.cap_button.setText("Small")
        self.cap_button.clicked.disconnect()
        self.cap_button.clicked.connect(self.do_caps)

    def initUI(self):
        self.layout = QGridLayout()

        # p = self.palette()
        # p.setColor(self.backgroundRole(),Qt.white)
        # self.setPalette(p)
        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 14))
        self.text_box.setMinimumHeight(50)
        self.text_box.setMaximumHeight(50)
        # text_box.setFixedHeight(50)
        # self.text_box.setFixedWidth(300)
        self.layout.addWidget(self.text_box, 0, 0, 1, 10)

        self.names_caps = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                           'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                           'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',
                           'Z', 'X', 'C', 'V', 'B', 'N', 'M']

        self.names_small = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
                            'z', 'x', 'c', 'v', 'b', 'n', 'm']

        self.names_sym = ['.', '~', '`', '@', '#', '$', '%', '^', '&&', '*', '(',
                          ')', '_', '-', '+', '=', '|', '[', ']', '{', '}', "'",
                          '"', '<', '>', '?', '\\', '/', '!', '~', ':', ';', '°C', '°F', 'α', 'θ', 'φ']

        self.names = self.names_small
        self.buttonAdd()

        # Cancel button
        clear_button = QPushButton('Clear')
        clear_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # clear_button.setFixedHeight(25)
        clear_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        clear_button.setFont(QFont('Arial', 14))
        clear_button.setMaximumHeight(42)
       # self.obj.changeAttributeColor(clear_button, "QPushButton")
        clear_button.KEY_CHAR = Qt.Key_Clear
        self.layout.addWidget(clear_button, 5, 6, 1, 2)
        # self.layout.addWidget(clear_button, 8, 2, 1, 2)
        clear_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)
        # clear_button.setFixedWidth(60)

        # Space button
        space_button = QPushButton('Space')
        # space_button.setFixedHeight(25)
        space_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
      #  self.obj.changeAttributeColor(space_button, "QPushButton")
        space_button.setFont(QFont('Arial', 14))
        space_button.setMinimumHeight(42)
        space_button.setMaximumHeight(42)
        space_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        space_button.KEY_CHAR = Qt.Key_Space
        self.layout.addWidget(space_button, 5, 2, 1, 4)
        # self.layout.addWidget(space_button, 5, 4, 1, 3)
        space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)
        # space_button.setFixedWidth(85)

        # Back button
        back_button = QPushButton('')
        back_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # back_button.setFixedHeight(25)
        back_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        back_button.setFont(QFont('Arial', 14))
        back_button.setMinimumHeight(42)
        back_button.setMaximumHeight(42)
       #  self.obj.changeAttributeColor(back_button, "QPushButton")
        icon11 = QIcon()
        icon11.addPixmap(QPixmap("icon/backspace-arrow.png"), QIcon.Normal, QIcon.On)
        back_button.setIcon(icon11)
        back_button.KEY_CHAR = Qt.Key_Backspace
        self.layout.addWidget(back_button, 4, 7, 1, 1)
        # self.layout.addWidget(back_button, 5, 7, 1, 2)
        back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)
        # back_button.setFixedWidth(60)

        # Enter button
        enter_button = QPushButton('Enter')
        enter_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # enter_button.setFixedHeight(25)
        enter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        enter_button.setFont(QFont('Arial', 14))
        enter_button.setMinimumHeight(42)
        enter_button.setMaximumHeight(42)
       # self.obj.changeAttributeColor(enter_button, "QPushButton")
        enter_button.KEY_CHAR = Qt.Key_Enter
        self.layout.addWidget(enter_button, 5, 0, 1, 2)
        # self.layout.addWidget(enter_button, 5, 9, 1, 2)
        enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)
        # enter_button.setFixedWidth(60)

        # Done button
        done_button = QPushButton('Done')
        # done_button.setFixedHeight(25)
        done_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        done_button.setFont(QFont('Arial', 14))
        done_button.setMinimumHeight(42)
        done_button.setMaximumHeight(42)
        done_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
       # self.obj.changeAttributeColor(done_button, "QPushButton")
        done_button.KEY_CHAR = Qt.Key_Home
        self.layout.addWidget(done_button, 4, 8, 1, 2)
        # self.layout.addWidget(done_button, 5, 11, 1, 2)
        done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)
        # done_button.setFixedWidth(60)

        # Done button
        self.cap_button = QPushButton('Caps')
        self.cap_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.cap_button.setFixedHeight(25)
        self.cap_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.cap_button.setFont(QFont('Arial', 14))
        self.cap_button.setMinimumHeight(42)
        self.cap_button.setMaximumHeight(42)
        # self.obj.changeAttributeColor(self.cap_button, "QPushButton")
        self.cap_button.KEY_CHAR = Qt.Key_Up
        self.layout.addWidget(self.cap_button, 5, 8, 1, 1)
        # self.layout.addWidget(self.cap_button, 5, 13, 1, 2)
        self.cap_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.cap_button, self.cap_button.KEY_CHAR)
        # self.cap_button.setFixedWidth(60)
        self.cap_button.clicked.connect(self.do_caps)
        # Done button

        sym_button = QPushButton('Sym')
        # sym_button.setFixedHeight(25)
        # sym_button.setFixedWidth(60)
        sym_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sym_button.setMaximumHeight(42)
        sym_button.setMinimumHeight(42)
        sym_button.setFont(QFont('Arial', 14))
        sym_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.obj.changeAttributeColor(sym_button, "QPushButton")
        sym_button.KEY_CHAR = Qt.Key_Down
        self.layout.addWidget(sym_button, 5, 9, 1, 1)
        # self.layout.addWidget(sym_button, 5, 15, 1, 2)
        sym_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(sym_button, sym_button.KEY_CHAR)

        self.setGeometry(0, 0, 480, 300)

        self.setLayout(self.layout)

    def buttonAdd(self):
        # self.names = self.names_small
        # print("loe keyboard")
        positions = [(i + 1, j) for i in range(6) for j in range(10)]
        for position, name in zip(positions, self.names):

            if name == '':
                continue
            button = QPushButton(name)
            button.setFont(QFont('Arial', 14))
            button.setMinimumSize(50, 20)
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            #self.obj.changeAttributeColor(button, "QPushButton")
            button.KEY_CHAR = ord(name[-1])
            button.clicked.connect(self.signalMapper.map)
            self.signalMapper.setMapping(button, button.KEY_CHAR)
            self.layout.addWidget(button, *position)

    def buttonClicked(self, char_ord):
        txt = self.text_box.toPlainText()
        if char_ord == Qt.Key_Up:
            pass
        elif char_ord == Qt.Key_Down:
            self.names = self.names_sym
            self.buttonAdd()
        elif char_ord == Qt.Key_Backspace:
            txt = txt[:-1]
        elif char_ord == Qt.Key_Enter:
            txt += chr(10)
        elif char_ord == Qt.Key_Home:
            self.currentTextBox.setText(txt)
            if self.text_box_name == 'nameLineEdit':
                self.dataModel.set_patient_name(txt)
                print("KEY_HOME_1: " + self.dataModel.get_patient_name())
            elif self.text_box_name == 'ageLineEdit':
                self.dataModel.set_patient_age(txt)
                print("KEY_HOME_2: " + self.dataModel.get_patient_age())
            elif self.text_box_name == 'sexLineEdit':
                self.dataModel.set_patient_sex(txt)
                print("KEY_HOME_3: " + self.dataModel.get_patient_sex())
            elif self.text_box_name == 'patientIdLineEdit':
                self.dataModel.set_patient_id(txt)
                print("KEY_HOME_4: " + self.dataModel.get_patient_id())
            elif self.text_box_name == 'skinLowEditLine':
                self.dataModel.set_skin_low_temp(txt)
            elif self.text_box_name == 'skinHighEditLine':
                self.dataModel.set_skin_high_temp(txt)
            elif self.text_box_name == 'airLowEditLine':
                self.dataModel.set_air_low_temp(txt)
            elif self.text_box_name == 'airHighEditLine':
                self.dataModel.set_air_high_temp(txt)
            # self.text_box.setText("")
            self.hide()
            return
        elif char_ord == Qt.Key_Clear:
            txt = ""
        elif char_ord == Qt.Key_Space:
            txt += ' '
        else:
            txt += chr(char_ord)

        self.text_box.setText(txt)


class Communicate(QObject):
    mousePressSignal = pyqtSignal()


class cQLineEdit(QTextEdit):
    clicked = pyqtSignal()

    def __init__(self, widget, name, dataModel, text_box_name):
        super().__init__(widget)
        # self.name = name
        self.ex = KeyboardWidget(dataModel, self)
        self.ex.setWindowTitle("Keyboard")
        self.ex.setMaximumHeight(375)
        self.ex.dataModel = dataModel
        self.ex.text_box_name = text_box_name
        self.ex.currentTextBox = self
        self.ex.currentTextBox.setText(name)
        self.ex.text_box.setText(name)
        self.ex.currentTextBox.setFixedHeight(40)
        self.ex.currentTextBox.setFixedWidth(350)
        # ==================Set Cursor at the end of text in textedit===============================
        self.ex.text_box.moveCursor(QTextCursor.End)
        self.ex.currentTextBox.moveCursor(QTextCursor.End)
        '''
        cursor1 = QTextCursor()
        self.ex.text_box.setTextCursor(cursor)
        cursor1.insertText(name)
        # neither of the following commands have any effect
        cursor1.setPosition(cursor1.position()-3)
        cursor1.movePosition(cursor1.Right, cursor1.KeepAnchor, 3)'''

    def mousePressEvent(self, QMouseEvent):
        self.ex.show()
        self.clicked.emit()
        '''
class cQLineEdit(QTextEdit):
    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)
        self.ex = KeyboardWidget()

    def mousePressEvent(self, QMouseEvent):
        self.ex.currentTextBox = self
        self.ex.show()
        self.clicked.emit()
'''
