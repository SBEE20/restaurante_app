class Cliente:
    """Clase que representa a un cliente en el restaurante."""

    def __init__(self, cedula: str, nombre: str, mesa_asignada: int):
        # Atributos esenciales para identificar al cliente y su ubicación
        self.cedula = cedula
        self.nombre = nombre
        self.mesa_asignada = mesa_asignada

    def __str__(self) -> str:
        # Representación en texto del objeto Cliente
        return f"Cliente: {self.nombre} (C.I: {self.cedula}) - Mesa: {self.mesa_asignada}"