def mostar_menu():
    print("******MENU PRINCIPAL******")
    print("1.- Agregar reserva")
    print("2.- Buscar reserva")
    print("3.- Eliminar reserva")
    print("4.- Confirmar reserva")
    print("5.- Mostrar reserva")
    print("6.- Salir")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            else:
                return opcion
        except ValueError:
            print("debe ingresar un numero del 1 al 6")

def buscar_reserva(lista, nombre):
    for i in range (len(lista)):
        if huesped == lista_reserva[i]["huesped"]
            return i
    return -1

 def agregar_reserva(lista):
    nombre_completo = input("ingrese nombre del huesped: ")
    correcto = validar_huesped(huesped)
    if not correcto:
        print("error: el nombre no puede estar vacio")
        return
    
    habitacion = input("Ingrese numero de la habitacion (1-200): ")
    correcto = validar_habitacion(habitacion)
    if not correcto(habitacion):
        print("error: cantidad de noches invalida")
        return
    noches = input("Ingrese cantidad de noches: ")
    correcto = validar_noches(noches)
    if not correcto(noches):
        print("Error: cantidad de noches invalida")
        return   

reserva = {
    "huesped": nombre_completo.strip().upper(),
    "habitacion": int(habitacion),
    "noches": int(noches)
    "confirmada": False
}
lista_reserva.append(reserva)
print("reserva agregada correctamente")


