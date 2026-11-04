import csv
from pilha_alertas import PilhaAlertas

ARQUIVO_CSV = "detritos.csv"
detritos = []
pilha_alertas = PilhaAlertas()

from busca_ordenacao import (
    busca_sequencial, 
    busca_binaria, 
    busca_binaria_recursiva, 
    ordenar_por_codigo_simples
)

def carregar_dados():
  """Lê os registros do arquivo CSV e armazena na lista detritos."""
  detritos.clear()
  try:
    with open(ARQUIVO_CSV, mode="r", encoding="utf-8") as arq:
      leitor = csv.DictReader(arq)
      for linha in leitor:
        detritos.append({
            "codigo": int(linha["codigo"]),
            "nome": linha["nome"].strip(),
            "altitude_km": float(linha["altitude_km"]),
            "velocidade_kms": float(linha["velocidade_kms"]),
            "tamanho_m": float(linha["tamanho_m"]),
            "nivel_risco": linha["nivel_risco"].strip(),
        })
    print(
        f"[LOG] {len(detritos)} registros carregados com sucesso de"
        f" '{ARQUIVO_CSV}'."
    )
  except FileNotFoundError:
    print(
        f"[AVISO] Arquivo '{ARQUIVO_CSV}' não encontrado. Iniciando base"
        " vazia."
    )

def listar_detritos():
  """Exibe todos os registros de detritos carregados na memória."""
  if not detritos:
    print("\nNenhum detrito cadastrado na base.")
    return

  print("\n" + "=" * 80)
  print(
      f"{'CÓDIGO':<8} | {'NOME':<25} | {'ALT(km)':<10} | {'VEL(km/s)':<10} |"
      f" {'TAM(m)':<8} | {'RISCO':<8}"
  )
  print("=" * 80)
  for d in detritos:
    print(
        f"{d['codigo']:<8} | {d['nome']:<25} | {d['altitude_km']:<10.1f} |"
        f" {d['velocidade_kms']:<10.1f} | {d['tamanho_m']:<8.2f} |"
        f" {d['nivel_risco']:<8}"
    )
  print("=" * 80)

def buscar_detrito():
    if not detritos:
        print("\nNenhum detrito cadastrado para busca.")
        return

    print("\n--- BUSCA DE DETRITO POR CÓDIGO ---")
    codigo = ler_inteiro("Digite o código do detrito a buscar: ")

    # 1. Busca Sequencial na lista original
    pos_seq, comp_seq = busca_sequencial(detritos, codigo)

    # 2. Busca Binária na lista ordenada por código
    coletas_ordenadas = ordenar_por_codigo_simples(detritos)
    pos_bin, comp_bin = busca_binaria(coletas_ordenadas, codigo)
    pos_rec, comp_rec = busca_binaria_recursiva(coletas_ordenadas, codigo)

    # Exibição dos resultados e contagem de comparações
    if pos_seq != -1:
        detrito = detritos[pos_seq]
        print(f"\n✓ Detrito encontrado!")
        print(f"  ID: {detrito['codigo']} | Nome: {detrito['nome']}")
        print(f"  Altitude: {detrito['altitude_km']} km | Velocidade: {detrito['velocidade_kms']} km/s")
        print(f"  Tamanho: {detrito['tamanho_m']} m | Nível de Risco: {detrito['nivel_risco']}")
    else:
        print(f"\n✗ Nenhum detrito encontrado com o código {codigo}.")

    print("\n--- METRICAS DE DESEMPENHO DA BUSCA ---")
    print(f"  • Busca Sequencial: {comp_seq} comparações")
    print(f"  • Busca Binária Iterativa: {comp_bin} comparações")
    print(f"  • Busca Binária Recursiva: {comp_rec} comparações")

from busca_ordenacao import (
    busca_sequencial, 
    busca_binaria, 
    busca_binaria_recursiva, 
    ordenar_por_codigo_simples,
    ordenar_insercao
)

def exibir_ranking_tamanho():
    if not detritos:
        print("\nNenhum detrito cadastrado para gerar o ranking.")
        return

    # Ordena por inserção no campo 'tamanho_m' em ordem decrescente (do maior para o menor)
    ranking = ordenar_insercao(detritos, "tamanho_m", decrescente=True)

    print("\n--- RANKING DE DETRITOS POR TAMANHO (MAIOR PARA O MENOR) ---")
    for i, d in enumerate(ranking, 1):
        print(f"{i}º | ID: {d['codigo']} | Nome: {d['nome']} | Tamanho: {d['tamanho_m']}m | Risco: {d['nivel_risco']}")


def cadastrar_detrito():
    print("\n--- CADASTRO DE DETRITO ESPACIAL ---")
 
  # 1. Validação de Código Único
    while True:
        codigo = ler_inteiro("Código (ID único): ")
        posicao, _ = busca_sequencial(detritos, codigo)
        if posicao == -1:
            break
        print("Erro: Já existe um detrito cadastrado com este código.")

    # 2. Nome do Objeto
    nome = input("Nome / Identificação do objeto: ").strip()
    while not nome:
        print("O nome não pode ser vazio.")
        nome = input("Nome / Identificação do objeto: ").strip()

    # 3. Altitude (> 100 km)
    altitude_km = ler_float_positivo("Altitude (km, > 100): ", minimo=100.0)

    # 4. Velocidade (> 0 km/s)
    velocidade_kms = ler_float_positivo("Velocidade (km/s, > 0): ", minimo=0.0)

    # 5. Tamanho (> 0 m)
    tamanho_m = ler_float_positivo("Tamanho (m, > 0): ", minimo=0.0)

    # 6. Nível de Risco (Lista fixa)
    riscos_validos = ["Baixo", "Médio", "Alto", "Crítico"]
    print(f"Níveis de risco aceitos: {', '.join(riscos_validos)}")
    nivel_risco = input("Nível de risco: ").strip().capitalize()
    while nivel_risco not in riscos_validos:
        print("Nível de risco inválido. Escolha entre: Baixo, Médio, Alto ou Crítico.")
        nivel_risco = input("Nível de risco: ").strip().capitalize()

    # Estruturação e Persistência
    novo_detrito = {
        "codigo": codigo,
        "nome": nome,
        "altitude_km": altitude_km,
        "velocidade_kms": velocidade_kms,
        "tamanho_m": tamanho_m,
        "nivel_risco": nivel_risco
    }
    
    coletas.append(novo_detrito)
    salvar_dados(coletas)
    print(f"\nDetrito '{nome}' (Código: {codigo}) cadastrado e salvo com sucesso!")

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def ler_float_positivo(mensagem, minimo=0.0):
    while True:
        try:
            valor = float(input(mensagem).strip())
            if valor > minimo:
                return valor
            print(f"O valor deve ser maior que {minimo}.")
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.")

def gerenciar_pilha_alertas():
    print("\n--- GERENCIAMENTO DE PILHA DE ALERTAS DE COLISÃO (LIFO) ---")
    print("1 - Registrar / Empilhar Novo Alerta (Push)")
    print("2 - Processar / Desempilhar Alerta Mais Recente (Pop)")
    print("3 - Visualizar Alerta do Topo (Peek)")
    print("4 - Listar Todos os Alertas Empilhados")
    print("0 - Voltar")
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        if not detritos:
            print("Nenhum detrito cadastrado para associar ao alerta.")
            return
        
        codigo = ler_inteiro("Código do detrito em rota de colisão: ")
        pos, _ = busca_sequencial(detritos, codigo)
        if pos == -1:
            print("Detrito não encontrado.")
            return

        detrito = detritos[pos]
        descricao = input("Descrição do evento / Objeto ameaçado: ").strip()
        alerta = {
            "codigo_detrito": detrito["codigo"],
            "nome_detrito": detrito["nome"],
            "nivel_risco": detrito["nivel_risco"],
            "descricao": descricao
        }
        pilha_alertas.push(alerta)
        print(f"\n✓ Alerta empilhado com sucesso para o detrito '{detrito['nome']}'!")

    elif opcao == "2":
        alerta = pilha_alertas.pop()
        if alerta:
            print(f"\n✓ Alerta processado e removido do topo:")
            print(f"  Detrito: {alerta['nome_detrito']} (ID: {alerta['codigo_detrito']}) | Risco: {alerta['nivel_risco']}")
            print(f"  Evento: {alerta['descricao']}")
        else:
            print("\nA pilha de alertas está vazia.")

    elif opcao == "3":
        alerta = pilha_alertas.peek()
        if alerta:
            print(f"\n▲ Alerta no TOPO da pilha:")
            print(f"  Detrito: {alerta['nome_detrito']} (ID: {alerta['codigo_detrito']}) | Risco: {alerta['nivel_risco']}")
            print(f"  Evento: {alerta['descricao']}")
        else:
            print("\nA pilha de alertas está vazia.")

    elif opcao == "4":
        if pilha_alertas.is_empty():
            print("\nA pilha de alertas está vazia.")
            return
        
        print(f"\n=== PILHA DE ALERTAS ({pilha_alertas.size()} pendentes) - DO TOPO PARA A BASE ===")
        for i, a in enumerate(pilha_alertas.listar_alertas(), 1):
            print(f"{i}. Detrito: {a['nome_detrito']} (ID: {a['codigo_detrito']}) | Risco: {a['nivel_risco']} | Evento: {a['descricao']}")



def main():
  """Laço principal do menu inicial."""
  carregar_dados()
  while True:
    print("\n--- ORBITGUARD: MONITORAMENTO DE DETRITOS ---")
    print("1 - Cadastrar Detritos Espaciais")
    print("2 - Listar Detritos Espaciais")
    print("3 - Busca Detrito por Código")
    print("4 - Ranking por Tamanho (Ordenação por Inserção)")
    print("5 - Gerenciar Pilha de Alertas de Colisão")
    print("0 - Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        cadastrar_detrito()
    elif opcao == "2":
       listar_detritos()
    elif opcao == "3":
       buscar_detrito()  
    elif opcao == "4":
      exibir_ranking_tamanho()
    elif opcao == "5" :
       gerenciar_pilha_alertas()  
    elif opcao == "0":
      print("Encerrando o OrbitGuard. Até logo!")
      break
    else:
      print("Opção inválida! Digite novamente.")


if __name__ == "__main__":
  main()