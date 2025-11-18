def generar_id(ids_usados):
    # Genera el siguiente ID entero disponible.
    if not ids_usados:
        return 1
    else:
        return max(ids_usados) + 1


def agregar_producto(stock, ids_usados, modelos_unicos, talles_disponibles,
                    modelo, talle, precio, cantidad):
    # Generar un ID único
    nuevo_id = 1
    while nuevo_id in ids_usados:
        nuevo_id += 1

    producto = {
        "id": nuevo_id,
        "modelo": modelo,
        "talle": talle,
        "precio": precio,
        "cantidad": cantidad
    }

    stock.append(producto)
    ids_usados.add(nuevo_id)
    modelos_unicos.add(modelo)
    talles_disponibles.add(talle)

    print(f"Producto agregado con ID {nuevo_id}.")

def mostrar_mensaje(mensaje):
    print(mensaje)


def listar_productos(stock):
    print("\n--- Lista de productos ---")
    if not stock:
        print("No hay productos cargados.")
        return

    for producto in stock:
        print(f"ID: {producto['id']} | Modelo: {producto['modelo']} | "
              f"Talle: {producto['talle']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")


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


# Función recursiva
def contar_productos(stock, indice=0):
    if indice == len(stock):
        return 0
    else:
        return 1 + contar_productos(stock, indice + 1)
