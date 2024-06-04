import menu.opciones as opciones
import campers.operaciones as operaciones_campers
import campers.consultas as consultas_campers
import coordinacion_academica.operaciones as operaciones_academicas

def menu_principal(): 
    while True: 
        opciones.separador()
        print("Bienvenido al menú principal, por favor indique su rol: ")
        opcion = opciones.recorrer_opciones(opciones.opc_principal)
        if opcion == "1": 
           operaciones_academicas.cambiar_estado() 
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_coordinacion(): 
    return

def menu_trainer(): 
    return

def menu_camper(): 
    return 


