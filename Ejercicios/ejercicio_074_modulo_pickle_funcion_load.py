#Función load -> recupera objetos de un fichero
import pickle

with open('peliculas.store', 'rb') as fichero_peliculas:
    peliculas = pickle.load(fichero_peliculas)
    print("Películas:")
    print(peliculas)

with open('series.store', 'rb') as fichero_series:
    series = pickle.load(fichero_series)
    print("Series:")
    print(series)

with open('entretenimiento.store', 'rb') as fichero_entretenimiento:
    peliculas_ent = pickle.load(fichero_entretenimiento)
    series_ent = pickle.load(fichero_entretenimiento)
    print("Películas y series:")
    print(peliculas_ent)
    print(series_ent)