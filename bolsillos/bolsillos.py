from data import *

def crear_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para crear un bolsillo.")
        return

    print("\n***** Tus Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        saldo = cuentas_registradas[usuario_actual][cuenta]["Saldo"]
        print(f"{i}. {cuenta} - Saldo: ${saldo:.2f} COP")

    try:
        opcion = int(input("Seleccione la cuenta de donde desea guardar dinero en el bolsillo: "))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print("Error. Opción inválida.")
            return

        cuenta_seleccionada = cuentas_usuario[opcion - 1]

        nombre_bolsillo = input("\nIngrese el nombre del bolsillo: ").strip().capitalize()
        monto = float(input("Ingrese el monto a guardar en el bolsillo: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        if monto > cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"]:
            print("Error. Fondos insuficientes.")
            return

        cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"] -= monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        if usuario_actual not in bolsillos:
            bolsillos[usuario_actual] = {}

        bolsillos[usuario_actual][nombre_bolsillo] = {
            "Monto": monto,
            "Cuenta_origen": cuenta_seleccionada
        }
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\n***** Bolsillo '{nombre_bolsillo}' creado con éxito *****")
        print(f"Se han guardado ${monto:.2f} COP desde la cuenta {cuenta_seleccionada}.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def agregar_dinero_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print("No tienes bolsillos registrados.")
        return

    print("\n***** Tus Bolsillos Registrados *****")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        monto = bolsillos[usuario_actual][bolsillo]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo]["Cuenta_origen"]
        print(f"{i}. {bolsillo} - Saldo: ${monto:.2f} COP - Cuenta Origen: {cuenta_origen}")

    try:
        opcion_bolsillo = int(input("Seleccione el bolsillo al que desea agregar dinero: "))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print("Error. Opción inválida.")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        if usuario_actual not in cuentas_registradas or cuenta_origen not in cuentas_registradas[usuario_actual]:
            print(f"Error: La cuenta origen '{cuenta_origen}' no está registrada.")
            return

        saldo_disponible = cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"]

        print(f"\nLa única cuenta permitida para agregar dinero a este bolsillo es '{cuenta_origen}' (Saldo disponible: ${saldo_disponible:.2f} COP)")

        monto = float(input("Ingrese el monto a agregar al bolsillo: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        if monto > saldo_disponible:
            print("Error. Fondos insuficientes.")
            return

        cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] -= monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"] += monto
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\n***** Transacción exitosa *****")
        print(f"Has agregado ${monto:.2f} COP al bolsillo '{bolsillo_seleccionado}'.")
        print(f"Nuevo saldo del bolsillo: ${bolsillos[usuario_actual][bolsillo_seleccionado]['Monto']:.2f} COP.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def retirar_dinero_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print("No tienes bolsillos registrados.")
        return

    print("\n***** Tus Bolsillos Registrados *****")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        monto = bolsillos[usuario_actual][bolsillo]["Monto"]
        print(f"{i}. {bolsillo} - Saldo: ${monto:.2f} COP")

    try:
        opcion_bolsillo = int(input("Seleccione el bolsillo del cual desea retirar dinero: "))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print("Error. Opción inválida.")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        saldo_bolsillo = bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        monto = float(input("\nIngrese el monto a retirar: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        if monto > saldo_bolsillo:
            print("Error. Fondos insuficientes en el bolsillo.")
            return

        bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"] -= monto
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] += monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        print(f"\n***** Retiro exitoso *****")
        print(f"Has retirado ${monto:.2f} COP del bolsillo '{bolsillo_seleccionado}'.")
        print(f"Nuevo saldo del bolsillo: ${bolsillos[usuario_actual][bolsillo_seleccionado]['Monto']:.2f} COP.")
        print(f"El dinero ha sido transferido de vuelta a la cuenta de origen '{cuenta_origen}'.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def eliminar_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print("\nNo tienes bolsillos registrados para eliminar.")
        return

    print("\n***** Tus Bolsillos Registrados *****")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        saldo = bolsillos[usuario_actual][bolsillo]["Monto"]
        print(f"{i}. {bolsillo} - Saldo: ${saldo:.2f} COP")

    try:
        opcion_bolsillo = int(input("\nSeleccione el bolsillo que desea eliminar: "))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print("Error. Opción inválida.")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        saldo_bolsillo = bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        confirmacion = input(f"\n¿Está seguro de que desea eliminar el bolsillo '{bolsillo_seleccionado}'? (S/N): ").strip().lower()

        if confirmacion != "s":
            print("Operación cancelada.")
            return

        if saldo_bolsillo > 0:
            cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] += saldo_bolsillo
            guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")
            print(f"\nSe han transferido ${saldo_bolsillo:.2f} COP de '{bolsillo_seleccionado}' a su cuenta de origen '{cuenta_origen}'.")

        del bolsillos[usuario_actual][bolsillo_seleccionado]
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\nEl bolsillo '{bolsillo_seleccionado}' ha sido eliminado exitosamente.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def listar_bolsillos(usuario_actual):
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print("\nNo tienes bolsillos registrados.")
        return

    print("\n***** Tus Bolsillos Registrados *****")
    
    for i, (nombre_bolsillo, datos) in enumerate(bolsillos[usuario_actual].items(), 1):
        saldo = datos["Monto"]
        print(f"{i}. {nombre_bolsillo} - Saldo: ${saldo:.2f} COP")

    print("-" * 40)