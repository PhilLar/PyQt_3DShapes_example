from PyQt5 import QtCore, QtGui, QtWidgets


class Window2(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self)
        self.setFrameStyle(QtWidgets.QFrame.StyledPanel |
                           QtWidgets.QFrame.Sunken)                  

        self.label_left = QtWidgets.QLabel()
        # self.label_left.resize(self.width()/2, self.height())
        self.label_right = QtWidgets.QLabel()
        # self.label_right.resize(self.width()/2, self.height())
        self.pixmap_r = QtGui.QPixmap('1.png')
        self.pixmap_l = QtGui.QPixmap('code.png')

        self.label_left.setPixmap(self.pixmap_l.scaled(
            self.height(),  self.width()*3, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label_right.setPixmap(self.pixmap_r.scaled(
            self.height(), self.width(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

        # self.label_left.setPixmap(self.pixmap_l)
        # self.label_right.setPixmap(self.pixmap_r)

        self.scrollArea_left = QtWidgets.QScrollArea()
        self.scrollArea_left.setBackgroundRole(QtGui.QPalette.Base)
        self.scrollArea_left.setWidget(self.label_left)

        self.scrollArea_right = QtWidgets.QScrollArea()
        self.scrollArea_right.setBackgroundRole(QtGui.QPalette.Base)
        self.scrollArea_right.setWidget(self.label_right)

        self.mainL = QtWidgets.QHBoxLayout()
        self.mainL.addWidget(self.scrollArea_left, 1)
        self.mainL.addWidget(self.scrollArea_right, 1)

        self.setLayout(self.mainL)

        self.show()
