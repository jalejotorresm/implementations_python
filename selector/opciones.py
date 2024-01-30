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
            message="Selecciona la opcion que deseas explorar:",
            choices=opciones,
        )
    ]

    opcion = inquirer.prompt(menu)

    return opcion
