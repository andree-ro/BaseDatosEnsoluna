from .manager import Manager

# Falta poner el tipo
columns_venta = ['id', 'Region', 'Finca', 'Cantidad', 'Estado']
columns_hasVenta = ['Venta_idVenta', 'Empacado_idEmpacado', 'Cafe_idCafe', 'cantidad', 'precioUnitario']

class Venta:
    def __init__(self, region, finca, cantidad, precioTotal, precioUnitario, idEmpacado, idCafe, estado, columna = None, valor = None):
        # idVenta
        self.region: str = region
        self.finca: str = finca
        self.cantidad: int = cantidad
        self.estado: str = estado
        self.precioUnitario: float = precioUnitario
        # self.idVenta: int = idVenta
        self.idEmpacado: int = idEmpacado
        self.precioTotal: float = precioTotal
        self.idCafe: int = idCafe
        self.columna = columna
        self.valor = valor

    def management(self, action):
        self.validate()

        if action == 'venta_cafe':
            self.venta_cafe()

        elif action == 'converse_coffee':
            pass

        elif action == 'update_coffee':
            self.cafe_update()

        elif action == 'delete_coffee':
            self.delete()

    def validate(self):
        if self.region == '--Seleccionar--' and self.finca == '' and self.cantidad < 0 and self.estado == '--Seleccionar--':
            raise Exception('Datos invalidos')

    def update_inventario(self):
        pass

    def venta_cafe(self):
        data = ['id', 'Estampa', 'Color', 'Tamaño']
        # 1 rojo = San Marcos
        # 2 verde = Coban
        # 3 Turquesa = Huehue
        # 4 Naranja = acatenango
        # 5 amarillo = antigua
        # 6 morado = Nuevo Oriente
        # 7 celeste = Fraijanes
        # 8 azul = atitlan

        management = Manager()

        color = ['rojo', 'verde', 'turquesa', 'naranja', 'amarillo', 'morado', 'celeste', 'azul']
        # data_listVenta = [self.region, self.finca, self.cantidad, self.estado]
        idEmpaque = management.get_id('Empacado', data, color, )
        data_listVenta = [self.estado, self.region, self.precioTotal, self.estado]
        data_listHasVenta = [self.idEmpacado, self.idCafe, self.cantidad, self.precioUnitario, 1]
        management.insert_into_table('venta', columns_venta, data_listVenta)
        management.insert_into_table_NID('venta_has_cafe', columns_hasVenta, data_listHasVenta)
