# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaz_grafica_registro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_segunda(object):
    def setupUi(self, segunda):
        segunda.setObjectName("segunda")
        segunda.resize(499, 591)
        segunda.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(88, 191, 82, 255));")
        self.centralwidget = QtWidgets.QWidget(segunda)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 30, 401, 541))
        self.frame.setStyleSheet("background-color: rgb(90, 160, 240);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(117, 191, 113, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.reg_boton_registro = QtWidgets.QPushButton(self.frame)
        self.reg_boton_registro.setGeometry(QtCore.QRect(50, 430, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.reg_boton_registro.setFont(font)
        self.reg_boton_registro.setStyleSheet("background-color: rgb(120, 152, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(88, 191, 82, 255));")
        self.reg_boton_registro.setObjectName("reg_boton_registro")
        self.reg_usuario = QtWidgets.QLineEdit(self.frame)
        self.reg_usuario.setGeometry(QtCore.QRect(50, 140, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.reg_usuario.setFont(font)
        self.reg_usuario.setObjectName("reg_usuario")
        self.reg_correo = QtWidgets.QLineEdit(self.frame)
        self.reg_correo.setGeometry(QtCore.QRect(50, 250, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.reg_correo.setFont(font)
        self.reg_correo.setObjectName("reg_correo")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(231, 231, 231);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 310, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.reg_clave = QtWidgets.QLineEdit(self.frame)
        self.reg_clave.setGeometry(QtCore.QRect(50, 360, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.reg_clave.setFont(font)
        self.reg_clave.setObjectName("reg_clave")
        segunda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(segunda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        segunda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(segunda)
        self.statusbar.setObjectName("statusbar")
        segunda.setStatusBar(self.statusbar)

        self.retranslateUi(segunda)
        QtCore.QMetaObject.connectSlotsByName(segunda)

    def retranslateUi(self, segunda):
        _translate = QtCore.QCoreApplication.translate
        segunda.setWindowTitle(_translate("segunda", "MainWindow"))
        self.reg_boton_registro.setText(_translate("segunda", "Registrate"))
        self.label.setText(_translate("segunda", "Registro"))
        self.label_2.setText(_translate("segunda", "Usuario:"))
        self.label_3.setText(_translate("segunda", "Correo Electronico:"))
        self.label_4.setText(_translate("segunda", "Contraseña:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    segunda = QtWidgets.QMainWindow()
    ui = Ui_segunda()
    ui.setupUi(segunda)
    segunda.show()
    sys.exit(app.exec_())

