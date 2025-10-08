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


def ejercicio_1():
    # Ejercicio 1
    # Ejercicio sobre control de flujos
    # 1 Pedir al usuario por consola que introduzca números enteros, para ello mostrar un mensaje donde se pida un número y tras pulsar enter se vuelva a pedir otro, y así hasta que el usuario pulse cero.
    # 2 Con los números introducidos, crear una lista de los que son primos, sin elementos duplicados y mostrarla por pantalla
    # Nota: Se considera un número primo aquel número entero que sólo es divisible (resto cero) por si mismo o por 1. Por ejemplo 1,2,3,5,7, etc...

    __numeros_primos = set()
    __numeros_usuario = []

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

    def es_un_entero(numero:int) -> (bool, int):
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

                if not __numeros_usuario:
                    contenido = "[dim italic]Esperando números...[/dim italic]"
                else:
                    lineas = []

                    for num in __numeros_usuario:
                        lineas.append(f"{num}")
                        contenido = ", ".join(lineas)

                return Panel(
                    contenido,
                    title=f"[bold blue]Números introducidos: {len(__numeros_usuario)}[/bold blue]",
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
                    __numeros_usuario.append(num)
                    if es_primo(num):
                        __numeros_primos.add(num)
                    console.clear()
                    console.print(panel_bienvenida)
                    console.print(generar_panel_numeros())
                else:
                    print(f"[red]✗ El valor '{num_usuario}' no es válido[/red]")

            if __numeros_primos:
                primos_ordenados = sorted(__numeros_primos)
                contenido_final = ", ".join([f"{num}" for num in primos_ordenados])
                console.clear()
                console.print(panel_bienvenida)
                console.print(generar_panel_numeros())
                console.print(Panel(
                    contenido_final,
                    title=f"[bold blue]Números primos encontrados: {len(__numeros_primos)}[/bold blue]",
                    title_align="left",
                    border_style="orchid1",
                    width=100,
                    padding=(1, 2)
                ))
            elif not __numeros_usuario:
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
                        __numeros_primos.add(num)
                else:
                    print(f"El valor {num_usuario} no es valido.")

            if __numeros_primos:
                print("\nLos números primos introducidos son:")
                print(", ".join([str(num) for num in sorted(__numeros_primos)]))
            elif not __numeros_usuario:
                print("\nNo se ha introducido ningún número")
            else:
                print("\nSin primos encontrados en los números introducidos.")

    main()

if __name__ == "__main__":
    ejercicio_1()