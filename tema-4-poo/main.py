from datetime import datetime

# Ejercicio 1
# Enunciado: Ejercicio de métodos de clases y estáticos
# Crear una clase inmueble con:
# 1. Cuatro atributos públicos: tipo(string), en_alquiler(bool), en_venta(bool),
# antigüedad_anuncio(int que representa los años de antigüedad).
# 2. Un método de clase que permita construir el objeto a partir del año de publicación del anuncio,
#  en vez del año de antigüedad.
# 3. Un método estático que devuelva True si el anuncio es un Fake o no.
# El método estático admite dos parámetros: Precio del anuncio y Precio del mercado,
# y el criterio será que si el precio_anuncio/precio_mercado < 0.6, entonces el anuncio es Falso.


class Inmueble:

    def __init__(self, tipo: str, en_alquiler: bool, en_venta: bool, antiguedad_anuncio: int):
        self.tipo = tipo
        self.en_alquiler = en_alquiler
        self.en_venta = en_venta
        self.antiguedad_anuncio = antiguedad_anuncio

    @classmethod
    def desdeAnoAnuncio(cls, tipo: str, en_alquiler: bool, en_venta: bool, anyo_anuncio: int):
        anyos_antiguedad = datetime.now().year - anyo_anuncio
        return cls(tipo, en_alquiler, en_venta, anyos_antiguedad)

    @staticmethod
    def es_fake(self, precio_anuncio: float, precio_mercado: float) -> bool:
        return precio_anuncio / precio_mercado < 0.6

    def __repr__(self):
        return f"Inmueble({self.tipo}, {self.en_alquiler}, {self.en_venta}, {self.antiguedad_anuncio})"

chalet = Inmueble.desdeAnoAnuncio("chalet", True, False, 2021)

piso = Inmueble("piso", False, True, 2020)

print(Inmueble.es_fake(piso,100000, 120000))

print(chalet.__repr__())

# Ejercicio 2
# Crear una clase Decorator que:
# 1. Ejecute la funcionalidad de una función simple, pero además indique el número de veces que se ha usado la función.

class Contador:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        if self.count > 1:
            print(f"Función {self.func.__name__} llamada {self.count} veces")
        else:
            print(f"Función {self.func.__name__} llamada {self.count} vez")

        return self.func(*args, **kwargs)

@Contador
def saludo():
    print("Hola")

saludo()
saludo()
saludo()

# Ejercicio 3
# Crear una clase Metaclase que:
# 1. Modifique los atributos públicos que se creen en las clases que lo usen, de forma que,
# lo deje todo en minúsculas salvo el primer carácter, y añada el sufijo _atr

class Metaclase(type):

    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in list(attrs.items()):
            if not attr_name.startswith('__'):
                attrs[attr_name.capitalize() + '_atr'] = attr_value
                del attrs[attr_name]
        return super().__new__(cls, name, bases, attrs)

class CocheJaguar(metaclass=Metaclase):

    marca = "Jaguar"
    modelo = "XF"


print(CocheJaguar.__dict__)