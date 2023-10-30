from microbit import *
from random import randint

def tirarMoneda():
    """Esta funcion tira la moneda aleatoriamente"""
    moneda = randint(0,1)
    return moneda

def mostrarMoneda5p(a):
    """ESta funcion imprime la cara correspondiente de la moneda"""
    b= [Image.HAPPY,5]
    return b[a]

def main():
    """Esta es la funcion principal del programa. Lleva un conteo de cuantas veces sale cada cara..."""
    caritas = 0
    numeritos = 0
    while True:

        if accelerometer.was_gesture('shake'):
            moneda = tirarMoneda()
            if moneda is 0:
                caritas += 1
            elif moneda is 1:
                numeritos += 1
            moneda = mostrarMoneda5p(moneda)
            display.show(moneda)
        if button_a.was_pressed():
            display.scroll("Caras: "+str(caritas)+"  Numeros: "+str(numeritos))
    


main()
