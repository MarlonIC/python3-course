MIN = 0
MAX = 99


def pedir_numero(invitacion, minimo=MIN, maximo=MAX):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + " : "

    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except ValueError:
            pass
        else:
            if minimo <= entrada <= maximo:
                break

    return entrada


# PARTE 1
numero = pedir_numero("Introduzca el número a adivinar")

minimo = MIN
maximo = MAX
# PARTE 2
while True:
    intento = pedir_numero("Adivine el número", MIN, MAX)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
    else:
        print("¡Ha ganado!")
        break
