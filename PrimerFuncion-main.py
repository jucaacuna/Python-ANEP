
from microbit import *


def juguera(fruta):
    jugo = "Jugo de: "+fruta
    return jugo

vaso = juguera("Naranja")
display.scroll(vaso)