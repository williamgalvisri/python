import random

def run():
    numero_aleatorio = random.randint(1, 10)
    numero_elegido = int(input("Elige un número del 1 al 10: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Elige un número más grande")
        elif numero_elegido > numero_aleatorio:
            print("Elige un número más grande") 
        numero_elegido =  int(input("Elige otro número: "))
    print("Juego terminado")


# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()