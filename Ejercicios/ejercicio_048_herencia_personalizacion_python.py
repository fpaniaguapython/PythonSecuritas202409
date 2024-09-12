#Lista
class MovieList(list): #list es una clase
    @staticmethod
    def check_type(obj):
        if (type(obj) is not Movie):
            raise TypeError("No es una película")
    
    def append(self, item):
        MovieList.check_type(item)
        super().append(item)

    def extend(self, items):
        for item in items:
            MovieList.check_type(item)
        super().extend(items)
   
#Movie  
class Movie:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director
    def __repr__(self) -> str:
        return f'{self.titulo}:{self.director}'

#La confirmación de que el método de chequeo funciona
#print(MovieList.check_type("dkd")) #TypeError
#print(MovieList.check_type(Movie("It", "Fred")))#OK

#La aplicación
lista_peliculas = MovieList() #Creación de una lista a través de la función list

lista_peliculas.append(Movie("It", "Fred"))
lista_peliculas.append(Movie("El Resplandor", "Kubrick"))
#lista_peliculas.append("Grillo") #Se detecta como que NO es del tipo Movie
print(lista_peliculas)

lista_peliculas_retro = list()
lista_peliculas_retro.append(Movie("Lo que el viento se llevó", "Director 1"))
lista_peliculas_retro.append(Movie("Casablanca", "Director 2"))
#lista_peliculas_retro.append("Sapo") #Se detecta como que NO es del tipo Movie
lista_peliculas.extend(lista_peliculas_retro)
print(lista_peliculas)