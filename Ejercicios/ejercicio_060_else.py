dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

for dia in dias:
    pass
else: #Se ejecutará cuando el bucle for se complete
    print("Else del for")

contador = 0
while (contador<10):
    contador+=1
    if (contador==5):
        break #Provoca que se no ejecute el bloque else
else: #Se ejecutará cuando el bucle while se complete
    print("Else del while")