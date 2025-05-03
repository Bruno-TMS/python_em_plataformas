"""
Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.


busca(['a', 'e', 'i'], 'e')
1
# deve devolver => 1

busca([1, 2, 3, 4, 5], 6)
2
3
4
# deve devolver => False

busca([1, 2, 3, 4, 5, 6], 4)
2
4
3
# deve devolver => 3
"""

def busca(lista, elemento):
    
    if len(lista) == 1:
        print('0')
        
        if elemento in lista:
            return 0
        
        else:
            return False 

    while len(lista) > 1:
        index_central = len(lista // 2)
        elemento_central = lista[index_central]
        
        print(f'{index_central}')
        
        if elemento_central == elemento:
            return index_central
        
        if elemento > elemento_central:
            lista =  lista[index_central:]
        
        if elemento < elemento_central:
            lista = lista[:index_central]
        
    return False

"""
Exercício 2: Ordenação com bubble sort
Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve imprimir o estado atual da lista toda vez que fizer uma alteração em seus elementos.

Exemplo:

bubble_sort([5, 1, 4, 2])
[1, 5, 4, 2]
[1, 4, 5, 2]
[1, 4, 2, 5]
[1, 2, 4, 5]
# deve devolver [1, 2, 4, 5]
"""

def bubble_sort(lista:list):
    len_lista = len(lista)
    max_index = len_lista-1
    
    for p in range(len_lista):
        
        for current_index in range(len_lista):
            next_index = current_index + 1
            
            if (next_index <= max_index) and (lista[next_index] < lista[current_index]):
                lista[current_index],lista[next_index] = lista[next_index],lista[current_index]
                print(lista)
    
    return lista



                
