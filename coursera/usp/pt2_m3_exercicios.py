"""
Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perímetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.
"""

class TrianguloInvalido(Exception):
    pass

class Triangulo:
    def __init__(self, a, b, c):
        
        Triangulo.validar_triangulo(a, b, c)
        
        self._a = a
        self._b = b
        self._c = c
        
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self,valor):
        Triangulo.validar_triangulo(valor, self._b, self._c)
        self._a = valor

    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, valor):
        Triangulo.validar_triangulo(self._a, valor, self._c)
        self._b = valor
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self,valor):
        Triangulo.validar_triangulo(self._a, self._b, valor)
        self._c = valor
    
    def perimetro(self):
        return sum([self.a, self.b, self.c])
    
    def tipo_lado(self):
        lados_unicos = len({l for l in [self.a, self.b, self.c]})
    
        if lados_unicos == 3:
            return 'escaleno'
        
        elif lados_unicos == 2:
            return 'isósceles'
        
        else:
            return 'equilátero'
    
    @staticmethod
    def validar_triangulo(a, b, c):
        lados = [a,b,c]
        
        if any([l > (sum(lados)-l) for l in lados]) or any((l<=0) for l in lados):
            raise TrianguloInvalido(f'Triângulo inválido para {a} {b} {c}')