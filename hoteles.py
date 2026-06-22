def validar_huesped(nombre):
    return nombre.strip() != ""

def validar_habitacion(habitacion):
    if habitacion .isdigit():
        val = int(habitacion)
        return 1 <= val <= 200
    return False
def validar_noches(noches):
    if noches.isdigit():
        return int(noches) > 0
    return False

def buscar_reserva(lista, nombre):
    for i in range (len(lista)):
        if lista[i]["huesped"] == nombre:
            return i
    return -1

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
            if 1 <= opcion <= 6:
                return opcion
            print("opcion no valida")
        except ValueError:
            print("debe ingresar un numero")
def agregar_reserva(lista):
    huesped = input("ingrese nombre del huesped: ")
    if not validar_huesped(huesped):
        print("error: el nombre no puede estar vacio")
        return
    habitacion = input("Ingrese numero de la habitacion (1-200): ")
    if not validar_habitacion(habitacion):
        print("error: cantidad de noches invalida")
        return
    noches = input("Ingrese cantidad de noches: ")
    if not validar_noches(noches):
        print("Error: cantidad de noches invalida")
        return

    reserva = {
        "huesped": huesped,
        "habitacion": int(habitacion),
        "noches": int(noches),
        "confirmacion": False
    }
    lista.append(reserva)
    print("reserva agregada exitosamente")

def confirmar_reservas(lista):
    for r in lista:
        if r["noches"] >= 2:
            r["confirmada"] = True
        else:
            r["confirmada"] = False

lista_reservas = []
op = 0
 
while op != 6:
    mostar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_reserva(lista_reservas)
    elif op == 2:
        nombre = input("Ingrese nombre del huesped a buscar: ")
        pos = buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            r = lista_reservas[pos]
            print(f"posicion: {pos}")
            print(f"huesped: {r['huesped']}, habitacion: {r['habitacion']}, noches: {r['noches']}")
        else:
            print("reserva no encontrada")
    elif op == 3:
        nombre = input("ingrese nombre del huesped a eliminar: ")
        pos = buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
            print("reserva eliminada")
        else:
            print(f"la reserva del huesped '{nombre}' no se encuentra registrada")
    elif op == 4:
        confirmar_reservas(lista_reservas)
        print("reservas actualizadas")
    elif op == 5:
        confirmar_reservas(lista_reservas)
        print("***lista reservas***")
        for r in lista_reservas:
            estado = "confirmada" if r["confirmada"] else "pendiente"
            print(f"huesped: {r['huesped']}\nHabitacion: {r['habitacion']}\nNoches: {r['noches']}\nEstado: {estado}\n")
    elif op == 6:
        print("Gracias por usar el sistema")