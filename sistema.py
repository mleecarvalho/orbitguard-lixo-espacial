import csv

ARQUIVO_CSV = "detritos.csv"
detritos = []

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

def cadastrar_detrito(coletas):
    print("\n--- CADASTRO DE DETRITO ESPACIAL ---")
 
  # 1. Validação de Código Único
    while True:
        codigo = ler_inteiro("Código (ID único): ")
        posicao, _ = busca_sequencial(coletas, codigo)
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


def main():
  """Laço principal do menu inicial."""
  coletas = carregar_dados()
  while True:
    print("\n--- ORBITGUARD: MONITORAMENTO DE DETRITOS ---")
    print("1 - Cadastrar Detrito Espacial")
    print("2 - Listar Detritos Espaciais")
    print("0 - Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        cadastrar_detrito(coletas)
    elif opcao == "2":
       listar_detritos(coletas)
    elif opcao == "0":
      print("Encerrando o OrbitGuard. Até logo!")
      break
    else:
      print("Opção inválida! Digite novamente.")


if __name__ == "__main__":
  main()