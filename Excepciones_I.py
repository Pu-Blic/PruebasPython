def Sumar(a,b):
    return int(a)+int(b)

def Restar(a,b):
    return int(a)-int(b)

def Multiplicar(a,b):
    return int(a)*int(b)

def Dividir(a,b):
    try:
        return int(a)/int(b)
    except ZeroDivisionError2:
        print("No se puede dividir entre 0. Operación errónea")
    except:
        print("Error al dividir")

def ValidarNumero(n):
    try:
        return int(n)
    except ValueError:        
        print("El valor introducido no es un número")
        return False
    finally:
        pass

a=input("Introduce un nmúmero: ")
while ValidarNumero(a)==False:    
    a=input("Introduce un nmúmero: ")

b=input("Introduce otro número: ")
while ValidarNumero(b)==False:    
    b=input("Introduce un nmúmero: ")


opcion =input("¿Qué operación quieres realizar? (sumar, restar, multiplicar, dividir): ")

if opcion =="sumar":
    print("La suma es:", Sumar(a,b))
elif opcion=="restar":
    print("La resta es:", Restar(a,b))
elif opcion=="multiplicar":
    print("La multiplicación es:", Multiplicar(a,b))
elif opcion=="dividir":
    print("La división es:", Dividir(a,b))
else:
    print("Opción no reconocida")

print("Operación realizada. Se sigue con la ejecución del programa")

#Pruebo a crear excepciones propias usando el método 'raise'

import math

def CalcularRaizCuadrada(num):
    if num<0:
        raise ValueError ("El número no puede ser negativo") #Defino un error de Valor erróneo y le asigno un texto para cuando de error
    else:
        return math.sqrt(num)

n=int(input("Introcude un número para calcular su raíz cuadrada: "))

try:
    print(CalcularRaizCuadrada(n))
except ValueError as ErrorRaizCuadrada:
    print(ErrorRaizCuadrada) #Aquí imprime el texto que se definió en la opción 'raise'


print("Fin Raiz cuadrada")