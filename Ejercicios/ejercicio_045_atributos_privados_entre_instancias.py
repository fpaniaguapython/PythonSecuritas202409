class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre
    def curiosear(self, cliente):
        print(cliente.__nombre)
    

class Empleado:
    def curiosear(self, cliente):
        print(cliente.__nombre)

c1 = Cliente("Leonardo")
c2 = Cliente("Aurora")

e1 = Empleado()

#e1.curiosear(c1)#KO. Attribute Error
c1.curiosear(c1)#OK. Leonardo
c1.curiosear(c2)#OK. Aurora --> Entre instancias de la misma clase se pueden ver los atributos privados

