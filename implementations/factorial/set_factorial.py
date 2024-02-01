from implementations.factorial.set_numero import set_numero


def set_factorial():
    numero = set_numero()

    resultado = 1

    for i in range(2, (numero + 1)):
        resultado *= i

    print(f"\nEl factorial de {numero} es: {resultado}\n")
