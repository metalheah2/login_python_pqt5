import sqlite3

conn=sqlite3.connect('base_datos_login.db')
c=conn.cursor()

def create_table():
	try:
		c.execute("CREATE TABLE IF NOT EXISTS Base_Usuarios(Usuario TEXT,Correo TEXT,Clave TEXT)")
		conn.commit()
		#c.close()
		#conn.close()
		print("Tabla creada")
	except:
		print("Hubo un error ó la tabla ya existe ¡")

def data_entry(usuario,correo,clave):
	try:
		c.execute("INSERT INTO Base_Usuarios VALUES('{}','{}','{}')".format(usuario,correo,clave))
		conn.commit()
		#c.close()
		#conn.close()
		return "Exito"
	except:
		return "Error"
		
def base_datos_recv(usuario):
	try:
		dato=c.execute("select Correo,Clave from Base_Usuarios Where Usuario=?",(usuario, ))
		fila=c.fetchone()
		correo_base=fila[0]
		clave_base=fila[1]
		return correo_base,clave_base

	except:
		print("Error , el usuario no existe ¡")
		correo_base,clave_base="Error","Error"
		return correo_base,clave_base

#c.close()
#conn.close()
	