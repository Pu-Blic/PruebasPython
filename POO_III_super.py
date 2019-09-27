class Persona():
    def __init__(self, nombre, edad, poblacion):
        self.nombre=nombre
        self.edad=edad
        self.poblacion=poblacion

    def descripcion(self):
        print("Nombre:",self.nombre,"\nEdad:",self.edad,"\nPoblacion:",self.poblacion)

class Empleado(Persona):
    def __init__(self, nombre, edad, poblacion,salario, antigüedad):
        super().__init__(nombre, edad, poblacion)

        self.salario=salario
        self.antigüedad=antigüedad

    def descripcion(self):
        super().descripcion() #Llamamos al método descripción de la clase padre de Empleado
        print("Salario:",self.salario,"\nAntigüedad:",self.antigüedad)


print("Creo una persona")
print("----------------")
Antonio=Persona("Antonio",36,"Toledo")
Antonio.descripcion()

print("")
print("")

print("Creo un empleado")
print("****************")
Lopez=Empleado("López", 42,"Santander",1300,5)
Lopez.descripcion()

print("¿La clase lopez es instancia de Empleado?:",isinstance(Lopez,Empleado))
print("¿La clase lopez es instancia de Persona?:",isinstance(Lopez,Persona))

manuel=Persona("Manuel",3,"Bilbao")
print("¿La clase manuel es instancia de Empleado?:",isinstance(manuel,Empleado))
print("¿La clase manuel es instancia de Persona?:",isinstance(manuel,Persona))