import inquirer, re


def set_decimal():
    question = [inquirer.Text("numero", "Ingresa el número a convertir")]
    numero = inquirer.prompt(question)

    verificador = r"^[0-9]+$"

    while not (re.match(verificador, numero["numero"])):
        print()
        question = [
            inquirer.Text(
                "numero", "Informacion incorrecta. Ingresa un numero positivo por favor"
            )
        ]
        numero = inquirer.prompt(question)

    numero = int(numero["numero"])

    base = numero

    return [base, numero]
