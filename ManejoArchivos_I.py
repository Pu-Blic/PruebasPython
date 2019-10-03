#Se utiliza la librería io
from io import open

archivo = open("fichero.txt","w") #La w es por write
texto="Este texto lo voy a meter\ndentro del fichero.\n"
archivo.write(texto)

for i in range(4):    
    archivo.write("Iteración: "+str(i)+"\n")

archivo.close()


archivo = open("fichero.txt","r") #La r es por read
texto=archivo.read()
archivo.close()
print(texto)

archivo = open("fichero.txt","r") #La r es por read
texto=archivo.readlines() #crea una lista con el contenido de cada línea del fichero
archivo.close()
print("La tercera línea del fichero es: "+texto[2])


archivo = open("fichero.txt","a") #La a es por append. Abierto para añadir
texto="Esta línea es nueva con el fichero abierto en modo append\n"
archivo.write(texto)
archivo.close()

print("Imprimo el fichero")
archivo = open("fichero.txt","r")
texto=archivo.read() 
print(texto) 
texto=archivo.read() #esta segunda vez no  imprime nada porque el cursor ha quedado al final del fichero en el read anterior
print("Ahora leo de nuevo el fichero y lo imprimo.")
print(texto) 
print("Muevo el puntero al inicio")
archivo.seek(0) #Esto hace que el puntero se coloque en la posición cero del fichero
texto=archivo.read()
print(texto) 


print("Muevo el puntero a la posición 20 del fichero e imprimo desde ahí")
archivo.seek(20) #Esto hace que el puntero se coloque en la posición cero del fichero
texto=archivo.read()
print(texto) 

#Si al método read se le pasa un parámetro lee desde el cursor hasta la posición indicada
print("Si al método read se le pasa un parámetro lee desde el cursor hasta la posición indicada")
print("Leo los 10 primeros caracteres del fichero")
archivo.seek(0)
texto=archivo.read(10)
print(texto)
archivo.close()


print("Abro el fichero en modo lectura-escritura")
archivo = open("fichero.txt","r+") #La r+ estaría abierto como lectura/escritura
lista=archivo.readlines()
lista.append("Línea nueva")
archivo.truncate(0)
archivo.writelines(lista)
archivo.close()