from .manager import Manager

# Falta poner el tipo
columns_ingreso = ['id', 'Region', 'Finca', 'Quintales', 'Estado', 'Tipo']
columns = ['id', 'Region', 'Finca', 'Libras', 'Estado', 'Tipo']


class Coffee:
    def __init__(self, region, finca, cantidad, estado, tipo, columna=None, valor=None, id=None):
        self.region: str = region
        self.finca: str = finca
        self.cantidad: int = cantidad
        self.estado: str = estado
        self.tipo: str = tipo
        self.columna = columna
        self.valor = valor
        self.id = id

    def management(self, action):
        # self.validate()
        if action == 'buy_coffee':
            self.cafe_ingreso()
        elif action == 'converse_coffee':
            pass
        elif action == 'update_coffee':
            self.cafe_update()
        elif action == 'delete_coffee':
            self.delete()

    def validate(self):
        if self.region == '--Seleccionar--' or self.finca == '' and self.cantidad < 0 and self.estado == '--Seleccionar--':
            raise Exception('Datos invalidos')

    def cafe_update(self):
        management = Manager()
        if self.columna == 'Quintales':
            data = int(self.valor) * 100
            columna = 'Libras'
            print(data, columna)
            management.update_table_with_id('Cafe_ingreso', columns_ingreso, self.columna, self.valor, self.id)
            management.update_table_with_id('Cafe', columns, columna, data, self.id)
        else:
            management.update_table_with_id('Cafe_ingreso', columns_ingreso, self.columna, self.valor, self.id)
            management.update_table_with_id('Cafe', columns, self.columna, self.valor, self.id)

    def cafe_ingreso(self):
        management = Manager()
        data_list = [self.region, self.finca, self.cantidad, self.estado, self.tipo]
        management.insert_into_table('Cafe_ingreso', columns_ingreso, data_list)
        cantidad = self.cantidad * 100
        data = [self.region, self.finca, cantidad, self.estado, self.tipo]
        management.insert_into_table('Cafe', columns, data)

    def delete(self):
        management = Manager()
        # cantidad = self.cantidad * 100
        # data = [self.region, self.finca, cantidad, self.estado]
        # data_list = [self.region, self.finca, self.cantidad, self.estado]
        management.delete_id_row('Cafe_ingreso', columns_ingreso, self.id)
        management.delete_id_row('Cafe', columns, self.id)

    def __str__(self):
        return f"{self.region}, {self.finca}, {self.cantidad}, {self.estado}"
