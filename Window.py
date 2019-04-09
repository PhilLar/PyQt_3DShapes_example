from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt3DCore, Qt3DExtras, Qt3DInput, Qt3DRender
import logging


from CodeExample import Window2
from WrapperCyl.PyCyl import PyCyl
from Cyl3DEntity import Cyl3DEntity
from QTextEditLogger import QTextEditLogger



class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        # BTNS CREATION #########################
        self.btnCrt_dflt = QtWidgets.QPushButton(
            'Создать объект "а" [конструктор по умолчанию]')
        self.btnCrt = QtWidgets.QPushButton(
            'Создать объект "b", передав аргументы в конструктор')
        self.btnCopy = QtWidgets.QPushButton(
            'Создать объект "с", скопировав объект "b"')
        self.btnCalc_a = QtWidgets.QPushButton(
            'Посчитать объем и полную площадь поверхности "а"')
        self.btnCalc_b = QtWidgets.QPushButton(
            'Посчитать объем и полную площадь поверхности "b"')
        self.btnCalc_c = QtWidgets.QPushButton(
            'Посчитать объем и полную площадь поверхности "c"')
        self.btnDel = QtWidgets.QPushButton('Удалить все созданные объекты')
        # CREATE 3DVIEW ##########################
        self.view = Qt3DExtras.Qt3DWindow()
        self.view.defaultFrameGraph().setClearColor(QtGui.QColor(0x4d4d4f))
        # CONTAINER3D #####################################
        self.container3D = QtWidgets.QWidget.createWindowContainer(self.view)
        screenSize = self.view.screen().size()
        self.container3D.setMinimumSize(QtCore.QSize(200, 100))
        self.container3D.setMaximumSize(screenSize)
        # 3D_SHAPE #####################################
        self.camera = self.view.camera()
        self.camera.lens().setPerspectiveProjection(45.0, 16.0/9.0, 0.1, 1000)
        self.camera.setPosition(QtGui.QVector3D(0, 0, 40))
        self.camera.setViewCenter(QtGui.QVector3D(0, 0, 0))
        # LIST OF OBJECTS #################################
        self.code = Window2()
        self.code.resize(4, 5)
        # LOGGER ##########################################
        logTextBox = QTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter(
            '%(asctime)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.INFO)
        # LAYOUT CREATION #################################
        # main box
        self.mainL = QtWidgets.QHBoxLayout()
        # main left box
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.container3D)

        # main right box
        self.vbox = QtWidgets.QVBoxLayout()
        
        # code example box
        self.codeEx = QtWidgets.QHBoxLayout()
        self.codeEx.addWidget(self.code)
        # btns box
        self.btnsBox = QtWidgets.QHBoxLayout()

        self.btnsBox_left = QtWidgets.QVBoxLayout()
        self.btnsBox_right = QtWidgets.QVBoxLayout()
        self.btnsBox_left.addWidget(self.btnCrt_dflt)
        self.btnsBox_left.addWidget(self.btnCrt)
        self.btnsBox_right.addWidget(self.btnCopy)
        self.btnsBox_right.addWidget(self.btnDel)

        self.btnsBox.addLayout(self.btnsBox_left, 1)
        self.btnsBox.addLayout(self.btnsBox_right, 1)

        # self.vbox.addStretch()
        #self.vbox.addStretch(3)
        self.vbox.addLayout(self.codeEx, 1)
        self.vbox.addLayout(self.btnsBox, 1)
        self.vbox.addWidget(logTextBox.widget, 1)

        self.hbox.setStretchFactor(self.vbox, 10)
        self.mainL.addLayout(self.hbox, 1)
        self.mainL.addLayout(self.vbox, 1)
        self.setLayout(self.mainL)
        # CONNECTIONS #####################################
        self.btnCrt_dflt.clicked.connect(self.Crt_dflt)
        self.btnCrt.clicked.connect(self.Crt)
        self.btnCopy.clicked.connect(self.Copy)
        self.btnCalc_a.clicked.connect(self.Calc_a)
        self.btnCalc_b.clicked.connect(self.Calc_b)
        self.btnCalc_c.clicked.connect(self.Calc_c)
        self.btnDel.clicked.connect(self.Destr)
        # INSTANCE FUNS ##############################

    def Crt(self):
        # self.modal = ModalWindowCrt(self)
        # self.view.setRootEntity(self.modal.scene)
        # MODAL INPUT FORM ##############################
        self.modal = QtWidgets.QWidget(self, QtCore.Qt.Window)
        self.modal.setWindowTitle('input data')
        self.modal.setWindowModality(QtCore.Qt.WindowModal)
        self.e1 = QtWidgets.QLineEdit()
        self.e2 = QtWidgets.QLineEdit()
        btn = QtWidgets.QPushButton('ок')
        flo = QtWidgets.QFormLayout()
        flo.addRow('высота', self.e1)
        flo.addRow('радиус', self.e2)
        flo.addWidget(btn)
        self.modal.setLayout(flo)
        self.modal.show()
        btn.clicked.connect(self.btnCrt_accept)

    def Crt_dflt(self):
        self.a = PyCyl()
        # self.l.append(self.a)
        logging.info('Создан объект "а" с параметрами высота = {}, радиус = {}'.format(
            self.a.getHeight(), self.a.getRad()))
        self.scene = Cyl3DEntity(self.a.getHeight(), self.a.getRad())
        self.view.setRootEntity(self.scene)
        # Switch to btn_Calc
        self.btnsBox_left.removeWidget(self.btnCrt_dflt)
        self.btnCrt_dflt.hide()
        self.btnCrt_dflt.setEnabled(False)
        self.btnsBox_left.insertWidget(0, self.btnCalc_a)
        self.btnCalc_a.show()
        self.btnCalc_a.setEnabled(True)

    def Destr(self):
        if not self.btnCrt_dflt.isEnabled():
            self.btnsBox_left.removeWidget(self.btnCalc_a)
            self.btnCalc_a.hide()
            self.btnCalc_a.setEnabled(False)

            self.btnsBox_left.insertWidget(0, self.btnCrt_dflt)
            self.btnCrt_dflt.show()
            self.btnCrt_dflt.setEnabled(True)

            del self.a
            self.view.setRootEntity(None)
            logging.info('Объект был удален')

        if not self.btnCrt.isEnabled():
            self.btnsBox_left.removeWidget(self.btnCalc_b)
            self.btnCalc_b.hide()
            self.btnCalc_b.setEnabled(False)

            self.btnsBox_left.insertWidget(1, self.btnCrt)
            self.btnCrt.show()
            self.btnCrt.setEnabled(True)

            del self.b
            self.view.setRootEntity(None)
            logging.info('Объект был удален')

        if not self.btnCopy.isEnabled():
            self.btnsBox_left.removeWidget(self.btnCalc_c)
            self.btnCalc_c.hide()
            self.btnCalc_c.setEnabled(False)

            self.btnsBox_right.insertWidget(0, self.btnCopy)
            self.btnCopy.show()
            self.btnCopy.setEnabled(True)

            del self.c
            self.view.setRootEntity(None)
            logging.info('Объект был удален')
            
        
    def Copy(self):
        try:
            self.c = PyCyl(obj = self.b)
            # self.l.append(self.c)
            logging.info('Создан объект "с" как копия объекта "b"')
            self.scene = Cyl3DEntity(self.c.getHeight(), self.c.getRad())
            self.view.setRootEntity(self.scene)
            # Switch to btn_Calc
            self.btnsBox_right.removeWidget(self.btnCopy)
            self.btnCopy.hide()
            self.btnCopy.setEnabled(False)
            self.btnsBox_right.insertWidget(0, self.btnCalc_c)
            self.btnCalc_c.show()
            self.btnCalc_c.setEnabled(True)
        except AttributeError:
            logging.info('Нельзя создать копию без оригинала')

    def btnCrt_accept(self):
        if self.e1.text().isdigit() and self.e2.text().isdigit():
            self.height = int(self.e1.text())
            print(self.height)
            self.rad = int(self.e2.text())
            self.modal.close()
            self.b = PyCyl(self.height, self.rad)
            # self.l.append(self.b)
            self.scene = Cyl3DEntity(self.b.getHeight(), self.b.getRad())
            self.view.setRootEntity(self.scene)
            #logging.info('an object was created with pa')
            self.btnsBox_left.removeWidget(self.btnCrt)
            self.btnCrt.hide()
            self.btnCrt.setEnabled(False)
            self.btnsBox_left.insertWidget(1, self.btnCalc_b)
            self.btnCalc_b.show()
            self.btnCalc_b.setEnabled(True)
            logging.info('Создан объект "b" с радиусом={} и высотой={}'.format(self.b.getRad(), self.b.getHeight()))
        else:
            logging.info('Высота и радиус должны быть положительными!')

    def Calc_a(self):
        logging.info('Объем объекта "а" = {}, полная площадь поверхности "а" = {}'.format(
            self.a.volume(), self.a.full_Square()))
    
    def Calc_b(self):
        logging.info('Объем объекта "b" = {}, полная площадь поверхности "b" = {}'.format(
            self.b.volume(), self.b.full_Square()))
    
    def Calc_c(self):
        logging.info(
            'Объем объекта "c" = {}, полная площадь поверхности "c" = {}'.format(
                self.c.volume(), self.c.full_Square()))
