from .manager import Manager
import pandas as pdf
import webbrowser
import pdfrw
from datetime import date

# Falta poner el tipo
columns_ingreso = ['id', 'Region', 'Finca', 'Cantidad', 'Estado']

class venta:
    def __init__(self, region, finca, cantidad, estado, columna = None, valor = None):
        self.region: str = region
        self.finca: str = finca
        self.cantidad: int = cantidad
        self.estado: str = estado
        self.columna = columna
        self.valor = valor

    def management(self, action):
        self.validate()

        if action == 'buy_coffee':
            self.cafe_ingreso()

        elif action == 'converse_coffee':
            pass

        elif action == 'update_coffee':
            self.cafe_update()

        elif action == 'delete_coffee':
            self.delete()

    def validate(self):
        if self.region == '--Seleccionar--' and self.finca == '' and self.cantidad < 0 and self.estado == '--Seleccionar--':
            raise Exception('Datos invalidos')

    def venta_ingreso(self):

        management = Manager()

        data_list = [self.region, self.finca, self.cantidad, self.estado]
        management.insert_into_table('Cafe_ingreso', columns_ingreso, data_list)

    def update_inventario(self):
        pass

