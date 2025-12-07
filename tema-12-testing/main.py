import pytest

# Ejercicio 1 - Enunciado.
# A partir de la siguiente función que devuelve los números pares de una lista:
# def get_pares(lst):
#     lst_result = []
#     for element in lst:
#         if element % 2 == 0:
#             lst_result.append(element)

#     return lst_result
# Crear un test unitario que verifique que el contenido de la lista devuelta sea igual al contenido de la lista esperada.
# Escoger la librería entre unittest o pytest.

# He preferido usar pytest

def get_pares(lst):
    lst_result = []
    for element in lst:
        if element % 2 == 0:
            lst_result.append(element)

    return lst_result

# Ejercicio 2 - Enunciado
# A partir de la siguiente función get_pares que devuelve los números pares de una lista,
# y cuya lista origen se obtiene a partir de un fichero con el método get_list_from_file:
def get_list_from_file():
    pass

def get_pares2():
    lst = get_list_from_file()
    lst_result = []
    for element in lst:
        if element % 2 == 0:
            lst_result.append(element)

    return lst_result

# Elaborar un test unitario que:
# 1.Use un Mock para sustituir la llamada al fichero.
# 2.Compruebe que la lista devuelta es igual que la de la lista esperada.

# Ejercicio 3
# A partir de la función get_pares:

def get_list_from_file():
    lst_data = []
    with open('input.txt','r') as reader:
        for element in reader:
            lst_data.append(int(element))
    return lst_data

def get_pares3(lst):
    lst_result = []
    for element in lst:
        if element % 2 == 0:
            lst_result.append(element)

    return lst_result

listado_numeros = get_list_from_file()
print(get_pares3(listado_numeros))

# Elaborar un test de integración que:
# 1.Que comprueba la integración entre el fichero de entrada de datos con el método
#  que devuelve los números pares de la lista obtenida por el fichero.
# 2.Se tiene que verificar que la lista devuelta es igual que la de la lista esperada.
