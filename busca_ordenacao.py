import random

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


def ordenar_insercao(registros, chave, decrescente=True):
    """
    Ordena a lista de registros utilizando o algoritmo de ORDENAÇÃO POR INSERÇÃO.
    Permite escolher qualquer chave/campo e a direção (decrescente por padrão).
    
    Retorna uma cópia ordenada da lista, preservando a lista original.
    """
    lista = registros[:]
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        
        if decrescente:
            # Para ordem decrescente: empurra os menores para a direita
            while j >= 0 and lista[j][chave] < atual[chave]:
                lista[j + 1] = lista[j]
                j -= 1
        else:
            # Para ordem crescente: empurra os maiores para a direita
            while j >= 0 and lista[j][chave] > atual[chave]:
                lista[j + 1] = lista[j]
                j -= 1
                
        lista[j + 1] = atual
    return lista


def ordenar_bolha(registros, chave, decrescente=True):
    """
    Ordena a lista de registros utilizando o algoritmo de ORDENAÇÃO POR BOLHA (Bubble Sort).
    Permite escolher qualquer chave/campo e a direção (decrescente por padrão).
    
    Retorna uma cópia ordenada da lista, preservando a lista original.
    """
    lista = registros[:]
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            condicao = (lista[j][chave] < lista[j + 1][chave]) if decrescente else (lista[j][chave] > lista[j + 1][chave])
            if condicao:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista


def gerar_detritos_ficticios(qtd: int) -> list:
    """
    Gera uma lista com 'qtd' registros fictícios de detritos espaciais
    com códigos numéricos únicos de 1 a qtd.
    """
    niveis = ["Baixo", "Médio", "Alto", "Crítico"]
    dados = []
    for i in range(1, qtd + 1):
        detrito = {
            "codigo": i,
            "nome": f"DEBRIS-{i:05d}",
            "altitude_km": round(random.uniform(160, 2000), 2),
            "velocidade_kms": round(random.uniform(7.0, 11.0), 2),
            "tamanho_m": round(random.uniform(0.01, 15.0), 2),
            "nivel_risco": random.choice(niveis)
        }
        dados.append(detrito)
    return dados
