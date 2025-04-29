from  coursera.usp.pt2_m3_exercicios import Triangulo

class TestTriangulo:
       
    def testa_validar_triangulo(self):
        assert Triangulo.validar_triangulo(5,4,3) == True
        assert Triangulo.validar_triangulo(0,0,0) == False
        assert Triangulo.validar_triangulo(-1,0,0) == False
        assert Triangulo.validar_triangulo(-1,0,2) == False
        assert Triangulo.validar_triangulo(5,4,-3) == False
        assert Triangulo.validar_triangulo(5,4,200) == False
      

