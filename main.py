from funciones_productos import agregar_producto, listar_productos, buscar_producto, eliminar_producto, contar_productos
from funciones_archivos import cargar_datos, guardar_datos
from interfaz import mostrar_menu, pedir_opcion, mostrar_mensaje, pausar

def main():
    nombre_archivo = "datos_stock.txt"
    stock = cargar_datos(nombre_archivo)

    if not stock:
        stock = [
            {"id": 1, "modelo": "Nike Air Max", "talle": 42, "cantidad": 5, "precio": 150000},
            {"id": 2, "modelo": "Adidas Superstar", "talle": 41, "cantidad": 8, "precio": 120000},
            {"id": 3, "modelo": "Puma RS-X", "talle": 43, "cantidad": 3, "precio": 135000},
            {"id": 4, "modelo": "Reebok Classic", "talle": 42, "cantidad": 6, "precio": 110000},
            {"id": 5, "modelo": "Converse All Star", "talle": 40, "cantidad": 7, "precio": 90000},
        ]

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            agregar_producto(stock)
        elif opcion == "2":
            listar_productos(stock)
        elif opcion == "3":
            buscar_producto(stock)
        elif opcion == "4":
            eliminar_producto(stock)
        elif opcion == "5":
            total = contar_productos(stock)
            mostrar_mensaje(f"Hay {total} producto(s) en el stock.")
        elif opcion == "6":
            guardar_datos(nombre_archivo, stock)
            mostrar_mensaje("Datos guardados. ¡Hasta luego!")
            break
        else:
            mostrar_mensaje("Opción no válida, intenta de nuevo.")
        
        pausar()




if __name__ == "__main__":
    main()
