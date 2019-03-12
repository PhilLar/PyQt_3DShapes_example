# -*- coding: utf-8 -*-
import sys
#from OpenGL import GL
from PyQt5 import QtCore, QtGui, QtWidgets
from Window import Window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    window = Window()

    window.setWindowTitle('exper')
    window.resize(1200, 800)

    window.show()
    sys.exit(app.exec_())
