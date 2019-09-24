
#Ejemplo de clase
class Coche():
    #Constructor
    def __init__(self):
        #Propiedades
        self.__largoChasis=2500
        self.__anchoChasis=1200
        self.__ruedas = 4  #Poniendo los dos guiones bajos se consigue que la variable no sea modificable desde fuera de la clase
        self.__enMarcha = False
    
    #métodos
    def arrancar(self): #self es el this de VB.net. Hace referencia del propio objeto. Es obligatorio y siempre es el primer parámetro de los métodos
        self.__enMarcha= True

    def detener(self):
        self.__enMarcha=False

    def Estado(self):
        if self.__enMarcha==True:
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
miCoche = Coche()
print(miCoche.Estado())
print("Lo arranco")
miCoche.arrancar()
print(miCoche.Estado())
print("Lo paro")
miCoche.detener()
print(miCoche.Estado())

print("Mi coche tiene", miCoche._Coche__ruedas, "ruedas")
miCoche.__ruedas=2 #esto no modifica la propiedad "__ruedas"
print("Mi coche tiene", miCoche._Coche__ruedas, "ruedas")