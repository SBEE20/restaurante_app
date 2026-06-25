from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def ejecutar_sistema():
    print("=== INICIALIZANDO SISTEMA DE GESTIÓN DE RESTAURANTE ===\n")

    # 1. Instanciar el servicio principal del restaurante
    mi_restaurante = Restaurante("La Sazón Amazónica")

    print("\n--- Creando e Insertando Productos ---")
    # 2. Instanciar objetos de la clase Producto
    plato1 = Producto("Maito de Pescado", 8.50, "Plato Fuerte")
    plato2 = Producto("Chontacuro Asado", 4.00, "Entrada")
    bebida1 = Producto("Guayusa Helada", 1.50, "Bebida")

    # 3. Registrar los productos en el restaurante
    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(bebida1)

    print("\n--- Registrando Clientes ---")
    # 4. Instanciar objetos de la clase Cliente
    cliente1 = Cliente("1600123456", "Carlos Mendoza", 4)
    cliente2 = Cliente("1700987654", "Ana María López", 2)

    # 5. Registrar los clientes en el restaurante
    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)

    # 6. Mostrar reportes por consola utilizando los métodos del servicio
    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()

    print("\n=== EJECUCIÓN FINALIZADA CON ÉXITO ===")


if __name__ == "__main__":
    # Asegura que el archivo se ejecute solo si es llamado directamente
    ejecutar_sistema()