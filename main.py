from funciones_productos import agregar_producto, listar_productos, buscar_producto, eliminar_producto, contar_productos
from funciones_archivos import cargar_datos, guardar_datos
from interfaz import mostrar_menu, pedir_opcion, mostrar_mensaje, pausar
import os

def main():
    # Crea carpeta de datos persistentes
    directorio_datos = "data"
    os.makedirs(directorio_datos, exist_ok=True)

    # Ruta al archivo
    nombre_archivo = os.path.join(directorio_datos, "datos_stock.txt")

    # Carga el stock
    stock = cargar_datos(nombre_archivo)

    # Si está vacío, se cargan valores iniciales predeterminados
    if not stock:
        stock = [
            {"id": 1, "modelo": "Nike Air Max", "talle": 42, "cantidad": 5, "precio": 150000},
            {"id": 2, "modelo": "Adidas Superstar", "talle": 41, "cantidad": 8, "precio": 120000},
            {"id": 3, "modelo": "Puma RS-X", "talle": 43, "cantidad": 3, "precio": 135000},
            {"id": 4, "modelo": "Reebok Classic", "talle": 42, "cantidad": 6, "precio": 110000},
            {"id": 5, "modelo": "Converse All Star", "talle": 40, "cantidad": 7, "precio": 90000}
        ]

    # Conjuntos
    modelos_unicos = {p["modelo"] for p in stock}
    talles_disponibles = {p["talle"] for p in stock}
    ids_usados = {p["id"] for p in stock}

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            # Agregar producto
            # Validación con conjuntos
            print("\n--- Agregar producto ---")
            modelo = input("Modelo: ")
            talle = int(input("Talle: "))

            if modelo in modelos_unicos:
                mostrar_mensaje("⚠ Este modelo ya existe en el stock.")
            else:
                mostrar_mensaje("Modelo nuevo agregado al listado de modelos únicos.")

            if talle in talles_disponibles:
                mostrar_mensaje("Este talle ya existía en el stock.")
            else:
                mostrar_mensaje("Nuevo talle incorporado al sistema.")

            agregar_producto(stock, ids_usados)

            # Actualiza los conjuntos
            modelos_unicos = {p["modelo"] for p in stock}
            talles_disponibles = {p["talle"] for p in stock}
            ids_usados = {p["id"] for p in stock}

        elif opcion == "2":
            listar_productos(stock)

        elif opcion == "3":
            buscar_producto(stock)

        elif opcion == "4":
            eliminar_producto(stock)

            modelos_unicos = {p["modelo"] for p in stock}
            talles_disponibles = {p["talle"] for p in stock}
            ids_usados = {p["id"] for p in stock}

        elif opcion == "5":
            total = contar_productos(stock)
            mostrar_mensaje(f"Hay {total} producto(s) en el stock.")

        elif opcion == "6":
            mostrar_mensaje(f"Modelos únicos: {modelos_unicos}")

        elif opcion == "7":
            mostrar_mensaje(f"Talles disponibles: {talles_disponibles}")

        elif opcion == "8":
            guardar_datos(nombre_archivo, stock)
            mostrar_mensaje("Datos guardados. ¡Hasta luego!")
            break

        else:
            mostrar_mensaje("Opción no válida, intenta de nuevo.")
        
        pausar()

if __name__ == "__main__":
    main()
