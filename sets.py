#Es una colección de datos sin índices, se ponen los datos entre los símbolos de llaves
colores = {'rojo','azul','verde'}

print (colores)
print(type(colores))
print("¿El color rojo está en el set?", 'rojo' in colores)

print("Añado el color morado con el método add")
colores.add("morado")
print(colores)
print("")
print("")
print("Para borrar un elemento se usa el método remove con el texto que se quiere borrar")
print("Borro el color azul. Si se intenta borrar un elemento que no existe salta una excepción y da error.")
colores.remove("azul")
print(colores)

print("")
print("")
print("Borro el set")
colores.clear()
print(colores)