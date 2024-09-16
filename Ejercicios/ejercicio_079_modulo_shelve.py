import shelve

nombre_fichero = "repositorio_serializado"

'''
#Almacenamiento
fichero_diccionario = shelve.open(nombre_fichero, flag='c') #El flag se podría evitar ya que el valor 'c' es el valor por defecto

fichero_diccionario['tt0096895'] = {'titulo':'Batman','director':'Tim Burton'}
fichero_diccionario['tt0089755'] = {'titulo':'Memorias de África', 'director':'Sydney Pollack'}

fichero_diccionario.close()
'''

#Recuperación
diccionario_fichero = shelve.open(nombre_fichero, flag='r')
for k,v in diccionario_fichero.items():
    print(k, v)
print(diccionario_fichero['tt0089755'])
diccionario_fichero.close()
