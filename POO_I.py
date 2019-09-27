
#Ejemplo de clase
class Coche():
    #Constructor
    def __init__(self):
        #Propiedades
        self.__largoChasis=2500 #Poniendo los dos guiones bajos se encapsula la variable.
        self.__anchoChasis=1200 #Poniendo los dos guiones bajos se encapsula la variable.
        self.__ruedas = 4  #Poniendo los dos guiones bajos se encapsula la variable.
        self.__enMarcha = False #Poniendo los dos guiones bajos se encapsula la variable.
    
    #métodos
    def arrancar(self): #self es el this de VB.net. Hace referencia del propio objeto. Es obligatorio y siempre es el primer parámetro de los métodos
        if (self.__ChequeoInterno()==True):
            self.__enMarcha= True
        else:
            self.__enMarcha=False

    def detener(self):
        self.__enMarcha=False

    def Estado(self):
        if self.__enMarcha==True:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def __ChequeoInterno(self): #Este método está encapsulado.
        print("Realizando chequeo")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            print("Gasolina:",self.gasolina,". Aceite:",self.aceite, ". Puertas:",self.puertas,". El coche tiene:",self.__ruedas,"ruedas.")
            return True
        else:
            print("Gasolina:",self.gasolina,". Aceite:",self.aceite, ". Puertas:",self.puertas,". El coche tiene:",self.__ruedas,"ruedas.")
            return False

miCoche = Coche()
print(miCoche.Estado())
print("Lo arranco")
miCoche.arrancar()
print(miCoche.Estado())
print("Lo paro")
miCoche.detener()
print(miCoche.Estado())
