with open("datos_fake.txt",mode='rt',encoding='utf-8') as fichero:
    for linea in fichero: #Lee una línea y pasa al siguiente. Cuando encuentra EOF finaliza el for
        print(linea.strip())