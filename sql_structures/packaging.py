from .manager import Manager

# Falta poner el tipo
columns_ingreso = ['id', 'Estampa', 'Color', 'Tamaño']

# 1 rojo = San Marcos
# 2 verde = Coban
# 3 Turquesa = Huehue
# 4 Naranja = acatenango
# 5 amarillo = antigua
# 6 morado = Nuevo Oriente
# 7 celeste = Fraijanes
# 8 azul = atitlan

# columns = ['id', 'Region', 'Finca', 'Libras', 'Estado']


class Packaging:
    def __init__(self, estampa, color, tamanio, columna=None, valor=None, id = None):
        self.estampa: str = estampa
        self.color: str = color
        self.tamanio: int = tamanio
        self.columna = columna
        self.valor = valor
        self.id = id
    def management(self, action):
        # self.validate()
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
        management.update_table_with_id('Empacado', columns_ingreso, self.columna, self.valor, self.id)

    def packaging_ingreso(self):
        management = Manager()
        data_list = [self.estampa, self.color, self.tamanio]
        management.insert_into_table('Empacado', columns_ingreso, data_list)

    def packaging_delete(self):
        management = Manager()
        # data_list = [self.estampa, self.color, self.tamanio]
        management.delete_id_row('Empacado', columns_ingreso, self.id)

    def __str__(self):
        return f"{self.estampa}, {self.color}, {self.tamanio}"
