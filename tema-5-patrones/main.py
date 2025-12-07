from datetime import datetime
import time
from abc import ABCMeta, abstractmethod


# Ejercicio 1
# Ejercicio con el patrón Command
# Diseñar una posible solución de clases a través del patrón Command que permita gestionar
# diferentes acciones entre una Persona y un Altavoz inteligente.
# Se deben poder registrar un historial de las peticiones y repetir las n ultimas.

class Altavoz:

    @staticmethod
    def reproducir(audio: str):
        print(f"Reproduciendo la canción {audio}")

    @staticmethod
    def pausar():
        print("Pausado el audio")

class Persona:

    def __init__(self):
        self._commands = {}
        self._history = []

    def mostrar_historial(self):
        for row in self._history:
            print(
                f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')}"
                f" : {row[1]}"
            )

    def registrar(self, command_name, command):
        self._commands[command_name] = command

    def ejecutar(self, command_name, attr = None):
        if command_name in self._commands.keys():
            if attr:
                self._commands[command_name].execute(attr)
                self._history.append((time.time(), (command_name, attr)))
            else:
                self._commands[command_name].execute()
                self._history.append((time.time(), (command_name)))
        else:
            print(f"El comando [{command_name}] no reconocido")

    def repetir_ultimo(self, number_of_commands):
        commands = self._history[-number_of_commands:]
        for command in commands:
            if isinstance(command[1], tuple) and len(command[1]) == 2:
                self._commands[command[1][0]].execute(command[1][1])
            else:
                self._commands[command[1]].execute()

"La interfaz Mando, tendrá los comandos implementados"
from abc import ABCMeta, abstractmethod

class IPersona(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute():
        """Un objeto comando, implementa la interfaz IMando y corre el comando designado por el receiver"""

class AltavozCommand1(IPersona):
    def __init__(self, altavoz):
        self._altavoz = altavoz

    def execute(self, audio: str):
        self._altavoz.reproducir(audio)

class AltavozCommand2(IPersona):
    def __init__(self, altavoz):
        self._altavoz = altavoz

    def execute(self):
        self._altavoz.pausar()

# Crear a receiver
Altavoz = Altavoz()

# Crear Comandos
COMANDO_1 = AltavozCommand1(Altavoz)
COMANDO_2 = AltavozCommand2(Altavoz)

persona = Persona()

persona.registrar("reproducir", COMANDO_1)
persona.registrar("pausar", COMANDO_2)

persona.ejecutar("reproducir", "Apaty Host")
persona.ejecutar("pausar", None)

persona.repetir_ultimo(2)

#Ejercicio 2
# Ejercicio con el patrón Facade
# Diseñar una posible solución de clases a través del patrón Facade que permita aglutinar
# todas las acciones que son necesarias para pasar de:
# Ropa sucia a ropa seca y planchada.
# Teniendo como actores, una persona y una lavadora-secadora.

class Persona:

    def recoger_ropa(self):
        return "Persona->Recoge la ropa"

    def introducir_ropa_lavadora(self):
        return "Persona->Introduce ropa en la lavadora"

    def encender_lavadora(self):
        return "Persona->Enciende la lavadora"

    def sacar_ropa_lavadora(self):
        return "Persona->Saca ropa la lavadora"

    def apagar_lavadora(self):
        return "Persona->Apaga la lavadora"


class LavadoraSecadora:

    def lava_ropa(self):
        return "LavadoraSecadora->Lava la ropa"

    def centrifuga_ropa(self):
        return "LavadoraSecadora->Centrifuga la ropa"

    def seca_ropa(self):
        return "LavadoraSecadora->Seca la ropa"


# facade
class Facade:

    def __init__(self):
        self.persona = Persona()
        self.lavaseca = LavadoraSecadora()

    def lavar_ropa(self):
        self.persona.recoger_ropa()
        self.persona.introducir_ropa_lavadora()
        self.lavaseca.lava_ropa()
        self.lavaseca.centrifuga_ropa()
        self.lavaseca.seca_ropa()
        self.persona.apagar_lavadora()
        self.persona.sacar_ropa_lavadora()

        print('Ropa Limpia y Seca')


FACADE = Facade()
RESULT = FACADE.lavar_ropa()

# Ejercicio 3
# Enunciado: Ejercicio con el patrón Factory
# Diseñar una posible solución de clases a través del patrón Factory que permita gestionar
# las diferentes fuentes de entrada de información a un sistema. Inicialmente se contemplan:
# Ficheros de texto locales.
# Texto procedente de peticiones HTTP a un endpoint.

class IOrigen(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self, *args):
        pass

# Clase Fichero
class Origen(IOrigen):
    def __init__(self, id_fichero, path_fichero = 'None', url_request = ''):

        self.id_fichero = id_fichero
        self.path_fichero = path_fichero
        self.url_request= url_request

    def get_info(self, lector):
        lector.iniciar_objeto('fichero', self.id_fichero)
        lector.aniadir_atrituto('path', self.path_fichero)
        lector.aniadir_atrituto('url', self.url_request)
        lector.procesar_extraer_info()


class ISource(metaclass=ABCMeta):

    @abstractmethod
    def iniciar_objeto(self,*args):
        pass

    @abstractmethod
    def aniadir_atrituto(self,*args):
        pass

    @abstractmethod
    def procesar_extraer_info(self):
        pass


class FILESource(ISource):

    def __init__(self):
        self._obj = None

    def iniciar_objeto(self, nombre_objeto, id_objeto):
        self._obj = {'id': id_objeto}

    def aniadir_atrituto(self, clave, valor):
        self._obj[clave] = valor

    def procesar_extraer_info(self):
        print('procesada info de FILE')


class HTTPSource(ISource):

    def __init__(self):
        self._obj = None

    def iniciar_objeto(self, nombre_objeto, id_objeto):
        self._obj = {'id': id_objeto}

    def aniadir_atrituto(self, clave, valor):
        self._obj[clave] = valor

    def procesar_extraer_info(self):
        print('procesada info de FILE')


class HTTPSource(ISource):

    def __init__(self):
        self._obj = None

    def iniciar_objeto(self, nombre_objeto, id_objeto):
        self._obj = {'id': id_objeto}

    def aniadir_atrituto(self, clave, valor):
        self._obj[clave] = valor

    def procesar_extraer_info(self):
        print('procesada info de REQUEST')


class SourceFactory:

    def __init__(self):
        self._creadores = {}

    def registrar_source(self, formato, creador):
        self._creadores[formato] = creador

    def get_source(self, formato):
        creador = self._creadores[formato]
        if not creador:
            raise ValueError(formato)
        return creador()


class ObjectoSource:
    def extractInfo(self, origen, format):
        obj_extractor = factory.get_source(format)
        origen.get_info(obj_extractor)

factory = SourceFactory()
factory.registrar_source('fichero_local', FILESource)
factory.registrar_source('request', HTTPSource)

origen1 = Origen(1, path_fichero='../info.txt')
origen2 = Origen(2, url_request='https://pokeapi.co/api/v2/pokemon/ditto')

objeto_source = ObjectoSource()
objeto_source.extractInfo(origen1, 'fichero_local')
objeto_source.extractInfo(origen2, 'request')