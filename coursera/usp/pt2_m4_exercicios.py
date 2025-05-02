def  ordenada(lista):
    ordenada = sorted(lista)
    return (lista[0] == ordenada[0]) and (lista[-1] == ordenada[-1])



def busca(lista, elemento):
    if not elemento in lista:
        return False
    
    for i, e in enumerate(lista):
        if e == elemento:
            return i
