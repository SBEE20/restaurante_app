# Sistema de Gestión de Restaurante - POO en Python

**Estudiante:** Samuel Elias Erraez Erraez
**Asignatura:** Programación Orientada a Objetos
**Semana:** 4 - Organización Modular

---

## Descripción del Sistema
Este proyecto implementa una aplicación básica para la administración de un restaurante utilizando el paradigma de Programación Orientada a Objetos (POO) en Python. El sistema modela de forma independiente los productos ofrecidos, el registro de clientes y un servicio centralizado que gestiona las operaciones generales del establecimiento sin depender de interfaces complejas o menús interactivos infinitos, priorizando la arquitectura limpia.

---

## Estructura del Proyecto
El software sigue estrictamente una organización arquitectónica modular que separa las responsabilidades del sistema:

```text
restaurante_app/
├── modelos/
│   ├── producto.py       # Define la clase Producto (atributos y formato de texto)
│   └── cliente.py        # Define la clase Cliente (información del comensal)
├── servicios/
│   └── restaurante.py    # Clase controladora que gestiona menús y flujos de clientes
└── main.py               # Orquestador del programa y punto de arranque