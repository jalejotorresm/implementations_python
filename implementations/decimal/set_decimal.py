from implementations.decimal.set_binario import set_binario


def set_decimal():
    array = set_binario()

    base = array[0]
    base = base[::-1]
    numero = array[1]

    decimal = 0

    for i in range(len(base)):
        if base[i] == "0":
            continue

        pre_decimal = 2**i

        decimal += pre_decimal

    print(f"\nEl binario {numero} convertido a decimal es: {decimal}\n")
