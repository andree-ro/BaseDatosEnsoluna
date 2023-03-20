from .manager import  Manager

columns_ingreso = ['id', 'Aroma', 'Finca', 'Region', 'Altura', 'Sabor', 'Color', 'Puntuacion', 'usuarios_id']

class Catacion:
    def __init__(self, aroma, finca, region, altura, sabor, color, puntuacion, columna = None, valor = None):
        self.aroma: str = aroma
        self.finca: str = finca
        self.region: str = region
        self.altura: str = altura
        self.sabor: str = sabor
        self.color: str = color
        self.puntuacion: float = puntuacion
        self.columna = columna
        self.valor = valor

    def management(self, action):
        self.validate()

        if action == 'ing_catacion':
            self.catacion_ingreso()

        elif action == 'update_catacion':
            self.catacion_update()

        elif action == 'delete_catacion':
            self.delete()

    def validate(self):
        if self.aroma == '' and self.finca == '' and self.region == '--Seleccionar--' and self.altura >= 0 and self.sabor == '' and self.color == '' and self.puntuacion >= 0:
            raise Exception('Datos invalidos')

    def catacion_update(self):

        management = Manager()
        data_list = [self.aroma, self.finca, self.region, self.altura, self.sabor, self.color, self.puntuacion]
        management.update_table('Catacion', columns_ingreso, data_list, self.columna, self.valor)

    def catacion_ingreso(self):

        management = Manager()

        data_list = [self.aroma, self.finca, self.region, self.altura, self.sabor, self.color, self.puntuacion]
        management.insert_into_table('Catacion', columns_ingreso, data_list)

    def delete(self):

        management = Manager()

        data_list = [self.aroma, self.finca, self.region, self.altura, self.sabor, self.color, self.puntuacion]
        management.delete_row('Catacion', columns_ingreso, data_list)
