import json

menu = {'primero':'ensalada','segundo':'escalope','postre':'naranja'}

menu_str = json.dumps(menu)#Obtenemos un string con el contenido del diccionario-json

print(type(menu_str))
print(menu_str)
    