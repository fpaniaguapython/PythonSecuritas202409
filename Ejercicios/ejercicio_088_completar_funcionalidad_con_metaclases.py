def arrancar(self):
    print("Arrancando por defecto...")

class Motor(type):
    def __new__(mcs, name, bases, dictionary):
        if 'arrancar' not in dictionary:
            dictionary['arrancar'] = arrancar
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    
class MotorCombustion(metaclass=Motor):
    pass

class MotorElectrico(metaclass=Motor):
    def arrancar(self):
        print("Arrancando el motor eléctrico...")

mc = MotorCombustion()
me = MotorElectrico()

mc.arrancar()
me.arrancar()