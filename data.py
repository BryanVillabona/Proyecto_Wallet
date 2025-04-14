import json

registros = {}
cuentas = {}
cuentas_registradas = {}
bolsillos = {}
movimientos = {}

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print("No se encontró el archivo, iniciando con una base de datos vacía.")
        return {}
    except json.JSONDecodeError:
        print("Error al leer los datos, el archivo puede estar corrupto.")
        return {}


def guardar_datos(datos, archivo):
    try:
        if datos:
            with open(archivo, "w") as file:
                json.dump(datos, file, indent=4)
        else:
            print("Advertencia: No hay datos para guardar.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")