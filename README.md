# Proyecto Wallet

----------
***

## Tabla de Contenido
1. [Informacion General](#informacion-general)
2. [Tecnologias](#tecnologias)
3. [Instalacion](#instalacion)
4. [Caracteristicas Principales](#caracteristicas-principales)
5. [Estructura del Sistema](#estructura-del-sistema)
6. [Colaboracion](#colaboracion)
7. [FAQs](#faqs)

### Informacion General
***

**Wallet** es un prototipo de aplicación desarrollado en Python como parte de un proyecto formativo en Campuslands. Su objetivo es permitir a los usuarios gestionar cuentas bancarias virtuales, realizar transacciones financieras, y organizar sus finanzas personales por medio de funcionalidades como bolsillos de ahorro, reportes de ingresos/gastos y conversión de monedas. Esta aplicación se ejecuta por consola, sin interfaz gráfica, y está orientada al aprendizaje y desarrollo de habilidades en programación y gestión de proyectos.

## Tecnologias
***

Este sistema ha sido desarrollado utilizando las siguientes tecnologías:

-   **Python**: Lenguaje de programación principal.
-   **GitHub**: Para la gestión de versiones y colaboración en el desarrollo.
- **Visual Studio Code**: Para el desarrollo del prototipo y ejecución por consola. Versión 1.99.2

## Instalacion
***
Siga estos pasos para instalar y ejecutar el sistema:
```
$ git clone https://github.com/BryanVillabona/Proyecto_Wallet
$ cd Proyecto_Wallet
$ python main.py
```
Para su funcionamiento, debes instalar la siguiente dependencia:
```
$ pip install requests
```

## Caracteristicas Principales
***

-   Registro e inicio de sesión de usuarios
    
-   Gestión de cuentas virtuales.
    
-   Visualización y registro de ingresos y gastos
    
-   Creación y administración de bolsillos de ahorro
    
-   Gestión de transacciones, pagos y retiros
    
-   Conversión entre monedas
    
-   Cálculo y visualización de saldo total
    
-   Menús interactivos en consola

## Estructura del Sistema
***
La aplicación se organiza en distintos módulos Python con responsabilidades específicas:
```
proyecto_wallet/
│
├── main.py                  # Punto de entrada del programa
├── data.py                  # Módulo para el cargue de datos.
├── registros.json           # Archivo json donde se guardan las cuentas registradas por usuario.
├── transacciones/           # Realizar pagos, retirar y depositar dinero y ver movimientos.
│   ├── transacciones.py
│   ├── movimientos.json
├── menu_submenu/            # Módulo del menú y submenús, navegación.
│   ├── utilidades_menu.py
├── iniciosesion_registro/   # Modulos para registrar un usuario e iniciar sesión.
│   ├── inicio_sesion.py
│   ├── registro.py
│   ├── registros.json
├── gestion_cuentas/         # Modulo para registrar nuevas cuentas, modificar o eliminar cuentas, ver las cuentas registradas y el saldo total.
│   ├── registro_cuentas.py
│   ├── cuentas.json
│   ├── cuentas_registradas.json
├── divisas/                 # Modulo para realizar la conversión entre diferentes monedas.
│   ├── divisas.py
├── bolsillos/               # Gestión de bolsillos, registrar bolsillo, agregar o retirar dinero al bolsillo, eliminar un bolsillo y listar los bolsillos creados.
│   ├── bolsillos.py
│   ├── bolsillos.json
└── README.md
```

## Colaboracion
***

Si deseas colaborar en el proyecto, puedes:

1.  Hacer un fork del repositorio.
    
2.  Crear una rama con tus cambios (`git checkout -b feature/mi_rama`).
    
3.  Realizar un commit (`git commit -m "Descripción de cambios"`).
    
4.  Haz push a tu rama (`git push origin feature/mi_rama`)
5. Abre un Pull Request
    

Proyecto desarrollado con fines educativos. Cualquier aporte es bienvenido para mejorar su funcionalidad o estructura.

## FAQs
***
1.  **¿Necesito tener experiencia previa para usar esta app?**  
    _R: No, la aplicación es amigable con el usuario y está pensada para aprender sobre programación básica en Python._
    
2.  **¿Puedo agregar más tipos de cuentas?**
    

-   Sí, puedes:
    
    -   Editar el módulo `gestion_cuentas/cuentas_registradas.json`
        
    -   Agregar nuevos tipos en el archivo `cuentas_registradas.json`
        
    -   Procura agregar la nueva cuenta siguiendo el mismo modelo de los que ya están registrados.
        

3.  **¿Se puede convertir a una versión con interfaz gráfica?**  
    _Sí, aunque actualmente es por consola, se puede agregar alguna interfaz en una nueva versión.
***
- Github: **[https://github.com/BryanVillabona](https://github.com/BryanVillabona)**