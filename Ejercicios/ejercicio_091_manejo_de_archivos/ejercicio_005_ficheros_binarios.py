
#Abriendo el fichero en modo binario-lectura
#Comprobando que contiene el 'texto' PDF en los
#primeros bytes con el objetivo de determinar que
#es un fichero PDF
with open("binary_file.pdf",mode='rb') as fichero:
    cabecera = fichero.read(4).decode("utf-8")[1:]
    if (cabecera=='PDF'):
        print("Es un PDF")
    else:
        print("No es un PDF")
    