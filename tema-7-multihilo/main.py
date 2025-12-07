import concurrent.futures
import os
import requests as rq
import logging
import time
import math

# A partir del siguiente código:
# Ejercicio 1
#
# import requests as rq
# import logging
# import time
#
# formato_log = "%(asctime)s: %(message)s"
# logging.basicConfig(format=formato_log, level=logging.INFO,
#                     datefmt="%H:%M:%S")
#
# keywords = ['python'] * 100
#
# def lanzar_request(key):
#     url = (f'http://www.google.es/search?q={key}')
#     response = rq.get(url)
#     result = response.text[:1000]
#
# start = time.time()
#
# for key in keywords:
#     lanzar_request(key)
#
# end = time.time()
# logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')
# Realizar los cambios necesarios para reducir su tiempo de ejecución mediante la implementación de hilos.
if __name__ == '__main__':
    formato_log = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formato_log, level=logging.INFO,
                        datefmt="%H:%M:%S")

    keywords = ['python'] * 100

    def lanzar_request(key):
        url = (f'http://www.google.es/search?q={key}')
        response = rq.get(url)
        result = response.text[:1000]

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lanzar_request, keywords)

    end = time.time()
    logging.info(f'Ha tardado en ejecutarse: {end - start} segundos')

# Ejercicio 2
# A partir del siguiente código:

# import logging
# import time
# import math
#
# formato_log = "%(asctime)s: %(message)s"
# logging.basicConfig(format=formato_log, level=logging.INFO,
#                     datefmt="%H:%M:%S")
#
# def lanzar_formula(value):
#     result = pow(math.sqrt(value / pow(value,2)),3)
# start = time.time()
# for valor in range(1, int(1E7)):
#     lanzar_formula(valor)
#
# end = time.time()
# logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')
# Realizar los cambios necesarios para reducir su tiempo de ejecución mediante la implementación de procesos.

def lanzar_formula(value):
    result = pow(math.sqrt(value / pow(value, 2)), 3)
    return result

if __name__ == '__main__':
    start = time.time()
    formato_log = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formato_log, level=logging.INFO,
                        datefmt="%H:%M:%S")

    start = time.time()

    with concurrent.futures.ProcessPoolExecutor(os.cpu_count() -2) as executor:
        results = executor.map(lanzar_formula, range(1, int(1E7)), chunksize=1000)

    end = time.time()
    logging.info(f'Ha tardado en ejecutarse: {end - start} segundos')