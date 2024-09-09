class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre


p1 = Persona("Manuel")

#Acceso de lectura al atributo
print(p1.nombre)
print(getattr(p1, 'nombre'))#Alternativa al acceso a través del objeto

#Acceso de modificación del atributo
p1.nombre = "Dolores" 
print(p1.nombre)
setattr(p1, "nombre", "Paula")#Alternativa al acceso a través del objeto
print(p1.nombre)

#Acceso a atributos o métodos inexistentes
#Tanto los atributos como los métodos inexistentes lanzan un AttributeError

#print(p1.email) #AttributeError
#p1.get_email() #AttributeError