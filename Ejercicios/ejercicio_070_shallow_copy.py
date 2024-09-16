#*****************************
#Haciendo una shallow copy con slicing
#Un único nivel no genera problemas
#*****************************
lista1 = [10, 'texto', True]
lista2 = lista1[:]
print(lista1)#[10, 'texto', True]
print(lista2)#[10, 'texto', True]
print(id(lista1))#2219927867776
print(id(lista2))#2219927869632
print(lista1==lista2)#True
print(lista1 is lista2)#False
lista1[2]=False
print(lista1)#[10, 'texto', False] -> Se ha modificado
print(lista2)#[10, 'texto', True] -> No se ha modificado


#*****************************
#Haciendo una shallow copy con slicing
#Varios niveles generan 'problemas'
#*****************************
lista1 = [10, 'texto', True, [100,110]]
lista2 = lista1[:]
print(lista1)#[10, 'texto', True, [100, 110]]
print(lista2)#[10, 'texto', True, [100, 110]]
lista1[2]=False #Modificación de primer nivel
lista1[3][0]=200 #Modificación de segundo nivel
print(lista1)#[10, 'texto', False, [200, 110]] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True,  [200, 110]] #Se ha cambiado en el segundo nivel (porque es una referencia)



#*****************************
#Haciendo una shallow copy con la función copy del modulo copy
#Varios niveles generan 'problemas'
#*****************************
import copy

lista1 = [10, 'texto', True, [100,110]]
lista2 = copy.copy(lista1)
print(lista1)#[10, 'texto', True, [100, 110]]
print(lista2)#[10, 'texto', True, [100, 110]]
lista1[2]=False #Modificación de primer nivel
lista1[3][0]=200 #Modificación de segundo nivel
print(lista1)#[10, 'texto', False, [200, 110]] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True, [200, 110]] #Se ha cambiado en el segundo nivel (porque es una referencia)

#*****************************
#Haciendo una shallow copy con la funciones list, dict, tuple
#Varios niveles generan 'problemas'
#*****************************
lista1 = [10, 'texto', True, [100,110]]
lista2 = list(lista1)
print(lista1)#[10, 'texto', True, [100, 110]]
print(lista2)#[10, 'texto', True, [100, 110]]
lista1[2]=False #Modificación de primer nivel
lista1[3][0]=200 #Modificación de segundo nivel
print(lista1)#[10, 'texto', False, [200, 110]] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True, [200, 110]] #Se ha cambiado en el segundo nivel (porque es una referencia)

#*****************************
#Haciendo una shallow copy con slicing y objetos
#Varios niveles generan 'problemas'
#*****************************
class Pelicula(object):
    def __init__(self, titulo, director) -> None:
        self.titulo = titulo
        self.director = director
    def __repr__(self) -> str:
        return f'{self.titulo}:{self.director}'

lista1 = [10, 'texto', True, Pelicula("El Resplandor", "John Ford")]
lista2 = lista1[:]   
lista1[2]=False 
lista1[3].director="Kubrick"
print(lista1)#[10, 'texto', False, El Resplandor:Kubrick] #Se ha cambiado en el primer nivel y en el segundo
print(lista2)#[10, 'texto', True, El Resplandor:Kubrick] #Se ha cambiado en el segundo nivel (porque es una referencia)