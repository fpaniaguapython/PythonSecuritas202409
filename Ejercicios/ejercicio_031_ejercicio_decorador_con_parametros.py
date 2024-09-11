#Decorador que escriba logs con el nombre de la función que se va a ejecutar y con los argumentos que recibe
#El decorador recibe un parámetro que indica si el LOG está en modo OFF, SHORT, FULL (enumeración)
#EL modo OFF no escribe; el modo SHORT escribe el nombre de la función; el modo FULL escribe nombre y argumentos 
from enum import Enum

class LogMode(Enum):
    OFF = 0
    SHORT = 1
    FULL = 2

LOG_MODE = LogMode.FULL

def xlogger(log_mode):
    def wrapper(funcion_a_decorar):
        def wrapper_interno(*args, **kwargs):
            if (log_mode==LogMode.SHORT):
                print(f'MYAPP-LOG-SHORT:{funcion_a_decorar.__name__}')
            elif (log_mode==LogMode.FULL):
                print(f'MYAPP-LOG-FULL:{funcion_a_decorar.__name__},{args},{kwargs}')
            funcion_a_decorar(*args, **kwargs)
        return wrapper_interno
    return wrapper

@xlogger(LOG_MODE)
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Raquel') #MYAPP-LOG-SHORT:saludar,('Raquel',),{}

@xlogger(LOG_MODE)
def despedir(nombre, apellido, estado_civil="Desconocido", edad=0):
    print(f'Despedir {nombre}')

despedir('Juan', "López", estado_civil="Soltero") #MYAPP-LOG-SHORT:despedir,('Juan', 'López'),{'estado_civil': 'Soltero'}