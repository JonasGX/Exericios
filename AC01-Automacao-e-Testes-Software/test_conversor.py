
"""
======== TDD (Test Driven Development) ========
- Primeiro se cria os testes depois o desenvolvimento do script

"""
from conversor import converte

# Converter esses numeros Romanos para numeros inteiros:
# I = 1 (um)
# V = 5 (cinco)
# X = 10 (dez)
# L = 50 (cinquenta)
# C = 100 (cem)
# D = 500 (quinhentos)
# M = 1000 (mil)



def test_deve_entender_simbolo_I():
    assert converte('I') ==  1

def test_deve_entender_simbolo_V():
    assert converte('V') ==  5

def test_deve_entender_simbolo_X():
    assert converte('X') ==  10

def test_deve_entender_simbolo_L():
    assert converte('L') ==  50

def test_deve_entender_simbolo_C():
    assert converte('C') ==  100

def test_deve_entender_simbolo_D():
    assert converte('D') ==  500

def test_deve_entender_simbolo_M():
    assert converte('M') ==  1000

def test_deve_entender_2_simbolos():
    assert converte('II') == 2