from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSlot, QTimer

import configVariables


class TimerCounter:
    def __init__(self, ui):
        self.start = ui.timerButton
        self.reset = ui.timerButton
        self.ui = ui.timerShowLabel
        self.TICK_TIME = 2 ** 6

        # ==================Stop Watch =====================================
        self.reset.clicked.connect(self.do_reset)
        self.start.clicked.connect(self.do_start)
        self.timer = QTimer()
        self.timer.setInterval(self.TICK_TIME)
        self.timer.timeout.connect(self.tick)
        self.do_reset()
        # ==========================+++End Stop watch ==============================================================

        # ================== Start Stop Watch ==================================

    def display(self):
        # self.ui.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))
        hour = "%0d:" % (self.time // 60)
        minSecond = "%05.2f" % (self.time % 60)
        self.convert(self.time)
        listMinSec = minSecond.split(".")

    def tick(self):
        self.time += self.TICK_TIME / 1000
        self.display()

    def do_start(self):
        self.timer.start()
        self.start.setText("Reset")
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/pause_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.start.setIcon(icon9)
        # self.start.setIcon(configVariables.pause_changed_image)
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_pause)

    def do_pause(self):
        self.timer.stop()
        self.time = 0
        self.display()
        self.start.setText("Start")
        # icon9 = QtGui.QIcon()
        # icon9.addPixmap(QtGui.QPixmap("icon/play_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.start.setIcon(icon9)
        # self.start.setIcon(configVariables.play_changed_image)
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_start)

    def do_reset(self):
        self.time = 0
        self.display()

    def convert(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        self.ui.setText(str(
            "%02d" % minutes) + "" + "<b><font size=12pt font weight:40>" + ":" + "</font></b></br>" + "<b><font size=12pt font weight:40>" +
                        str("%02d" % seconds) + "</font></b></br>")
        # return "%d:%02d:%02d" % (hour, minutes, seconds)

        # ==================End Stop Watch =====================================
