# Ejercicio 1
# Crear una clase que implemente los siguientes métodos mágicos:
# __new__
# __init__
# __del__
# __repr__
# __str__
#
# Y a continuación, un objeto de la misma que los invoque.
from rich import print_json


class Profesion():

    def __new__(cls, *args, **kwargs):
        print(f" Se ha creado el objeto {cls.__name__}")
        return object.__new__(cls)

    def __init__(self, nombre: str, sueldo: float, descripcion: str, funciones: list):
        self.nombre = nombre
        self.sueldo = sueldo
        self.descripcion = descripcion
        self.funciones = funciones

    def __repr__(self):
        return f"Profesion(nombre={self.nombre}, sueldo={self.sueldo}, descripcion={self.descripcion}, funciones={self.funciones})"

    def __str__(self):
        return f"Profesion: {self.nombre}\n - Sueldo: {self.sueldo}\n - Descripcion: {self.descripcion}\n - Funciones: {", ".join(self.funciones)}"

    def __del__(self):
        print(f"Se ha eliminado la profesión {self.nombre}")

policia = Profesion("Policía", 1200, "Agentes de seguridad", ["arrestar", "cachear"])

bombero = Profesion("Bombreo", 1000, "Profesionales antiincendios y de rescate", ["apagar fuegos", "rescatar personas"])

print(policia)

print(bombero)

print(policia.__repr__())
print(bombero.__repr__())

# Ejercicio 2
# Crear una clase que implemente los métodos mágicos de comparación:
# __lt__
# __gt__
# __eq__
#
# Y a continuación, varios objetos de la misma que los invoquen a partir de los operadores respectivos.

class Profesion2():

    def __init__(self, nombre: str, sueldo: float, descripcion: str, funciones: list):
        self.nombre = nombre
        self.sueldo = sueldo
        self.descripcion = descripcion
        self.funciones = funciones

    def __repr__(self):
        return f"Profesion(nombre={self.nombre}, sueldo={self.sueldo}, descripcion={self.descripcion}, funciones={self.funciones})"

    def __str__(self):
        return f"Profesion: {self.nombre}\n - Sueldo: {self.sueldo}\n - Descripcion: {self.descripcion}\n - Funciones: {", ".join(self.funciones)}"

    def __del__(self):
        print(f"Se ha eliminado la profesión {self.nombre}")

    def __lt__(self, other):
        return self.sueldo < other.sueldo

    def __gt__(self, other):
        return self.sueldo > other.sueldo

    def __eq__(self, other):
        return self.sueldo == other.sueldo

policia = Profesion2("Policía", 1200, "Agentes de seguridad", ["arrestar", "cachear"])

bombero = Profesion2("Bombreo", 1000, "Profesionales antiincendios y de rescate", ["apagar fuegos", "rescatar personas"])

print(policia > bombero)
print(policia < bombero)
print(policia == bombero)

# Ejercicio 3
# Crear una clase que implemente los métodos mágicos:
# __bool__
# __call__
# __add__
# __sub__
#
# Y a continuación, varios objetos de la misma que los invoquen a partir de los operadores respectivos.

class Profesion3():

    def __init__(self, nombre: str, sueldo: float, descripcion: str, funciones: list):
        self.nombre = nombre
        self.sueldo = sueldo
        self.descripcion = descripcion
        self.funciones = funciones

    def __repr__(self):
        return f"Profesion(nombre={self.nombre}, sueldo={self.sueldo}, descripcion={self.descripcion}, funciones={self.funciones})"

    def __str__(self):
        return f"Profesion: {self.nombre}\n - Sueldo: {self.sueldo}\n - Descripcion: {self.descripcion}\n - Funciones: {", ".join(self.funciones)}"

    def __call__(self):
        print(self.__str__())

    def __bool__(self):
        # Para evaluar si cobra o no la profesión
        return self.sueldo > 0

    def __add__(self, other):
        self.sueldo = self.sueldo + other if isinstance(other, float) or isinstance(other, int) else self.sueldo + other.sueldo
        return self.sueldo + other if isinstance(other, float) or isinstance(other, int) else self.sueldo + other.sueldo

    def __sub__(self, other):
        self.sueldo = self.sueldo - other if isinstance(other, float) or isinstance(other, int) else self.sueldo - other.sueldo
        return self.sueldo - other if isinstance(other, float) or isinstance(other, int) else self.sueldo - other.sueldo

    def __del__(self):
        print(f"Se ha eliminado la profesión {self.nombre}")
        
policia = Profesion3("Policía", 1200, "Agentes de seguridad", ["arrestar", "cachear"])

becario = Profesion3("Becario", 0, "Personal en aprendizaje", ["aprender", "llevar cafés"])

policia()

becario()

if bool(becario):
    print("El becario cobra")
elif not bool(becario):
    print("El becario no cobra")

policia + becario

policia - 100

print(f"El policía cobra {policia.sueldo} tras su recorte de 100 euros")

