import threading
import time

# proceso Usuario

cuenta = ["twee1", "tweet2", "tweet3", "tweet4", "tweet5"]

def iniciaLectura(cuenta):
    for i in cuenta:
        if i == cuenta[4]:
            print("Tweet Eliminado: ", cuenta.pop())
            time.sleep(6)
        i = +1

def terminarLectura(cuenta):
    for j in cuenta:
        print("Termina la lectura de un Tweet :", j)
        time.sleep(3)
    j = +1

terminarLectura(cuenta)
iniciaLectura(cuenta)

# proceso Seguidor

def iniciaEscritura(cuenta):
    for i in cuenta:
        if i == i:
            print("Se modifico el Tweet: ")
            i = print(i , "modificado")
            time.sleep(2)
    i = +1

def terminaEscritura(cuenta):
    for i in cuenta:
        if i == cuenta[3]:
            cuenta.append('tweet5')
            print("Termino la escritura de tweet: ", cuenta[4])
            time.sleep(4)
    i = +1

iniciaEscritura(cuenta)
terminaEscritura(cuenta)

# proceso contador 

def iniciaConteo(cuenta):
        print("los tweets de la cuenta son: ", cuenta)
        time.sleep(6)

def terminaConteo(cuenta):
    print("terminar conteo")
    time.sleep(5)


iniciaConteo(cuenta)
terminaConteo(cuenta)

hilo1 = threading.Thread(target= iniciaLectura, args=(cuenta,))
hilo2 = threading.Thread(target= terminarLectura, args=(cuenta,))
hilo3 = threading.Thread(target= iniciaEscritura, args=(cuenta,))
hilo4 = threading.Thread(target= terminaEscritura, args=(cuenta,))
hilo5 = threading.Thread(target= iniciaConteo, args=(cuenta,))
hilo6 = threading.Thread(target= terminaConteo, args=(cuenta,))


hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()