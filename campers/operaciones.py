import data.datos as datos 

def crear_camper(): 
    campers = datos.cargar_datos("data\campers.json")
    camper = {}

    doc = input("Ingrese el documento del nuevo camper: ").strip()
    if doc in campers:
        print("Error, el documento ya se encuentra registrado.")
        return
    
    camper["nombres"] = input("Ingrese nombres: ").strip()
    camper["apellidos"] = input("Ingrese apellidos: ").strip()
    camper["direccion"] = input("Ingrese la direccion: ").strip()
    camper["acudiente"] = input("Ingrese el nombre del acudiente: ").strip()
    camper["telefono_celular"] = input("Ingrese teléfono celular: ").strip()
    camper["telefono_fijo"] = input("Ingrese teléfono fijo: ").strip()
    camper["estado"] = "Inscrito"
    camper["riesgo"] = ""
    camper["pruebaIngreso"] = {
        "nota_practica": 0,
        "nota_teorica": 0,
        "promedio": 0
    }
    
    campers[doc] = camper
    datos.guardar_datos("data\campers.json", campers)

def actualizar_camper(): 
    campers = datos.cargar_datos("data\campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("Error: El documento ingresado no corresponde a ningún camper.")
        return

    print("Datos actuales del camper:")
    for clave, valor in campers[doc].items():
        if clave not in ["pruebaIngreso", "estado", "riesgo"]: 
            print(f"{clave.capitalize()}: {valor}")

    campo_actualizar = input("Ingrese el campo que desea actualizar: ").strip().lower()
    if campo_actualizar not in campers[doc] or campo_actualizar in ["pruebaingreso", "estado", "riesgo"]:
        print("Error: El campo ingresado no existe o no puede ser actualizado.")
        return

    nuevo_valor = input(f"Ingrese el nuevo valor para '{campo_actualizar.capitalize()}': ").strip()
    campers[doc][campo_actualizar] = nuevo_valor

    datos.guardar_datos("data\campers.json", campers)
    print("Datos del camper actualizados correctamente.")
