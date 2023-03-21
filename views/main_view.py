from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
import sql_structures
import pandas as pdf
import webbrowser
import pdfrw
from datetime import date

# usuarios = sql_structures.SqlDataBase_usuarios()

# TODO
# - Agregar mensajes de confirmacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('views/designs/DB1.ui', self)

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
        # self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

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
        self.btn_agregar_usuarios.clicked.connect(self.new_user)
        self.btn_eliminar_usuarios.clicked.connect(self.delete_user)
        self.btn_actualizar_usuarios.clicked.connect(self.update_user)
        # Inicio sesion
        #self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

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

        self.info_usuario_e.clear()

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
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(dato[i-1][1])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(dato[i-1][2])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(dato[i-1][3])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(dato[i-1][4])))
                self.tableWidget.setItem(i, 4, QTableWidgetItem('Hola'))
            self.tableWidget_2.setRowCount(len(dato2))
            for x in range(len(dato2)):
                self.tableWidget_2.setItem(x, 0, QTableWidgetItem(str(dato2[x-1][1])))
                self.tableWidget_2.setItem(x, 1, QTableWidgetItem(str(dato2[x-1][2])))
                self.tableWidget_2.setItem(x, 2, QTableWidgetItem(str(dato2[x-1][3])))
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
            dato = mana.print_table('Usuarios')
            self.tableWidget_usuarios.setRowCount(len(dato))

            for i in range(len(dato)):
                self.tableWidget_usuarios.setItem(i, 0, QTableWidgetItem(str(dato[i - 1][1])))
                self.tableWidget_usuarios.setItem(i, 1, QTableWidgetItem(str(dato[i - 1][2])))
                self.tableWidget_usuarios.setItem(i, 2, QTableWidgetItem(str(dato[i - 1][3])))

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

    # def iniciar_sesion(self):
    #    usuario_comprobacion = str(self.lineEdit_usuarios.text())
    #       SELECT * FROM users WHERE name = 'texto' -> consulta que nos devuelve un usuario
    #       tambien hacer una consulta a la tabla rol
    #    rol = str(usuarios.get_rol(usuario_comprobacion))
    #    if rol == 'Administrador':
    #        self.btn_menu.show()

    #    elif rol == 'Vendedor':
    #        self.btn_menu.show()
    #        self.btn_inventario.hide()
    #        self.btn_mobiliario.hide()
    #        self.btn_catacion.hide()
    #        self.btn_usuario.hide()

    #    elif rol == 'Bodegero':
    #        self.btn_menu.show()

    #    elif rol == 'Catador':
    #        self.btn_menu.show()

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

    def write_pdf(self, template, output, data_dict):
        ANNOT_KEY = '/Annots'
        ANNOT_FIELD_KEY = '/T'
        ANNOT_VAL_KEY = '/V'
        ANNOT_RECT_KEY = '/Rect'
        SUBTYPE_KEY = '/Subtype'
        WIDGET_SUBTYPE_KEY = '/Widget'

        def fill_pdf(input_pdf_path, output_pdf_path, data):
            template_pdf = pdfrw.PdfReader(input_pdf_path)

            print(data)

            for page in template_pdf.pages:
                annotations = page[ANNOT_KEY]
                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]
                            if key in data.keys():
                                if type(data[key]) == bool:
                                    if data[key] == True:
                                        annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('Yes')))
                                else:
                                    annotation.update(pdfrw.PdfDict(V='{}'.format(data[key])))
                                    annotation.update(pdfrw.PdfDict(AP=''))
            template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
        fill_pdf(template, output, data_dict)
        webbrowser.open_new(output)

    def realizarCotizacion(self):
        try:
            region = self.regionAcCombobx_3.currentText()
            finca = self.fincaAcText_3.text()
            estado = self.estadoAcText_3.currentText()
            tipo = 'oro'
            precio = self.lineEdit_5.text()
            print("Hola")
            print(region)
            if region != '--Seleccionar--' and finca != '' and estado != '--Seleccionar--':
                print("Hola")
                cantidad = int(self.cantidadAcText_3.text())
                if cantidad > 0:
                    print("Hola")
                    QMessageBox.about(self, 'Aviso', 'Se ha generado la cotización!')
                    data_dict = {
                        'Fecha': date.today(),
                        'Numero': '0',
                        'Cliente': '',
                        'Nit': 'C/F',
                        'Direccion': 'Ciudad',
                        'Telefono': '',
                        'Correo': '',
                        'Producto': f"Café de {self.regionAcCombobx_3.currentText()}, finca {finca}, {estado}, {tipo}",
                        'Producto1': '',
                        'Producto3': '',
                        'Producto4': '',
                        'Producto5': '',
                        'Producto2': '',
                        'Precio1': precio,
                        'Precio2': '',
                        'Precio3': '',
                        'Precio4': '',
                        'Precio5': '',
                        'Unidades': cantidad,
                        'Unidades1': '',
                        'Unidades2': '',
                        'Unidades3': '',
                        'Unidades4': '',
                        'Unidades5': '',
                        'Precio': '',
                        'Preciot': '',
                        'Preciot1': '',
                        'Preciot2': '',
                        'Preciot3': '',
                        'Preciot4': '',
                        'Totalp': '',
                        'Descuento': '',
                        'Total': ''
                    }
                    self.write_pdf('cotizacion.pdf', 'cotizacion_final.pdf', data_dict)
                    self.cantidad_line.clear()
                    #self.
                else:
                    raise Exception('Debe ser un valor mayor a 0')
            else:
                raise Exception('No se ha seleccionado uno de los parametros para la cotización.')
        except Exception as e:
            'Error'
