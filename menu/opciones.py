opc_principal = ("1. Coordinación", "2. Trainers", "3. Campers", "4. Salir del programa")

opc_coordinacion = ("1. Gestión de matrícula", "2. Gestión de reportes", "3. Gestión de rutas", "4. Gestión de campers", "5. Salir del menú")

opc_gestion = ("1. Asignación de campers a rutas", "2. Asignacion de trainers a rutas", "3. Asignacion de fechas a rutas", "3. Asignación de salones a rutas", "4. Salir del menú")

opc_reportes = ("1. Mostrar campers inscritos", "2. Mostrar campers aprobados", "3. Mostrar lista de entrenadores", "4. Mostrar campers de bajo rendimiento", "5. Mostrar trainers y campers asociados a rutas de entrenamiento", "6. Mostrar cantidad de campers aprobados y no aprobados por módulo", "7. Salir del menú")

opc_rutas = ("1. Mostrar rutas de entrenamiento", "2. Crear nueva ruta de entrenamiento", "3. Salir del menú")

opc_gestion_campers = ("1. Inscripción de nuevo camper", "2. Ingresar notas de prueba de ingreso", "3. Salir del menú")

opc_trainers = ("1. Mostrar información personal", "2. Mostrar rutas asignadas", "3. Ingresar notas", "4. Salir del menú")

opc_campers = ("1. Mostrar información personal", "2. Mostraer notas", "3. Mostrar advertencias", "4. Salir del menú")

def recorrer_opciones(opciones): 
    for i in opciones:
        print(i)
    separador()
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def separador(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def mini_separador(): 
    print("**************************")