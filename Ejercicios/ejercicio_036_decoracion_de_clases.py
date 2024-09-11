def contador(clase):
    clase.atributos = clase.__getattribute__
    
    def detector(self, name):#Se va a 'disparar' cada vez que se acceda a un atributo de la clase
        if name=='kilometros':
            print("Se ha leído el kilometraje")#Sólo si se accede al atributo 'kilometros'
        return clase.atributos(self, name)

    clase.__getattribute__ = detector
    return clase

@contador
class Coche:
    def __init__(self, matricula):
        self.kilometros = 0
        self.matricula = matricula

coche = Coche('M-7797-HH')
print(coche.matricula)
print(coche.kilometros)

