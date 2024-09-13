try:
    #resultado = 5 / 0 # Except -> Finally
    resultado = 5 / 2 # Else -> Finally
except:
    print("Except")
else:#Agrupa de manera explícita el código que se ejecuta si no hay error en el bloque try
    print("Else")
finally:#Opcional
    print("Finally")