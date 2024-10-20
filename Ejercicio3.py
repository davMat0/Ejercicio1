import psutil

#Funcion que recorre todos los procesos en ejecucion y muestra la informacion de cada uno
def mostrar_procesos():
    for proc in psutil.process_iter():
        #se obtiene pid del proceso
        processPID = proc.pid
        #se obtiene nombre del proceso
        processName = proc.name()
        #se obtiene porcentaje de uso de cpu del proceso
        processCpu = proc.cpu_percent()
        #se obtiene porcentaje de uso de ram del proceso
        processMemory = proc.memory_percent()
        print(processPID,processName,processCpu,processMemory)

def main():
    continuar = True

    while continuar:
        #llama a la funcion que muestra los procesos
        mostrar_procesos()

        #se solicita al usuario si quiere continuar
        opcion = input("Presiona 'q' para salir o cualquier otra para refrescar: ")

        #se comprueba la elección del usuario
        if opcion.lower() == 'q':
            continuar = False

main()