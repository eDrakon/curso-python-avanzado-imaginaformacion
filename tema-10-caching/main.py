import math
from functools import reduce
import math
import time
from functools import reduce, lru_cache


# Ejercicio 1 - Enunciado.
# Implementar una solución que calcule la suma de los factoriales de cada uno de los elementos de una lista de enteros.
# Realizar dos versiones, una usando reduce y otra sin reduce.
def suma_factoriales_sin_reduce(lista_enteros):
    suma_factoriales = 0

    for numero in lista_enteros:
        factorial_actual = math.factorial(numero)

        suma_factoriales += factorial_actual

    return suma_factoriales

mi_lista = [3, 4, 0]
start = time.time()
resultado_1 = suma_factoriales_sin_reduce(mi_lista)
end = time.time()
print(end - start)
print(f"Resultado sin reduce: {resultado_1}")

# Con reduce
def suma_factoriales_con_reduce(lista_enteros):
    factoriales = map(math.factorial, lista_enteros)
    suma_factoriales = reduce(lambda x, y: x + y, factoriales)

    return suma_factoriales

mi_lista = [3, 4, 0]
start = time.time()
resultado_2 = suma_factoriales_con_reduce(mi_lista)
end = time.time()
print(end - start)
print(f"Resultado con reduce: {resultado_2}")

# Ejercicio 2 - Enunciado
# Sobre las dos versiones anteriores aplicar una cache y calcular su rendimiento para 100 llamadas
# y un tamaño de la lista de 250 enteros.
# Verificar que la cache reduce más de un 90% el tiempo de ejecución,
# mientras que los resultados con reduce o sin reduce son similares.

@lru_cache(maxsize=None)
def factorial_cacheado(n):
    return math.factorial(n)

def suma_factoriales_cache_sin_reduce(lista_enteros):
    suma_factoriales = 0
    for numero in lista_enteros:
        suma_factoriales += factorial_cacheado(numero)
    return suma_factoriales

def suma_factoriales_cache_con_reduce(lista_enteros):
    factoriales = map(factorial_cacheado, lista_enteros)
    suma_factoriales = reduce(lambda x, y: x + y, factoriales)
    return suma_factoriales

mi_lista = [3, 4, 0]
start = time.time()
resultado_3 = suma_factoriales_cache_sin_reduce(mi_lista)
end = time.time()
print(end - start)
print(f"Resultado sin reduce: {resultado_3}")

mi_lista = [3, 4, 0]
start = time.time()
resultado_4 = suma_factoriales_cache_con_reduce(mi_lista)
end = time.time()
print(end - start)
print(f"Resultado con reduce: {resultado_4}")