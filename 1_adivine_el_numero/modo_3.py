MIN = 0
MAX = 99


def pedir_numero(invitacion):
    invitacion += " entre " + str(MIN) + " y " + str(MAX) + ": "
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except ValueError:
            pass
        else:
            if MIN <= entrada <= MAX:
                break
    return entrada


# PARTE 1
numero = pedir_numero("Introduzca el numero a adivinar")

# PARTE 2
while True:
    intento = pedir_numero("Adivine el numero")
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
        break
