"""
Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.
"""

class Triangulo:
    def __init__(self, a, b, c):

        if not self.validar_triangulo(a,b,c):
            raise ValueError('Triangulo Inválido')

        self.a = a
        self.b = b
        self.c = c
        self.perimetro = a + b + c
        
        self.tipo_lado = None
        
        if a == b == c:
            self.tipo_lado = 'equilátero'
        
        elif a != b != c:
            self.tipo_lado = 'escaleno'
        
        else:
            self.tipo_lado = 'isósceles'

    def perimetro(self):
        return self.perimetro
    
    def tipo_lado(self):
        return self.tipo_lado
    

    @staticmethod
    def validar_triangulo(a, b, c):
        lados = [a,b,c]
        
        if any([l<=0 for l in lados]):
            return False
        
        if any([l > (sum(lados)-l) for l in lados]):
            return False

        return True