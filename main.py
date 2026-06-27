# Sistema básico de inventario en Python
# Proyecto integrador - Lógica de Programación
# Autor: Erick Rodríguez

# El inventario se manejará mediante una lista de diccionarios.
# Cada producto tendrá nombre, cantidad y precio.
inventario = []


def mostrar_menu():
    """Muestra las opciones principales del sistema."""
    print("\n===== SISTEMA BÁSICO DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. Registrar venta o salida")
    print("6. Mostrar productos con bajo stock")
    print("7. Salir")


def agregar_producto():
    """Permite registrar un nuevo producto en el inventario."""
    print("\n--- Agregar producto ---")

    nombre = input("Ingrese el nombre del producto: ").strip().lower()

    # Verificar si el producto ya existe
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("El producto ya existe en el inventario.")
            return

    try:
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio unitario: "))

        if cantidad < 0 or precio < 0:
            print("La cantidad y el precio no pueden ser negativos.")
            return

        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

        inventario.append(producto)
        print("Producto agregado correctamente.")

    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")


def mostrar_inventario():
    """Muestra todos los productos registrados en el inventario."""
    print("\n--- Inventario actual ---")

    if len(inventario) == 0:
        print("No existen productos registrados.")
        return

    for indice, producto in enumerate(inventario, start=1):
        print(f"{indice}. Producto: {producto['nombre'].title()}")
        print(f"   Cantidad: {producto['cantidad']}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Valor total: ${producto['cantidad'] * producto['precio']:.2f}")


def buscar_producto():
    """Busca un producto por su nombre."""
    print("\n--- Buscar producto ---")

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            print("Producto encontrado:")
            print(f"Nombre: {producto['nombre'].title()}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']:.2f}")
            return

    print("Producto no encontrado.")


def actualizar_cantidad():
    """Actualiza la cantidad disponible de un producto."""
    print("\n--- Actualizar cantidad ---")

    nombre_buscar = input("Ingrese el nombre del producto: ").strip().lower()

    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                producto["cantidad"] = nueva_cantidad
                print("Cantidad actualizada correctamente.")
                return

            except ValueError:
                print("Error: debe ingresar un número entero.")
                return

    print("Producto no encontrado.")


def registrar_venta():
    """Registra la salida o venta de un producto."""
    print("\n--- Registrar venta o salida ---")

    nombre_buscar = input("Ingrese el nombre del producto vendido: ").strip().lower()

    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            try:
                cantidad_vendida = int(input("Ingrese la cantidad vendida o retirada: "))

                if cantidad_vendida <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    return

                if cantidad_vendida > producto["cantidad"]:
                    print("No existe stock suficiente para realizar la venta.")
                    return

                producto["cantidad"] -= cantidad_vendida
                total = cantidad_vendida * producto["precio"]

                print("Venta registrada correctamente.")
                print(f"Total de la venta: ${total:.2f}")
                print(f"Stock restante: {producto['cantidad']}")
                return

            except ValueError:
                print("Error: debe ingresar un número entero.")
                return

    print("Producto no encontrado.")


def mostrar_bajo_stock():
    """Muestra productos con cantidad baja en inventario."""
    print("\n--- Productos con bajo stock ---")

    limite = 5
    encontrados = False

    for producto in inventario:
        if producto["cantidad"] <= limite:
            print(f"Producto: {producto['nombre'].title()} - Cantidad: {producto['cantidad']}")
            encontrados = True

    if not encontrados:
        print("No existen productos con bajo stock.")


def ejecutar_sistema():
    """Controla la ejecución principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_cantidad()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            mostrar_bajo_stock()
        elif opcion == "7":
            print("Gracias por utilizar el sistema de inventario.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Punto de inicio del programa
ejecutar_sistema()