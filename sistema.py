import csv
import busca_ordenacao as buscaOrdenacao
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
        print(f"\n{YELLOW}Nenhum detrito cadastrado na base.{RESET}")
        return

    exibir_cabecalho("CATÁLOGO ORBITAL DE DETRITOS (LEO)", largura=94)

    print(f"{BG_BLUE}{WHITE}{BOLD}| {'CÓDIGO':<8} | {'NOME':<25} | {'ALTITUDE (KM)':>13} | {'VEL. (KM/S)':>11} | {'TAM. (M)':>9} | {'RISCO':<9} |{RESET}")
    print(f"{BLUE}{'-' * 94}{RESET}")

    for d in detritos:
        risco = d['nivel_risco']
        cor_risco = cor_nivel_risco(risco)
        nome = d['nome'] if len(d['nome']) <= 25 else d['nome'][:22] + "..."

        print(f"| {WHITE}{d['codigo']:<8}{RESET} | {CYAN}{nome:<25}{RESET} | {WHITE}{d['altitude_km']:>13.2f}{RESET} | {WHITE}{d['velocidade_kms']:>11.2f}{RESET} | {WHITE}{d['tamanho_m']:>9.2f}{RESET} | {cor_risco}{risco:<9}{RESET} |")

    print(f"{BLUE}{'=' * 94}{RESET}\n")

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

    exibir_cabecalho("RANKING DE DETRITOS POR TAMANHO", largura=94)
    print(f"{BG_BLUE}{WHITE}{BOLD}| {'POS.':>5} | {'CÓDIGO':<8} | {'NOME':<38} | {'TAMANHO (M)':>16} | {'RISCO':<11} |{RESET}")
    print(f"{BLUE}{'-' * 94}{RESET}")
    for i, d in enumerate(ranking, 1):
        risco = d['nivel_risco']
        cor_risco = cor_nivel_risco(risco)
        nome = d['nome'] if len(d['nome']) <= 38 else d['nome'][:35] + "..."
        print(f"| {WHITE}{i:>5}{RESET} | {WHITE}{d['codigo']:<8}{RESET} | {CYAN}{nome:<38}{RESET} | {WHITE}{d['tamanho_m']:>16.2f}{RESET} | {cor_risco}{risco:<11}{RESET} |")
    print(f"{BLUE}{'=' * 94}{RESET}\n")


def cor_nivel_risco(risco):
    risco_normalizado = risco.casefold()
    if risco_normalizado in ("crítico", "critico"):
        return f"{RED}{BOLD}"
    if risco_normalizado == "alto":
        return YELLOW
    if risco_normalizado in ("médio", "medio"):
        return CYAN
    return GREEN


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
    
    detritos.append(novo_detrito)
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
    while True:
        limpar_tela()
        exibir_cabecalho("GERENCIAMENTO DE ALERTAS (PILHA LIFO)")
        print(f"{BG_BLUE}{WHITE}{BOLD}+{'-' * 73}+{RESET}")
        exibir_item_menu("1", "Registrar e empilhar novo alerta")
        exibir_item_menu("2", "Processar alerta mais recente")
        exibir_item_menu("3", "Visualizar alerta do topo")
        exibir_item_menu("4", "Listar alertas pendentes")
        exibir_item_menu("0", "Voltar ao menu principal")
        print(f"{BG_BLUE}{WHITE}{BOLD}+{'-' * 73}+{RESET}\n")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Voltando ao menu principal.")
            return

        if opcao == "1":
            if not detritos:
                print("Nenhum detrito cadastrado para associar ao alerta.")
            else:
                codigo = ler_inteiro("Código do detrito em rota de colisão: ")
                pos, _ = busca_sequencial(detritos, codigo)
                if pos == -1:
                    print("Detrito não encontrado.")
                else:
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
                print("\n✓ Alerta processado e removido do topo:")
                print(f"  Detrito: {alerta['nome_detrito']} (ID: {alerta['codigo_detrito']}) | Risco: {alerta['nivel_risco']}")
                print(f"  Evento: {alerta['descricao']}")
            else:
                print("\nA pilha de alertas está vazia.")

        elif opcao == "3":
            alerta = pilha_alertas.peek()
            if alerta:
                print("\n▲ Alerta no TOPO da pilha:")
                print(f"  Detrito: {alerta['nome_detrito']} (ID: {alerta['codigo_detrito']}) | Risco: {alerta['nivel_risco']}")
                print(f"  Evento: {alerta['descricao']}")
            else:
                print("\nA pilha de alertas está vazia.")

        elif opcao == "4":
            if pilha_alertas.is_empty():
                print("\nA pilha de alertas está vazia.")
            else:
                print(f"\n=== PILHA DE ALERTAS ({pilha_alertas.size()} pendentes) - DO TOPO PARA A BASE ===")
                for i, alerta in enumerate(pilha_alertas.listar_alertas(), 1):
                    print(f"{i}. Detrito: {alerta['nome_detrito']} (ID: {alerta['codigo_detrito']}) | Risco: {alerta['nivel_risco']} | Evento: {alerta['descricao']}")
        else:
            print("Opção inválida. Escolha uma opção do menu.")

        input("\nPressione ENTER para continuar no menu de alertas...")

def executar_experimento_desempenho():
    """
    Executa o experimento comparativo entre Busca Sequencial e Busca Binária
    em cenários de 100, 1.000 e 10.000 registros fictícios no pior caso.
    """
    tamanhos = [100, 1000, 10000]
    
    print("\n" + "=" * 70)
    print("      EXPERIMENTO DE DESEMPENHO: BUSCA SEQUENCIAL VS. BINÁRIA")
    print("=" * 70)
    print(f"{'Registros (N)':<15} | {'Busca Sequencial (Comp.)':<26} | {'Busca Binária (Comp.)':<22}")
    print("-" * 70)
    
    for qtd in tamanhos:
        # 1. Gerar dados fictícios
        registros = buscaOrdenacao.gerar_detritos_ficticios(qtd)
        
        # 2. Definir o alvo para o PIOR CASO (código inexistente)
        codigo_alvo = -1 
        
        # 3. Teste na Busca Sequencial (não exige ordenação)
        _, comp_seq = busca_sequencial(registros, codigo_alvo)
        
        # 4. A Busca Binária exige pré-ordenação pela chave 'codigo'
        registros_ordenados = sorted(registros, key=lambda x: x["codigo"])
        
        # 5. Teste na Busca Binária
        _, comp_bin = busca_binaria(registros_ordenados, codigo_alvo)
        
        # 6. Exibição formatada dos resultados
        print(f"{qtd:<15,d} | {comp_seq:<26,d} | {comp_bin:<22,d}".replace(",", "."))
        
    print("=" * 70)
    print("Análise:")
    print(" - A Busca Sequencial possui complexidade O(n), crescendo linearmente.")
    print(" - A Busca Binária possui complexidade O(log n), exigindo no máximo")
    print("   14 comparações mesmo para 10.000 registros.")
    print("=" * 70 + "\n")

# ==============================================================================
# CORES E ESTILOS ANSI (ESTILO CLIPPER / MS-DOS)
# ==============================================================================
RESET      = "\033[0m"
BOLD       = "\033[1m"

# Cores de Texto
BLUE       = "\033[34m"
CYAN       = "\033[36m"
YELLOW     = "\033[33m"
GREEN      = "\033[32m"
WHITE      = "\033[97m"
RED        = "\033[31m"

# Fundos (Backgrounds estilo Clipper)
BG_BLUE    = "\033[44m"
BG_CYAN    = "\033[46m"
BG_BLACK   = "\033[40m"

# Arte ASCII: Satélite OrbitGuard
ARTE_ASCII = rf"""{CYAN}{BOLD}
       .---.          
      /  .  \         .-----------------------------------------.

     |\_/|\_/|       |   {YELLOW}ORBITGUARD v1.0 - SENSORIAMENTO LEO{CYAN}    |
     |   |   |  ==== |   {WHITE}Sistema de Monitoramento e Triagem{CYAN}     |
     |\_/|\_/|       '-----------------------------------------'
      \  '  /         
       '---'          
{RESET}"""

def limpar_tela():
    """Limpa o terminal e reseta cores."""
    print(f"{RESET}\033[2J\033[H", end="")

def exibir_cabecalho(titulo: str, largura: int = 75):
    """Exibe o cabeçalho estilizado estilo Clipper."""
    print(f"{BG_BLUE}{WHITE}{BOLD}")
    print("=" * largura)
    print(f" {titulo.upper().center(largura - 2)} ")
    print("=" * largura + RESET)


def exibir_item_menu(opcao: str, descricao: str):
    texto = f"[{opcao}] {descricao}"
    destaque = RED if opcao == "0" else CYAN
    linha = f"{destaque}{BOLD}[{opcao}]{RESET}{WHITE} {descricao}"
    linha += " " * (71 - len(texto))
    print(f"{BG_BLUE}{WHITE}| {linha} |{RESET}")


def exibir_menu_principal():
    limpar_tela()
    print(ARTE_ASCII)
    exibir_cabecalho("MENU PRINCIPAL - OPERAÇÕES ORBITAIS")
    print(f"{BG_BLUE}{WHITE}{BOLD}+{'-' * 73}+{RESET}")
    exibir_item_menu("1", "Cadastrar novo detrito espacial")
    exibir_item_menu("2", "Listar detritos catalogados")
    exibir_item_menu("3", "Buscar detrito por código")
    exibir_item_menu("4", "Ranking por tamanho")
    exibir_item_menu("5", "Auditoria de alertas críticos")
    exibir_item_menu("6", "Experimento de desempenho algorítmico")
    exibir_item_menu("0", "Encerrar sistema OrbitGuard")
    print(f"{BG_BLUE}{WHITE}{BOLD}+{'-' * 73}+{RESET}")
    print()

def main():
  """Laço principal do menu inicial."""
  carregar_dados()
  while True:
    exibir_menu_principal()
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
    elif opcao == "6":
        executar_experimento_desempenho()
    elif opcao == "0":
      print("Encerrando o OrbitGuard. Até logo!")
      break
    else:
      print("Opção inválida! Digite novamente.")

    input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
  main()