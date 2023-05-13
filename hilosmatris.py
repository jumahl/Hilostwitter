import threading
from random import randint

n = 5
matris1=()
matris2=()
resultado=()



def creamatris1(matris1):
    print("Primera matris:")

def dfnmatris1(matris1):
    matris1= [[randint(1,50) for j in range(n)] for i in range(n)]
    print(matris1)

creamatris1(matris1)
dfnmatris1(dfnmatris1)    
  
def creamatris2(matris2):
    print("segunda matris:")

def dfnmatris2(matris2):
    matris2= [[randint(1,50) for j in range(n)] for i in range(n)]
    print(matris2)

creamatris2(matris2)
dfnmatris2(dfnmatris2)

def crearesultado(resultado):       
    print("Resultado de la multiplicacion")
    

def resuelve(resultado):
    resultado = [[0 for j in range(n)] for i in range(n)]

    for x in range(len(dfnmatris1)):
        for y in range(len(dfnmatris2[0])):
            for z in range(len(dfnmatris2)):
                resultado[x][y] += dfnmatris1[x][z] * dfnmatris2[z][y]

    for r in resultado:
        print(r)

crearesultado(resultado)
resuelve(resultado)

hilo1 = threading.Thread(target= creamatris1, args=(matris1,))
hilo2 = threading.Thread(target= dfnmatris1, args=(matris1,))
hilo3 = threading.Thread(target= creamatris2, args=(matris2,))
hilo4 = threading.Thread(target= dfnmatris2, args=(matris2,))
hilo5 = threading.Thread(target= crearesultado, args=(resultado,))
hilo6 = threading.Thread(target= resuelve, args=(resultado,))


hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()

