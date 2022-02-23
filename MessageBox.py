from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox


class AutoCloseMessageBox(QMessageBox):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.timeout = 0
        self.autoclose = False
        self.currentTime = 0

    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        self.currentTime += 1
        if self.currentTime >= self.timeout:
            self.done(0)

    @staticmethod
    def showWithTimeout(timeoutSeconds, message, title, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = AutoCloseMessageBox()
        w.autoclose = True
        w.timeout = timeoutSeconds
        w.setText(message)
        w.setWindowTitle(title)
        w.setIcon(icon)
        # w.setStandardButtons(buttons)
        w.exec_()

    '''
    @staticmethod
    def showWithTimeout(timeoutSeconds, message, title, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = AutoCloseMessageBox()
        w.autoclose = True
        w.timeout = timeoutSeconds
        w.setText(message)
        w.setWindowTitle(title)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()
    
    self.timeout = int()
        self.autoClose = bool()
        self.currentTime = int()
        self.timer = QTimer()

    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoClose:
            self.timer.start(1000)

    def timerEvent(self, *args, **kwargs):
        self.currentTime += 1
        print(self.currentTime)
        if self.currentTime >= self.timeout:
            self.done(0)

    def setAutoClose(self, value):
        self.autoClose = value

    def setTimeout(self, value):
        self.timeout = value'''
