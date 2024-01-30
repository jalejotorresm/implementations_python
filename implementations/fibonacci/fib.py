from implementations.fibonacci.secuencia import secuencia

def fib():
    numeros = secuencia()

    print(f"\nLos primeros {len(numeros)} numeros de la secuencia Fibonacci son: ")

    for i in range(2, len(numeros)):
        numeros[i] = numeros[i - 2] + numeros[i - 1]
    
    for i in range(len(numeros)):
        if i < (len(numeros) - 2):
            print(f"{numeros[i]}, ", end="")
        elif i == (len(numeros) - 2):
            print(f"{numeros[i]} y ", end="")
        else:
            print(f"{numeros[i]}.")

    print()