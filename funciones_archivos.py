def cargar_datos(nombre_archivo):
    lista_productos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) == 5:
                    producto = {
                        "id": int(datos[0]),
                        "modelo": datos[1],
                        "talle": int(datos[2]),
                        "cantidad": int(datos[3]),
                        "precio": float(datos[4])
                    }
                    lista_productos.append(producto)
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}. Se creará uno nuevo al guardar los datos.")
    return lista_productos


def guardar_datos(nombre_archivo, lista_productos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for producto in lista_productos:
            linea = f"{producto['id']},{producto['modelo']},{producto['talle']},{producto['cantidad']},{producto['precio']}\n"
            archivo.write(linea)
