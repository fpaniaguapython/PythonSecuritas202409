import logging

'''
CONSTANTES DE LEVEL SON:
CRITICAL    50
ERROR       40
WARNING     30
INFO        20
DEBUG       10
NOTSET       0
'''

def configurar_logger():
    #Establecer el nivel mínimo de log
    #logging.getLogger().setLevel(logging.ERROR)
    
    #Establecer la configuración del log
    logging.basicConfig(
        filename='log.txt',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.ERROR)



if __name__=='__main__':
    configurar_logger()

    logging.debug("Mensaje de Debug")
    logging.info("Mensaje de Info")
    logging.warning("Mensaje de Warning")
    logging.error("Mensaje de Error")
    logging.critical("Mensaje de Critical")
    logging.exception("Mensaje de Exception") #Tiene nivel ERROR

