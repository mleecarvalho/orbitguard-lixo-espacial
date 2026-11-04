# ==============================================================================
# ORBITGUARD - MÓDULO DE BUSCA E ORDENAÇÃO
# ==============================================================================

def busca_sequencial(registros, codigo):
    """
    Percorre a lista de registros item a item até encontrar o código desejado.
    Funciona em listas ordenadas ou não.
    
    Retorna: (posição, comparações) ou (-1, comparações) se não encontrar.
    """
    comparacoes = 0
    for i in range(len(registros)):
        comparacoes += 1
        if registros[i]["codigo"] == codigo:
            return i, comparacoes
    return -1, comparacoes


def busca_binaria(registros, codigo):
    """
    Realiza a busca binária de forma ITERATIVA.
    PRÉ-CONDIÇÃO: A lista de registros deve estar ordenada pelo campo 'codigo'.
    
    Retorna: (posição, comparações) ou (-1, comparações) se não encontrar.
    """
    inicio = 0
    fim = len(registros) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        
        if registros[meio]["codigo"] == codigo:
            return meio, comparacoes
        elif registros[meio]["codigo"] < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes


def busca_binaria_recursiva(registros, codigo, inicio=0, fim=None, comparacoes=0):
    """
    Realiza a busca binária de forma RECURSIVA.
    PRÉ-CONDIÇÃO: A lista de registros deve estar ordenada pelo campo 'codigo'.
    
    Retorna: (posição, comparações) ou (-1, comparações) se não encontrar.
    """
    if fim is None:
        fim = len(registros) - 1

    # Caso base: faixa de busca inválida (elemento não existe)
    if inicio > fim:
        return -1, comparacoes

    meio = (inicio + fim) // 2
    comparacoes += 1

    if registros[meio]["codigo"] == codigo:
        return meio, comparacoes
    elif registros[meio]["codigo"] < codigo:
        return busca_binaria_recursiva(registros, codigo, meio + 1, fim, comparacoes)
    else:
        return busca_binaria_recursiva(registros, codigo, inicio, meio - 1, comparacoes)


def ordenar_por_codigo_simples(registros):
    """
    Função auxiliar para garantir ordenação por código antes da busca binária.
    Retorna uma cópia ordenada da lista sem alterar a original.
    """
    lista = registros[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["codigo"] > lista[j + 1]["codigo"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista