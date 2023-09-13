from .manager import Manager
columns_ingreso = ['id', 'Hora', 'Usuario', 'Modulo', 'Estado', 'Error']

class Transaccion:
    def __init__(self, hora, usuario, modulo, estado, error, columna=None, valor=None, id=None):
        self.hora = hora
        self.usuario = usuario
        self.modulo = modulo
        self.estado = estado
        self.error = error
        self.columna = columna
        self.valor = valor
        self.id = id

    def management(self, action):
        if action == 'ingresar_transaccion':
            self.transaccion_ingreso()

    def transaccion_ingreso(self):
        management = Manager()
        data_list = [self.hora, self.usuario, self.modulo, self.estado, self.error]
        management.insert_into_table('transaccion', columns_ingreso, data_list)

    def __str__(self):
        return f"{self.hora}, {self.usuario}, {self.modulo}, {self.estado}, {self.error}"

