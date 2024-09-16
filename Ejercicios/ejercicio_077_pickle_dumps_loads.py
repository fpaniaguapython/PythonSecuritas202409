import pickle

#función dumps como alternativa a dump para generar la versión 'bytes' del objeto sin almacenar en fichero

class Pelicula(object):
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
    def mostrar_titulo(self):
        print(self.titulo)
    def mostrar_director(self):
        print(self.director)

alien = Pelicula("Alien", "Ridley Scott")

alien_b = pickle.dumps(alien)#Se obtiene un 'array de bytes' del objeto
print(type(alien)) #<class '__main__.Pelicula'>
print(type(alien_b)) #<class 'bytes'>

pelicula = pickle.loads(alien_b) #A partir del 'array de bytes' se restaura el objeto
pelicula.mostrar_titulo() #Alien