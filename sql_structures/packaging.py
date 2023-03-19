from .manager import Manager

# Falta poner el tipo
columns_ingreso = ['id', 'Estampa', 'Color', 'Tamaño']


# columns = ['id', 'Region', 'Finca', 'Libras', 'Estado']


class Packaging:
    def __init__(self, estampa, color, tamanio, columna=None, valor=None):
        self.estampa: str = estampa
        self.color: str = color
        self.tamanio: int = tamanio
        self.columna = columna
        self.valor = valor

    def management(self, action):
        self.validate()

        if action == 'buy_packaging':
            self.packaging_ingreso()
        elif action == 'update_packaging':
            self.packaging_update()
        elif action == 'delete_packaging':
            self.packaging_delete()

    def validate(self):
        if self.estampa == '' and self.color == '' and self.tamanio == '':
            raise Exception('Datos invalidos')

    def packaging_update(self):
        management = Manager()
        data_list = [self.estampa, self.color, self.tamanio]
        management.update_table('Empacado', columns_ingreso, data_list, self.columna, self.valor)

    def packaging_ingreso(self):
        management = Manager()
        data_list = [self.estampa, self.color, self.tamanio]
        management.insert_into_table('Empacado', columns_ingreso, data_list)

    def packaging_delete(self):
        management = Manager()
        data_list = [self.estampa, self.color, self.tamanio]
        management.delete_row('Empacado', columns_ingreso, data_list)

    def __str__(self):
        return f"{self.estampa}, {self.color}, {self.tamanio}"
