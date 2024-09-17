with open("datos_salida.txt",mode='w',encoding='utf-8') as fichero:
    fichero.write("Texto 1") #No incluye saltos de línea
    fichero.write("Texto 2")


lineas = ['Texto 3', 'Texto 4']
with open("datos_salida.txt",mode='w',encoding='utf-8') as fichero:
    fichero.writelines(lineas)#No incluye saltos de línea




