from random import randint

def  ordenada(lista):
    pass
    #ordenada = sorted(lista)
    #return (lista[0] == ordenada[0]) and (lista[-1] == ordenada[-1])



def busca(lista, elemento):
    if not elemento in lista:
        return False
    
    for i, e in enumerate(lista):
        if e == elemento:
            return i


def lista_grande(n):
    return [randint(0,10000) for r in range(n)]


def ordena(lista:list):
    ord_lst = []
    while lista:
        min_index = lista.index(min(lista))
        ord_lst = lista.pop(min_index)
    return ord_lst
        

