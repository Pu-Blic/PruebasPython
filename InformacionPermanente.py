import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado uns persona con el nombre: "+self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    ListaPersonas=[]

    def __init__(self):
        ListadoPersonas=open("listaPersonas","ab+") #Abro el fichero para añadir en binario en lectura escritura
        ListadoPersonas.seek(0) #Me posiciono al principio del fichero

        try:
            self.ListaPersonas=pickle.load(ListadoPersonas)
            print("Se han cargado {} personas".format(len(self.ListaPersonas)))
        except:
            print("El fichero está vacío")
        finally:
            ListadoPersonas.close()
            del (ListadoPersonas)

    def AgregarPersona(self,persona):
        self.ListaPersonas.append(persona)
        self.GuardarPersonasEnFicheroExterno()
        
    def MostrarPersonas(self):
        for persona in self.ListaPersonas:
            print(persona)

    def GuardarPersonasEnFicheroExterno(self):
        ListadoPersonas=open("listaPersonas","wb") #Abro el fichero en modo escritura binaria
        pickle.dump(self.ListaPersonas,ListadoPersonas)
        ListadoPersonas.close()
        del (ListadoPersonas)

#hombre = Persona("Juan","Hombre","34")
#mujer= Persona("Sandra","Mujer","23")

l=ListaPersonas()
#l.AgregarPersona(hombre)
#l.AgregarPersona(mujer)
#l.AgregarPersona(Persona("Lucía","Mujer","6"))
#l.AgregarPersona(Persona("Rodrigo","Hombre","72"))
l.MostrarPersonas()

