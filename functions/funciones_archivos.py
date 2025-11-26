import json
import os

def cargar_datos(archivo="data/datos_stock.json", stock_predeterminado=None):
   # Carga el stock desde JSON. Si no existe, crea carpeta y archivo con stock predeterminado.
   # Devuelve stock y conjunto de IDs usados.
    carpeta = os.path.dirname(archivo)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            stock = json.load(f)
    else:
        stock = stock_predeterminado if stock_predeterminado else []
        with open(archivo, "w") as f:
            json.dump(stock, f, indent=4)

    # Conjunto de IDs usados
    ids_usados = {p["id"] for p in stock}
    return stock, ids_usados

def guardar_datos(stock, archivo="data/datos_stock.json"):
    # Guarda el stock en JSON dentro de la carpeta data
    with open(archivo, "w") as f:
        json.dump(stock, f, indent=4)
