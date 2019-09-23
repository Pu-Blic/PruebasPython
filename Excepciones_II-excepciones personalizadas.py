import math

def CalcularRaizCuadrada(num):
    if num<0:
        raise ValueError ("El número no puede ser negativo") #Defino un error de Valor erróneo y le asigno un texto para cuando de error
    else:
        return math.sqrt(num)

def ValidarNumero(n):
    try:
        return int(n)
    except ValueError:        
        print("El valor introducido no es un número")
        return False
    
n=input("Introduce un nmúmero: ")
while ValidarNumero(n)==False:    
    n=input("Introduce un nmúmero: ")

try:
    print(CalcularRaizCuadrada(float(n)))
except ValueError as ErrorRaizCuadrada:
    print(ErrorRaizCuadrada) #Aquí imprime el texto que se definió en la opción 'raise'
    
print("Fin del programa")
