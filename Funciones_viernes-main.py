from microbit import *


def ensalada():
    """Muestra en la pantalla la lista de frutas para la ensalada."""
    frutas = ["banana","manzana","frutillas","naranja"]
    display.scroll(str(frutas))

def juguera(fruta):
    """Recibo como parametro una fruta y muestra en pantalla su jugo."""
    display.scroll("Jugo de: "+fruta)

def puchero():
    """Muestra en la pantalla la lista de verduras para el puchero."""
    verduras = ["choclo", "boniato", "papa", "zanahoria", "zapallo", "nabo"]
    display.scroll(str(verduras))
    
def main():
    while True:
        if button_a.was_pressed():
            ensalada()
        if button_b.was_pressed():
            juguera("naranja")
        if accelerometer.was_gesture('shake'):
            puchero()

            

main()