from implementations.binario.set_decimal import set_decimal


def set_binario():
    array = set_decimal()

    base = array[0]
    numero = array[1]

    binario = ""

    while base > 0:
        digit = base % 2
        digit = str(digit)

        binario += digit
        base //= 2

    binario = binario[::-1]

    print(f"\nEl número {numero} convertido en binario es: " + binario + "\n")
