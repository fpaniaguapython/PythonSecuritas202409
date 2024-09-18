#Utilizado como 'calificador' de un argumento
def sumar(*numeros):
    print(type(numeros))#<class 'tuple'>
    print(numeros)#(1, 3, 5, 7)

sumar(1,3,5,7)

#Utilizandose como 'desempaquetador'
def restar(*numeros):
    print(type(numeros))#<class 'tuple'>
    print(numeros)#([11, 13, 17, 19],) Si no es usa el operador * en la llamada

numeros=(11,13,17,19)
restar(*numeros) #Transforma (11,13,17,19) (puede ser lista o tupla) en 11, 13, 17, 19


#Utilizandose como 'desempaquetador' recibiendo un diccionario
def multiplicar(*numeros):
    print(type(numeros))#<class 'tuple'>
    print(numeros)#('k1', 'k2', 'k3')

numeros={'k1':11,'k2':13,'k3':17}
#restar(*numeros) #('k1', 'k2', 'k3')
#restar(*numeros.items()) #(('k1', 11), ('k2', 13), ('k3', 17))
#restar(*numeros.keys()) #('k1', 'k2', 'k3')
restar(*numeros.values()) #(11, 13, 17)