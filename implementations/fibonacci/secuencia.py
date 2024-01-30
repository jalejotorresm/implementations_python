import re
import inquirer

def secuencia ():
    question = [inquirer.Text(name="input", message="Cuantos numeros de la secuencia quieres ver")]
    input = inquirer.prompt(question)

    verificador = r"^[0-9]+$"

    while not (re.match(verificador, input["input"])):
        print()
        question = [inquirer.Text(name="input", message="Informacion errada. Necesito un numero positivo para continuar")]
        input = inquirer.prompt(question)

    input = int(input["input"])

    numeros = []

    for i in range(input):
        numeros.append(1)
    
    return numeros