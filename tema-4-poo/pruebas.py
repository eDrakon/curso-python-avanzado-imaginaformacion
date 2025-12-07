# class MiMetaclase(type):
#     def __new__(cls, clsname, bases, attrs):
#         uppercase_attrs = {
#             attr if attr.startswith("_") or callable(v) else 'app_' + attr.lower(): v
#             for attr, v in attrs.items()
#         }
#         return super().__new__(cls, clsname, bases, uppercase_attrs)
#
# class MiClase(metaclass=MiMetaclase):
#     atributo1 = "valor1"
#     _atributoPrivado = "valorPrivado"
#
#     @staticmethod
#     def saludar():
#         print("Hola")
#
#
# print(MiClase.__dict__)

from itertools import product

for i,j,k in product([0,1,2], [10,11,12], [3,4,5]):
    print(i,j,k)

'''
0 10 3
0 10 4
0 10 5
0 11 3
....
'''
