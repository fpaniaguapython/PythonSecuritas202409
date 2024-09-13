def sumar(s1, s2):
    if (s1<0 or s2<0):
        raise ValueError("Los sumandos deben ser positivos")
    resultado = s1 + s2
    return resultado

try:
    print("Comenzando la operativa")#Siempre
    resultado = sumar(3,-15)#Siempre
    print(resultado)#Solo si la línea anterior se ha ejecutado correctamente
except ValueError as ve:
    print("ValueError")
    print(ve)#Si hay un ValueError
except Exception as e:
    print("Exception")
    print(e)#Si hay un Exception
finally:#Opcional
    print("Fin del proceso")#Siempre

#OJO AL ORDEN DE LOS EXCEPT: en este caso SIEMPRE entra por el primer except (EXCEPTION)
try:
    print("Comenzando la operativa")#Siempre
    resultado = sumar(3,-15)#Siempre
    print(resultado)#Solo si la línea anterior se ha ejecutado correctamente
except Exception as e:
    print("Exception")
    print(e)#Si hay un Exception
except ValueError as ve:
    print("ValueError")
    print(ve)#Si hay un ValueError
finally:#Opcional
    print("Fin del proceso")#Siempre