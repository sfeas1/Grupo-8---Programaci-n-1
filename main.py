from funciones_productos import agregar_producto, listar_productos, buscar_producto, eliminar_producto
from funciones_archivos import cargar_datos, guardar_datos

def mostrar_menu():
    print("\n=== GESTOR DE STOCK - TIENDA DE ZAPATILLAS ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Guardar y salir")

def main():
    stock = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto(stock)
        elif opcion == "2":
            listar_productos(stock)
        elif opcion == "3":
            buscar_producto(stock)
        elif opcion == "4":
            eliminar_producto(stock)
        elif opcion == "5":
            guardar_datos(stock)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
