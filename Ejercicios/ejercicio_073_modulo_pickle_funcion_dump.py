#Función dump -> Volcar un objeto en un fichero (binario)
import pickle

peliculas = dict()
peliculas['El Resplandor'] = {'director':'Kubrick', 'año':1980}
peliculas['Star Wars IV'] = {'director':'George Lucas', 'año':1977}

series = ['From', 'La Pareja Perfecta', 'Friends']

with open('peliculas.store', 'wb') as fichero_peliculas:
    pickle.dump(peliculas, fichero_peliculas)

with open('series.store', 'wb') as fichero_series:
    pickle.dump(series, fichero_series)

with open('entretenimiento.store', 'wb') as fichero_entretenimiento:
    pickle.dump(peliculas, fichero_entretenimiento)
    pickle.dump(series, fichero_entretenimiento)