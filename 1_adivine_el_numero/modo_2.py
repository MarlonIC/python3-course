import random

print("Introduzca el número a adivinar")
while True:
    numero = input("Introduzca un número entre 0 y 99: ")
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
            break

# PARTE 2
print("Intente adivinar el número")
while True:  # BUCLE 1
    while True:  # BUCLE 2
        intento = input("Introduzca un número entre 0 y 99: ")
        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break  # Bucle 2
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
        break  # Bucle 1
