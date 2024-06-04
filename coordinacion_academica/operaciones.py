import data.datos as datos

def notas_prueba_ingreso():
    campers = datos.cargar_datos("data/campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("Error: El documento ingresado no corresponde a ningún camper.")
        return

    if campers[doc]["pruebaIngreso"]["promedio"] != 0:
        print("Las notas de la prueba de ingreso ya han sido ingresadas.")
        return

    while True:
        try:
            nota_practica = float(input("Ingrese la nota de la prueba práctica (0-100): "))
            if nota_practica < 0 or nota_practica > 100:
                print("Error: La nota de la prueba práctica debe ser entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número entre 0 y 100.")

    while True:
        try:
            nota_teorica = float(input("Ingrese la nota de la prueba teórica (0-100): "))
            if nota_teorica < 0 or nota_teorica > 100:
                print("Error: La nota de la prueba teórica debe ser entre 0 y 100.")
                continue
            break
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número entre 0 y 100.")

    promedio = (nota_practica + nota_teorica) / 2
    campers[doc]["pruebaIngreso"]["nota_practica"] = nota_practica
    campers[doc]["pruebaIngreso"]["nota_teorica"] = nota_teorica
    campers[doc]["pruebaIngreso"]["promedio"] = promedio

    if promedio >= 60:
        campers[doc]["estado"] = "Aprobado"

    datos.guardar_datos("data/campers.json", campers)
    print("Notas de la prueba de ingreso ingresadas correctamente.")


def cambiar_estado():
    campers = datos.cargar_datos("data/campers.json")
    doc = input("Ingrese el documento del camper: ").strip()

    if doc not in campers:
        print("Error: El documento ingresado no corresponde a ningún camper.")
        return

    print(f"Estado actual del camper: {campers[doc]['estado']}")
    print("Opciones de estado: Graduado, Expulsado, Retirado")

    while True:
        nuevo_estado = input("Ingrese el nuevo estado del camper: ").strip().capitalize()
        if nuevo_estado not in ["Graduado", "Expulsado", "Retirado"]:
            print("Error: El estado ingresado no es válido. Por favor, ingrese un estado válido (Graduado, Expulsado, Retirado).")
        else:
            break

    campers[doc]["estado"] = nuevo_estado
    datos.guardar_datos("data/campers.json", campers)
    print("Estado del camper actualizado correctamente.")

   