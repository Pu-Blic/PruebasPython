#Se introducen número hasta "fin" y después se ordenan

def OrdenarTabla(tabla):
    for i in range(len(tabla)):
        for j in range(i,len(tabla)):
            pequeño=tabla[j]
            if tabla[j]<tabla[i]:
                aux=tabla[i]
                tabla[i]=tabla[j]
                tabla[j]=aux

    return tabla


tabla=[]

numero = input("Introduce un número a la lista. Escribe 'fin' para terminar: ")
while numero !="fin":
    tabla.append(int(numero))
    numero = input("Introduce un número a la lista. Escribe 'fin' para terminar: ")
    
print ("Esta es la lista de número:",tabla)
print ("Esta es la lista ordenada:" , OrdenarTabla(tabla))
