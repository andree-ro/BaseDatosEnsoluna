from .manager import Manager
from encrypt import *

table_name = 'mobiliario'
table_data = ['idMoviliario', 'maquina', 'ultimo_servicio', 'proximo_servicio', 'fecha_adquisicion']

management = Manager()


class SqlDataBase_mobiliario:
	def __init__(self, maquina, ultimo_servicio, proximo_servicio, fecha_adquisicion, column = None, data = None, id = None):
		self.maquina = maquina
		self.ultimo_servicio = ultimo_servicio
		self.proximo_servicio = proximo_servicio
		self.fecha_adquisicion = fecha_adquisicion
		self.column = column
		self.data = data
		self.id = id
		self.data_list = [self.maquina, self.ultimo_servicio, self.proximo_servicio, self.fecha_adquisicion]

	def management(self, action):
		self.validate()
		if action == 'add_mobiliario':
			self.new_mobiliario()

	def validate(self):
		if self.maquina == '' or self.ultimo_servicio == '' or self.proximo_servicio == '' or self.fecha_adquisicion == '':
			raise Exception('Datos invalidos')

	def new_mobiliario(self):
		# self.validate()
		data_list = [self.maquina, self.ultimo_servicio, self.proximo_servicio, self.fecha_adquisicion]
		management.insert_into_table(table_name, table_data, data_list)

	def __str__(self):
		return f"maquina = {self.maquina}\nultimo servicio = {self.ultimo_servicio}\nproximo servicio = {self.proximo_servicio}" \
			   f"\nfecha de adquisicion = {self.fecha_adquisicion}\ncolumn = {self.column}\ndata = {self.data}\nid = {self.id}"