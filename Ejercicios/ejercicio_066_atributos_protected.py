class MyClass:
    def __init__(self, nombre, edad, salario) -> None:
        self.nombre = nombre #público
        self._edad = edad #'protected', sólo como notación, no tiene efectos restrictivos
        self.__salario = salario #'privado'


class MyClassChildren(MyClass):
    def __init__(self, nombre, edad, salario) -> None:
        super().__init__(nombre, edad, salario)

    def mostrar_edad(self):
        print(self._edad)

    def mostrar_salario(self):
        print(self.__salario)


mcc = MyClassChildren("Pedro", 30, 20_000)
mcc.mostrar_edad() #30
#mcc.mostrar_salario() #Error

class MyClassAnexa(object):
    def __init__(self, mcc : MyClassChildren) -> None:
        self.mcc = mcc

    def mostrar_edad_mcc(self):
        print(self.mcc._edad)

mca = MyClassAnexa(mcc)
mca.mostrar_edad_mcc() #30 -> OK pese a la notación del atributo _edad