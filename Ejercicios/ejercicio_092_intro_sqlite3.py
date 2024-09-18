import sqlite3
#Tipos: NULL, INTEGER, REAL, TEXT, BLOB

NOMBRE_BBDD = 'dpeliculas.sqlite'
MODELO_DE_DATOS = 'CREATE TABLE IF NOT EXISTS tpeliculas(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, director TEXT NOT NULL)'

class Pelicula:
    def __init__(self, titulo, director, id=0) -> None:
        self.id = id
        self.titulo = titulo
        self.director = director

class GestorPeliculasDB(object):
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

    def create(self, pelicula:Pelicula):
        cursor = self.conexion.cursor()
        cursor.execute(f"INSERT INTO tpeliculas (titulo, director) VALUES ('{pelicula.titulo}','{pelicula.director}')")
        self.conexion.commit()
        cursor.close()

    def readOne(self, id : int) -> Pelicula:
        cursor = self.conexion.cursor()
        pelicula = cursor.execute(f"SELECT * FROM tpeliculas WHERE id= {id}").fetchone()
        cursor.close()
        return pelicula
    
    def readAll(self) -> list:
        cursor = self.conexion.cursor()
        peliculas = cursor.execute(f"SELECT * FROM tpeliculas").fetchall()
        cursor.close()
        return peliculas
    
    def update(self, pelicula) -> None:
        cursor = self.conexion.cursor()
        cursor.execute(f"UPDATE  tpeliculas SET titulo=?, director=? WHERE id=?",(pelicula.titulo, pelicula.director, pelicula.id))
        self.conexion.commit()
        cursor.close()

    def delete(self, id) -> int:
        cursor = self.conexion.cursor()
        cursor.execute(f"DELETE from tpeliculas WHERE id=?",(id,))
        numero_borrados = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return numero_borrados
    
    def create_many(self, lista_tuplas_peliculas):
        cursor = self.conexion.cursor()
        cursor.executemany(f"INSERT INTO tpeliculas (titulo, director) VALUES (?,?)",lista_tuplas_peliculas)
        self.conexion.commit()
        cursor.close()
        

gestor = GestorPeliculasDB(NOMBRE_BBDD)
#gestor.create(Pelicula(titulo='Título 1', director='Director 1'))
#gestor.create(Pelicula(titulo='Título 2', director='Director 2'))
pelicula = gestor.readOne(2)
pelicula = Pelicula(id=pelicula[0],titulo=pelicula[1],director=pelicula[2])
pelicula.director=pelicula.director+"*"
gestor.update(pelicula)
peliculas = gestor.readAll()
print(peliculas)
'''
numero_borrados = gestor.delete(1)
if (numero_borrados==0):
    print("No se ha borrado ningún registro")
else:
    print(f'Se han borrado {numero_borrados} registros')
'''
peliculas = gestor.readAll()
print(peliculas)


'''
#Inserción múltiple de registros

p3 = Pelicula(titulo='Título 10', director='Director 10')
p4 = Pelicula(titulo='Título 11', director='Director 11')
p5 = Pelicula(titulo='Título 12', director='Director 12')

nuevas_peliculas = [p3, p4, p5]

lista_nuevas_peliculas = [(nueva_pelicula.titulo, nueva_pelicula.director) for nueva_pelicula in nuevas_peliculas]
gestor.create_many(lista_tuplas_peliculas=lista_nuevas_peliculas)
peliculas = gestor.readAll()
print(peliculas)
'''