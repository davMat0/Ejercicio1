import psutil


try:
    #Se recorre cada proceso que se esta ejecutando
    for proc in psutil.process_iter():

        processName = proc.name()
        processID = proc.pid

        print(processID, processName)

    #se solicta al usuario el pid del proceso que desea terminar
    pidUser = int(input("Introduce un PID para terminar "))

    #Se obtiene el proceso usando el pid indicado por el usuario
    proceso = psutil.Process(pidUser)
    #Termina el proceso
    proceso.terminate()

#Excepcion si el pid ingresado no existe
except psutil.NoSuchProcess:
    print("No se encontro el proceso con pid",pidUser)
#excepcion si no se tiene permisos suficentes para terminar el proceso
except psutil.AccessDenied:
    print("No se tiene los permisos suficientes para terminar con el proceso",proc.name())
#excepcion si el pid ingresado por el usuario no es valido
except ValueError:
    print("No es un numero PID valido")
