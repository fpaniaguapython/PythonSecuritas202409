class Animal:
    def __init__(self, nombre) -> None:
        print("Constructor 1")
        self.nombre = nombre
    
    def comer(self):
        print(f"El animal {self.nombre} está comiendo") #f-string

class Mamifero(Animal):
    def __init__(self, nombre="Desconocido", periodo_gestacion=5):
        super().__init__(nombre) #No es obligatorio invocar al constructor de la clase base
        print("Constructor 2")
        
    def comer(self):#Sobreescritura del método
        print(f'El mamífero {self.nombre} está comiendo')
        super().comer() #Llamada a la forma del método correspondiente a la clase base

m1 = Mamifero("Perro", 4)
m1.comer()

m2 = Mamifero()
m2.comer()   
