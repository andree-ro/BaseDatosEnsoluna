from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
import sql_structures

usuarios = sql_structures.SqlDataBase_usuarios()


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
        self.cargar_usuarios.clicked.connect(self.loaddata)
        self.btn_administrar.clicked.connect(self.show_page_usuarios_admin)
        self.btn_agregar_usuarios.clicked.connect(self.registar_usuarios)
        self.btn_eliminar_usuarios.clicked.connect(self.eliminar_usuarios)
        self.btn_actualizar_usuarios.clicked.connect(self.actualizar_usuarios)

        # Inicio sesion
        self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        # COPMRAS CAFE
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
        usuario_comprobacion = str(self.lineEdit_usuarios.text())
        rol = str(usuarios.get_rol(usuario_comprobacion))
        if rol == 'Administrador':
            self.btn_menu.show()

        elif rol == 'Vendedor':
            self.btn_menu.show()
            self.btn_inventario.hide()
            self.btn_mobiliario.hide()
            self.btn_catacion.hide()
            self.btn_usuario.hide()

        elif rol == 'Bodegero':
            self.btn_menu.show()

        elif rol == 'Catador':
            self.btn_menu.show()

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

    def registar_usuarios(self):
        usuario = str(self.info_usuario.text())
        contrasena = str(self.info_contrasena.text())
        rol = str(self.info_rol.currentText())
        usuarios.insertRow(usuario, contrasena, rol)
        self.info_usuario.setText(" ")
        self.info_contrasena.setText(" ")

    def actualizar_usuarios(self):
        usuario = str(self.info_usuario_a.text())
        contrasena = str(self.info_contrasena_a.text())
        rol = str(self.info_rol_a.currentText())
        usuarios.updateFields(usuario, contrasena, rol)
        self.info_usuario_a.setText(" ")
        self.info_contrasena_a.setText(" ")

    def eliminar_usuarios(self):
        usuario = str(self.info_usuario_e.text())
        usuarios.deleteRow(usuario)
        self.info_usuario_e.setText(" ")

    def loaddata(self):
        tableWidget_usuarios = self.tableWidget_usuarios
        usuarios.usuarios(tableWidget_usuarios)
