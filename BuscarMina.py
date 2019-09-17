

def IniciarTablero(Tablero, Filas, Columnas):
    Tablero=[]
    for i in range(Filas):
        Tablero.append(["O"] * int(Columnas))

    return Tablero

def PintarTablero(tablero): 
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):            
            if tablero[i][j]=="O":
                print(tablero[i][j],end="")
            elif tablero[i][j]=="X":
                print(tablero[i][j],end="")
            else:
                print(tablero[i][j],end="")
        print("")

Tablero=[]
FilaEquis=1
ColumnaEquis=2
Coordenadas=""

Tablero=IniciarTablero(Tablero, 5,10)

Tablero[1][2]="X"

PintarTablero(Tablero)
Coordenadas=input("Introduce las coordenadas para localizar la mina. Formato(fila,columna): ")
Coordenadas=Coordenadas.split(",")
while FilaEquis!=int(Coordenadas[0]) and ColumnaEquis != int(Coordenadas[1]):
    print("Has fallado")
    Coordenadas=input("Introduce las coordenadas para localizar la mina. Formato(fila,columna): ")
    Coordenadas=Coordenadas.split(",")

print("Has acertado")