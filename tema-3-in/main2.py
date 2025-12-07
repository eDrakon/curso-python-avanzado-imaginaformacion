class Contador:
    def __init__(self, valor=0):
        self.valor = valor

    def __iadd__(self, other):
        self.valor += other
        return self

    def __isub__(self, other):
        self.valor -= other
        return self

    def __str__(self):
        return f"Contador: {self.valor}"

    def __add__(self, other):
        self.valor + other
        return self

    def __sub__(self, other):
        self.valor - other
        return self

c = Contador(10)
c = c + 20
print(c)
c = c - 10
print(c)