from .manager import Manager

# Falta poner el tipo
columns_ingreso = ['id', 'Region', 'Finca', 'Quintales', 'Estado']
columns = ['id', 'Region', 'Finca', 'Libras', 'Estado']


class Coffee:
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

    def cafe_update(self):
        management = Manager()
        data_list = [self.region, self.finca, self.cantidad, self.estado]
        management.update_table('Cafe_ingreso', columns_ingreso, data_list, self.columna, self.valor)

    def cafe_ingreso(self):

        management = Manager()

        data_list = [self.region, self.finca, self.cantidad, self.estado]
        management.insert_into_table('Cafe_ingreso', columns_ingreso, data_list)

    def delete(self):

        management = Manager()

        data_list = [self.region, self.finca, self.cantidad, self.estado]
        management.delete_row('Cafe_ingreso', columns_ingreso, data_list)

    def __str__(self):
        return f"{self.region}, {self.finca}, {self.cantidad}, {self.estado}"
