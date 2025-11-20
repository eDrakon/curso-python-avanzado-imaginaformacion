# Ejercicios tema 2 por Erika Fernández Moreno
try:
    from rich import print
    from rich.panel import Panel
    from rich.live import Live
    from rich.console import Group, Console
    from rich.table import Table
    from rich.prompt import Prompt
    rich_installed = True
except ImportError, :
    rich_installed = False
import os


def ejercicio_1():
    # Enunciado:
    # Usando una función generadora, calcular el producto de los números impares que hay del 1 al 20 incluidos.

    # El resultado debe ser:
    # 654729075

    def generador_impares(numero_maximo:int):
        for num in range(1, numero_maximo + 1, 2):
            yield num

    producto = 1
    for numero in generador_impares(20):
        producto *= numero

    print(producto)


def ejercicio_2():
    # Enunciado:
    # Usando una expresión generadora para calcular el iva y la siguiente lista de pagos:
    # pagos = [100, 200, 150, 300]
    # Calcular una nueva lista que contenga la suma de cada pago con su IVA correspondiente del 10%.

    pagos = [100, 200, 150, 300]

    iva = (x * 0.1 for x in pagos)

    total = list(map(sum, zip(pagos, iva)))

    print(" €, ".join(map(str, total)))


def ejercicio_3():
    # Enunciado:
    # Crear una clase que sea un iterador y devuelva los elementos de una lista en orden inverso a partir de la invocación de __next__()

    class InversorListas:

        def __init__(self, lista: list):
            self.lista = lista
            self.indice = len(lista) - 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.indice < 0:
                raise StopIteration

            valor = self.lista[self.indice]
            self.indice -= 1
            return valor

    lista = [1, 2, 3, 4, 5]

    inversor = InversorListas(lista)

    for valor in inversor:
        print(valor)


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":

    textos = {
        "bienvenida": "Te doy la bienvenida a los primeros ejercicios del tema 2",
        "autora": "Erika Fernández Moreno",
        "ejercicio1": {
            "titulo": "Ejercicio 1 - Función generadora",
            "descripcion": "Este ejercicio consiste en crear una función generadora que calcule el producto"
                           " de los números primos entre el 1 y el 20"
        },
        "ejercicio2": {
            "titulo": "Ejercicio 2 - Calculo IVA sobre lista",
            "descripcion": "Este ejercicio consiste en crear una función generadora que calcule el IVA del 10%"
                           " sobre los valores de una lista, y luego devolver la lista con el IVA aplicado."
        },
        "ejercicio3": {
            "titulo": "Ejercicio 3 - Clase iteradora",
            "descripcion": "Este ejercicio consiste en crear una clase que permite iterar una lista en orden inverso"
        },
        "selector": "Seleccione un ejercicio (1, 2, 3 o x para salir): "
    }

    def selector():

        for clave, valor in textos.items():
            if clave.startswith("ejercicio"):
                print(f"{valor['titulo']}\n{valor['descripcion']}\n")

        while True:
            seleccion_usuario = input(textos["selector"])

            if seleccion_usuario.upper() == "X":
                return seleccion_usuario

            if not seleccion_usuario.isnumeric():
                print("\nOpción invalida, seleciona entre los ejercicios con 1, 2 y 3, o x para salir")
                continue

            if 0 > int(seleccion_usuario) > 3:
                print("Opción invalida, el mayor ejercicio es 3")

            break

        return seleccion_usuario

    while True:

        limpiar_pantalla()

        if rich_installed:
            print(Panel(
                "Te doy la bienvenida a los primeros ejercicios del tema 1."
                "Acontinuación saldrá el selector de ejercicios para que puedas probarlos.",
                title="[bold blue]Tema 1 - Introducción[/bold blue]",
                title_align="left",
                subtitle="[bold red]Erika Fernández Moreno[/bold red]",
                subtitle_align="right",
                width=100,
                border_style="orchid1",
                padding=(1, 4)
            ))
        else:
            print(textos["bienvenida"])
            print(f"Por {textos['autora']}\n")

        ejercicio = selector()

        if ejercicio.upper() == "X":
            print("Saliendo del programa...")
            break

        if ejercicio == "1":
            ejercicio_1()
        elif ejercicio == "2":
            ejercicio_2()
        elif ejercicio == "3":
            ejercicio_3()

        input("Presione enter para continuar...")