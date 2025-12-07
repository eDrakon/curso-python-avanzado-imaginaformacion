import pytest
from main import get_pares, get_pares2, get_pares3
from unittest import mock


# Ejercicio 1
def test_ejercicio1_lista_enteros():
    lista_input = [1, 2, 3, 4, 5]
    lista_output = [2, 4]
    assert get_pares(lista_input) == lista_output

def test_ejercicio1_lista_vacia():
    lista_input = []
    lista_output = []
    assert get_pares(lista_input) == lista_output

# Ejercicio 2
@mock.patch('main.get_list_from_file')
def test_ejercicio2_mocks(mock_get_list):

    lista_falsa_del_fichero = [1, 10, 3, 22, 5, 8]
    mock_get_list.return_value = lista_falsa_del_fichero
    resultado_obtenido = get_pares2()

    lista_esperada = [10, 22, 8]

    assert resultado_obtenido == lista_esperada

    mock_get_list.assert_called_once()

# Ejercicio 3
@pytest.fixture
def lista_de_entrada():
    lst = []
    with open("input.txt", "r") as reader:
        for line in reader:
            lst.append(int(line.strip()))
    return lst

def test_ejercicio3(lista_de_entrada):
    datos_leidos = lista_de_entrada

    lst_output = get_pares(datos_leidos)

    lst_esperada = [2, 4, 6, 8, 10]

    assert lst_output == lst_esperada