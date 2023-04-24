from .manager import Manager

# Falta poner el tipo
columns_venta = ['id', 'Presentacion', 'Region', 'precioTotal', 'usuarios_id']
columns_hasVenta = ['Venta_idVenta', 'Empacado_idEmpacado', 'Cafe_idCafe', 'cantidad', 'precioUnitario']


class Venta:
    def __init__(self, region, finca, cantidad, precioTotal, precioUnitario, idEmpacado, idCafe, columna = None, valor = None):
        # idVenta
        self.region = region
        self.finca = finca
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        # self.idVenta: int = idVenta
        self.idEmpacado = idEmpacado
        self.precioTotal = precioTotal
        self.idCafe = idCafe
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
        # 1 rojo = San Marcos
        # 2 verde = Coban
        # 3 Turquesa = Huehue
        # 4 Naranja = acatenango
        # 5 amarillo = antigua
        # 6 morado = Nuevo Oriente
        # 7 celeste = Fraijanes
        # 8 azul = atitlan
        u_id = 0
        libra = 'Libra'

        management = Manager()
        print(self.region, self.precioTotal)
        data_listVenta = [libra, self.region, self.precioTotal, u_id]
        data_listHasVenta = [self.idEmpacado, self.idCafe, self.cantidad, self.precioUnitario]
        management.insert_into_table('Venta', columns_venta, data_listVenta)
        management.insert_into_table('Venta_has_Cafe', columns_hasVenta, data_listHasVenta)
