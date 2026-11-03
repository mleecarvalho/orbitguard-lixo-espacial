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

def main():
  """Laço principal do menu inicial."""
  carregar_dados()
  while True:
    print("\n--- ORBITGUARD: MONITORAMENTO DE DETRITOS ---")
    print("1 - Listar Detritos Espaciais")
    print("0 - Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
      listar_detritos()
    elif opcao == "0":
      print("Encerrando o sistema...")
      break
    else:
      print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
  main()