#Cada célula tiene 8 células "vecinas"
#Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
#Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").

import random
from colorama import Fore, Back, Style, init
init(convert = True)

def PintarTablero(tablero, tableroNuevo): 
    for i in range(len(tablero[0])):
        for j in range(len(tablero[1])):
            if tablero[i][j] == tableroNuevo[i][j]:
                print(Fore.GREEN + tablero[i][j],end="")
            else:
                print(Fore.RED + tablero[i][j],end="")
        print("")

def IniciarTablero():
    tablero=[]
    
    for i in range(13):
        tablero.append([""] * 13)

    #Ponto una O en cada elemento de cada una de las diez listas de la matriz
    for i in range(len(tablero[0])):
        for j in range(len(tablero[1])):
            #Pongo los bordes del tablero con un caracter distinto
            if (i>0 and i<len(tablero[0])-1) and (j>0 and j<len(tablero[1])-1):
                if random.random()<0.5:                
                    tablero[i][j]="O"
                else:
                    tablero[i][j]="X"
            else:
                tablero[i][j]="■"
    return tablero

def Iterar(tableroOld):    
    filas=len(tableroOld[0])-2
    columnas=len(tableroOld[1])-2
    
    for fila in range(filas):        
        for columna in range(columnas):
            CelulasVivas=0            
            CelulasVivas=ContarCelulasVivas(tableroOld, fila+1, columna+1)
            if CelulasVivas<2 or CelulasVivas>3:
                if tableroOld[fila+1][columna+1]=="O":
                    tableroOld[fila+1][columna+1]="X"
            elif CelulasVivas==3 and tablero[fila+1][columna+1] == "X":
                tableroOld[fila+1][columna+1] =  "O"

    return tableroOld
                        
def ContarCelulasVivas(tableroAnt, fila, columna):
    ContarCelulasVivas=0

    for i in  (range(fila-1,fila+2)):
        for j in (range (columna-1, columna+2)):
            if (i==fila and j==columna):
                continue
            else:
                if tableroAnt[i][j]=="O":
                    ContarCelulasVivas=ContarCelulasVivas+1

    return ContarCelulasVivas


print("***********************")
print("**El juego de la vida**")
print("***********************")
print("")

# Se crea e inicia el tablero del juego
tablero = IniciarTablero()

tableroNuevo = tablero
iteraciones=int(input("¿Cuántas iteraciones quieres hacer?: "))
PintarTablero(tablero, tableroNuevo)

for i in range(iteraciones):        
    tableroNuevo = Iterar(tablero)    
    print ("Iteración:", i+1)
    PintarTablero(tablero, tableroNuevo)
    tablero=tableroNuevo