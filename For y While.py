i=1
j=1

for k in  (range(i-1,i+2)):
    for l in (range (j-1, j+2)):
        print (k,":",l)



alimentos = ["Pera", "Macarrones", "Alubias", "Pimientos", "Lechuga", "Puerros", "Zanahoria"]

#Imprimir todos los items de la lista
#El bucle puede romperse con 'brake'
#Se puede usar 'continue' para continuar con la siguiente iteración del bucle
for comida in alimentos:
    print("Comida:", comida)
    
#La tabla de multiplicar
tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
while tabla != "no":
    tabla =tabla
    print("La tabla del", tabla, "es")
    for i in range(1,11):    
        tabla=int(tabla)
        resultado = tabla * i
        print(tabla, "x", i, "=",resultado)
    tabla= (input("Escribe qué tabla de multiplicar quieres ver (escribe 'no' para no mostar ninguna tabla: "))
print("Parece que ya no quieres saber más tablas de multiplicar")


