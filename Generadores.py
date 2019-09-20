def FuncionPares(limite):
    lista=[]

    i=1

    while i<limite:
        lista.append(i*2)
        i=i+1

    return lista

def GeneradorPares(limite):
    i=1

    while i<limite:
        yield i*2
        i=i+1


print("Función Pares")
print(FuncionPares(11))

print("Usando el generador de 10 pares, pero se detiene si el par es el número 12")
Pares=GeneradorPares(11)
for i in Pares:
    if i==12:
        break
    else:
        print(i)

NuevosPares=GeneradorPares(11)
print("Creo una nueva generación de pares e imprimo el primer elemento")
print(next(NuevosPares))
print("Aquí podría ir más código...")
print("El siguiente número par es:", next(NuevosPares))
print("Aquí podría ir más código...")
print("El siguiente número par es:", next(NuevosPares))
next(NuevosPares)
next(NuevosPares)
print("Salto 2 números pares y el siguiente es:",next(NuevosPares))