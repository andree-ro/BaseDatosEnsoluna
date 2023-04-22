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

# usuarios = sql_structures.SqlDataBase_usuarios()

# TODO
# - Agregar mensajes de confirmacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/designs/DB1.ui', self)
        self.productos = []
        self.frame_menu.hide()
        # self.btn_menu.hide()
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
        self.btn_eliminar_I.clicked.connect(self.show_page_compras_e)
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
        self.btn_eliminar_C.clicked.connect(self.show_page_eliminar_catacion)
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

        # AGREGAR FACTURA AL ARRAY
        self.agregarFactura.clicked.connect(self.agregarFacturaUno)

        # Agregar mobiliario
        self.agregarmobiliario.clicked.connect(self.add_mobiliario)
        self.cargar_mobiliario.clicked.connect(self.carga_mobiliario)

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
        except Exception as e:
            print(e)

    def new_user(self):
        usuarios = sql_structures.SqlDataBase_usuarios(self.info_usuario.text(),
                                                       self.info_contrasena.text(),
                                                       self.info_rol.currentText())

        usuarios.new_user()

        self.info_usuario.clear()
        self.info_contrasena.clear()

    def update_user(self):
        usuarios = sql_structures.SqlDataBase_usuarios(self.info_usuario_a.text(),
                                                       self.info_contrasena_a.text(),
                                                       self.info_rol_a.currentText(),
                                                       self.info_rol_a_columna.currentText(),
                                                       self.info_usuario_a_valor.text())

        usuarios.update_user()

        self.info_usuario_a.clear()
        self.info_contrasena_a.clear()
        self.info_usuario_a_valor.clear()

    def delete_user(self):
        usuarios = sql_structures.SqlDataBase_usuarios('', '', '', '', '', self.info_usuario_e.text())

        usuarios.delete_user()

    def new_catacion(self):
        catacion = sql_structures.Catacion(self.aroma_catacion.text(),
                                           self.finca_catacion.text(),
                                           self.region_catacion.currentText(),
                                           self.altura_catacion.text(),
                                           self.sabor_catacion.text(),
                                           self.color_catacion.text(),
                                           self.puntuacion_catacion.text())

        catacion.management('ing_catacion')

    def update_catacion(self):
        catacion = sql_structures.Catacion(self.aroma_catacion.text(),
                                           self.finca_catacion.text(),
                                           self.region_catacion.currentText(),
                                           self.altura_catacion.text(),
                                           self.sabor_catacion.text(),
                                           self.color_catacion.text(),
                                           self.puntuacion_catacion.text(),
                                           self.columnaAcText_2.currentText(),
                                           self.valorAcText_2.text())
        catacion.catacion_update()

    def delete_catacion(self):
        catacion = sql_structures.Catacion(self.aroma_catacion.text(),
                                           self.finca_catacion.text(),
                                           self.region_catacion.currentText(),
                                           self.altura_catacion.text(),
                                           self.sabor_catacion.text(),
                                           self.color_catacion.text(),
                                           self.puntuacion_catacion.text())

        catacion.delete()

    # METODOS/FUNCIONES CLASE COFFEE
    def buy_coffee(self):
        try:
            coffee = sql_structures.Coffee(self.regionCombobx.currentText(),
                                           self.fincaText.text(),
                                           int(self.cantidadText.text()),
                                           self.estadoCombobx.currentText())

            coffee.management('buy_coffee')

            self.fincaText.clear()
            self.cantidadText.clear()

        except Exception as e:
            print(e)

    def nueva_venta(self):
        try:
            region = self.comboBox.currentText()
            finca = self.lineEdit_3.text()

            data = ['id', 'Estampa', 'Color', 'Tamaño']

            manager = sql_structures.Manager()

            if region == 'Huehuetenango':
                self.idEmpaque = manager.get_id('Empacado', data, 'Turquesa')
            elif region == 'San Marcos':
                self.idEmpaque = manager.get_id('Empacado', data, 'Rojo')
            elif region == 'Coban':
                self.idEmpaque = manager.get_id('Empacado', data, 'Verde')
            elif region == 'Acatenango':
                self.idEmpaque = manager.get_id('Empacado', data, 'Naranja')
            elif region == 'Antigua':
                self.idEmpaque = manager.get_id('Empacado', data, 'Amarillo')
            elif region == 'Nuevo Oriente':
                self.idEmpaque = manager.get_id('Empacado', data, 'Morado')
            elif region == 'Fraijanes':
                self.idEmpaque = manager.get_id('Empacado', data, 'Celeste')
            elif region == 'Atitlan':
                self.idEmpaque = manager.get_id('Empacado', data, 'Azul')

            columnsCafe = ['id', 'Region', 'Finca', 'Cantidad', 'Estado']
            self.idCafe = manager.get_id('Cafe', columnsCafe, finca)

            venta_d = sql_structures.Venta(self.regionCombobx.currentText(),
                                         self.fincaText.text(),
                                         int(self.cantidadText.text()),
                                         self.total, float(self.lineEdit_6.text()), self.idEmpaque, self.idCafe, '')

            venta_d.management('venta_cafe')

            self.fincaText.clear()
            self.cantidadText.clear()

        except Exception as e:
            print(e)

    def update_coffee(self):
        try:
            coffee = sql_structures.Coffee(self.regionAcCombobx.currentText(),
                                           self.fincaAcText.text(),
                                           int(self.cantidadAcText.text()),
                                           self.estadoAcText.currentText(),
                                           self.columnaAcText.currentText(),
                                           self.valorAcText.text())

            coffee.management('update_coffee')

            self.fincaText.clear()
            self.cantidadText.clear()
            self.valorAcText.clear()

        except Exception as e:
            print(e)

    def delete_coffee(self):
        try:
            coffee = sql_structures.Coffee(self.regionElimComboBx.currentText(),
                                           self.fincaElimText.text(),
                                           int(self.cantidadElimText.text()),
                                           self.estadoElimComboBx.currentText())

            coffee.management('delete_coffee')

            self.fincaText.clear()
            self.cantidadText.clear()

        except Exception as e:
            print(e)

    # METODOS/FUNCIONES CLASE PACKAGING
    def buy_packaging(self):
        try:
            coffee = sql_structures.Packaging(self.stickerText.text(),
                                              self.colorBolsaText.text(),
                                              self.tamanioText.text())

            coffee.management('buy_packaging')

            self.colorBolsaText.clear()
            self.stickerText.clear()
            self.tamanioText.clear()

        except Exception as e:
            print(e)

    def update_packaging(self):
        try:
            coffee = sql_structures.Packaging(
                self.stickerAcText.text(),
                self.colorAcText.text(),
                self.tamanioAcText.text(),
                self.columnaAcEmCombobx.currentText(),
                self.valorAcEmText.text())

            coffee.management('update_packaging')

            self.colorAcText.clear()
            self.stickerAcText.clear()
            self.tamanioAcText.clear()
            self.valorAcEmText.clear()

        except Exception as e:
            print(e)

    def delete_packaging(self):
        try:
            coffee = sql_structures.Packaging(self.stickerElimText.text(),
                                              self.colorElimText.text(),
                                              self.tamanioElimText.text())

            coffee.management('delete_packaging')

            self.stickerElimText.clear()
            self.colorElimText.clear()
            self.tamanioElimText.clear()

        except Exception as e:
            print(e)

    def carga_cafe_empacado(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('Cafe')
            dato2 = mana.print_table('Empacado')
            self.tableWidget.setRowCount(len(dato))

            for i in range(len(dato)):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(dato[i - 1][1])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(dato[i - 1][2])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(dato[i - 1][3])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(dato[i - 1][4])))
                self.tableWidget.setItem(i, 4, QTableWidgetItem('Hola'))
            self.tableWidget_2.setRowCount(len(dato2))
            for x in range(len(dato2)):
                self.tableWidget_2.setItem(x, 0, QTableWidgetItem(str(dato2[x - 1][1])))
                self.tableWidget_2.setItem(x, 1, QTableWidgetItem(str(dato2[x - 1][2])))
                self.tableWidget_2.setItem(x, 2, QTableWidgetItem(str(dato2[x - 1][3])))
        except Exception as e:
            print(e)

    def carga_catacion(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('Catacion')
            self.tableWidget_5.setRowCount(len(dato))

            for i in range(len(dato)):
                self.tableWidget_5.setItem(i, 0, QTableWidgetItem(str(dato[i - 1][1])))
                self.tableWidget_5.setItem(i, 1, QTableWidgetItem(str(dato[i - 1][2])))
                self.tableWidget_5.setItem(i, 2, QTableWidgetItem(str(dato[i - 1][3])))
                self.tableWidget_5.setItem(i, 3, QTableWidgetItem(str(dato[i - 1][4])))
                self.tableWidget_5.setItem(i, 4, QTableWidgetItem(str(dato[i - 1][5])))
                self.tableWidget_5.setItem(i, 5, QTableWidgetItem(str(dato[i - 1][6])))
                self.tableWidget_5.setItem(i, 6, QTableWidgetItem(str(dato[i - 1][7])))

        except Exception as e:
            print(e)

    def carga_usuario(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('usuarios')
            self.tableWidget_usuarios.setRowCount(len(dato))

            for i in range(len(dato)):
                self.tableWidget_usuarios.setItem(i, 0, QTableWidgetItem(str(dato[i - 1][1])))
                self.tableWidget_usuarios.setItem(i, 1, QTableWidgetItem(str(dato[i - 1][2])))
                self.tableWidget_usuarios.setItem(i, 2, QTableWidgetItem(str(dato[i - 1][3])))

        except Exception as e:
            print(e)

    def carga_mobiliario(self):
        try:
            mana = sql_structures.Manager()
            dato = mana.print_table('mobiliario')
            self.tableWidget_6.setRowCount(len(dato))

            for i in range(len(dato)):
                self.tableWidget_6.setItem(i, 0, QTableWidgetItem(str(dato[i - 1][1])))
                self.tableWidget_6.setItem(i, 1, QTableWidgetItem(str(dato[i - 1][2])))
                self.tableWidget_6.setItem(i, 2, QTableWidgetItem(str(dato[i - 1][3])))
                self.tableWidget_6.setItem(i, 3, QTableWidgetItem(str(dato[i - 1][4])))

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
                self.menu_show(t)
                self.btn_menu.show()
            elif rol == 2:
                self.menu_show(t)
                self.btn_inventario.hide()
                self.btn_mobiliario.hide()
                self.btn_catacion.hide()
                self.btn_usuario.hide()
            elif rol == 3:
                self.menu_show(t)
                self.btn_ventas.hide()
                self.btn_mobiliario.hide()
                self.btn_catacion.hide()
                self.btn_usuario.hide()
            elif rol == 4:
                self.menu_show(t)
                self.btn_inventario.hide()
                self.btn_mobiliario.hide()
                self.btn_ventas.hide()
                self.btn_usuario.hide()
            else:
                QMessageBox.about(self, 'Aviso', 'Usuario incorrecto!')
        else:
            QMessageBox.about(self, 'Aviso', 'Contraseña incorrecta!')

    def menu_show(self, t):
        self.btn_menu.hide()
        self.btn_menu_2.show()
        if t == True:
            self.frame_menu.show()
        else:
            pass
            # self.frame_menu.hide()

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
        # TODO
        # lIMPIAR TEXT

    def realizarCotizacion(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')

        # Crear un nuevo documento PDF
        pdf = canvas.Canvas("contizacion.pdf")
        # Configurar el estilo del texto
        pdf.setFont("Helvetica", 12)

        # Agregar los datos del cliente
        cliente_nombre = "Juan Perez"
        cliente_direccion = "Calle 123"
        pdf.drawString(100, 700, "Cliente: " + cliente_nombre)
        pdf.drawString(100, 680, "Dirección: " + cliente_direccion)
        # Agregar los datos de la factura
        pdf.drawString(400, 700, "Cotizacion #001")
        pdf.drawString(400, 680, f"Fecha: {formato}")
        # Agregar los productos a la factura
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

        # Calcular el total de la factura
        total = 0
        print(self.productos)
        for producto in self.productos:
            total = float(producto["precioUnidad"]) * int(producto["cantidadUnidad"])
            total = + total
        print(total)
        # Agregar el total a la factura
        pdf.drawString(400, y - 20, "Total: " + str(total))
        print("error")
        # Guardar el documento PDF
        pdf.save()
        webbrowser.open_new("contizacion.pdf")

        # FACTURA
        # METODO AGREGAR COTIZACION BOTON

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
        # TODO
        # lIMPIAR TEXT

    def realizarFactura(self):
        now = datetime.now()
        formato = now.strftime('%d - %m - %Y')

        # Crear un nuevo documento PDF
        pdf = canvas.Canvas("factura.pdf")
        # Configurar el estilo del texto
        pdf.setFont("Helvetica", 12)

        # Agregar los datos del cliente
        cliente_nombre = "Juan Perez"
        cliente_direccion = "Calle 123"
        pdf.drawString(100, 700, "Cliente: " + cliente_nombre)
        pdf.drawString(100, 680, "Dirección: " + cliente_direccion)
        # Agregar los datos de la factura
        pdf.drawString(400, 700, "Factura #001")
        pdf.drawString(400, 680, f"Fecha: {formato}")
        # Agregar los productos a la factura
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

        # Calcular el total de la factura
        self.total = 0
        print(self.productos)
        for producto in self.productos:
            self.total = float(producto["precioUnidad"]) * int(producto["cantidadUnidad"])
            self.total = + self.total
        # Agregar el total a la factura
        pdf.drawString(400, y - 20, "Total: " + str(self.total))
        print("error")
        # Guardar el documento PDF
        pdf.save()
        webbrowser.open_new("factura.pdf")
