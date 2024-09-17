#Utilizando class, crear la clase Vehiculo que tiene el método arrancar (escribe 'Arrancando...')
#Utilizando type, crear una clase Automovil que herede de la clase Vehiculo
#Automovil tiene los atributos marca y modelo
#Automovil tiene el método mostrar_info (escribe marca y modelo)

class Vehiculo(object):
    def arrancar(self):
        print("Arrancando...")

def mostrar_info(self):
    print(f'Marca:{self.marca}. Modelo:{self.modelo}')

Automovil = type('Automovil',(Vehiculo,),{'marca':'Skoda','modelo':'Fabia','mostrar_info':mostrar_info})

automovil = Automovil()
print(Automovil.__bases__)
automovil.mostrar_info()
