from registro import *
from inicio_sesion import inicio_sesion
from gestion_cuentas.registro_cuentas import *
from transacciones.transacciones import *
from bolsillos.bolsillos import *
from divisas.divisas import *

menu_principal = """
***** Bienvenido a Campers Wallet *****
1. Iniciar Sesión
2. Registrarse
3 Salir
***************************************
"""

menu_inicio = """
***************************************
1. Gestión de Cuentas
2. Transacciones
3. Bolsillos
4. Conversión de Divisas
5. Cerrar Sesión
***************************************
"""

menu_gestion_cuentas = """
***************************************
1. Registrar Cuenta
2. Modificar Cuenta
3. Eliminar Cuenta
4. Ver Cuentas Registradas
5. Ver Gastos/Ingresos
6. Saldo Total
7. Regresar al menú principal
***************************************
"""

menu_transacciones = """
***************************************
1. Realizar pagos
2. Retirar dinero
3. Depositar dinero
4. Movimientos
5. Regresar menu principal
***************************************
"""

menu_bolsillos = """
***************************************
1. Crear bolsillo
2. Agregar dinero a bolsillo
3. Retirar dinero de bolsillo
4. Eliminar bolsillo
5. Ver bolsillos
6. Regresar menu principal
***************************************
"""

menu_conversion_divisas = """
***************************************
1. Convertir de COP a USD (Dolar)
2. Convertir de COP a EUR (Euros)
3. Convertir de COP a GBP (Libras Esterlinas)
4. Convertir de COP a JPY (Yenes Japoneses)
5. Convertir de COP a CAD (Dolares Canadienses)
6. Regresar menu principal
***************************************
"""

def mostrar_menu():
    return print(menu_principal)

def mostrar_menu_inicio():
    return print(menu_inicio)

def mostrar_menu_gestion_cuentas():
    return print(menu_gestion_cuentas)

def mostrar_menu_transacciones():
    return print(menu_transacciones)

def mostrar_menu_bolsillos():
    return print(menu_bolsillos)

def mostrar_menu_conversion_divisas():
    return print(menu_conversion_divisas)

def pedir_opcion():
    return int(input("Bienvenido. Elija una opción: "))

def ejecucion_menu_principal():
    while True:
        mostrar_menu()
        try:
            opc = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc:
            case 1:
                inicio_sesion()
            case 2:
                registro()
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Error. Elija una opcion válida")

def ejecucion_menu_inicio(usuario_actual):
    while True:
        mostrar_menu_inicio()
        try:
            opc_inicio = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc_inicio:
            case 1:
                ejecucion_menu_gestion_cuentas(usuario_actual)
            case 2:
                ejecucion_menu_transacciones(usuario_actual)
            case 3:
                ejecucion_menu_bolsillos(usuario_actual)
            case 4:
                ejecucion_menu_conversion_divisas()
            case 5:
                print("Cerrando sesión...")
                break
            case _:
                print("Error. Elija una opcion válida")

def ejecucion_menu_gestion_cuentas(usuario_actual):
    while True:
        mostrar_menu_gestion_cuentas()
        try:
            opc_gestion_cuentas = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc_gestion_cuentas:
            case 1:
                registrar_cuentas(usuario_actual)
            case 2:
                modificar_cuenta(usuario_actual)
            case 3:
                eliminar_cuenta(usuario_actual)
            case 4:
                ver_cuentas_registradas(usuario_actual)
            case 5:
                ver_gastos_ingresos_usuario(usuario_actual)
            case 6:
                ver_saldo_total(usuario_actual)
            case 7:
                break
            case _:
                print("Error. Elija una opcion válida")

def ejecucion_menu_transacciones(usuario_actual):
    while True:
        mostrar_menu_transacciones()
        try:
            opc_transacciones = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc_transacciones:
            case 1:
                realizar_pago(usuario_actual)
            case 2:
                retirar_dinero(usuario_actual)
            case 3:
                depositar_dinero(usuario_actual)
            case 4:
                listar_movimientos(usuario_actual)
            case 5:
                break
            case _:
                print("Error. Elija una opcion válida")

def ejecucion_menu_bolsillos(usuario_actual):
    while True:
        mostrar_menu_bolsillos()
        try:
            opc_bolsillos = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc_bolsillos:
            case 1:
                crear_bolsillo(usuario_actual)
            case 2:
                agregar_dinero_bolsillo(usuario_actual)
            case 3:
                retirar_dinero_bolsillo(usuario_actual)
            case 4:
                eliminar_bolsillo(usuario_actual)
            case 5:
                listar_bolsillos(usuario_actual)
            case 6:
                break
            case _:
                print("Error. Elija una opcion válida")

def ejecucion_menu_conversion_divisas():
    while True:
        mostrar_menu_conversion_divisas()
        try:
            opc_conversion_divisas = pedir_opcion()
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue
        match opc_conversion_divisas:
            case 1:
                convertir_cop_a_usd()
            case 2:
                convertir_cop_a_eur()
            case 3:
                convertir_cop_a_gbp()
            case 4:
                convertir_cop_a_jpy()
            case 5:
                convertir_cop_a_cad()
            case 6:
                break
            case _:
                print("Error. Elija una opcion válida")