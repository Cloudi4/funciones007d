#funciones
def conersion_notas(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return round(nota,1)
#codigo principal
while True:
    try:
        p = float(input("ingrese la nota del estudiante: "))
        if p < 0:
            print("debe ser una nota positiva")
        else:
         break
    except ValueError:
        print("debe ingresar un numero")

while True:
    try:
        pt = float(input("ingrese la nota total de la evaluacion: ")) 
        if p < 0:
            print("debe ser una nota positiva")
        else:
         break
    except ValueError:
        print("debe ingresar un numero")
#llamar a la funcion, enviar datos y mostrar la nota convertida
calificacion = conersion_notas(p, pt)
print(f"la nota chilena es: {calificacion}")