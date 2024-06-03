import json 

data = {}

def cargar_datos(nombre_archivo): 
    global data
    try: 
        with open(nombre_archivo, "r") as file:
            data = json.load(file)
            print ("Datos cargados exitosamente")
    except Exception: 
        print("Error al cargar los datos")


def guardar_datos(): 

    return 

def guardar_datos(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error al guardar datos: {e}")
