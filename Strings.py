myStr ="hola oJEtes 25"

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
