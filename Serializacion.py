
#Guardar datos en ficheros binarios
import pickle

lista=["Juan","Ana","María","Andrés"]

fichero = open("fichero_binario.bin","wb") #wb es escritura en binario
pickle.dump(lista,fichero) #Copia el contenido de la lista en el fichero
fichero.close()
del (fichero) #€sto borra el objeto fichero de la memoria

#Ahora abro el fichero creado antes

fichero=open("fichero_binario.bin","rb")
lista=pickle.load(fichero)
print(lista)
