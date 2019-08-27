
def multiplicar(a, b):
    return int(a) * int(b)

#La tabla de multiplicar
tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
while tabla != "no":
    tabla =int(tabla)
    print("La tabla del", tabla, "es")
    for i in range(1,11):    
        resultado = multiplicar(tabla, i)
        print(tabla, "x", i, "=",resultado)
    tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))

