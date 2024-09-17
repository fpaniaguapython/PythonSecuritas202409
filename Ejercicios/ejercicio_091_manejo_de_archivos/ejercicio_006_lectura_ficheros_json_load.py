import json

with open("pelicula.json") as fichero:#Apertura
    pelicula = json.load(fichero)#Lectura y carga del contenido del fichero como objeto json
    print(type(pelicula))#<class 'dict'>
    print(pelicula['Title'])
    print(pelicula['Ratings'][0]['Source'])
    print(pelicula['Ratings'][0]['Value'])
