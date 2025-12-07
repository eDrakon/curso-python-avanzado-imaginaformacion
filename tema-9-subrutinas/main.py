# Ejercicio 1 - Enunciado.
# A partir de los siguientes datos:
# input_data = [{'nombre': 'Roberto', 'salario': 32000, 'sexo': 'M'},
#               {'nombre': 'Gema', 'salario': 28000, 'sexo': 'F'},
#               {'nombre': 'Ana', 'salario': 40000, 'sexo': 'F'},
#               {'nombre': 'Alba', 'salario': 20000, 'sexo': 'F'}]
# Calcular el salario medio de las mujeres cuyo nombre empieza por la letra a, usando listas de comprensión en vez de programación funcional.
input_data = [{'nombre': 'Roberto', 'salario': 32000, 'sexo': 'M'},
              {'nombre': 'Gema', 'salario': 28000, 'sexo': 'F'},
              {'nombre': 'Ana', 'salario': 40000, 'sexo': 'F'},
              {'nombre': 'Alba', 'salario': 20000, 'sexo': 'F'}]

salario_medio = sum(
    [
        persona['salario'] for persona in input_data if persona['sexo'] == 'F'
        and persona['nombre'].upper().startswith('A')]) / len([persona for persona in input_data if persona['sexo'] == 'F'
        and persona['nombre'].upper().startswith('A')
    ]
)

print(salario_medio)

# Ejercicio 2 - Enunciado.
# A partir de las siguientes puntuaciones de una partida de bolos de cuatro jugadores:
#
# input_data = [(10,5,23,8,12,6,11,9,21,4),
#               (11,15,13,18,2,4,1,29,21,14),
#               (1,15,3,28,22,4,1,9,1,2),
#               (13,15,13,8,2,24,1,19,12,24)]
# Calcular mediante programación funcional la puntuación obtenida por cada jugador.

input_data = [
    (10, 5, 23, 8, 12, 6, 11, 9, 21, 4),
    (11, 15, 13, 18, 2, 4, 1, 29, 21, 14),
    (1, 15, 3, 28, 22, 4, 1, 9, 1, 2),
]

puntuaciones = [sum(jugador) for jugador in input_data]

print(puntuaciones)

# Ejercicio 3 - Enunciado.
# A partir de este fichero de texto input.txt:
#
# contenido linea 1
# contenido linea 2
# contenido ultima linea
# Generar un fichero de salida output.txt a medida que se vaya leyendo cada línea del fichero input.txt.
# Se creará un gestor de contexto personalizado para gestionar ficheros de lectura.

from contextlib import contextmanager

path_input = 'input.txt'
path_output = 'output.txt'

@contextmanager
def cm_fichero_lectura(file_path):
    file = open(file_path, mode= 'r')
    try:
        yield file
    finally:
        file.close()


with cm_fichero_lectura(path_input) as file_reader:
    with open(path_output, "w") as file_writer:
        for line in file_reader:
            # Lectura y escritura simultánea
            file_writer.write(line)
