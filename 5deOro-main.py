## Ejemplo de sucesos dependientes. Extraccion sin reemplazo.

from microbit import *
from random import randint

bolillero = list(range (1, 45))
ganadores = []


def ExtraerBola():
    while True:
        bola = randint(1, 45)
        if bola in bolillero:
            bolillero.remove(bola)
            return bola        
    

    
def main ():
    
    while True:
        display.show("#")
        sleep(1000)
        display.clear()
        sleep(1000)
        if button_a.was_pressed():
            ganadores.clear()
            i =0
            while ( i < 5):
                ganadores.append(ExtraerBola())
                i+=1
        elif button_b.was_pressed():
            display.scroll(str(ganadores))
            
    
main()
