import inquirer, re


def set_numero():
    question = [inquirer.Text("input", "Dame un numero para calcular")]
    input = inquirer.prompt(question)

    verificador = r"^[0-9]+$"

    while not (re.match(verificador, input["input"])):
        print()
        question = [
            inquirer.Text(
                "input", "Respuesta errada. Dame un numero entero positivo por favor"
            )
        ]
        input = inquirer.prompt(question)

    numero = int(input["input"])

    return numero
