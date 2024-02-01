import inquirer


def mi_opcion():
    opciones = [
        "Calculo de Secuencia de Fibonacci",
        "Implementacion de Persona",
        "Conversor Decimal a Binario",
        "Conversor Binario a Decimal",
        "Calculadora de Factoriales",
    ]

    menu = [
        inquirer.List(
            "opcion",
            "Selecciona la opcion que deseas explorar",
            opciones,
        )
    ]

    opcion = inquirer.prompt(menu)

    return opcion
