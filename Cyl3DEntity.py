from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt3DCore, Qt3DExtras, Qt3DInput, Qt3DRender


class Cyl3DEntity(Qt3DCore.QEntity):
    def __init__(self, height, rad):
        Qt3DCore.QEntity.__init__(self)

        self.cylMesh = Qt3DExtras.QCylinderMesh()
        self.cylMesh.setRadius(rad)
        self.cylMesh.setLength(height)
        # self.cylMesh.setRings(100)
        # self.cylMesh.setSlices(20)

        self.cylTransform = Qt3DCore.QTransform()
        self.cylTransform.setScale(1)
        self.cylTransform.setRotation(
            QtGui.QQuaternion.fromAxisAndAngle(QtGui.QVector3D(1, 0, 0), 45))
        self.cylTransform.setTranslation(QtGui.QVector3D(0, 0, 0))

        self.material = Qt3DExtras.QDiffuseSpecularMaterial()
        self.material.setSpecular(QtGui.QColor(0x928327))
        self.material.setShininess(100)

        self.addComponent(self.cylMesh)
        self.addComponent(self.material)
        self.addComponent(self.cylTransform)
