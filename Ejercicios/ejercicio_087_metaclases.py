def arrancar(cls):
    print("Arrancando...")

#Definición de la metaclase
class Motor(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.cilindrada = 1_000 #Atributo de clase
        obj.arrancar = arrancar #Método de clase 
        return obj
    
class MotorCombustion(metaclass = Motor):
    def __init__(self) -> None:
        pass

motor1 = MotorCombustion()
print("Cilindrada de motor 1:", motor1.cilindrada)

motor2 = MotorCombustion()
print("Cilindrada de motor 2:", motor2.cilindrada)

motor1.cilindrada = 1200 #Agregando un atributo de instancia, cuyo nombre 'oculta' al atributo de clase
print("Cilindrada de motor 1:", motor1.cilindrada)#1200
print("Cilindrada de motor 2:", motor2.cilindrada)#1000

print(MotorCombustion.__dict__)#{'__module__': '__main__', '__init__': <function MotorCombustion.__init__ at 0x00000234F3C84EA0>, '__dict__': <attribute '__dict__' of 'MotorCombustion' objects>, '__weakref__': <attribute '__weakref__' of 'MotorCombustion' objects>, '__doc__': None, 'cilindrada': 1000, 'arrancar': <function arrancar at 0x00000234F39BA3E0>}
print(motor1.__dict__)#{'cilindrada': 1200}
print(motor2.__dict__)#{}



