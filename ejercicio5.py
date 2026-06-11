#funciones
def mostrar_encabezado():
    print("==== Sistema de admision escolar =====")

def solicitar_datos():
    estudiantes = {}
    estudiantes["rut"] = input("ingrese el rut del estudiante: ")
    estudiantes["nombre"] = input("ingrese el nombre del estudiante: ")
    estudiantes["carrera"] = input("ingrese la carrera que estudia: ")
    while True:
        try:
            estudiantes["semestre"] = int(input("ingrese el semestre que cursa: "))
            if estudiantes["semestre"] < 1 or estudiantes["semestre"] > 4:
                print("debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("debe ingresar un numero")

    return estudiantes

def mostrar_datos(alumnos):
    print(f"nombre del estudiante: {alumnos["nombre"]} ")
    print(f"rut del estudiante:{alumnos["rut"]}")
    print(f"carrera del estudiante: {alumnos["carrera"]}")
    print(f"semestre del estudiante: {alumnos["semestre"]} ")

#codigo principal
datos = solicitar_datos()
#imprimir encabezado
mostrar_encabezado()
mostrar_datos(datos)