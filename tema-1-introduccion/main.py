try:
    from rich import print
    from rich.panel import Panel
    from rich.live import Live
    from rich.console import Group, Console
    from rich.table import Table
    from rich.prompt import Prompt
    rich_installed = True
except ImportError:
    rich_installed = False
from abc import ABC, abstractmethod
import os

def ejercicio_1():
    # Ejercicio 1
    # Ejercicio sobre control de flujos
    # 1 Pedir al usuario por consola que introduzca números enteros, para ello mostrar un mensaje donde se pida un número y tras pulsar enter se vuelva a pedir otro, y así hasta que el usuario pulse cero.
    # 2 Con los números introducidos, crear una lista de los que son primos, sin elementos duplicados y mostrarla por pantalla
    # Nota: Se considera un número primo aquel número entero que solo es divisible (resto cero) por sí mismo o por 1. Por ejemplo 1,2,3,5,7, etc...

    numeros_primos = set()
    numeros_usuario = []

    def bienvenida():
        if rich_installed:
            return Panel(
                "El usuario puede introducir varios números, para finalizar debe introducir 0."
                + " Al finalizar debe mostrar los números primos introducidos",
                title="[bold blue]Ejercicio 1 - Selector de números primos[/bold blue]",
                title_align="left",
                subtitle="[bold red]Erika Fernández Moreno[/bold red]",
                subtitle_align="right",
                width=100,
                border_style="orchid1",
                padding=(1, 4)
            )
        else:
            print("Ejercicio 1 - Selector de números primos, por Erika Fernández Moreno\n")
            print(
                "El usuario puede introducir varios números, para finalizar debe introducir 0."
                + "Al finalizar debe mostrar los números primos introducidos\n"
            )
            return None

    def es_un_entero(numero:str) -> tuple[bool, int]:
        try:
            num = int(numero)
            if num < 0:
                return False, 0
            else:
                return True, num
        except ValueError:
            return False, 0

    def es_primo(numero:int) -> bool:

        if numero == 1:
            return False

        for i in range(2, numero):
            if numero % i == 0:
                return False

        return True

    def main():

        if rich_installed:
            console = Console()
            console.clear()

            def generar_panel_numeros():

                contenido = ""

                if not numeros_usuario:
                    contenido = "[dim italic]Esperando números...[/dim italic]"
                else:
                    lineas = []

                    for num_u in numeros_usuario:
                        lineas.append(f"{num_u}")
                        contenido = ", ".join(lineas)

                return Panel(
                    contenido,
                    title=f"[bold blue]Números introducidos: {len(numeros_usuario)}[/bold blue]",
                    title_align="left",
                    width=100,
                    border_style="orchid1",
                    padding=(1, 4)
                )

            panel_bienvenida = bienvenida()
            console.print(panel_bienvenida)
            console.print(generar_panel_numeros())

            while True:
                num_usuario = Prompt.ask("\n[bold cyan]Introduce un número entero[/bold cyan] (0 para finalizar)")

                if num_usuario == "0":
                    break

                check, num = es_un_entero(num_usuario)
                if check:
                    numeros_usuario.append(num)
                    if es_primo(num):
                        numeros_primos.add(num)
                    console.clear()
                    console.print(panel_bienvenida)
                    console.print(generar_panel_numeros())
                else:
                    print(f"[red]✗ El valor '{num_usuario}' no es válido[/red]")

            if numeros_primos:
                primos_ordenados = sorted(numeros_primos)
                contenido_final = ", ".join([f"{num}" for num in primos_ordenados])
                console.clear()
                console.print(panel_bienvenida)
                console.print(generar_panel_numeros())
                console.print(Panel(
                    contenido_final,
                    title=f"[bold blue]Números primos encontrados: {len(numeros_primos)}[/bold blue]",
                    title_align="left",
                    border_style="orchid1",
                    width=100,
                    padding=(1, 2)
                ))
            elif not numeros_usuario:
                console.clear()
                console.print(panel_bienvenida)
                console.print(generar_panel_numeros())
                console.print(Panel(
                    "Vacío, no has introducido ningún número",
                    title=f"[bold blue]Resultado[/bold blue]",
                    title_align="left",
                    border_style="orchid1",
                    width=100,
                    padding=(1, 2)
                ))
            else:
                console.clear()
                console.print(panel_bienvenida)
                console.print(generar_panel_numeros())
                console.print(Panel(
                    "[orange]No se introdujeron números primos[/orange]",
                    title="[bold blue]Resultado[/bold blue]",
                    title_align="left",
                    border_style="orchid1",
                    width=100,
                    padding=(1, 2)
                ))

        else:

            bienvenida()

            while True:
                num_usuario = input("Introduce un número entero (0 para finalizar):")

                if num_usuario == "0":
                    break

                check, num = es_un_entero(num_usuario)
                if check:
                    if es_primo(num):
                        numeros_primos.add(num)
                else:
                    print(f"El valor {num_usuario} no es valido.")

            if numeros_primos:
                print("\nLos números primos introducidos son:")
                print(", ".join([str(num) for num in sorted(numeros_primos)]))
            elif not numeros_usuario:
                print("\nNo se ha introducido ningún número")
            else:
                print("\nSin primos encontrados en los números introducidos.")

    main()


def ejercicio_2():
    # Ejercicio de Programación Funcional.
    # A partir de los siguientes datos, calcular el peso medio del sexo masculino menores de edad.

    data = [
        {'nombre': 'Juan', 'edad': 20, 'sexo': 'M', 'peso': 60},
        {'nombre': 'Sergio', 'edad': 13, 'sexo': 'M', 'peso': 45},
        {'nombre': 'Ana', 'edad': 18, 'sexo': 'F', 'peso': 50},
        {'nombre': 'Alba', 'edad': 14, 'sexo': 'F', 'peso': 35},
        {'nombre': 'Leo', 'edad': 6, 'sexo': 'M', 'peso': 23},
        {'nombre': 'Evan', 'edad': 9, 'sexo': 'M', 'peso': 26}
    ]

    menores_masculinos = filter(lambda persona: persona['sexo'] == 'M' and persona['edad'] < 18, data)
    pesos_menores_masculinos = list(map(lambda persona: persona['peso'], menores_masculinos))
    peso_medio = sum(pesos_menores_masculinos) / len(pesos_menores_masculinos)

    print("\nPara los datos:\n")

    print(f"{'Nombre':<10} {'Edad':>6} {'Sexo':>6} {'Peso (kg)':>10}")
    print("-" * 40)

    # Datos
    for persona in data:
        print(f"{persona['nombre']:<10} {persona['edad']:>6} {persona['sexo']:>6} {persona['peso']:>10}")

    print(f"\nEl peso promedio del sexo masculino en los menores de edad es: {peso_medio:.2f} kg")


def ejercicio_3():

    class Coche(ABC):

        def __init__(self, marca: str, modelo: str):
            self.marca = marca
            self.modelo = modelo

        def __str__(self):
            return f"Marca: {self.marca}"

        @abstractmethod
        def gasto_cada_100km(self):
            pass

    class CocheElectrico(Coche):

        def __init__(self, marca: str, modelo: str, w_por_h: float, precio_w_por_h: float):
            super().__init__(marca, modelo)
            self.consumo_watios_hora = w_por_h
            self.precio_watio_hora = precio_w_por_h

        def gasto_cada_100km(self):
            gasto_100km = self.consumo_watios_hora * self.precio_watio_hora
            return round(gasto_100km, 2)

        def gasto_cada_100km_texto(self):
            return f"El gasto de este coche marca {self.marca} modelo {self.modelo} es de {self.gasto_cada_100km()} € cada 100Km"

    class CocheGasolina(Coche):

        def __init__(self, marca: str, modelo: str, consumo_litros_100km: float, precio_litro: float):
            super().__init__(marca, modelo)
            self.consumo_litros_100km = consumo_litros_100km
            self.precio_litro = precio_litro

        def gasto_cada_100km(self):
            gasto_100km = self.consumo_litros_100km * self.precio_litro
            return round(gasto_100km, 2)

        def gasto_cada_100km_texto(self):
            return f"El gasto de este coche marca {self.marca} modelo {self.modelo} es de {self.gasto_cada_100km()} € cada 100Km"


    coche_electrico = CocheElectrico("BYD", "seal", 120, 0.25)

    coche_gasolina = CocheGasolina("DODGE", "Charger", 100, 0.15)

    print()

    print(coche_electrico.gasto_cada_100km_texto())

    print(coche_gasolina.gasto_cada_100km_texto())


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":

    textos = {
        "bienvenida": "Te doy la bienvenida a los primeros ejercicios del tema 1",
        "autora": "Erika Fernández Moreno",
        "ejercicio1": {
            "titulo": "Ejercicio 1 - Identificador de números primos",
            "descripcion": "Este ejercicio solicita al usuario que introduzca números enteros positivos de forma consecutiva."
                           " El programa identifica cuáles son números primos, los almacena sin duplicados y,"
                           " al finalizar (cuando el usuario introduce 0), muestra la lista de números primos encontrados."
        },
        "ejercicio2": {
            "titulo": "Ejercicio 2 - Peso promedio",
            "descripcion": "Este ejercicio consiste en dentro de unos datos ya establecidos, buscar"
                           " los pesos de los menores de edad masculinos y calcular su peso medio."
        },
        "ejercicio3": {
            "titulo": "Ejercicio 3 - Clases de coches",
            "descripcion": "Este ejercicio consiste en crear clases para dos tipos de coches: un coche electrico y un coche gasolina."
                           " Estos dos tipos de coches, heredan de la clase padre coche y tiene un método abtracto"
                           " llamado gasto_cada_100km que retorna el gasto por cada 100km. En función del tipo de coche"
                           " se calcula de una forma diferente."
        },
        "selector": "Seleccione un ejercicio (1, 2, 3 o x para salir): "
    }

    def selector():

        seleccion_usuario = None

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