'''
En esta solución los métodos no sobreescribos en las clases derivadas
producen un error de tipo NotImplemented cuando se invoca al método no implementado
pero no se produce cuando se instancia el objeto
'''

class Enemigo():
    def __init__(self, nombre, salud) -> None:
        super().__init__()
        self.nombre = nombre
        self.salud = salud
    def recibir_danyo(self, danyo):
        raise NotImplementedError("El método recibir_danyo no está implementado")
    def morir(self):
        raise NotImplementedError("El método morir no está implementado")
    def desplazarse(self):
        raise NotImplementedError("El método desplazarse no está implementado")

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
if (isinstance(engendro, Enemigo)):
    engendro.recibir_danyo(40)

orco = Orco("Orco",100)
if (isinstance(engendro, Enemigo)):
    orco.recibir_danyo(60) #Se genera una excepción de tipo NotImplementedError