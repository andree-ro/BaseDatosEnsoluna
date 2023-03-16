import sqlite3 as sql
from PyQt5 import QtWidgets


class SqlDataBase_usuarios:
	def __init__(self):
		self.conn = sql.connect("usuarios.db")

	def createDB(self):
		self.conn.commit()
		self.conn.close()

	def createTable(self):
		cursor = self.conn.cursor()
		cursor.execute(
			"""CREATE TABLE usuarios (
				usuario text,
				contrasena text,
				rol text
			)"""
		)
		self.conn.commit()
		self.conn.close()

	def updateFields(self, usuario, contrasena, rol):
		cursor = self.conn.cursor()
		instruccion = f"UPDATE usuarios SET contrasena = '{contrasena}' WHERE usuario like '{usuario}%'  "
		instruccion_2 = f"UPDATE usuarios SET rol = '{rol}' WHERE usuario like '{usuario}%'  "
		cursor.execute(instruccion)
		cursor.execute(instruccion_2)
		self.conn.commit()

	def insertRow(self, usuario, contrasena, rol):
		cursor = self.conn.cursor()
		instruccion = f"INSERT INTO usuarios VALUES ('{usuario}', '{contrasena}', '{rol}') "
		cursor.execute(instruccion)
		self.conn.commit()

	def deleteRow(self, usuario):
		cursor = self.conn.cursor()
		instruccion = f"DELETE FROM usuarios WHERE usuario like '{usuario}%'"
		cursor.execute(instruccion)
		self.conn.commit()

	def usuarios(self, tableWidget_usuarios):
		cursor = self.conn.cursor()
		instruccion = "SELECT * FROM usuarios"
		result = cursor.execute(instruccion)
		tableWidget_usuarios.setRowCount(0)

		for row_number, row_data in enumerate(result):
			tableWidget_usuarios.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				tableWidget_usuarios.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

	def get_rol(self, usuario):
		cursor = self.conn.cursor()
		instruccion = f"SELECT rol FROM usuarios Where usuario = '{usuario}'"
		cursor.execute(instruccion)
		result = cursor.fetchall()
		result = result[0][0]
		return str(result)
