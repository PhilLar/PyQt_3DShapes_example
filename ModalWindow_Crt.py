from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt3DCore, Qt3DExtras, Qt3DInput, Qt3DRender
from WrapperCyl.PyCyl import PyCyl
from Cyl3DEntity import Cyl3DEntity


class ModalWindowCrt(QtWidgets.QWidget):
    def __init__(self, Parent):
        QtWidgets.QWidget.__init__(self)
        self.resize(200, 50)
        self.setWindowModality(QtCore.Qt.WindowModal)
        # BTNS CREATION ############################
        btn = QtWidgets.QPushButton('ок')
        # INPUT LINES ###############################
        self.e1 = QtWidgets.QLineEdit()
        self.e2 = QtWidgets.QLineEdit()
        # LAYOUT ####################################
        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow('высота', self.e1)
        self.flo.addRow('радиус', self.e2)
        self.flo.addWidget(btn)
        self.setLayout(self.flo)
        self.show()
        # CONNECTIONS ###############################
        btn.clicked.connect(self.btn_press)
        Parent.view.setRootEntity(self.scene)
        # INSTANCE FUNS ###############################

    def btn_press(self):
        print(self.Parent)
        height = int(self.e1.text())
        print(height)
        rad = int(self.e2.text())
        self.close()
        self.b_obj = PyCyl(height, rad)
        self.scene = Cyl3DEntity(self.b.getHeight(), self.b.getRad())
        #Parent.view.setRootEntity(self.scene)
           # logging.info('something to remember')

            # def Crt(self):
            # self.modal=QtWidgets.QWidget(self, QtCore.Qt.Window)
            # self.modal.resize(200, 50)
            # self.modal.setWindowModality(QtCore.Qt.WindowModal)
            # self.e1=QtWidgets.QLineEdit()
            # self.e2=QtWidgets.QLineEdit()
            # btn=QtWidgets.QPushButton('ок')
            # flo=QtWidgets.QFormLayout()
            # flo.addRow('высота', self.e1)
            # flo.addRow('радиус', self.e2)
            # flo.addWidget(btn)
            # self.modal.setLayout(flo)
            # self.modal.show()
            # btn.clicked.connect(self.btn_press)
