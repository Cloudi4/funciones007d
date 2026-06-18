#funciones
#validaciones
def buscar_mascota(lista_m, nombre_m):
    #recorrer lista
    for x in range(len(lista_m)):
        #verificar si el nombre coincide
        if nombre_m == lista_m [x]["nombre"]:
            return x
        #si no la encuentro
    return - 1
def validar_nombre(name):
    #una funcion de python que elimina los espacios al inicio o al final de un string y si queda vacia devuelve un false
    return name.strip() != "" #retorna true si es valido - false si es invalido
def validar_especie(especie):
    #verificar que sea perro gato o ave solamente (sin diferenciar mayusculas o minusculas)
    especies_validas = ["perro","gato","ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    #que sean numeros y mayor a cero
    return edad.isdigit() and int(edad) > 0

def mostrar_menu():
    print("||****** Menu principal ******||")
    print("||1.- Agregar mascota ||")
    print("||2.- buscar mascota||")
    print("||3.- eliminar mascota ||")
    print("||4.- marcar como vacunada||")
    print("||5.- mostrar mascotas ||")
    print("||6.- salir ||")
    print("||**************||")
    
def ingresar_opcion():
    while True:
        try:
            opcion = int(input("seleccione una opcion del 1 al 6: "))
            if opcion < 1 or opcion > 6:
                print("debe seleccionar ua opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("debe ingresar un numero")
    return opcion
#funcion para agregar una mascota nueva
def agregar_mascota(lista):
    nombre = input("ingrese el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje
    correcto = validar_nombre(nombre)
    if not correcto:
        print("el nombre no puede estar vacio")
        return 
    especie = input("ingrese la especie de la mascota: (perro/gato/ave): ")
    correcto = validar_especie(especie)
    if not correcto:
        print("la especie solo puede ser perro, gato o ave")
        return
    edad =  input("ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
    if not correcto:
        print("la edad debe ser un numero entero mayor a cero")
        return
    #aqui agrego al diccionario
    mascota = { 
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agrego a la lista
    lista.append(mascota)
    print("mascota agregada correctamente")
    #opcion 4
def actualizar_vacunas(lista_m):
    #recorrer lista 
    for m in lista_m:
        #validar la edad 
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False
#codigo principal
#declaro la lista de mascotas
lista_mascotas = []

op = 0
while op != 6:
    mostrar_menu()
    op = ingresar_opcion()

    if op == 1:
        agregar_mascota(lista_mascotas)
    elif op == 2:
        print("** buscar mascota ***")
        nombre = input("ingrese el nombre de la mascota: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontro
            m = lista_mascotas[posicion]
            print(f"nombre mascota: {m["nombre"]}")
            print(f"especie mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            print(f"vacunada: {m["vacunada"]}")
    elif op == 3:
        print("** eliminar mascota ***")
        nombre = input("ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(lista_mascotas, nombre)
        #validar que devolvio la funcion
        if posicion != -1: #la encontro
            lista_mascotas.pop(posicion)
            print("la mascota ha sido eliminada de la lista")
        else:
            print(f"la mascota '{nombre}' no se encuentra en la lista")
    elif op == 4:
        actualizar_vacunas(lista_mascotas)
        print("vacunas actualizadas")
    elif op == 5:
        #actualizar vacunas
        actualizar_vacunas(lista_mascotas)
        #mostrar los datos de las mascotas
        if len(lista_mascotas) == 0: #lista vacia
            print("no hay mascotas en la lista")
        else:
            print("**lista mascotas**")
            for m in lista_mascotas:
                print(f"nombre mascota: {m["nombre"]}")
                print(f"especie mascota: {m["especie"]}")
                print(f"edad mascota: {m["edad"]}")
                estado = "al dia" if m["vacunada"] else "pendiente"
                print(f"estado vacuna: {estado}")
                print("**********")

    elif op == 6:
        print("gracias por usar el sistema")