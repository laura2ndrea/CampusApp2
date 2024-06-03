opc_principal = ("1. Coordinación", "2. Trainers", "3. Campers", "4. Salir del programa")

def recorrer_opciones(opciones): 
    for i in opciones:
        print(i)
    separador()
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def separador(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")