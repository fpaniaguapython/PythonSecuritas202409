class Cera:
    def derretir(self):
        print("Derritiendo cera")

class Queso:
    def derretir(self):
        print("Derritiendo queso")

class Madera:
    def quemar(self):
        print("Quemando madera")

elementos = [Cera(), Queso(), Madera()]

#Verificación de la existencia de un método en una lista de elementos heterogéneos
for elemento in elementos:
    try:
        elemento.derretir()
    except AttributeError:#Tipo de error que se produce al intentar acceder a un método no existente
        print("No podemos derretir eso")    

#Verificación de la existencia de un método en una lista de elementos heterogéneos
for elemento in elementos:
    if (hasattr(elemento, "derretir")):
        elemento.derretir()
    else:
        print("No podemos derretir eso") 


    