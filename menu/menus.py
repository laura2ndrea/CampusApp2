import menu.opciones as menuOpciones
import campers.operaciones as operacionesCampers
import campers.consultas as consultasCampers
import coordinacion_academica.operaciones as operacionesAcademicas

def menu_principal(): 
    while True: 
        menuOpciones.separador()
        print("Bienvenido al menú principal, por favor indique su rol: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_principal)
        if opcion == "1": 
           print("En construccion")
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


