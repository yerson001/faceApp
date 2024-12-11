import flet as ft


# Clase para manejar la pantalla de "Agregar Usuario"
class AddUserScreen:
    def __init__(self, page, main_app):
        self.page = page  # Guardamos la instancia de la página
        self.main_app = main_app  # Guardamos la instancia de MainApp para poder llamar a main_menu

    def show(self):
        self.page.controls.clear()
        self.page.add(ft.Text("Pantalla: Agregar Usuario"))
        # Agregar un botón para regresar al menú principal
        back_button = ft.ElevatedButton("Volver al Menú", on_click=self.back_to_menu)
        self.page.add(back_button)
        self.page.update()

    def back_to_menu(self, e):
        self.page.controls.clear()
        self.main_app.main_menu()  # Llamamos directamente al método main_menu
        self.page.update()


# Clase para manejar la pantalla de "Registrar"
class RegisterScreen:
    def __init__(self, page, main_app):
        self.page = page  # Guardamos la instancia de la página
        self.main_app = main_app  # Guardamos la instancia de MainApp para poder llamar a main_menu

    def show(self):
        self.page.controls.clear()
        self.page.add(ft.Text("Pantalla: Registrar"))
        # Agregar un botón para regresar al menú principal
        back_button = ft.ElevatedButton("Volver al Menú", on_click=self.back_to_menu)
        self.page.add(back_button)
        self.page.update()

    def back_to_menu(self, e):
        self.page.controls.clear()
        self.main_app.main_menu()  # Llamamos directamente al método main_menu
        self.page.update()


# Clase para manejar la pantalla de "Listar Usuarios"
class ListUsersScreen:
    def __init__(self, page, main_app):
        self.page = page  # Guardamos la instancia de la página
        self.main_app = main_app  # Guardamos la instancia de MainApp para poder llamar a main_menu

    def show(self):
        self.page.controls.clear()
        self.page.add(ft.Text("Pantalla: Listar Usuarios"))
        # Agregar un botón para regresar al menú principal
        back_button = ft.ElevatedButton("Volver al Menú", on_click=self.back_to_menu)
        self.page.add(back_button)
        self.page.update()

    def back_to_menu(self, e):
        self.page.controls.clear()
        self.main_app.main_menu()  # Llamamos directamente al método main_menu
        self.page.update()


# Clase para manejar la pantalla de "Configuraciones"
class SettingsScreen:
    def __init__(self, page, main_app):
        self.page = page  # Guardamos la instancia de la página
        self.main_app = main_app  # Guardamos la instancia de MainApp para poder llamar a main_menu

    def show(self):
        self.page.controls.clear()
        self.page.add(ft.Text("Pantalla: Configuraciones"))
        # Agregar un botón para regresar al menú principal
        back_button = ft.ElevatedButton("Volver al Menú", on_click=self.back_to_menu)
        self.page.add(back_button)
        self.page.update()

    def back_to_menu(self, e):
        self.page.controls.clear()
        self.main_app.main_menu()  # Llamamos directamente al método main_menu
        self.page.update()


# Clase principal de la aplicación
class MainApp:
    def __init__(self):
        self.page = None
        # Instanciamos las pantallas y les pasamos la página y la referencia a MainApp
        self.add_user_screen = AddUserScreen(self.page, self)
        self.register_screen = RegisterScreen(self.page, self)
        self.list_users_screen = ListUsersScreen(self.page, self)
        self.settings_screen = SettingsScreen(self.page, self)

    def navigate_to(self, route):
        if route == "add_user":
            self.add_user_screen.show()
        elif route == "register":
            self.register_screen.show()
        elif route == "list_users":
            self.list_users_screen.show()
        elif route == "settings":
            self.settings_screen.show()

    def main_menu(self):
        def create_card(title, color, icon, route):
            return ft.GestureDetector(
                on_tap=lambda e: self.navigate_to(route),
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(icon, size=30, color=ft.Colors.WHITE),  # Icono más pequeño
                                ft.Text(title, color=ft.Colors.WHITE, weight="bold"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        alignment=ft.alignment.center,
                        bgcolor=color,
                        border_radius=10,
                        padding=10,  # Menos padding para que las tarjetas sean más pequeñas
                        width=150,  # Establece un ancho fijo para las tarjetas
                        height=150,  # Establece una altura fija para las tarjetas
                    ),
                    expand=False,  # No expandir las tarjetas a todo el espacio disponible
                ),
            )

        # Crear las tarjetas
        cards = [
            create_card("Agregar Usuario", ft.Colors.GREEN, ft.Icons.PERSON_ADD, "add_user"),
            create_card("Registrar", ft.Colors.BLUE, ft.Icons.LOCK_OPEN, "register"),
            create_card("Listar Usuarios", ft.Colors.AMBER, ft.Icons.LIST, "list_users"),
            create_card("Configuraciones", ft.Colors.PURPLE, ft.Icons.SETTINGS, "settings"),
            create_card("Salir", ft.Colors.RED, ft.Icons.EXIT_TO_APP, "exit"),
        ]

        # Usar GridView para organizar las tarjetas
        grid = ft.GridView(
            controls=cards,
            runs_count=4,  # Número de columnas en el grid (5 columnas por fila)
            spacing=10,  # Espacio entre las tarjetas
            run_spacing=10,  # Espacio entre filas
        )

        # Añadir el GridView a la página
        self.page.controls.clear()
        self.page.add(grid)
        self.page.update()

        self.page.controls.clear()
        self.page.add(grid)
        self.page.update()

    def run(self, page: ft.Page):
        self.page = page
        # Ahora que la página está disponible, podemos crear las pantallas correctamente
        self.add_user_screen = AddUserScreen(self.page, self)
        self.register_screen = RegisterScreen(self.page, self)
        self.list_users_screen = ListUsersScreen(self.page, self)
        self.settings_screen = SettingsScreen(self.page, self)

        page.title = "Menú Principal"
        self.main_menu()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = MainApp()
    ft.app(target=app.run)
