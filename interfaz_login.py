# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaz_grafica.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_principal(object):
    def setupUi(self, principal):
        principal.setObjectName("principal")
        principal.resize(482, 571)
        principal.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(88, 191, 82, 255));")
        self.centralwidget = QtWidgets.QWidget(principal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 401, 471))
        self.frame.setStyleSheet("background-color: rgb(90, 160, 240);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(117, 191, 113, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.log_boton_login = QtWidgets.QPushButton(self.frame)
        self.log_boton_login.setGeometry(QtCore.QRect(50, 350, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.log_boton_login.setFont(font)
        self.log_boton_login.setStyleSheet("background-color: rgb(120, 152, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(88, 191, 82, 255));")
        self.log_boton_login.setObjectName("log_boton_login")
        self.log_usuario = QtWidgets.QLineEdit(self.frame)
        self.log_usuario.setGeometry(QtCore.QRect(50, 160, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.log_usuario.setFont(font)
        self.log_usuario.setObjectName("log_usuario")
        self.log_clave = QtWidgets.QLineEdit(self.frame)
        self.log_clave.setGeometry(QtCore.QRect(50, 280, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.log_clave.setFont(font)
        self.log_clave.setText("")
        self.log_clave.setObjectName("log_clave")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(231, 231, 231);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(46, 112, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 230, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.log_boton_registro = QtWidgets.QPushButton(self.frame)
        self.log_boton_registro.setGeometry(QtCore.QRect(130, 410, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_boton_registro.setFont(font)
        self.log_boton_registro.setObjectName("log_boton_registro")
        principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")
        principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(principal)
        self.statusbar.setObjectName("statusbar")
        principal.setStatusBar(self.statusbar)

        self.retranslateUi(principal)
        QtCore.QMetaObject.connectSlotsByName(principal)

    def retranslateUi(self, principal):
        _translate = QtCore.QCoreApplication.translate
        principal.setWindowTitle(_translate("principal", "MainWindow"))
        self.log_boton_login.setText(_translate("principal", "Login"))
        self.label.setText(_translate("principal", "Bienvenido"))
        self.label_2.setText(_translate("principal", "Usuario:"))
        self.label_3.setText(_translate("principal", "Contraseña:"))
        self.log_boton_registro.setText(_translate("principal", "Registrarse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    principal = QtWidgets.QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())

