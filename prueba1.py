#funciones
def mostrar_menu():
    print("||****** Menu principal ******||")
    print("||1.- Agregar mascota ||")
    print("||2.- buscar mascota||")
    print("||3.- eliminar mascota ||")
    print("||4.- masrcar como vacunada||")
    print("||5.- mostrar mascotas ||")
    print("||6.- salir ||")
    print("||**************||")
    
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("seleccione una opcion del 1 al 6"))
            if opcion < 1 or opcion > 6:
                print("debe seleccionar ua opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("debe ingresar un numero")
    return opcion
#codigo principal
#declaro la lista de mascotas
lista_mascotas = []

mostrar_menu()
op = ingresar_opcion()