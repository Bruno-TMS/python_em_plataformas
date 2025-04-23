import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    cal_ass_a = calcula_assinatura(as_a)
    cal_ass_b = calcula_assinatura(as_b)

    return sum([abs(t[0] - t[1]) for t in zip(cal_ass_a, cal_ass_b)]) / 6

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [f for s in sentencas for f in separa_frases(s)]
    palavras = [p for f in frases for p in separa_palavras(f)]

    tamanho_palavras = [len(p) for p in palavras]
    num_tot_palavras = len(palavras)

    tamanho_medio_palavra = sum(tamanho_palavras) / num_tot_palavras
    relacao_type_token  = n_palavras_diferentes(palavras) / num_tot_palavras
    razao_hapax_legomana = n_palavras_unicas(palavras) /  num_tot_palavras
    caracteres_in_sentenca = [c for s in sentencas for f in s for p in f for c in p] 
    tamanho_medio_sentenca = sum([len(c) for c in caracteres_in_sentenca]) / len(sentencas)
    complexidade_sentenca = len(frases) / len(sentencas)
    caracteres_in_frase = [c for f in frases for p in f for c in p]
    tamanho_medio_frase = sum([len(c) for c in caracteres_in_frase]) / len(frases)

    return [tamanho_medio_palavra,
            relacao_type_token,
            razao_hapax_legomana,
            tamanho_medio_sentenca,
            complexidade_sentenca,
            tamanho_medio_frase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valores = [(i,compara_assinatura(calcula_assinatura(t), ass_cp)) for i,t in enumerate(textos)]
    menor_valor = min(v[1] for v in valores)
    index_menor_valor = [v[0] for v in valores if v[1] == menor_valor][0]
    return index_menor_valor + 1

if __name__ == '__main__':
    ass = calcula_assinatura("Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.")
    print(ass)