class Bicho(object):
    pass

class Engendro(Bicho):
    pass

class Orco(object):
    pass

class Cosa(Engendro, Orco):
    longevidad = 10
    def __init__(self) -> None:
        super().__init__()
        self.nombre="La cosa"
    def atacar(self):
        pass

cosa = Cosa()

#__name__
print(Cosa.__name__)#Cosa
#print(cosa.__name__)#Error (AttributeError)

#__class__
print(Cosa.__class__)#<class 'type'>
print(cosa.__class__)#<class '__main__.Cosa'>

#Función type (proporciona la misma información que __class__)
print(type(Cosa))#<class 'type'>
print(type(cosa))#<class '__main__.Cosa'>

#__bases__ --> Información sobre la herencia directa (los 'padres' de los que hereda directamente)
print(Cosa.__bases__)#(<class '__main__.Engendro'>, <class '__main__.Orco'>)
#print(cosa.__bases__)#Error (AttributeError)

#__dict__
print(Cosa.__dict__) #{'__module__': '__main__', 'longevidad': 10, '__init__': <function Cosa.__init__ at 0x0000020C2DC08EA0>, 'atacar': <function Cosa.atacar at 0x0000020C2DC08F40>, '__doc__': None}
print(cosa.__dict__) #{'nombre': 'La cosa'}