from coursera.usp.pt2_m3_exercicios import Triangulo

class TestTriangulo:
    def testa_triangulo_valido(self):
        assert Triangulo.validar_triangulo(200, 1, 2) == False
        assert Triangulo.validar_triangulo(1, 1, 1) == True
        assert Triangulo.validar_triangulo(0, 0, 0) == False
        assert Triangulo.validar_triangulo(-1, -1, -1) == False

