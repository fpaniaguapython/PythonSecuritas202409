from tarea import Tarea
from tarea_enviar_correo import CorreoTarea
from tarea_generar_pdf import GeneradorPDFTarea
from parametro import Parametro

def ejecutador(tareas : tuple[Tarea]) -> None:
    for tarea in tareas:
        if (isinstance(tarea, Tarea)):
            tarea.ejecutar()
        else:
            print("Hemos encontrado un grillo")

def mostrar_parametros(tareas : tuple[Tarea]) -> None:
    for tarea in tareas:
        if (isinstance(tarea, Tarea)):
            tarea.mostrar_parametros()
        else:
            print("Hemos encontrado un sapo")


if __name__=='__main__':
    parametros_t1 = (Parametro("email","destinatario1@hotmail.com"), Parametro("texto","Te invitamos a visitar nuestras oficinas"))
    t1 = CorreoTarea(nombre="Correo 1", parametros=parametros_t1)
    
    parametros_t2 = (Parametro("email","destinatario2@hotmail.com"), Parametro("texto","Debes recibir el paquete la próxima semana"))
    t2 = CorreoTarea(nombre="Correo 2", parametros=parametros_t2)
    
    parametros_t3 = (Parametro("nombre_fichero","factura001"), Parametro("importe","Importe de la factura 5000"))
    t3 = GeneradorPDFTarea(nombre="PDF 1", parametros=parametros_t3)
    
    tareas = (t1, "grillo 1", t2, t3)
       
    mostrar_parametros(tareas)
   
    ejecutador(tareas)