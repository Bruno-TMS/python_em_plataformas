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
    if (not lista):
        return False
    
    lista = [i_e for i_e in enumerate(lista)]
  
    def get_index_meio(lista):
        if len(lista) % 2 == 0:
            return (len(lista)//2)-1
        else:
            return len(lista)//2
    
    def get_lista_a_direita(lista):
        return lista[get_index_meio(lista)+1:]
    
    def get_lista_a_esquerda(lista):
        return lista[:get_index_meio(lista)]
    
    def get_idx_orig_ele_orig(lista):
        idx_m = get_index_meio(lista)
        idx_original = lista[idx_m][0]
        elemento = lista[idx_m][1]
        return (idx_original, elemento)
    
    
    while True:
        idx_orig, ele_orig = get_idx_orig_ele_orig(lista)
        print(idx_orig)
        
        if ele_orig == elemento:
            return idx_orig

        if len(lista) <= 1:
            break
        
        if elemento > ele_orig:
            lista =  get_lista_a_direita(lista)

        if elemento < ele_orig:
            lista =  get_lista_a_esquerda(lista)
        
        
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


def insertion_sort(lista):
    return bubble_sort(lista)


                
