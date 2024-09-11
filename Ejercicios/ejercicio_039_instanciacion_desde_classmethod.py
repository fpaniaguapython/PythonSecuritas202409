class Artefacto:
    def __init__(self, nombre):
        print("Construyendo con el constructor")
        self.nombre = nombre


    @classmethod
    def crear_artefacto(cls, nombre, danyo):#Devuelve una instancia de Artefacto
        print("Construyendo con el método de clase")
        artefacto = cls(nombre) #Instancia un objeto de la clase 'cls'
        artefacto.danyo = danyo #Agrega un nuevo atributo
        return artefacto


ballesta = Artefacto("Ballesta")
catapulta = Artefacto.crear_artefacto("Catapula",100) #Construyendo una instancia a través de un método de clase


print(ballesta.nombre)
print(catapulta.nombre, catapulta.danyo)
