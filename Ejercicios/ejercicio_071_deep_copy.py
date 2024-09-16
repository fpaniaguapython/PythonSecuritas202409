import copy

#*****************************
#función deepcopy del módulo copy para hacer hacer 'deep copy'
#*****************************
lista1 = [10, 'texto', True, [100,110]]
lista2 = copy.deepcopy(lista1)
print(lista1)#[10, 'texto', True, [100, 110]]
print(lista2)#[10, 'texto', True, [100, 110]]
lista1[2]=False #Modificación de primer nivel
lista1[3][0]=200 #Modificación de segundo nivel
print(lista1)#[10, 'texto', False, [200, 110]] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True, [100, 110]] #No se ha cambiado nada por ser una copia 'profunda'

#*****************************
#Haciendo una deep copy con copy.deepcopy
#*****************************
class Pelicula(object):
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
    def __repr__(self) -> str:
        return f'{self.titulo}:{self.director}'

lista1 = [10, 'texto', True, Pelicula("El Resplandor", "John Ford")]
lista2 = copy.deepcopy(lista1)   
lista1[2]=False 
lista1[3].director="Kubrick"
print(lista1)#[10, 'texto', False, El Resplandor:Kubrick] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True, El Resplandor:John Ford] #No ha cambiado nada