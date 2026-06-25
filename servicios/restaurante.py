from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que administra la gestión global del restaurante."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.menu_productos = []  # Lista para almacenar los objetos de tipo Producto
        self.clientes_actuales = []  # Lista para almacenar los objetos de tipo Cliente

    def agregar_producto(self, producto: Producto):
        """Agrega un nuevo producto al menú del restaurante."""
        self.menu_productos.append(producto)
        print(f"✔ Producto '{producto.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente: Cliente):
        """Registra la llegada de un cliente al restaurante."""
        self.clientes_actuales.append(cliente)
        print(f"✔ Cliente '{cliente.nombre}' registrado en la mesa {cliente.mesa_asignada}.")

    def mostrar_menu(self):
        """Muestra de forma organizada todos los productos del menú."""
        print(f"\n--- MENÚ DE {self.nombre.upper()} ---")
        if not self.menu_productos:
            print("El menú está vacío.")
        for prod in self.menu_productos:
            print(prod)  # Llama implícitamente al método __str__() de Producto

    def mostrar_clientes(self):
        """Muestra de forma organizada los clientes atendidos actualmente."""
        print(f"\n--- CLIENTES EN {self.nombre.upper()} ---")
        if not self.clientes_actuales:
            print("No hay clientes registrados en este momento.")
        for cli in self.clientes_actuales:
            print(cli)  # Llama implícitamente al método __str__() de Cliente