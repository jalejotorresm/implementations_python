from implementations.fibonacci.fibonacci import fibonacci
from selector.opciones import mi_opcion

def menu_seleccion():
    final = mi_opcion()

    programas = {
        "Calculo de Secuencia de Fibonacci":fibonacci(),
        #"Implementacion de Persona":persona(),
        #"Conversor Decimal a Binario":binario(),
        #"Conversor Binario a Decimal":decimal(),
        #"Calculadora de Factoriales":factorial(),
    }

    for clave, valor in programas.items():
        if clave == final["opcion"]:
            valor