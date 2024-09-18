import sqlite3
'''
1. Crear la base de datos
2. Crear la tabla
3. Crear el CREATE
4. Crear el READ
'''

#Crea la base de datos y establece la conexión
def database_creator(db_name):
    def wrapper_externo(metodo):
        def wrapper_interno(self, *args):
            print("Conectando a la base de datos...")
            self.conexion = sqlite3.connect(db_name)
            metodo(self, *args)
        return wrapper_interno
    return wrapper_externo

#Desconecta de la base de datos
def database_disconnect(metodo):
    def wrapper(self):
        print("Desconectando de la base de datos...")
        self.conexion.close()
        metodo(self)
    return wrapper

#Crea la tabla
def table_creator(metodo):
    def wrapper(self, *args):
        metodo(self, *args) #Es la llamada a __init__ y hay que hacerla al principio para disponer de los atributos a la hora de crear la tabla
        #Construyendo la estructura de la tabla
        table_name = self.__class__.__name__
        sentencia_creacion_tabla = f'CREATE TABLE IF NOT EXISTS {table_name}('
        for nombre_columna in self.__dict__.keys():
            if (nombre_columna=='conexion'): continue
            sentencia_creacion_tabla += f'{nombre_columna} TEXT,'
        sentencia_creacion_tabla = sentencia_creacion_tabla[:-1]#Quitamos la última coma
        sentencia_creacion_tabla+=')'
        print(sentencia_creacion_tabla)
        #Creando la tabla
        cursor = self.conexion.cursor()
        cursor.execute(sentencia_creacion_tabla)
        self.conexion.commit()
        cursor.close()
    return wrapper

#Crea (INSERT) el objeto en la persistencia
def storer(metodo):
    def wrapper(self, *args):
        metodo(self, *args)
        print("Guardando el registro...")
        table_name = self.__class__.__name__
        sentencia = f"INSERT INTO {table_name} ("
        for atributo in self.__dict__.keys():
            if (atributo=='conexion'): continue
            sentencia+=(atributo+',')
        sentencia=sentencia[:-1]
        sentencia+=') VALUES ('
        for k,v in self.__dict__.items():
            if (k=='conexion'): continue
            sentencia+=("'"+v+"',")
        sentencia=sentencia[:-1]
        sentencia+=')'
        print(sentencia)
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        self.conexion.commit()
        cursor.close()
        
    return wrapper

#Se encarga de guardar (UPDATE) el objeto cuando se modifica un atributo
def column(metodo):
    def wrapper(self, *args):
        metodo(self, *args)
        print("Construimos el UPDATE con los datos del objeto y lo guardamos...")
    return wrapper

class Pelicula:
    @storer
    @database_creator('peliculasdb.sqlite')
    @table_creator
    def __init__(self, titulo, director) -> None:
        self.__titulo = titulo
        self.__director = director

    def __str__(self):
        return f'{self.__titulo}:{self.__director}'
    
    @property
    def titulo(self):
        return self.__titulo
    
    
    @titulo.setter
    @column
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @database_disconnect
    def __del__(self):
        pass

p1 = Pelicula("Alien","Ridley Scott")
p2 = Pelicula("La maldición del escorpión de jade", "Woody Allen")
p1.titulo = "Cambio"

class Serie:
    @storer
    @database_creator('peliculasdb.sqlite')
    @table_creator
    def __init__(self, nombre, numero_temporadas) -> None:
        self.nombre = nombre
        self.numero_temporadas = numero_temporadas
    
    @database_disconnect
    def __del__(self):
        pass

s = Serie("From", "3")