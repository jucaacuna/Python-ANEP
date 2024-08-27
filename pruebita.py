import random

##########################################
#                                        #
#               JUAN ACUÑA               #
#                                        #
##########################################
# Resolución a un ejercicio planteado por el Prof. Sebastián Dos Santos. En el marco del curso CC de DGES.



energia = 100
salud = 80
experiencia = 0 #cada 50 puntos sube de nivel
nivel = 1
pocionUsada = False
manzanaUsada = False

def mensaje_inicial():
    print ("Bienvenido al bosque encantado! Tu aventura comienza ahora")
    if(energia>=50):
        print("Estas listo para la aventura")
    else:
        print("Necesitas más energia antes de comenzar")


def verificar_estado():
    
    if(salud<=50):
        msj = "El aventurero sigue luchando"
    else:
        msj = "Aventurero caído"

    return msj

def descansar():
    global energia
    energia += 20
    global salud

def pelear(enemigo):
    global energia
    global salud
    if(enemigo == "goblin"):
        energia -= 30
        salud -= 10
    elif (enemigo == "troll"):
        energia -= 50
        salud -= 30
    verificar_estado()


def usar_objeto(objeto):
    global salud
    global pocionUsada
    global energia
    global manzanaUsada
    global pocionUsada
    if(objeto == "pocion de curacion"):
        if(pocionUsada == False):
            salud += 30
            pocionUsada = True
        else:
            print(f"El objeto{objeto} ya ha sido usado.")
    elif(objeto == "manzana"):
        if(manzanaUsada == False):
            energia += 10
            manzanaUsada = True
        else:
            print(f"El objeto{objeto} ya ha sido usado.")

def explorar():
    evento = random.randint(1,6)
    if (evento == 3):
        pelear("goblin")
    elif(evento == 5):
        pelear("troll")
    else:
        print("Aventura superada con éxito. Ganas 10p exp.")
        global experiencia
        global nivel
        experiencia += 10
        if (experiencia==50):
            experiencia = 0
            global nivel
            nivel += 1
        elif(experiencia>50):
            experiencia -= 50
            nivel += 1




def main():
    bandera = True
    while (bandera):
        print("\n #### BIENVENIDO AL GRAN JUEGO 11.8 ####")
        mensaje_inicial()

        print("\n0 - Finalizar juego (aburrido)")
        print("1 - Descansar ")
        print("2 - Explorar ")
        print("3 - Usar objeto ")
        print("4 - Estado de la partida")
        op = int(input("Elige una opción: "))

        match op:
            case 0:
                bandera = False
                print("\n A B U R R I D O")
                break
            case 1:
                descansar()
            case 2:
                explorar()
            case 3:
                o = input("¿manzana o pocion de curacion? ")
                usar_objeto(o)
            case 4:
                print(f" El jugador tiene: salud [{salud}], energía [{energia}] y esta en el nivel [{nivel}]")
            case _:
                print(f"Usted ingreso {op} y no es una opcion válida. Vuelva a intentarlo.")
        





main()