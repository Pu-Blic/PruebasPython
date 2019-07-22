colores =['rojo','azul','verde']
print (dir(colores))


# crear una lista con un rango de números del 1 al 10. 
# Hay que poner un número más del rago que se quiere crear
rango= list(range(1,11))
print(rango)


print("La lista 'colores' tiene", len(colores), "elementos")
print("El primer elemento de la lista 'colores' es:", colores[0])

BuscarColor = input("Introduce un color para buscarlo: ")
print("El resultado de la búsqueda es:", BuscarColor in colores) #Busca un elemento de una lista. Devuelve true o false 

print("La lista de colores es:", colores)
print("Voy a cambiar el verde por morado")
colores[2]="morado"
print("La nueva lista de colores es:", colores)


color=input("Nuevo color: ")
colores.append(color) #Añade un nuevo elemento
print("La nueva lista de colores es:", colores)

#Si queremos añadir más de un elemento a la lista hay que usar el método 'Extend'
#También debemos pasarle los datos a través de una tupla
colores.extend(["magenta","negro","blanco"])
print("La nueva lista de colores es:", colores)

#Insertar un elemento a partir de una posición. 
#Insertamos el color en la posición 1
colores.insert(1,"gris")
print("Añado el color gris en la posicíón 1")
print("La nueva lista de colores es:", colores)

print("Borro el último elemento")
colores.pop(len(colores)-1) #borra el último elemento. También sirve sin ponerle índice.
print("La nueva lista de colores es:", colores)

print("Borro el elemento 'negro'")
colores.remove("negro") #elimina el color negro
print("La nueva lista de colores es:", colores)

print("Ordeno alfabéticamente la lista")
colores.sort()
print(colores)

print("Ordeno alfabéticamente, al revés, la lista")
colores.sort(reverse=True)
print(colores)

#mostrar el índice de un elemento
print(colores.index("rojo"))

#contar los elementos de la lista
print("La lista tiene", colores.count(), " elementos")