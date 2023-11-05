from microbit import *
from random import randint




def tirarMoneda():
    """Esta funcion tira la moneda aleatoriamente"""
    moneda = randint(0,1)
    return moneda
    
     

def main():
    """Esta es la funcion principal del programa. Lleva un conteo de cuantas veces sale cada cara..."""
    moneda = -1
    caritas = 0
    numeritos = 0
    
    while True:
        display.show(Image.BUTTERFLY)
        if button_a.was_pressed():

            for x in range(0, 100):
                moneda = tirarMoneda()
                if moneda is 0:
                    caritas += 1
                elif moneda is 1:
                    numeritos += 1

            display.scroll("Caritas: "+str(caritas)+"  Numeros: "+str(numeritos))
        


main()
