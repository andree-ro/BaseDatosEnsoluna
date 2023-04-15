from .manager import Manager
from encrypt import *




table_name = 'usuarios'
table_data = ['id', 'nombre', 'rol', 'contraseña', 'Permisos_id']

management = Manager()

encrip = Metodo()
refue = Metodos_refuerzo()
key = "abcdefghijkl12345678!@#$"
# key = 'protodrjympg15599357!@#$'
key1 = "~~Marp~~__842631597"
a = ""
offset = 8
encrypted = ""


class SqlDataBase_usuarios:
	def __init__(self, name, password, role, column = None, data = None, id = None):
		self.name = name
		self.password = password
		self.role = role

		self.column = column
		self.data = data
		self.id = id

		self.permiso_id = self.set_permisos() if self.role != '' else ''

		self.data_list = [self.name, self.role, self.password, self.permiso_id]

	def set_permisos(self):
		if self.role == 'Administrador':
			self.permiso_id = 0

		elif self.role == 'Vendedor':
			self.permiso_id = 1

		elif self.role == 'Bodegero':
			self.permiso_id = 2

		elif self.role == 'Catador':
			self.permiso_id = 3

		return self.permiso_id

	def validate(self):
		if self.name == '' or self.password == '' or self.role == '--Seleccionar--':
			raise Exception('Datos invalidos')

	def new_user(self):
		# self.validate()

		self.set_permisos()
		# falta utilizar libreria para cifrar
		password = self.password
		encrypted = encrip.encrypt(offset, password, key)
		data_list = [self.name, self.role, encrypted, self.permiso_id]


		management.insert_into_table(table_name, table_data, data_list)
		print(encrypted)

	def set_column_name(self):
		if self.column == 'Usuario':
			self.column = 'nombre'

		elif self.column == 'Contraseña':
			self.column = 'contraseña'

	def update_user(self):
		self.validate()

		self.set_permisos()

		if self.column != 'Rol':
			self.set_column_name()

		else:
			self.column = 'Permisos_id'

			tmp = self.data
			tmp2 = self.role

			self.role = self.data

			self.data = self.set_permisos()

			self.role = tmp2

			management.update_table(table_name, table_data, self.data_list, self.column, self.data)

			self.column = 'rol'

			self.data_list[3] = self.data

			self.data = tmp

		management.update_table(table_name, table_data, self.data_list, self.column, self.data)

	def delete_user(self):
		management.delete_id_row(table_name, table_data, self.id)


	def __str__(self):
		return f"name = {self.name}\npassword = {self.password}\nrole = {self.role}" \
			   f"\ncolumn = {self.column}\ndata = {self.data}\nid = {self.id}\npermiso = {self.permiso_id}"