#Decorador que escriba logs con el nombre de la función que se va a ejecutar y con los argumentos que recibe
#El decorador recibe un parámetro que indica si el LOG está en modo OFF, SHORT, FULL (enumeración)
#EL modo OFF no escribe; el modo SHORT escribe el nombre de la función; el modo FULL escribe nombre y argumentos 
from enum import Enum
import time

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

def xtimer(funcion_a_decorar):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion_a_decorar(*args, **kwargs)
        fin = time.time()
        print(f'La ejecución de {funcion_a_decorar.__name__} ha tardado {fin-inicio}ms')
    return wrapper

@xtimer
@xlogger(LOG_MODE)
def despedir(nombre, apellido, estado_civil="Desconocido", edad=0):
    time.sleep(2)
    print(f'Despedir {nombre}')

despedir('Juan', "López", estado_civil="Soltero") #MYAPP-LOG-SHORT:despedir,('Juan', 'López'),{'estado_civil': 'Soltero'}

#Atención a los nombres de función en el log, porque dependen del orden de los decoradores

#Poniendo los decoradores en el orden @xlogger->@xtimer, la salida es la siguiente: 
#MYAPP-LOG-FULL:wrapper,('Juan', 'López'),{'estado_civil': 'Soltero'}
#Despedir Juan
#La ejecución de despedir ha tardado 2.0013492107391357ms

#Poniendo los decoradores en el orden @xtimer->@xlogger, la salida es la siguiente: 
#MYAPP-LOG-FULL:despedir,('Juan', 'López'),{'estado_civil': 'Soltero'}
#Despedir Juan
#La ejecución de wrapper_interno ha tardado 2.002272367477417ms