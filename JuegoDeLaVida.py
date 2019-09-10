#Cada célula tiene 8 células "vecinas"
#Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
#Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").

import random

def PintarTablero(tablero): 
    for i in range(len(tablero[0])):
        for j in range(len(tablero[1])):
            print(tablero[i][j],end="")                  
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
                if random.random()<0.7:                
                    tablero[i][j]="O"
                else:
                    tablero[i][j]="X"
            else:
                tablero[i][j]="■"
    return tablero

def Iterar(tablero):
    pass #A partir de aquí no se ejecuta
    filas=len(tablero[0])-2
    columnas=len(tablero[1])-2
    
    for fila in range(filas):
        print(tablero[fila+1])
        for columna in range(columnas):
            CelulasVivas=0
            CelulasVivas=ContarCelulasVivas(tablero, fila+1, columna+1)
            if CelulasVivas<2 or CelulasVivas>3:
                tablero[fila+1][columna+1]="X"
            elif CelulasVivas==3 and tablero[fila+1][columna+1] == "X":
                tablero[fila+1][columna+1] = "O"
                        
def ContarCelulasVivas(tablero, fila, columna):
    pass


print("***********************")
print("**El juego de la vida**")
print("***********************")
print("")

# Se crea e inicia el tablero del juego
tablero = IniciarTablero()
#iteraciones=int(input("¿Cuántas iteraciones quieres hacer?: "))

#for i in range(iteraciones):    
#    print ("Iteración: ",i+1)
    Iterar(tablero)
#    PintarTablero(tablero)

