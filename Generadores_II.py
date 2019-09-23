# El asterisco sirve para decir que la función recibirá un número indeterminado de parámetros
def GenerarCudades(*ciudades):
    for elemento in ciudades:
        for SubElemento in elemento:
            yield SubElemento

#Otra forma de hacer estos mismo, pero usando yield from
def GenerarCudades2(*ciudades):
    for elemento in ciudades:        
        yield from elemento

CiudadesDevueltas=GenerarCudades("Santander","Bilbao","Burgos","Jaén")
CiudadesDevueltas2=GenerarCudades2("Santander","Bilbao","Burgos","Jaén")

print ("Usando for anidados")
print(next(CiudadesDevueltas))
print(next(CiudadesDevueltas))

print ("Usando yield from")
print(next(CiudadesDevueltas2))
print(next(CiudadesDevueltas2))