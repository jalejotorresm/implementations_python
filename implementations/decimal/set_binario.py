import inquirer, re

def set_binario():
    question = [inquirer.Text("input", "Ingresa el número a convertir")]
    input = inquirer.prompt(question)

    verificador = r"^[01]+$"

    while not (re.match(verificador, input["input"])):
        print()
        question = [inquirer.Text("input", "Informacion errada. Dame un numero binario valido por favor")]
        input = inquirer.prompt(question)

    pre_base = input["input"]
    base = pre_base[:]

    return [pre_base, base]