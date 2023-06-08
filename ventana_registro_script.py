# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ventana_registro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana_reg(object):
    def setupUi(self, ventana_reg):
        ventana_reg.setObjectName("ventana_reg")
        ventana_reg.setEnabled(True)
        ventana_reg.resize(359, 161)
        ventana_reg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(88, 191, 82, 255));")
        self.centralwidget = QtWidgets.QWidget(ventana_reg)
        self.centralwidget.setObjectName("centralwidget")
        self.label_registro = QtWidgets.QLabel(self.centralwidget)
        self.label_registro.setGeometry(QtCore.QRect(20, 10, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_registro.setFont(font)
        self.label_registro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_registro.setObjectName("label_registro")
        self.boton_aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_aceptar.setGeometry(QtCore.QRect(120, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.boton_aceptar.setFont(font)
        self.boton_aceptar.setObjectName("boton_aceptar")
        ventana_reg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventana_reg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 21))
        self.menubar.setObjectName("menubar")
        ventana_reg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventana_reg)
        self.statusbar.setObjectName("statusbar")
        ventana_reg.setStatusBar(self.statusbar)

        self.retranslateUi(ventana_reg)
        QtCore.QMetaObject.connectSlotsByName(ventana_reg)

    def retranslateUi(self, ventana_reg):
        _translate = QtCore.QCoreApplication.translate
        ventana_reg.setWindowTitle(_translate("ventana_reg", "MainWindow"))
        self.label_registro.setText(_translate("ventana_reg", "Registro Existoso ¡¡"))
        self.boton_aceptar.setText(_translate("ventana_reg", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_reg = QtWidgets.QMainWindow()
    ui = Ui_ventana_reg()
    ui.setupUi(ventana_reg)
    ventana_reg.show()
    sys.exit(app.exec_())

