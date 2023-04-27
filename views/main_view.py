from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sql_structures
import pandas as pdf
import webbrowser
import pdfrw
from datetime import date
from encrypt import *
from reportlab.pdfgen import canvas
from datetime import datetime

from sql_structures import Manager


# usuarios = sql_structures.SqlDataBase_usuarios()

# TODO
# Agregar al calendario mes y año (Juan Diego)
# Agregar mensajes de confirmacion
# Componer ventas(Agregar nit, nombre e incrementar numero de factura y cotizacion)

# Obtener fechas y no string (Javier)
# Ordenar el codigo
# Manual de usuario
# Explicarnos el codigo


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/designs/DB1.ui', self)


        # ATENCION A CLICK EN TABLA
        self.fila = 0
        self.idFactura = 0
        self.tableWidget.cellClicked.connect(self.mostrarFila_c)
        self.tableWidget_2.cellClicked.connect(self.mostrarFila_e)
        self.tableWidget_5.cellClicked.connect(self.mostrarFila_cat)
        self.tableWidget_usuarios_2.cellClicked.connect(self.mostrarFila_ventas)
        self.tableWidget_usuarios_2.cellClicked.connect(self.carga_detalles)
        self.agregarCotizacion_2.clicked.connect(self.agregarCliente)


        self.productos = []
        self.total = 0
        self.frame_menu.hide()
        self.btn_menu.hide()
        self.btn_menu_2.hide()
        self.btn_menu_3.hide()
        self.btn_menu_5.hide()
        self.btn_restaurar.hide()
        self.btn_minimizar.clicked.connect(self.minimizar)
        self.btn_restaurar.clicked.connect(self.normal)
        self.btn_maximizar.clicked.connect(self.maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())
        self.btn_menu.clicked.connect(self.menu_show)
        self.btn_menu_2.clicked.connect(self.menu_hide)
        self.btn_menu_4.clicked.connect(self.menu_2_hide)
        self.btn_menu_3.clicked.connect(self.menu_2_show)
        self.btn_menu_6.clicked.connect(self.menu_3_hide)
        self.btn_menu_5.clicked.connect(self.menu_3_show)
        self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        # paginas
        self.btn_inventario.clicked.connect(self.show_page_inventario)
        self.btn_ventas.clicked.connect(self.show_page_ventas)
        self.btn_mobiliario.clicked.connect(self.show_page_mobiliario)
        self.btn_catacion.clicked.connect(self.show_page_catacion)
        self.btn_usuario.clicked.connect(self.show_page_usuarios)
        self.btn_ensoluna.clicked.connect(self.show_page_inicio)
        self.btn_agregar_I.clicked.connect(self.show_page_compras)
        self.btn_actualizar_I.clicked.connect(self.show_page_compras_a)
        self.btn_eliminar_I.clicked.connect(self.delete_coffee)
        self.btn_eliminar_2.clicked.connect(self.delete_packaging)
        self.btn_detalles_venta.clicked.connect(self.show_page_detalles_venta)

        # Volver
        self.btn_volver_I.clicked.connect(self.show_page_inventario)
        self.btn_volver_I_2.clicked.connect(self.show_page_inventario)
        self.btn_volver_I_3.clicked.connect(self.show_page_inventario)
        self.btn_volver_I_4.clicked.connect(self.show_page_usuarios)
        self.btn_volver_catacion.clicked.connect(self.show_page_catacion)
        self.btn_volver_catacion_2.clicked.connect(self.show_page_catacion)
        self.btn_volver_catacion_3.clicked.connect(self.show_page_catacion)
        # catacion
        self.btn_agregar_C.clicked.connect(self.show_page_agregar_catacion)
        self.btn_actualizar_C.clicked.connect(self.show_page_actualizar_catacion)
        self.btn_eliminar_C.clicked.connect(self.delete_catacion)
        # Usuarios
        # self.cargar_usuarios.clicked.connect(self.loaddata)
        self.btn_administrar.clicked.connect(self.show_page_usuarios_admin)
        # self.btn_agregar_usuarios.clicked.connect(self.new_user)
        # self.btn_eliminar_usuarios.clicked.connect(self.delete_user)
        # self.btn_actualizar_usuarios.clicked.connect(self.update_user)
        # Inicio sesion
        # self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        # COMPRAS CAFE
        self.cafeComprarBTN.clicked.connect(self.buy_coffee)

        # ACTUALIZACION CAFE
        self.cafeAcBTN.clicked.connect(self.update_coffee)

        # BORRAR CAFE
        self.eliminarBTN.clicked.connect(self.delete_coffee)

        # COMPRAS EMPAQUETADO
        self.empaquetadoComprarBTN.clicked.connect(self.buy_packaging)

        # ACTUALIZACION EMPAQUETADO
        self.actualizarEmpaqueBTN.clicked.connect(self.update_packaging)

        # BORRAR EMPAQUETADO
        self.eliminarEmpBTN.clicked.connect(self.delete_packaging)

        # AGREGAR USUSARIO
        self.btn_agregar_usuarios.clicked.connect(self.new_user)
        self.btn_actualizar_usuarios.clicked.connect(self.update_user)
        self.btn_eliminar_usuarios.clicked.connect(self.delete_user)

        # BOTON CARGAR CAFE Y EMPAQUETADO
        self.cargar_invetario.clicked.connect(self.carga_cafe_empacado)
        self.cargar_invetario_3.clicked.connect(self.carga_catacion)
        self.cargar_usuarios.clicked.connect(self.carga_usuario)

        # AGREGAR CATACION
        self.cafeComprarBTN_2.clicked.connect(self.new_catacion)
        self.cafeComprarBTN_3.clicked.connect(self.update_catacion)
        self.eliminarBTN_2.clicked.connect(self.delete_catacion)

        # GENERAR COTIZACION
        self.realizado_cotizacion.clicked.connect(self.realizarCotizacion)

        # AGREGAR COTIZACION ARRAY
        self.agregarCotizacion.clicked.connect(self.agregarCotizacionUno)

        # GENERAR FACTURA
        self.realizado_facturacion.clicked.connect(self.realizarFactura)
        #self.realizado_facturacion.clicked.connect(self.nueva_venta)

        # AGREGAR FACTURA AL ARRAY
        self.agregarFactura.clicked.connect(self.agregarFacturaUno)

        # Agregar mobiliario
        self.agregarmobiliario.clicked.connect(self.add_mobiliario)
        self.cargar_mobiliario.clicked.connect(self.carga_mobiliario)

        # Detalle venta
        self.cargar_usuarios_2.clicked.connect(self.carga_venta)

    def mostrarFila_ventas(self, row, column):
        print('1')
        manager = sql_structures.Manager()
        print('2')
        item = self.tableWidget_usuarios_2.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'Presentacion', 'Region', 'precioTotal', 'usuario_id']
        print('3')

        # Obtener el nombre de la columna
        header_item = self.tableWidget_usuarios_2.horizontalHeaderItem(column)
        column_name = header_item.text()
        print('4')

        # Realizar la búsqueda en la base de datos según la columna correspondiente
        if column_name == 'No.':
            self.id_v = manager.get('venta', columns_ingreso, value, 'id')
        elif column_name == 'Region':
            self.id_v = manager.get('venta', columns_ingreso, value, 'Region')
        elif column_name == 'Presentacion':
            self.id_v = manager.get('venta', columns_ingreso, value, 'Presentacion')
        elif column_name == 'Precio Total':
            self.id_v = manager.get('venta', columns_ingreso, value, 'PrecioTotal')

        print(value)
        print(column_name)
        print(self.id_v)

    def mostrarFila_e(self, row, column):
        print('1')
        manager = sql_structures.Manager()
        print('2')
        item = self.tableWidget_2.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'Estampa', 'Color', 'Tamaño', 'Cantidad']
        print('3')

        # Obtener el nombre de la columna
        header_item = self.tableWidget_2.horizontalHeaderItem(column)
        column_name = header_item.text()
        print('4')

        # Realizar la búsqueda en la base de datos según la columna correspondiente
        if column_name == 'Sticker-Región':
            self.id_e = manager.get('Empacado', columns_ingreso, value, 'Estampa')
        elif column_name == 'Bolsa-Color':
            self.id_e = manager.get('Empacado', columns_ingreso, value, 'Color')
        elif column_name == 'Tamaño':
            self.id_e = manager.get('Empacado', columns_ingreso, value, 'Tamaño')
        elif column_name == 'Cantidad':
            self.id_e = manager.get('Empacado', columns_ingreso, value, 'Cantidad')

        print(value)
        print(column_name)
        print(self.id_e)

    def mostrarFila_c(self, row, column):
        manager = sql_structures.Manager()
        item = self.tableWidget.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'Region', 'Finca', 'Libras', 'Estado']

        # Obtener el nombre de la columna
        header_item = self.tableWidget.horizontalHeaderItem(column)
        column_name = header_item.text()

        # Realizar la búsqueda en la base de datos según la columna correspondiente
        if column_name == 'Región':
            self.id_c = manager.get('Cafe', columns_ingreso, value, 'Region')
        elif column_name == 'Finca':
            self.id_c = manager.get('Cafe', columns_ingreso, value, 'Finca')
        elif column_name == 'Cantidad':
            self.id_c = manager.get('Cafe', columns_ingreso, value, 'Libras')
        elif column_name == 'Estado':
            self.id_c = manager.get('Cafe', columns_ingreso, value, 'Estado')
        elif column_name == 'Tipo':
            self.id_c = manager.get('Cafe', columns_ingreso, value, 'Tipo')

        print(value)
        print(column_name)
        print(self.id_c)

    def mostrarFila_cat(self, row, column):
        manager = sql_structures.Manager()
        item = self.tableWidget_5.item(row, column)
        value = item.text()
        columns_ingreso = ['id', 'Aroma', 'Finca', 'Region', 'Altura', 'Sabor', 'Color', 'Puntuacion']

        # Obtener el nombre de la columna
        header_item = self.tableWidget_5.horizontalHeaderItem(column)
        column_name = header_item.text()

        # Realizar la búsqueda en la base de datos según la columna correspondiente
        if column_name == 'Aroma':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Aroma')
        elif column_name == 'Finca':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Finca')
        elif column_name == 'Región':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Region')
        elif column_name == 'Altura':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Altura')
        elif column_name == 'Sabor':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Sabor')
        elif column_name == 'Color':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Color')
        elif column_name == 'Puntuación':
            self.id_cat = manager.get('Catacion', columns_ingreso, value, 'Puntuacion')
        # elif column_name == 'Tipo':
        #     self.id_c = manager.get('Cafe', columns_ingreso, value, 'Tamaño')

        print(value)
        print(column_name)
        print(self.id_cat)

    def add_mobiliario(self):
        date = str(self.calendar.selectedDate())
        date_split = date.split("(")
        Str = date_split[1]
        lenght = len(date_split[1])
        calendario = Str[:lenght - 1]
        date = str(self.ultserv.date())
        date_split = date.split("(")
        Str = date_split[1]
        lenght = len(date_split[1])
        ult = Str[:lenght - 1]
        date = str(self.proxser.date())
        date_split = date.split("(")
        Str = date_split[1]
        lenght = len(date_split[1])
        prox = Str[:lenght - 1]
        try:
            mobiliario = sql_structures.SqlDataBase_mobiliario(self.ag_maquina.currentText(),
                                           ult,
                                           prox,
                                           calendario)
            mobiliario.management('add_mobiliario')
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def new_user(self):
        try :
            usuarios = sql_structures.SqlDataBase_usuarios(self.info_usuario.text(),
                                                           self.info_contrasena.text(),
                                                           self.info_rol.currentText())
            usuarios.new_user()
            self.info_usuario.clear()
            self.info_contrasena.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def update_user(self):
        try:
            usuarios = sql_structures.SqlDataBase_usuarios(self.info_usuario_a.text(),
                                                           self.info_contrasena_a.text(),
                                                           self.info_rol_a.currentText(),
                                                           self.combo_edit.currentText(),
                                                           self.Info_edit.text())
            usuarios.update_user()
            self.info_usuario_a.clear()
            self.info_contrasena_a.clear()
            self.Info_edit.clear()
            QMessageBox.about(self, 'Aviso', 'Modificado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al modificar!')

    def delete_user(self):
        try:
            usuarios = sql_structures.SqlDataBase_usuarios('', '', '', '', '', self.info_usuario_e.text())
            usuarios.delete_user()
            self.info_usuario_e.clear()
            QMessageBox.about(self, 'Aviso', 'Eliminado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al eliminar!')

    def new_catacion(self):
        try:
            catacion = sql_structures.Catacion(self.aroma_catacion.text(),
                                               self.finca_catacion.text(),
                                               self.region_catacion.currentText(),
                                               self.altura_catacion.text(),
                                               self.sabor_catacion.text(),
                                               self.color_catacion.text(),
                                               self.puntuacion_catacion.text())
            catacion.management('ing_catacion')
            self.aroma_catacion.clear()
            self.finca_catacion.clear()
            self.altura_catacion.clear()
            self.sabor_catacion.clear()
            self.color_catacion.clear()
            self.puntuacion_catacion.clear()
            QMessageBox.about(self, 'Aviso', 'Agregado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error de agregado!')

    def update_catacion(self):
        try:
            catacion = sql_structures.Catacion('',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               self.columnaAcText_2.currentText(),
                                               self.valorAcText_2.text(),
                                               self.aroma_catacion_2.text())
            catacion.management('update_catacion')
            self.aroma_catacion_2.clear()
            self.valorAcText_2.clear()
        except Exception as e:
            print(e)

    def delete_catacion(self):
        try:
            catacion = sql_structures.Catacion('',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               '',
                                               self.id_cat)
            catacion.management('delete_catacion')
            self.finca_catacion_3.clear()
            QMessageBox.about(self, 'Aviso', 'Eliminado correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al Eliminar!')

    # METODOS/FUNCIONES CLASE COFFEE
    def buy_coffee(self):
        try:
            coffee = sql_structures.Coffee(self.regionCombobx.currentText(),
                                           self.fincaText.text(),
                                           int(self.cantidadText.text()),
                                           self.estadoCombobx.currentText(),
                                           self.tipoCombobx.currentText())
            coffee.management('buy_coffee')

            self.fincaText.clear()
            self.cantidadText.clear()
            QMessageBox.about(self, 'Aviso', 'La compra se realizo con exito!')

        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Compra fallida!')

    def update_coffee(self):
        try:
            coffee = sql_structures.Coffee('',
                                           '',
                                           '',
                                           '',
                                           self.columnaAcText.currentText(),
                                           self.valorAcText.text(), int(self.fincaAcText.text()))
            coffee.management('update_coffee')
            self.fincaAcText.clear()
            self.valorAcText.clear()
            QMessageBox.about(self, 'Aviso', 'Se modifico con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Modificacion fallida!')

    def delete_coffee(self):
        try:
            coffee = sql_structures.Coffee('',
                                           '',
                                           '',
                                           '',
                                           '',
                                           '',
                                           self.id_c)
            coffee.management('delete_coffee')
            self.fincaElimText.clear()
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')

    # METODOS/FUNCIONES CLASE PACKAGING
    def buy_packaging(self):
        try:
            coffee = sql_structures.Packaging(self.stickerText.text(),
                                              self.colorBolsaText.text(),
                                              self.tamanioText.text(),
                                              self.lineEdit.text())
            coffee.management('buy_packaging')
            self.stickerText.clear()
            self.colorBolsaText.clear()
            self.tamanioText.clear()
            QMessageBox.about(self, 'Aviso', 'La compra se realizo con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Compra fallida!')

    def update_packaging(self):
        try:
            coffee = sql_structures.Packaging(
                '',
                '',
                '',
                self.columnaAcEmCombobx.currentText(),
                self.valorAcEmText.text(),
                self.colorAcText.text())
            coffee.management('update_packaging')

            self.colorAcText.clear()
            self.valorAcEmText.clear()
            QMessageBox.about(self, 'Aviso', 'Se modifico con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Modificacion fallida!')

    def delete_packaging(self):
        try:
            coffee = sql_structures.Packaging('',
                                              '',
                                              '',
                                              '',
                                              '',
                                              self.id_e)
            coffee.management('delete_packaging')
            self.colorElimText.clear()
            QMessageBox.about(self, 'Aviso', 'Se elimino con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Eliminacion fallida!')

    def carga_cafe_empacado(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('Cafe')
            dato2 = mana.print_table('Empacado')
            self.tableWidget.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
            self.tableWidget_2.setRowCount(len(dato2))
            for x in range(len(dato2)):
                self.tableWidget_2.setItem(x, 0, QTableWidgetItem(str(dato2[x][1])))
                self.tableWidget_2.setItem(x, 1, QTableWidgetItem(str(dato2[x][2])))
                self.tableWidget_2.setItem(x, 2, QTableWidgetItem(str(dato2[x][3])))
                self.tableWidget_2.setItem(x, 3, QTableWidgetItem(str(dato2[x][4])))
        except Exception as e:
            print(e)

    def carga_catacion(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('Catacion')
            self.tableWidget_5.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tableWidget_5.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tableWidget_5.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tableWidget_5.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
                self.tableWidget_5.setItem(i, 4, QTableWidgetItem(str(dato[i][5])))
                self.tableWidget_5.setItem(i, 5, QTableWidgetItem(str(dato[i][6])))
                self.tableWidget_5.setItem(i, 6, QTableWidgetItem(str(dato[i][7])))
        except Exception as e:
            print(e)

    def carga_usuario(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('usuarios')
            self.tableWidget_usuarios.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tableWidget_usuarios.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tableWidget_usuarios.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tableWidget_usuarios.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
        except Exception as e:
            print(e)

    def carga_mobiliario(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('mobiliario')
            self.tableWidget_6.setRowCount(len(dato))
            for i in range(len(dato)):
                self.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(dato[i][1])))
                self.tableWidget_6.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tableWidget_6.setItem(i, 2, QTableWidgetItem(str(dato[i][3])))
                self.tableWidget_6.setItem(i, 3, QTableWidgetItem(str(dato[i][4])))
        except Exception as e:
            print(e)

    def carga_venta(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('Venta')
            dato1 = mana.print_table('Venta_has_Cafe')
            self.tableWidget_usuarios_2.setRowCount(len(dato))
            self.tableWidget_usuarios_2.setRowCount(len(dato1))
            for i in range(len(dato)):
                self.tableWidget_usuarios_2.setItem(i, 0, QTableWidgetItem(str(dato[i][0])))
                self.tableWidget_usuarios_2.setItem(i, 1, QTableWidgetItem(str(dato[i][2])))
                self.tableWidget_usuarios_2.setItem(i, 2, QTableWidgetItem(str(dato[i][1])))
                self.tableWidget_usuarios_2.setItem(i, 3, QTableWidgetItem(str(dato[i][3])))
        except Exception as e:
            print(e)

    def carga_detalles(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('factura')
            dato2 = mana.print_table('Cafe')


            dato1 = mana.print_table('Venta_has_Cafe')
            self.tableWidget_usuarios_3.setRowCount(len(dato))
            self.tableWidget_usuarios_3.setRowCount(len(dato2))
            self.tableWidget_usuarios_3.setRowCount(len(dato1))

            self.tableWidget_usuarios_3.setItem(0, 0, QTableWidgetItem(str(dato1[int(self.id_v)][3])))
            self.tableWidget_usuarios_3.setItem(0, 1, QTableWidgetItem(str(dato1[int(self.id_v)][4])))
            finca = dato1[int(self.id_v)][2]
            self.tableWidget_usuarios_3.setItem(0, 2, QTableWidgetItem(str(dato2[int(finca)][2])))
            self.tableWidget_usuarios_3.setItem(0, 3, QTableWidgetItem(str(dato[int(self.id_v)][2])))
        except Exception as e:
            print(e)

    def minimizar(self):
        self.showMinimized()

    def normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()

    def iniciar_sesion(self):
        encrip = Metodo()
        refue = Metodos_refuerzo()
        key = "abcdefghijkl12345678!@#$"
        # key = 'protodrjympg15599357!@#$'
        key1 = "~~Marp~~__842631597"
        a = ""
        offset = 8
        encrypted = ""
        usuario_comprobacion = self.lineEdit_usuarios.text()
        usuario = sql_structures.Manager()
        rol = usuario.iniciar_ses(usuario_comprobacion)
        contrasena_comprobacion = self.lineEdit_contrasena.text()
        contrasena = usuario.iniciar_contra(usuario_comprobacion)
        c = encrip.decrypt(offset, contrasena, key)
        if contrasena_comprobacion == c:
            t = True
            if rol == 1:
                self.menu_show()
            elif rol == 2:
                self.menu_show()
                self.btn_inventario.hide()
                self.btn_mobiliario.hide()
                self.btn_catacion.hide()
                self.btn_usuario.hide()
            elif rol == 3:
                self.menu_show()
                self.btn_ventas.hide()
                self.btn_mobiliario.hide()
                self.btn_catacion.hide()
                self.btn_usuario.hide()
            elif rol == 4:
                self.menu_show()
                self.btn_inventario.hide()
                self.btn_mobiliario.hide()
                self.btn_ventas.hide()
                self.btn_usuario.hide()
            else:
                QMessageBox.about(self, 'Aviso', 'Usuario incorrecto!')
        else:
            QMessageBox.about(self, 'Aviso', 'Contraseña incorrecta!')

    def menu_show(self):
        self.btn_menu.hide()
        self.btn_menu_2.show()
        self.frame_menu.show()

    def menu_hide(self):
        self.btn_menu.show()
        self.btn_menu_2.hide()
        self.frame_menu.hide()

    def menu_2_show(self):
        self.btn_menu_4.show()
        self.btn_menu_3.hide()
        self.frame_menu_2.show()

    def menu_2_hide(self):
        self.btn_menu_3.show()
        self.btn_menu_4.hide()
        self.frame_menu_2.hide()

    def menu_3_show(self):
        self.btn_menu_6.show()
        self.btn_menu_5.hide()
        self.frame_menu_3.show()

    def menu_3_hide(self):
        self.btn_menu_5.show()
        self.btn_menu_6.hide()
        self.frame_menu_3.hide()

    def show_page_inventario(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def show_page_ventas(self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def show_page_mobiliario(self):
        self.stackedWidget.setCurrentWidget(self.page_mobiliario)

    def show_page_catacion(self):
        self.stackedWidget.setCurrentWidget(self.page_catacion)

    def show_page_usuarios(self):
        self.stackedWidget.setCurrentWidget(self.page_usuario)

    def show_page_inicio(self):
        self.stackedWidget.setCurrentWidget(self.page_inicio)

    def show_page_compras(self):
        self.stackedWidget.setCurrentWidget(self.page_compras)

    def show_page_compras_a(self):
        self.stackedWidget.setCurrentWidget(self.page_compras_actualizar)

    def show_page_compras_e(self):
        self.stackedWidget.setCurrentWidget(self.page_compras_eliminar)

    def show_page_usuarios_admin(self):
        self.stackedWidget.setCurrentWidget(self.page_administrar_usuarios)

    def show_page_agregar_catacion(self):
        self.stackedWidget.setCurrentWidget(self.page_catacion_agregar)

    def show_page_actualizar_catacion(self):
        self.stackedWidget.setCurrentWidget(self.page_catacion_actualizar)

    def show_page_eliminar_catacion(self):
        self.stackedWidget.setCurrentWidget(self.page_catacion_eliminar)

    def show_page_detalles_venta(self):
        self.stackedWidget.setCurrentWidget(self.page_detalles_venta)

    # COTIZACION
    # METODO AGREGAR COTIZACION BOTON
    def agregarCotizacionUno(self):
        try:
            region = self.regionAcCombobx_3.currentText()
            finca = self.fincaAcText_3.text()
            cantidadUnidad = self.cantidadAcText_3.text()
            estado = self.estadoAcText_3.currentText()
            precioUnidad = self.lineEdit_5.text()
            self.productos.append({"region": region,
                                   "finca": finca,
                                   "cantidadUnidad": cantidadUnidad,
                                   "estado": estado,
                                   "precioUnidad": precioUnidad})
            self.fincaAcText_3.clear()
            self.cantidadAcText_3.clear()
            self.lineEdit_5.clear()
            QMessageBox.about(self, 'Aviso', 'Cotizacion realizada con exito!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error en la cotizacion!')

    def realizarCotizacion(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')

        # Crear un nuevo documento PDF
        pdf = canvas.Canvas(f"cotizacion{self.idFactura}.pdf")
        # Configurar el estilo del texto
        pdf.setFont("Helvetica", 12)

        # Agregar los datos del cliente
        cliente_nombre = str(self.fincaAcText_4.text())
        cliente_nit = str(self.fincaAcText_5.text())
        cliente_direccion = str(self.fincaAcText_6.text())
        pdf.drawString(100, 700, "Cliente: " + cliente_nombre)
        pdf.drawString(100, 680, "NIT: " + cliente_nit)
        pdf.drawString(100, 660, "Dirección: " + cliente_direccion)
        pdf.drawString(400, 700, f"Cotizacion: ---")
        pdf.drawString(400, 680, f"Fecha: {formato}")
        y = 600  # Posición vertical inicial
        pdf.drawString(50, 620, "PROUCTO")
        pdf.drawString(150, 620, "FINCA")
        pdf.drawString(225, 620, "CANTIDAD UNIDAD")
        pdf.drawString(375, 620, "ESTADO")
        pdf.drawString(450, 620, "PRECIO UNIDAD")

        for producto in self.productos:
            pdf.drawString(50, y, producto["region"])
            pdf.drawString(150, y, str(producto["finca"]))
            pdf.drawString(225, y, str(producto["cantidadUnidad"]))
            pdf.drawString(375, y, str(producto["estado"]))
            pdf.drawString(450, y, str(producto["precioUnidad"]))
            y -= 20

        for producto in self.productos:
            total = float(producto["precioUnidad"]) * int(producto["cantidadUnidad"])
            self.total = total + self.total

        pdf.drawString(400, y - 20, "Total: " + str(self.total))
        pdf.save()
        factura = f"cotizacion{self.idFactura}.pdf"
        webbrowser.open_new(factura)
        self.productos.clear()
        self.total = 0

    def agregarFacturaUno(self):
        region = self.comboBox.currentText()
        finca = self.lineEdit_3.text()
        cantidadUnidad = self.lineEdit_4.text()
        estado = self.comboBox_2.currentText()
        precioUnidad = self.lineEdit_6.text()
        self.productos.append({"region": region,
                               "finca": finca,
                               "cantidadUnidad": cantidadUnidad,
                               "estado": estado,
                               "precioUnidad": precioUnidad})
        try:
            region = self.comboBox.currentText()
            finca = self.lineEdit_3.text()
            data = ['id', 'Estampa', 'Color', 'Tamaño']
            color = 'Color'
            manager = sql_structures.Manager()
            # print(region)
            if region == 'Huehuetenango':
                self.idEmpaque = manager.get('Empacado', data, 'Turquesa', color)
            elif region == 'San Marcos':
                self.idEmpaque = manager.get('Empacado', data, 'Rojo', color)
            elif region == 'Coban':
                self.idEmpaque = manager.get('Empacado', data, 'Verde', color)
            elif region == 'Acatenango':
                self.idEmpaque = manager.get('Empacado', data, 'Naranja', color)
            elif region == 'Antigua':
                self.idEmpaque = manager.get('Empacado', data, 'Amarillo', color)
            elif region == 'Nuevo Oriente':
                self.idEmpaque = manager.get('Empacado', data, 'Morado', color)
            elif region == 'Fraijanes':
                self.idEmpaque = manager.get('Empacado', data, 'Celeste', color)
            elif region == 'Atitlan':
                self.idEmpaque = manager.get('Empacado', data, 'Azul', color)
            columnsCafe = ['id', 'Region', 'Finca', 'Libras', 'Estado']
            fin = 'Finca'
            print(finca)
            self.idCafe = manager.get('Cafe', columnsCafe, finca, fin)
            print('hola3')
            total = 0
            total = int(self.lineEdit_4.text()) * int(self.lineEdit_6.text())
            venta_d = sql_structures.Venta(self.comboBox.currentText(),
                                         self.lineEdit_3.text(),
                                         int(self.lineEdit_4.text()),
                                         total, self.lineEdit_6.text(), self.idEmpaque, self.idCafe)
            venta_d.management('venta_cafe')
            QMessageBox.about(self, 'Aviso', 'Se agrego correctamente!')
        except Exception as e:
            print(e)
            QMessageBox.about(self, 'Aviso', 'Error al agregar!')

        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_6.clear()

        # TODO
        # lIMPIAR TEXT

    def agregarCliente(self):
        management = Manager()
        mana = sql_structures.Manager()
        nombre = self.fincaAcText_4.text()
        # nit = self.fincaAcText_5.text()
        direccion = self.fincaAcText_6.text()
        data_list = [direccion, nombre, 0]
        columns_ingreso = ['id', 'Direccion', 'Cliente', 'Venta_id']
        management.insert_into_table('factura', columns_ingreso, data_list)
        self.idFac = mana.get('factura', columns_ingreso, nombre, 'Cliente')

    def realizarFactura(self):

        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')

        # Crear un nuevo documento PDF
        pdf = canvas.Canvas(f"factura{self.idFactura}.pdf")
        # Configurar el estilo del texto
        pdf.setFont("Helvetica", 12)

        # Agregar los datos del cliente
        cliente_nombre = str(self.fincaAcText_4.text())
        cliente_nit = str(self.fincaAcText_5.text())
        cliente_direccion = str(self.fincaAcText_6.text())
        pdf.drawString(100, 700, "Cliente: " + cliente_nombre)
        pdf.drawString(100, 680, "NIT: " + cliente_nit)
        pdf.drawString(100, 660, "Dirección: " + cliente_direccion)
        pdf.drawString(400, 700, f"Factura: {self.idFactura + self.idFac}")
        pdf.drawString(400, 680, f"Fecha: {formato}")
        y = 600  # Posición vertical inicial
        pdf.drawString(50, 620, "PROUCTO")
        pdf.drawString(150, 620, "FINCA")
        pdf.drawString(225, 620, "CANTIDAD UNIDAD")
        pdf.drawString(375, 620, "ESTADO")
        pdf.drawString(450, 620, "PRECIO UNIDAD")

        for producto in self.productos:
            pdf.drawString(50, y, producto["region"])
            pdf.drawString(150, y, str(producto["finca"]))
            pdf.drawString(225, y, str(producto["cantidadUnidad"]))
            pdf.drawString(375, y, str(producto["estado"]))
            pdf.drawString(450, y, str(producto["precioUnidad"]))
            y -= 20

        for producto in self.productos:
            total = float(producto["precioUnidad"]) * int(producto["cantidadUnidad"])
            self.total = total + self.total

        pdf.drawString(400, y - 20, "Total: " + str(self.total))
        pdf.save()
        factura = f"factura{self.idFactura}.pdf"
        webbrowser.open_new(factura)
        self.productos.clear()
        self.total = 0
