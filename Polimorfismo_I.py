class coche:
    def Mover(self):
        print("Me muevo usando 4 ruedas")


class moto:
    def Mover(self):
        print("Me muevo usando 2 ruedas")

class camion:
    def Mover(self):
        print("Me muevo usando 6 ruedas")

def MoverVehiuclo(vehiculo):
    vehiculo.Mover()


miMoto=moto()
miCoche=coche()
miCamion=camion()

MoverVehiuclo(miMoto)
MoverVehiuclo(miCoche)
MoverVehiuclo(miCamion)
