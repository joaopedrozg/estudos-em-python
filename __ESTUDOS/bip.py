import time
import winsound

def monitorar(path):
    duration = 1000
    frequency = 2500
    ligado = False
    with open(path, 'r') as arq:
        while True:
            nova_linha = arq.readline()
            while nova_linha:
            #Isto para quando nova_linha == '', um valor Falso
            #isto é - quando não há mais linhas para serem lidas
                if 'N' in nova_linha:
                   ligado = True
                elif 'FF' in nova_linha:
                   ligado = False
                yield nova_linha
                nova_linha = arq.readline()
            if ligado:
                winsound.Beep(2500, 1000)
