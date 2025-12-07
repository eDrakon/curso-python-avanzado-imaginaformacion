# Ejercicio 1
# Enunciado. Ejercicio sobre Programación asíncrona
# A partir del siguiente código:

# import requests as rq
# import logging
# import time
#
# formato_log = "%(asctime)s: %(message)s"
# logging.basicConfig(format=formato_log, level=logging.INFO, datefmt="%H:%M:%S")
#
# keywords = ['python'] * 100
#
# def lanzar_request(key):
#     url = (f'http://www.google.es/search?q={key}')
#     response = rq.get(url)
#     result = response.text[:1000]
# start = time.time()
# for key in keywords:
#   lanzar_request(key)
#
# end = time.time()
# logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')
# Realizar los cambios necesarios para reducir su tiempo de ejecución mediante la implementación de tareas asíncronas
# usando la librería requests para las peticiones.

import asyncio
import aiohttp
import logging
import time

formato_log = "%(asctime)s: %(message)s"
logging.basicConfig(format=formato_log, level=logging.INFO, datefmt="%H:%M:%S")

keywords = ['python'] * 100
URL_BASE = 'http://www.google.es/search?q='


async def lanzar_request_async(session, key):
    url = f'{URL_BASE}{key}'
    try:
        async with session.get(url, timeout=10) as response:
            result = await response.text()
            return len(result[:1000])
    except aiohttp.ClientError as e:
        logging.error(f"Error en la peticion para {key}: {e}")
        return 0


async def main(keywords):
    async with aiohttp.ClientSession() as session:
        tareas = [lanzar_request_async(session, key) for key in keywords]
        await asyncio.gather(*tareas)


if __name__ == '__main__':
    start = time.time()

    asyncio.run(main(keywords))

    end = time.time()
    logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')

# Ejercicio 2
# Enunciado. Ejercicio sobre Programación asíncrona
# A partir del siguiente código:
#
# import requests as rq
# import logging
# import time
#
# formato_log = "%(asctime)s: %(message)s"
# logging.basicConfig(format=formato_log, level=logging.INFO, datefmt="%H:%M:%S")
#
# keywords = ['python'] * 100
#
# def lanzar_request(key):
#     url = (f'http://www.google.es/search?q={key}')
#     response = rq.get(url)
#     result = response.text[:1000]
#
#
# start = time.time()
# for key in keywords:
#     lanzar_request(key)
#
# end = time.time()
# logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')
# Realizar los cambios necesarios para reducir su tiempo de ejecución mediante la implementación de tareas
# asíncronas usando la librería aiohttp para las peticiones.

formato_log = "%(asctime)s: %(message)s"
logging.basicConfig(format=formato_log, level=logging.INFO, datefmt="%H:%M:%S")

keywords = ['python'] * 100
URL_BASE = 'http://www.google.es/search?q='


async def lanzar_request_async(session, key):
    url = f'{URL_BASE}{key}'
    try:
        async with session.get(url, timeout=10) as response:
            # await response.text() tambien es una operacion de I/O asincrona
            result = await response.text()
            return len(result[:1000])
    except aiohttp.ClientError as e:
        logging.error(f"Error en la peticion para {key}: {e}")
        return 0


async def main(keywords):
    async with aiohttp.ClientSession() as session:

        tareas = [lanzar_request_async(session, key) for key in keywords]

        await asyncio.gather(*tareas)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main(keywords))

    end = time.time()
    logging.info(f'Ha tardado en ejecutarse: {end-start} segundos')