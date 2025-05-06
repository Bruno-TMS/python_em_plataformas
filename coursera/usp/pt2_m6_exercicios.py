"""
Exercício 1: Soma dos elementos de uma lista
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
"""
def soma_lista(lista:list):
    if len(lista)<=1:
        return lista.pop()
    
    else:
        return lista.pop() + soma_lista(lista)
"""

Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
"""

def encontra_impares(lista):
    if not lista:
        return []
    
    impares = []
    if lista[0] % 2 != 0:
        impares.append(lista[0])
    
    impares.extend(encontra_impares(lista[1:]))
    return impares


"""
Exercício 3: Elefantes
Este exercício tem duas partes:

Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. Essa função deve ser implementada utilizando recursão.

Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no singular ("Um elefante..."); para os demais, utilize números e o plural ("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+". Lembre-se também que é possível transformar números em strings com a função str().

Dica: Será que neste caso a base da recursão é diferente de 
n
=
=
1
n==1n, equals, equals, 1?

No exemplo de execução abaixo, note que há uma diferença entre como a string é e como ela é interpretada. Na função print o símbolo "\n" é interpretado como quebra de linha
"""


def incomodam(n):
    # Verifica se n não é um inteiro ou não é estritamente positivo
    if not isinstance(n, int) or n <= 0:
        return ""
    # Caso base: quando n == 1, retorna "incomodam "
    if n == 1:
        return "incomodam "
    # Caso recursivo: retorna "incomodam " seguido da chamada para n-1
    return "incomodam " + incomodam(n - 1)


def elefantes(n):
    # Verifica se n não é um inteiro ou não é maior que 1
    if not isinstance(n, int) or n <= 1:
        return ""
    
    # Função auxiliar para formatar a linha de cada elefante
    def linha_elefante(i):
        # Para i == 1, usa "Um elefante" no singular
        if i == 1:
            return "Um elefante incomoda muita gente\n"
        # Para i > 1, usa número e plural
        return f"{i} elefantes {incomodam(i)}muito mais\n"
    
    # Caso base: quando n == 2, retorna a parte de 1 e 2 elefantes
    if n == 2:
        return linha_elefante(1) + linha_elefante(2)
    
    # Caso recursivo: retorna a música até n-1 elefantes, seguida da parte de n-1 e n
    return elefantes(n - 1) + linha_elefante(n - 1) + linha_elefante(n)


def fibonacci(n):
    # Verifica se n é um inteiro não negativo
    if not isinstance(n, int) or n < 0:
        return None  # Ou poderia levantar uma exceção, dependendo do contexto
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


def fatorial(x):
    # Verifica se x é um inteiro não negativo
    if not isinstance(x, int) or x < 0:
        return None  # Ou poderia levantar uma exceção, dependendo do contexto
    # Caso base
    if x == 0:
        return 1
    # Caso recursivo: x! = x * (x-1)!
    return x * fatorial(x - 1)