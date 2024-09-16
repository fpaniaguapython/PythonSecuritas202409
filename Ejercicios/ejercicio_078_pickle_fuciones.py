import pickle

def saludar():
    print("Hola")

'''
#Almacenamiento de función
with open('funcion_almacenada.fa','wb') as fichero:
    pickle.dump(saludar, fichero) #Se almacena únicamente el nombre de la función
'''

#Recuperación de función
with open('funcion_almacenada.fa','rb') as fichero:
    f = pickle.load(fichero)
    f()