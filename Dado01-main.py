## Ejemplo de sucesos independientes. Extraccion con reemplazo
from microbit import *
from random import randint

sucesos = []


def LanzarDado():
    a = randint(1,6)
    sucesos.append(a)
    display.show(a)
    sleep(1000)
    display.clear()

def MostrarSucesos():
    display.scroll(str(sucesos))

    
while True:
    if button_a.is_pressed():
        LanzarDado()
    elif button_b.was_pressed():
        MostrarSucesos()





