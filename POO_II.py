class vehiculo():
    def __init__(self, Marca, Modelo):
        self.Marca=Marca
        self.Modelo=Modelo
        self.enMarcha=False
        self.Acelerar=False
        self.Frenar=False        

    def Arrancar(self):
        self.enMarcha=True

    def Acelerar(self):
        self.Acelerar=True

    def Frenar(self):
        self.Frenar=True

    def Estado(self):
        print("Marca:",self.Marca,"\nModelo:",self.Modelo,"\nEn Marcha:",self.enMarcha,"\nAcelerar:",self.Acelerar,"\nFrenar:",self.Frenar)

class VehiculoElectrico(vehiculo):
    Autonomia=0
    def __init__(self):
        self.Autonomia=100

    def CargarEnergia(self):
        self.Cargando=True

class moto(vehiculo):
   HaciendoCaballito=""

   def Caballito():
       HaciendoCaballito="Voy haciendo el caballito"

   def Estado(self):  #método sobreescrito
        print("Marca:",self.Marca,"\nModelo:",self.Modelo,"\nEn Marcha:",self.enMarcha,"\nAcelerar:",self.Acelerar,"\nFrenar:",self.Frenar,
              "\n¿Haciendo caballito?",self.HaciendoCaballito)

class furgoneta(vehiculo):
    def Cargar(self,carga):
        self.cargado=carga
        if self.cargado==True:
            return"La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class BicicletaElectrica(vehiculo,VehiculoElectrico): #Herencia múltiple. Se da preferencia, en cuanto al constructor, a la primera de los argumentos.
    def Estado(self):
        print("Marca:",self.Marca,"\nModelo:",self.Modelo,"\nEn Marcha:",self.enMarcha,"\nAcelerar:",self.Acelerar,"\nFrenar:",self.Frenar)
        print("Autonomía:",self.Autonomia)

        

miMoto=moto("Honda","CBR")
miMoto.Estado()

print("Creo una furgoneta")
print("------------------")
miFurgoneta=furgoneta("Mercedes","Ni idea")
miFurgoneta.Estado()
print(miFurgoneta.Cargar(True))

print("Creo una Bicicleta Electrica")
print("------------------")
miBiciElectrica=BicicletaElectrica("orbea","O344")
miBiciElectrica.Autonomia=150
miBiciElectrica.Estado()