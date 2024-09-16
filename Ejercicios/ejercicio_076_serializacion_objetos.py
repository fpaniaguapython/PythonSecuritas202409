import pickle

class Pelicula(object):
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
    def mostrar_titulo(self):
        print(self.titulo)
    def mostrar_director(self):
        print(self.director)
    def __repr__(self) -> str:
        return f'{self.titulo}:{self.director}'
    def __str__(self) -> str:
        return f'{self.titulo}:{self.director}'

'''
#
#Serialización y escritura
#
peliculas = (Pelicula("El Resplandor", "Kubrick"),Pelicula("Alien", "Ridley Scott"))
with open("peliculas.pobj",'wb') as fichero:
    for pelicula in peliculas:        
        pickle.dump(pelicula, fichero)
'''

#Lectura y deserialización
with open("peliculas.pobj",'rb') as fichero:
    peli1 = pickle.load(fichero)
    peli2 = pickle.load(fichero)
print(peli1)
print(peli2)
peli1.mostrar_titulo()
peli1.mostrar_director()