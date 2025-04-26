"""
Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.
"""
lst_upper = [c for c in range(ord('A'), ord('Z')+1)]
lst_lowwer = [c for c in range(ord('a'), ord('z')+1)]
lst_vogais = ['a', 'e', 'i', 'o', 'u']
lst_consoantes = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in lst_vogais]

def maiusculas(frase):
    return ''.join([c for c in frase if c.strip() and ord(c) in lst_upper])


"""
Exercício 2: Menor nome
Como pedido no primeiro vídeo desta semana, escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o primeiro nome com o menor comprimento presente na lista.

Exemplos:
"""
def menor_nome(nomes:str):
    return min([nome.strip().capitalize() for nome in nomes], key=lambda x:len(x))

"""Exercício 1: Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

Exemplos:"""

def conta_letras(frase:str, contar="vogais"):
    frase = frase.lower()
    total_consoantes = len([c for c in frase if c in lst_consoantes])
    total_vogais = len([c for c in frase if c in lst_vogais])
    
    if contar == 'consoantes':
        return total_consoantes
    
    return total_vogais


"""
Exercício 2: Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

Exemplos:"""
def primeiro_lex(lista):
    return sorted(lista)[0]
    


if __name__ == '__main__':
    #print([chr(c) for c in lst_lowwer])
    #print(maiusculas('Programamos em python 2?'))
    # deve devolver 'P'

    #print(maiusculas('Programamos em Python 3.'))
    # deve devolver 'PP'

    #print(maiusculas('PrOgRaMaMoS em python!'))
    # deve devolver 'PORMMS'

    print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
    # deve devolver 'José'

    print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
    # deve devolver 'José'

    print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
    # deve devolver José

    print(conta_letras('programamos em python', 'consoantes'))
    # deve devolver 13

    print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
    # deve devolver 'A'

    print(primeiro_lex(['AAAAAA', 'b']))
    # deve devolver 'AAAAAA'