from .manager import Manager

columns_ingreso = ['id', 'Region', 'Finca', 'Quintales', 'Estado', 'Tipo']
columns = ['id', 'Region', 'Finca', 'Libras', 'Estado', 'Tipo']

class Coffee:
    def __init__(self, region, finca, cantidad, estado, tipo):
        self.region : str = region
        self.finca : str = finca
        self.cantidad : int = cantidad
        self.estado : str = estado
        self.tipo : str = tipo

    def management(self, action):
        self.validate()

        if action == 'buy_coffee':
            self.cafe_ingreso()

        elif action == 'converse_coffee':
            pass

    def validate(self):
        if self.region == '--Seleccionar--' and self.finca == '' and self.cantidad < 0 and self.estado == '--Seleccionar--' and self.tipo == '--Seleccionar--':
            raise Exception('Datos invalidos')

    def cafe_update(self):
        pass

    def cafe_ingreso(self):


        management = Manager()

        data_list = [self.region, self.finca, self.cantidad, self.estado, self.tipo]

    def __str__(self):
        return f"{self.region}, {self.finca}, {self.cantidad}, {self.estado}, {self.tipo}"
