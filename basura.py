# generadores

def suma(a, b):
    yield a + b

resultado = suma(1, 2)

resultado2 = suma(3, 3)

for i in resultado2:
    print(i)