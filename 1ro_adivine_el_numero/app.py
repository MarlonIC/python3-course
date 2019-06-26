import random


if __name__ == '__main__':
    numero = random.randint(0, 100)
    intento = 0

    while True:
        numero_ingresado = int(input('Adivine el numero entre 0 y 99 incluidos: '))

        intento += 1
        if numero_ingresado > numero:
            print('Demasiado grande')
        elif numero_ingresado < numero:
            print('Demasiado pequeño')
        else:
            print('¡Ha ganado!')
            print('Numero de intentos:', intento)
            break

