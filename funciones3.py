#funciones
def ficha_producto(nombre, precio, stock): #no importa el orden de los parametros
    print("=========")
    print(f"nombre del producto: {nombre}")
    print(f"stock del producto: {stock}")
    print(f"precio del producto: {precio}")
    print("=========")
#codigo principal
nombre1 = input("ingrese el nombre del procuto: ")
while True:
    try:
        stock1 = int(input("ingrese el stock del producto: "))
        if stock1 < 0:
            print("debe ser mayor o igual a cero")
        else:
            break
    except ValueError:
        print("debe ingresar numeros")


while True:
    try:
        precio1 = int(input("ingrese el precio: "))
        if precio1 <= 0:
            print("debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("debe ingresar numeros")
        

ficha_producto(nombre1, precio1, stock1) #debemos enviarlo en el mismo orden que lo creamos en la funcion