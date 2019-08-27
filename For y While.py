alimentos = ["Pera", "Macarrones", "Alubias", "Pimientos", "Lechuga", "Puerros", "Zanahoria"]

#Imprimir todos los items de la lista
#El bucle puede romperse con 'brake'
#Se puede usar 'continue' para continuar con la siguiente iteración del bucle
for comida in alimentos:
    print("Comida:", comida)
    
#La tabla de multiplicar
tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
while tabla != "no":
    tabla =int(tabla)
    print("La tabla del", tabla, "es")
    for i in range(1,11):    
        resultado = tabla * i
        print(tabla, "x", i, "=",resultado)
    tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
print("Parece que ya no quieres saber más tablas de multiplicar")