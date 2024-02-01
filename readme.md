# Coleccion de Programas con Python (Virtualenv)

Este es un proyecto pequeño que construi hace unas semanas para practicar mis conocimientos en el lenguaje de programacion Python.

A medida que vaya mejorando mis conocimientos en el lenguaje, se iran haciendo cambios en el repositorio, o se iran incluyendo mas proyectos pequeños.

## Ejecucion

Para ejecutar este proyecto de forma local, realiza los siguientes pasos:

Clona el proyecto:

```bash
  $ git clone https://github.com/jalejotorresm/implementations_python.git
```

Ubicate dentro del directorio del proyecto:

```bash
  $ cd my-project
```

Crea y activa el entorno virtual con virtualenv

```bash
   # Utilizando virtualenv
   $ virtualenv venv

   # Utilizando venv (a partir de Python 3.3)
   $ python3 -m venv venv

   # Activar venv en Windows
   $ venv\Scripts\activate

   # Activar venv en macOS y Linux
   $ source venv/bin/activate
```

Instala las dependencias necesarias

```bash
   $ pip install -r requirements.txt
```

Inicia el programa con python

```bash
  $ python main.py
```

Una vez en ejecucion, te recibira el siguiente menu principal:

```bash
------ Bienvenido a mi Coleccion de Miniprogramas en Python ------

? Selecciona la opcion que deseas explorar:
> Calculo de Secuencia de Fibonacci
  Implementacion de Persona
  Conversor Decimal a Binario
  Conversor Binario a Decimal
  Calculadora de Factoriales
```

Selecciona la opcion que mas te llame la atencion e interactua con el programa.

De momento para intentar otro programa debes repetir el procedimiento desde `python main.py`. La funcionalidad de retornar al menu principal esta en construccion y estara disponible pronto.

## Actualizaciones

A medida que mis conocimientos vayan avanzando, ire incluyendo nuevos miniprogramas o modificando la estructura del repositorio en si.

Por ese motivo, es posible que hayan versiones del proyecto que no coincidan en absoluto.

# Muchas gracias por tu visita y apoyo!
