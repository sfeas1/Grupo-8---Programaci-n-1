from functions.funciones_productos import (
    agregar_producto, listar_productos, buscar_producto,
    eliminar_producto, contar_productos
)
from functions.funciones_archivos import cargar_datos, guardar_datos
from functions.funciones_validaciones import (
    validar_modelo, validar_talle,
    validar_precio, validar_cantidad
)
from utils.interfaz import mostrar_menu, pedir_opcion, mostrar_mensaje, pausar, pedir_input
import os


def main():
    # Crea carpeta de datos persistentes
    directorio_datos = "data"
    os.makedirs(directorio_datos, exist_ok=True)

    # Valores iniciales si no existe el archivo
    stock_predeterminado = [
        {"id": 1, "modelo": "Nike Air Max", "talle": 42, "cantidad": 5, "precio": 150000},
        {"id": 2, "modelo": "Adidas Superstar", "talle": 41, "cantidad": 8, "precio": 120000},
        {"id": 3, "modelo": "Puma RS-X", "talle": 43, "cantidad": 3, "precio": 135000},
        {"id": 4, "modelo": "Reebok Classic", "talle": 42, "cantidad": 6, "precio": 110000},
        {"id": 5, "modelo": "Converse All Star", "talle": 40, "cantidad": 7, "precio": 90000}
    ]

    # Carga el stock
    stock, ids_usados = cargar_datos(stock_predeterminado=stock_predeterminado)

    # Conjuntos
    modelos_unicos = {p["modelo"] for p in stock}
    talles_disponibles = {p["talle"] for p in stock}

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            print("\n--- Agregar producto ---")

            # Pide y valida el modelo
            while True:
                try:
                    modelo = validar_modelo(pedir_input("Modelo: "))
                    break
                except ValueError as e:
                    mostrar_mensaje(f"❌ {e}")

            # Pide y valida el talle
            while True:
                try:
                    talle = validar_talle(pedir_input("Talle: "))
                    break
                except ValueError as e:
                    mostrar_mensaje(f"❌ {e}")

            # Pide y valida el precio
            while True:
                try:
                    precio = validar_precio(pedir_input("Precio: "))
                    break
                except ValueError as e:
                    mostrar_mensaje(f"❌ {e}")

            # Pide y valida la cantidad
            while True:
                try:
                    cantidad = validar_cantidad(pedir_input("Cantidad: "))
                    break
                except ValueError as e:
                    mostrar_mensaje(f"❌ {e}")

            agregar_producto(stock, ids_usados, modelos_unicos, talles_disponibles, modelo, talle, precio, cantidad)

            mostrar_mensaje("✅ Producto agregado correctamente.")

        elif opcion == "2":
            listar_productos(stock)

        elif opcion == "3":
            buscar_producto(stock)

        elif opcion == "4":
            eliminar_producto(stock)

            # Actualiza conjuntos
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
            guardar_datos(stock)
            mostrar_mensaje("Datos guardados. ¡Hasta luego!")
            break

        else:
            mostrar_mensaje("Opción no válida, intenta de nuevo.")

        pausar()


if __name__ == "__main__":
    main()
