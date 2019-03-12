from PyQt5 import QtCore, QtGui, QtWidgets


class Window2(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self)
        self.setFrameStyle(QtWidgets.QFrame.StyledPanel |
                           QtWidgets.QFrame.Sunken)

        self.label_left = QtWidgets.QLabel()
        self.label_right = QtWidgets.QLabel()
        self.pixmap = QtGui.QPixmap('1.png')
        self.label_left.resize(50, 50)
        # self.pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.label_left.setPixmap(self.pixmap)
        self.label_right.setPixmap(self.pixmap)

        self.mainL = QtWidgets.QHBoxLayout()
        self.mainL.addWidget(self.label_left)
        self.mainL.addWidget(self.label_right)

        self.setLayout(self.mainL)

        self.show()
