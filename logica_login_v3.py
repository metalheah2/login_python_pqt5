import sys
#from PyQt5 import uic, QtWidgets
from interfaz_login import *
from interfaz_registro import *
from ventana_registro_script import *
from base_datos_login_script_v2 import *

create_table()



class MainWindow(QtWidgets.QMainWindow,Ui_principal,Ui_segunda):
	def __init__(self,*args,**kwargs):
		QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
		_translate=QtCore.QCoreApplication.translate
		self.setupUi(self)
		
		self.log_boton_registro.clicked.connect(self.ventana_de_registro)
		self.log_boton_login.clicked.connect(self.base_datos_usuarios)
		
	def ventana_de_registro(self):
		self.ventana_de_registro=QtWidgets.QMainWindow()
		self.registro=Ui_segunda()
		self.registro.setupUi(self.ventana_de_registro)
		self.ventana_de_registro.show()
		self.registro.reg_boton_registro.clicked.connect(self.vent_registro_confirmacion)
		
	def vent_registro_confirmacion(self):
		self.ventana_registro_confirmacion=QtWidgets.QMainWindow()
		self.vent_confirmacion=Ui_ventana_reg()
		self.vent_confirmacion.setupUi(self.ventana_registro_confirmacion)
		self.ventana_registro_confirmacion.show()
		usuario_reg=self.registro.reg_usuario.text()
		usuario_correo=self.registro.reg_correo.text()
		usuario_clave=self.registro.reg_clave.text()
		data=data_entry(usuario_reg,usuario_correo,usuario_clave)
		if(data=="Exito"):
			self.vent_confirmacion.label_registro.setText("Registro Exitoso")
		if(data=="Error"):
			self.vent_confirmacion.label_registro.setText("Error")
		self.vent_confirmacion.boton_aceptar.clicked.connect(self.terminar_registro)
		
	def terminar_registro(self):
		self.ventana_registro_confirmacion.close()
		self.ventana_de_registro.close()
		
	def base_datos_usuarios(self):
		self.ventana_registro_confirmacion=QtWidgets.QMainWindow()
		self.vent_confirmacion=Ui_ventana_reg()
		self.vent_confirmacion.setupUi(self.ventana_registro_confirmacion)
		usuario=self.log_usuario.text()
		correo,clave=base_datos_recv(usuario)
		clave_login=self.log_clave.text()
		if(clave_login==clave):
			self.vent_confirmacion.label_registro.setText("Bienvenido ¡¡")
			self.ventana_registro_confirmacion.show()
		else:
			self.vent_confirmacion.label_registro.setText("Error")
			self.ventana_registro_confirmacion.show()
		
	
 
if __name__=="__main__":
	app=QtWidgets.QApplication([])
	window=MainWindow()
	window.show()
	app.exec_()