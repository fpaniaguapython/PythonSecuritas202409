'''
En esta solución los métodos son abstractos
producen un error de tipo TypeError cuando seinstancia el objeto
de la clase derivada que no implementa todos los métodos
abstractos de la clase Enemigo
'''
import abc

class Enemigo(abc.ABC):
    def __init__(self, nombre, salud) -> None:
        super().__init__()
        self.nombre = nombre
        self.salud = salud
    @abc.abstractmethod
    def recibir_danyo(self, danyo):
        pass
    @abc.abstractmethod
    def morir(self):
        pass
    @abc.abstractmethod
    def desplazarse(self):
        pass

class Engendro(Enemigo):
    def __init__(self, nombre, salud) -> None:
        super().__init__(nombre, salud)
    def recibir_danyo(self, danyo):
        print(f'Recibiendo daño de {danyo}...')
        self.salud-=danyo
        print(f'A {self.nombre} le queda una salud de {self.salud}')
    def morir(self):
        print("Engendro muriendo...")
    def desplazarse(self):
        print("Engendro desplazándose...") 

class Orco(Enemigo):
    def __init__(self, nombre, salud) -> None:
        super().__init__(nombre, salud)
    def morir(self):
        print("Engendro muriendo...")
    def desplazarse(self):
        print("Engendro desplazándose...")  

engendro = Engendro("Engendro",100)
engendro.recibir_danyo(40)

orco = Orco("Orco",100) #En compilación, nos avisa que Orco no implementa el método recibir_danyo
orco.recibir_danyo(60)