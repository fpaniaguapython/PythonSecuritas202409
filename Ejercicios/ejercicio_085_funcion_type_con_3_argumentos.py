'''
type(x, y, z) --> Construir una clase
- x --> Nombre de la clase --> El valor de __name__
- y --> Tupla de las clases bases de las que hereda la clase --> El valor de __bases__
- z --> Diccionario con todos los atributos (variables y métodos de la clase)
'''

#Construcción más sencilla
Engendro = type('Engendro',(),{}) #Creando la clase Engendro
engendro = Engendro()
print(type(engendro))

#Construcción con variables y métodos
def avisar(self):
    print(f'Atención, los {self.duracion} minutos han terminado')

Alarma = type('Alarma',(object,),{'duracion':10,'avisar':avisar})
alarma1 = Alarma()
alarma1.duracion = 15
alarma1.avisar()