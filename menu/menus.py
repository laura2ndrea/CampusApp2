import menu.opciones as opciones

def menu_principal(): 
    while True: 
        opciones.separador()
        print("Bienvenido al menú principal, por favor indique su rol: ")
        opcion = opciones.recorrer_opciones(opciones.opc_principal)
        if opcion == "1": 
            print("coordinacion")
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


