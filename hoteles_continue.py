import hoteles as p
#codigo principal
lista_reservas = []
opcion = 0
while opcion != 6:
    p.mostar_menu()
    opcion = p.ingresar_opcion()

    if opcion == 1:
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        nombre = input("ingrese el nombre del huesped a buscar")
        pos = p.buscar_reserva(lista_reservas, nombre)
        if opcion != -1:
            print("reserva encontrada")
            print(f"nombre del huesped: {lista_reservas[pos]["huesped"]}")
            print(f"numero de habitacion: {lista_reservas[pos]["habitacion"]}")
            print(f"noches de hospedaje: {lista_reservas[pos]["noches"]}")
            estado = "confirmada" if lista_reservas[pos]["confirmada"] else "pendiente"
            print(f"estado: {estado}")
        else:
            print(f"el huesped '{nombre}' no ha sido encontrado")
    elif opcion == 3:
        nombre = input("ingrese el nombre del huesped a eliminar")
        pos = p.buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
            print("la reserva ha sido eliminada")
        else:
            print(f"el huesped '{nombre}' no ha sido encontrado")
    elif opcion == 4:
        p.confirmar_reservas(lista_reservas)
    elif opcion == 5:
        p.confirmar_reservas(lista_reservas)
        p.mostrar_reservas(lista_reservas)
        
    elif opcion == 6:
        print("gracias por usar el programa. vuelva pronto")