def  ordenada(lista):
    ordenada = sorted(lista)
    return (lista[0] == ordenada[0]) and (lista[-1] == ordenada[-1])



def busca(lista:list, elemento):
    if not elemento in lista:
        return False
    
    return [i for i,e in enumerate(list) if e == elemento][0]
