def validar_entero(valor_str, campo):
    # Valida que un dato ingresado sea un número entero.
    try:
        return int(valor_str)
    except ValueError:
        print(f"Error: el campo '{campo}' debe ser un número entero.")
        return None

def validar_flotante(valor_str, campo):
    # Valida que un dato ingresado sea un número decimal/float.
    try:
        return float(valor_str)
    except ValueError:
        print(f"Error: el campo '{campo}' debe ser un número decimal.")
        return None

# VALIDACIONES DE STOCK
def validar_modelo(modelo: str) -> str:
    # Valida que el modelo no esté vacío y no contenga solo espacios. Limpia espacios extras y devuelve el modelo limpio.
    if not modelo or modelo.strip() == "":
        raise ValueError("El modelo no puede estar vacío.")
    
    # Normaliza
    modelo_limpio = " ".join(modelo.split()).title()
    return modelo_limpio


def validar_talle(talle: str) -> int:
    # Valida que el talle sea un número entero dentro de un rango razonable. Retorna el talle como entero.
    if not talle.isdigit():
        raise ValueError("El talle debe ser un número entero.")

    talle_int = int(talle)

    if talle_int < 35 or talle_int > 48:
        raise ValueError("El talle debe estar entre 35 y 48.")

    return talle_int


def validar_precio(precio: str) -> float:
    # Valida que el precio sea un número válido mayor a 0. Devuelve el precio como float.
    try:
        precio_float = float(precio)
    except:
        raise ValueError("El precio debe ser un número.")

    if precio_float <= 0:
        raise ValueError("El precio debe ser mayor a 0.")

    return precio_float


def validar_cantidad(cantidad: str) -> int:
    # Valida que la cantidad sea un número entero mayor o igual a 0.
    if not cantidad.isdigit():
        raise ValueError("La cantidad debe ser un número entero.")

    cantidad_int = int(cantidad)

    if cantidad_int < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    return cantidad_int


def validar_confirmacion(confirmacion: str) -> bool:
    # Valida respuestas. Devuelve True para confirmación positiva, False para negativa.
    if not confirmacion:
        raise ValueError("Debes ingresar una opción válida (s/n).")

    respuesta = confirmacion.strip().lower()

    if respuesta in ("s", "si"):
        return True
    elif respuesta in ("n", "no"):
        return False
    else:
        raise ValueError("Respuesta inválida. Solo se permite 's' o 'n'.")
    

def validar_modelo_unico(modelo, modelos_unicos):
    # Informa si el modelo ya existe o es nuevo. 
    if modelo in modelos_unicos:
        print("⚠ Este modelo ya existe en el stock.")
        return False
    else:
        print("Modelo nuevo agregado al listado de modelos únicos.")
        return True


def validar_talle_unico(talle, talles_disponibles):
    # Informa si el talle ya existe o es nuevo. 
    if talle in talles_disponibles:
        print("Este talle ya existía en el stock.")
        return False
    else:
        print("Nuevo talle incorporado al sistema.")
        return True


def validar_id_existente(id_buscar, stock):
    # Busca un ID en el stock y devuelve el producto si existe. 
    for producto in stock:
        if producto["id"] == id_buscar:
            return producto
    return None
