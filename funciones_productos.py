def buscar_producto(stock):
    print("\n--- Buscar producto ---")
    print("1. Buscar por modelo")
    print("2. Buscar por ID")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        termino = input("Ingrese el modelo a buscar: ").lower()
        encontrados = [p for p in stock if termino in p['modelo'].lower()]

        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} resultado(s):")
            for producto in encontrados:
                print(f"ID: {producto['id']} | Modelo: {producto['modelo']} | "
                      f"Talle: {producto['talle']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")
        else:
            print("No se encontró ningún producto con ese modelo.")

    elif opcion == "2":
        try:
            id_buscar = int(input("Ingrese el ID del producto: "))
        except ValueError:
            print("Error: el ID debe ser un número.")
            return

        for producto in stock:
            if producto["id"] == id_buscar:
                print(f"\nProducto encontrado:")
                print(f"ID: {producto['id']} | Modelo: {producto['modelo']} | "
                      f"Talle: {producto['talle']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")
                return
        print("No se encontró ningún producto con ese ID.")

    else:
        print("Opción inválida.")


def eliminar_producto(stock):
    print("\n--- Eliminar producto ---")
    try:
        id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("Error: el ID debe ser un número.")
        return

    for producto in stock:
        if producto["id"] == id_eliminar:
            stock.remove(producto)
            print(f"Producto con ID {id_eliminar} eliminado correctamente.")
            return

    print("No se encontró ningún producto con ese ID.")


# Función recursiva para contar productos
def contar_productos(stock, indice=0):
    """Cuenta recursivamente cuántos productos hay en el stock."""
    if indice == len(stock):  # Caso base: cuando llegamos al final de la lista
        return 0
    else:  # Caso recursivo: contamos 1 y seguimos con el siguiente elemento
        return 1 + contar_productos(stock, indice + 1)
