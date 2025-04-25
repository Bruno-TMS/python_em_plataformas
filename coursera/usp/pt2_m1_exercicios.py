def count_rows(matriz):
    return len(matriz)

def count_columns(matriz):
    return len(matriz[0])

"""
Exercício 1: Tamanho da matriz
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
"""
def dimensoes(matriz):
     print(f'{count_rows(matriz)}X{count_columns(matriz)}')


"""
Exercício 2: Soma de matrizes
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.
"""
def soma_matrizes(m1, m2):
    dim_m1 = dimensoes(m1)
    dim_m2 = dimensoes(m2)
    
    if dim_m1 != dim_m2:
        return False
    
    matrix = []
    
    for i in range(count_rows(m1)):
        sum_rows = []
        
        for j in range(count_columns(m1)):
            sum_rows.append(m1[i][j] + m2[i][j])
        
        matrix.append(sum_rows)
    
    return matrix


"""
Exercício 1: Imprimindo matrizes
Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. Note que NÃO se deve imprimir espaços após o último elemento de cada linha!
Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma
"""
def imprime_matriz(minha_matriz):
  print('\n'.join([' '.join([str(coluna) for coluna in linha]) for linha in minha_matriz]))


"""
Exercício 2: Matrizes multiplicáveis
Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função sao_multiplicaveis(m1, m2) que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.
"""

def sao_multiplicaveis(m1, m2):
    return count_columns(m1) == count_rows(m2)


#if __name__ == '__main__':
#    m = [[1, 2], [3, 4]]
#
#    print(imprime_matriz(m))