from PyQt5 import QtCore, QtGui, QtWidgets
import logging

class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.widget.setFixedHeight(250)
        #self.widget.setFixedWidth(600)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)
