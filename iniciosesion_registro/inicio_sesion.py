from data import *

def inicio_sesion():    
    registros = cargar_datos("registros.json")

    if not registros:
        print("***** No hay usuarios registrados. Por favor, regístrese primero. *****")
        return  

    print("\n***** INICIO DE SESIÓN *****")  
    usuario = input("Ingrese su usuario: ").strip()  

    usuario_actual = None  
    for nombre, datos in registros.items():  
        if datos["Usuario"].strip().lower() == usuario.lower():
            usuario_actual = nombre  
            break  

    if usuario_actual:  
        contrasenia = input("Ingrese su contraseña: ").strip()  
        if registros[usuario_actual]["Contraseña"] == contrasenia:  
            print(f"***** Inicio de sesión exitoso. Bienvenido de nuevo, {usuario_actual} *****")
            
            from utilidades_menu import ejecucion_menu_inicio  
            ejecucion_menu_inicio(usuario_actual)
        else:  
            print("***** Error: Contraseña incorrecta. *****")  
    else:  
        print("***** Usuario no encontrado. Primero debe registrarse. *****")