def mostrar_menu():
    print("\n=== GESTOR DE STOCK - TIENDA DE ZAPATILLAS ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Contar productos")
    print("6. Mostrar modelos únicos")
    print("7. Mostrar talles disponibles")
    print("8. Guardar y salir")

def pedir_opcion():
    opcion = input("Selecciona una opción: ")
    return opcion

def pedir_input(texto):
    return input(texto)

def mostrar_mensaje(mensaje):
    print(mensaje)

def pausar():
    input("\nPresiona ENTER para continuar...")
