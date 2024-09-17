#Manejo de ficheros simple con open-close
fichero = open("datos.txt","w")
fichero.write("Una prueba")
fichero.close()

#Manejo de ficheros simple con with (no requiere llamar al método close, se cierra 'solo')
with open("salida.txt","w") as archivo:
    archivo.write("Otra prueba")

