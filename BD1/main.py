import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from usuarios import SqlDataBase_usuarios

usuarios = SqlDataBase_usuarios()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('DB1.ui', self)

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

        # Usuarios
        self.cargar_usuarios.clicked.connect(self.loaddata)
        self.btn_administrar.clicked.connect(self.show_page_usuarios_admin)
        self.btn_agregar_usuarios.clicked.connect(self.registar_usuarios)
        self.btn_eliminar_usuarios.clicked.connect(self.eliminar_usuarios)
        self.btn_actualizar_usuarios.clicked.connect(self.actualizar_usuarios)

        # Inicio sesion
        self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

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
            self.self.btn_menu.show()
        elif rol == 'Vendedor':
            self.self.btn_menu.show()
            self.btn_inventario.hide()
            self.btn_mobiliario.hide()
            self.btn_catacion.hide()
            self.btn_usuario.hide()
        elif rol == 'Bodegero':
            self.self.btn_menu.show()
        elif rol == 'Catador':
            self.self.btn_menu.show()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec())
