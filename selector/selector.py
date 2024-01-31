from implementations.fibonacci.fibonacci import fibonacci
from implementations.persona.persona import persona
from selector.opciones import mi_opcion

def menu_seleccion():
    final = mi_opcion()

    base = final["opcion"]

    programas = {
        "Calculo de Secuencia de Fibonacci":fibonacci,
        "Implementacion de Persona":persona,
        #"Conversor Decimal a Binario":binario(),
        #"Conversor Binario a Decimal":decimal(),
        #"Calculadora de Factoriales":factorial(),
    }

    if base in programas:
        programas[base]()
