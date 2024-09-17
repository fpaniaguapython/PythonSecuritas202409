import json

menu = {'primero':'ensalada','segundo':'escalope','postre':'naranja'}

with open('dmenu.json', mode="w") as fichero:
    json.dump(menu, fichero) #Escribe el objeto convertido a json en un fichero