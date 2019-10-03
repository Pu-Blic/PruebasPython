import pickle

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

coche1=vehiculo("Nissan","Note")
coche2=vehiculo("For","Fiesta")
coche3=vehiculo("Renol","11")

#creo una colección 
coches=[coche1, coche2, coche3]

archivo = open("coches.bin","wb")
pickle.dump(coches,archivo)
archivo.close()
del (archivo)

#Leo el fichero
archivo=open("coches.bin","rb")
coches=pickle.load(archivo)
archivo.close()

for c in coches:
    print(c.Estado()) #Python sabe que el objeto c es un objeto de la clase vehículo.