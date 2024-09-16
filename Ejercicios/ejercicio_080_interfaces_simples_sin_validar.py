'''
En esta solución no se produce ningún error de ejecución
pero el método recibir_danyo de la clase Orco no realiza ninguna 
acción
'''

class Enemigo():
    def __init__(self, nombre, salud) -> None:
        super().__init__()
        self.nombre = nombre
        self.salud = salud
    def recibir_danyo(self, danyo):
        pass
    def morir(self):
        pass
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
if (isinstance(engendro, Enemigo)):
    engendro.recibir_danyo(40)

orco = Orco("Orco",100)
if (isinstance(engendro, Enemigo)):
    orco.recibir_danyo(60)