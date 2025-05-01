
import pytest
from  coursera.usp.pt2_m3_exercicios import Triangulo, TrianguloInvalido

@pytest.fixture
def t():
    return Triangulo(5,4,3)
    

@pytest.mark.parametrize('a, b, c',[(1, 1, -1),
                                    (0, 0, 0),
                                    (-5, -4, 3),
                                    (5, 4, 0),
                                    (5, 4, -3),
                                    (5, 4, 200)])
def test_triangulo_invalido(a, b, c):
    with pytest.raises(TrianguloInvalido):
        Triangulo.validar_triangulo(a,b,c)
      

def test_triangulo_perimetro(t):
    assert t.perimetro() == 12

@pytest.mark.parametrize('a,b,c,tipo_lado', [(5,5,5,'equilátero'),
                                             (5,4,3,'escaleno'),
                                             (3,3,4,'isósceles')])
def test_triangulo_tipo_lado(a,b,c,tipo_lado):
    assert Triangulo(a,b,c).tipo_lado() == tipo_lado

def test_a(t):
    assert t.a == 5

def test_b(t):
    assert t.b == 4

def test_c(t):
    assert t.c == 3

def test_change_a(t):
    t.a = 3
    assert t.a == 3