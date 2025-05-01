
import pytest
from  coursera.usp.pt2_m3_exercicios import Triangulo


@pytest.mark.parametrize('a, b, c, is_triangulo',[(1, 1, 1, True),
                                                  (5, 4, 3, True),
                                                  (1, 1, -1, False),
                                                  (0, 0, 0, False),
                                                  (-5, -4, 3, False),
                                                  (5, 4, 0, False),
                                                  (5, 4, 200, False)])

def test_validar_triangulo(a, b, c, is_trigangulo):
    Triangulo._validar_triangulo(a,b,c) ==  is_trigangulo
      

