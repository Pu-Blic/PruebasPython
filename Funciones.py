
def multiplicar(a, b):
    return int(a) * int(b)

def sumar (a, b):
    return int(a) + int(b)

#La tabla de multiplicar
tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
while tabla != "no":
    tabla =int(tabla)
    print("La tabla del", tabla, "es")
    for i in range(1,11):    
        resultado = multiplicar(tabla, i)
        suma = sumar(tabla,i)
        print(tabla, "x", i, "=",resultado, ". Su suma es: ", suma)
    tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))

print ("*******")
print ("* Fin *")
print ("*******")