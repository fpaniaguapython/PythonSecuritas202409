class Artefacto:

    longevidad = 10 #Atributo de clase

    def __init__(self, nombre) -> None:
        self.nombre = nombre #Atributo de instancia

    def metodo_de_instancia(self):#Método de instancia
        print("***Método de instancia***")
        print(Artefacto.longevidad) #Ok
        print(self.nombre) #Ok
        print(self.longevidad) #Ok, pero no se debe (no tiene consecuencias)
        self.longevidad = 11 #No Ok, porque crear un atributo de instancia con el nombre del atributo de clase
        print("*",Artefacto.longevidad)
        print("*",self.longevidad)

    @classmethod #Este decorador es el que convierte al método en método de clase
    def metodo_de_clase(cls):#Método de clase
        print("***Método de clase***")
        print(Artefacto.longevidad) #Ok. 10
        print(cls.longevidad) #Ok. Ok
    
    @staticmethod
    def metodo_estatico():
        print("***Método estático***")
        print(Artefacto.longevidad) #Ok. 10
        #print(self.longevidad) #Ko
        #print(cls.longevidad) #Ko
        

artefacto = Artefacto("Catapulta")
artefacto.metodo_de_instancia()#Llamada al método de instancia
Artefacto.metodo_de_clase()#Llamada al método de clase
Artefacto.metodo_estatico()