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
    nombre_archivo = "datos_stock.txt"
    
    # Carga stock desde el archivo si existe
    stock = cargar_datos(nombre_archivo)


    if not stock:  # Solo si el archivo está vacío
        stock = [
            {"modelo": "Nike Air Max", "talle": 42, "cantidad": 5, "precio": 150000},
            {"modelo": "Adidas Superstar", "talle": 41, "cantidad": 8, "precio": 120000},
            {"modelo": "Puma RS-X", "talle": 43, "cantidad": 3, "precio": 135000},
            {"modelo": "Reebok Classic", "talle": 42, "cantidad": 6, "precio": 110000},
            {"modelo": "Converse All Star", "talle": 40, "cantidad": 7, "precio": 90000},
            {"modelo": "Vans Old Skool", "talle": 41, "cantidad": 4, "precio": 95000},
            {"modelo": "New Balance 574", "talle": 43, "cantidad": 5, "precio": 130000},
            {"modelo": "Asics Gel-Lyte", "talle": 42, "cantidad": 2, "precio": 140000},
            {"modelo": "Fila Disruptor", "talle": 40, "cantidad": 3, "precio": 100000},
            {"modelo": "Under Armour HOVR", "talle": 41, "cantidad": 6, "precio": 125000},
        ]

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
            guardar_datos(nombre_archivo, stock)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
