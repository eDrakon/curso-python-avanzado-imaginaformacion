# Importamos reduce
from functools import reduce

# Definimos una lista con las cadenas para ahorrarnos tiempo
cadenas = ["Python", "", "AI", "Machine Learning", "GPT"]

# Primero creamos una función lambda asociada a una variable, esta función nos permite obtener la longitud de una cadena.
longitud_cadena = lambda cadena: len(cadena)

# La siguiente función devolvería 5, dado que es la longitud de elementos en la cadena "cadenas".
print(longitud_cadena(cadenas))

# Creamos una función que nos permita filtrar las cadenas con menos de tres caracteres o vacías usando filter, que itera
# cada elemento de la lista y solo devuelve aquellos que cumplan la sentencía evaluada en la función lambda.
def filtra_cadenas_cortas_o_vacias(lista_cadenas: list[str]) -> list[str]:
    return list(filter(lambda cadena: len(cadena) >= 3, cadenas))

# La siguiente función tras aplicar el filtro, devuelve la lista de cadenas sin las cadenas con una longitud menor a 3 o vacías
print(filtra_cadenas_cortas_o_vacias(cadenas))

# Creamos una lista para guardar las longitudes de las cadenas ya filtradas.
longitudes_cadenas_filtradas = list(map(longitud_cadena, filtra_cadenas_cortas_o_vacias(cadenas)))

# Para finalizar, con reduce, sumamos todas las longitudes de las cadenas filtradas guardadas en la lista.
print(reduce((lambda acc, longitud: acc + longitud), longitudes_cadenas_filtradas, 0))
# Está función devuelve 25, que es la suma de las longitudes de las cadenas una vez filtradas.