myStr ="hola oJEtes"

#print(dir(myStr))

print(myStr.upper())
print(myStr.title())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace("o","0"))

oes= myStr.count("o")
print (oes)
print("El texto tiene" , oes  , "oes")

print(myStr.split()) #Por defecto Lo separa usando los caracteres en blanco

myArray=myStr.split("o")
print("Array: ",  myArray)
print(type(myArray))

#Encontrar la posición de la letra 'l'
print("La posición de la letra l es:", myStr.find("l"))

#Encontrar el índice de una palabra
print("El índice de la letra l es:", myStr.index("l"))

#Comprobar si la variable es numérica
print("El texto es numérico:", myStr.isnumeric())

#Comprobar si la variable es alfanumérico
print("El texto es numérico:", myStr.isalpha())

#Mostrar el carácter de la posición 6
print("En la posición 6 hay una letra", myStr[6])
print("La primera letra o está en la posición:" , myStr.index("o"))