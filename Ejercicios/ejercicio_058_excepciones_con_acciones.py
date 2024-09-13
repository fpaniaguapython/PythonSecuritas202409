# Definir una clase abstracta SuperBaseException (hereda de Exception)
# - El constructor recibe un tipo de una enumeración Level (LOW, HIGHT)
# - Método abstracto es el metodo do_action 
#
# Programar dos clases concretas heredadas de SuperBaseException que implementen
# el método abstracto (tendrán algo del tipo print "Enviando correo..." o "Escribiendo log...").
#
# Definir una función cuya invocación tenga dos reglas de validación
# que lanzan las dos excepciones anteriores.
# 
# Llamar a la función, hacer que falle y en el except comprobar que la excepción
# es del tipo SuperBaseException y ejectuar la acción programada en do_action

import abc
from enum import Enum

class Level(Enum):
    LOW = 0
    HIGHT = 1

class SuperBaseException(BaseException):
    def __init__(self, level:Level, *args: object) -> None:
        super().__init__(*args)
        self.level = level
    
    @abc.abstractmethod
    def do_action(self):
        pass

class SBException1(SuperBaseException):
    def __init__(self, level: Level, *args: object) -> None:
        super().__init__(level, *args)

    def do_action(self):
        print("Enviando correo al administrador...")


class SBException2(SuperBaseException):
    def __init__(self, level: Level, *args: object) -> None:
        super().__init__(level, *args)

    def do_action(self):
        print("Destruir la información almacenada en los discos duros...")


def hacer_cosas(dato):
    if (type(dato)!=int):
        raise SBException1(Level.LOW)
    if (dato<0):
        raise SBException2(Level.HIGHT)
    

try:
    hacer_cosas("cosa")
except SuperBaseException as e:
    e.do_action()

try:
    hacer_cosas(-5)
except BaseException as be:
    if (isinstance(be, SuperBaseException)):
        be.do_action()