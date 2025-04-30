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
        
        
    def perimetro(self):
        return sum([self.a, self.b, self.c])
    
    def tipo_lado(self):
        count_lados_diferentes = len({l for l in [self.a, self.b, self.c]})
        
        if count_lados_diferentes == 3:
            return 'escaleno'
        
        elif count_lados_diferentes == 2:
            return 'isósceles'
        
        else:
            return 'equilátero'
    
    @staticmethod
    def _validar_triangulo(a, b, c):
        lados = [a,b,c]
        
        if any([l <= 0 for l in lados]):
            return False
        
        if any([l > (sum(lados)-l) for l in lados]):
            return False

        return True