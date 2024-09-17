import sqlite3
#Tipos: NULL, INTEGER, REAL, TEXT, BLOB

NOMBRE_BBDD = 'dpeliculas.sqlite'
MODELO_DE_DATOS = 'CREATE TABLE IF NOT EXISTS tpeliculas(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, director TEXT NOT NULL)'

class GestorDB(object):
    def __init__(self, nombre_db) -> None:
        print('Inicializador...')
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.__crear_modelo_de_datos()

    def __crear_modelo_de_datos(self):
        print("Creando el modelo de datos...")
        cursor = self.conexion.cursor()
        cursor.execute(MODELO_DE_DATOS)
        self.conexion.commit()
        cursor.close()

    def __del__(self):
        print('Eliminador...')
        self.conexion.close()


gestor = GestorDB(NOMBRE_BBDD)

