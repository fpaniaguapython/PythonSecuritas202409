#Excepciones posibles: FileNotFoundError, IOError, OSError

#Modos r(lectura), w(escritura), a(append), x(creación)
#Modos binarios: rb, wb, ab, xb
#Modos texto (por defecto): rt, wt, at, xt
#Modo r+: lectura y escritura.

#Modo por defecto es 'rt'
fichero = open("datos_fake.txt",mode='rt')
print(fichero.read())#Todo el fichero en una única cadena
#print(fichero.read(10))# #Modos r(l
#print(fichero.readline())# #Modos r(lectura), w(escritura), a(append), x(creaciÃ³n)
#print(fichero.readline().strip())# Con strip() eliminamos el salto de línea del final (espacios en blanco y saltos de línea en los dos extremos del string)
#print(fichero.readlines())#Una lista con todas las líneas del fichero
fichero.close()
'''
#Indicando el tipo de codificación utf-8
fichero = open("datos.txt",mode='rt',encoding='utf-8')
print(fichero.readline())# #Modos r(lectura), w(escritura), a(append), x(creación)
fichero.close()

#Con r+ leemos y escribimos
fichero = open("datos.txt",mode='r+',encoding='utf-8')
linea1 = fichero.readline()
linea2 = fichero.readline()
print(linea1, linea2, sep='')
fichero.write("Línea nueva")
fichero.close()

#Con w --> Truncar el fichero (elimina el contenido) y escribe
fichero = open("datos.txt",mode='w',encoding='utf-8')
fichero.write("Línea nueva creada por w")
fichero.close()

#Con w+ --> Truncar el fichero (elimina el contenido) y escribe
#Permite leer pero hay que utilizar seek
fichero = open("datos.txt",mode='w+',encoding='utf-8')
fichero.write("Creado por w+")
fichero.seek(0)
print("Leído:", fichero.readline())
fichero.close()
'''


