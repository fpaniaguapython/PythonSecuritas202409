class Motor(type):
    metodos = ('arrancar','parar','acelerar')
    def __new__(mcs, name, bases, dictionary):
        errores = []
        for metodo in Motor.metodos:
            if metodo not in dictionary:
                errores.append(f'No se ha implementado el método {metodo}')
        if len(errores)>0:
            raise NotImplementedError(errores)
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    
class MotorCombustion(metaclass=Motor):
    def parar(self):
        print("Parando...")

#La mera definición de la clase produce un error ya que no cumple con las restricciones de la metaclase