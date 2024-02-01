import inquirer, re


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, eres {self.nombre} y tienes {self.edad} años de edad.\n")

    def set_data(self):
        question = [inquirer.Text("nombre", "Dime tu nombre")]
        nombre = inquirer.prompt(question)

        verificador = r"^[a-zA-ZÀ-ÿ\u00f1\u00d1]+$"

        while not (re.match(verificador, nombre["nombre"])):
            print()
            question = [
                inquirer.Text(
                    "nombre", "Informacion incorrecta. Dime tu nombre por favor"
                )
            ]
            nombre = inquirer.prompt(question)

        self.nombre = nombre["nombre"]

        print()

        question = [inquirer.Text("edad", "Dime tu edad")]
        edad = inquirer.prompt(question)

        verificador = r"^[0-9]+$"

        while not (re.match(verificador, edad["edad"])):
            print()
            question = [
                inquirer.Text("edad", "Informacion incorrecta. Dime tu edad por favor")
            ]
            edad = inquirer.prompt(question)

        self.edad = int(edad["edad"])

        print()

        self.saludar()
