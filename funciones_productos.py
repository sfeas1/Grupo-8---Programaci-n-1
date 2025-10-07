def agregar_producto(stock):
    print("\n--- Agregar producto ---")
    modelo = input("Modelo: ")
    talle = int(input("Talle: "))
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))


    nuevo = {
        "modelo": modelo,
        "talle": talle,
        "cantidad": cantidad,
        "precio": precio
    }

    stock.append(nuevo)
    print(f" Producto '{modelo}' agregado correctamente.")


def listar_productos(stock):
    print("\n--- Lista de productos ---")
    if not stock:
        print("No hay productos cargados.")
        return

    for i, producto in enumerate(stock, start=1):
        print(f"{i}. {producto['modelo']} - Talle {producto['talle']} - Cantidad: {producto['cantidad']} - Precio: ${producto['precio']}")


def buscar_producto(stock):
    print("\n--- Buscar producto ---")
    termino = input("Ingrese el modelo a buscar: ").lower()
    encontrados = [p for p in stock if termino in p['modelo'].lower()]

    if encontrados:
        print(f"Se encontraron {len(encontrados)} resultado(s):")
        for producto in encontrados:
            print(f"- {producto['modelo']} (Talle {producto['talle']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']})")
    else:
        print(" No se encontró ningún producto con ese nombre.")


def eliminar_producto(stock):
    print("\n--- Eliminar producto ---")
    modelo = input("Ingrese el modelo a eliminar: ").lower()

    for producto in stock:
        if producto['modelo'].lower() == modelo:
            stock.remove(producto)
            print(f" Producto '{modelo}' eliminado correctamente.")
            return

    print(" No se encontró el producto en el stock.")
