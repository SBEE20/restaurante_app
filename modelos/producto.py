class Producto:
    """Clase que representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, precio: float, categoria: str):
        # Inicialización de los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ejemplo: 'Entrada', 'Plato Fuerte', 'Bebida'

    def __str__(self) -> str:
        # Representación en texto del objeto Producto
        return f"[{self.categoria}] {self.nombre} - ${self.precio:.2f}"