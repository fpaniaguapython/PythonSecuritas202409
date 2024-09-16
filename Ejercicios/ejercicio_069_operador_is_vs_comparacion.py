cadena1 = "El texto de la cadena 1" 
cadena2 = "El texto de la cadena 1" 

print(cadena1==cadena2)#True. Comparando es el contenido (el texto)
print(cadena1 is cadena2)#True. Comparando la identidad (el resultado de id())

lista1 = [10, 'MSI', True]
lista2 = lista1
print(lista1==lista2)#True
print(lista1 is lista2)#True

lista1 = [10, 'MSI', True]
lista2 = [10, 'MSI', True]
print(lista1==lista2)#True. Comparando es el contenido
print(lista1 is lista2)#False. Comparando la identidad (el resultado de id())
