import psutil

try:

    blocnotasIsRun = False

    #Se recorre cada proceso que se esta ejecutando
    for proc in psutil.process_iter():

        processName = proc.name()
        procesID = proc.pid

        print(procesID, processName)

        #Se verifica si el nombre del proceso es 'notepad.exe' (Bloc de notas)
        if processName.lower() == 'notepad.exe':
            blocnotasIsRun = True

    if blocnotasIsRun:
        print('Bloc de notas está en ejecución')

except:
    print("error")