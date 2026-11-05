# 🛰️ OrbitGuard: Monitoramento e Triagem de Detritos Espaciais

> **Projeto Integrador — Laboratório de Programação**  
> **Curso:** Bacharelado em Engenharia de Software  
> **Instituição:** Universidade Santo Amaro (UNISA)  
> **Estudante:** Marcio de Carvalho  
> **Professor Orientador:** Prof. Me. Patrick Araújo  

---

## 📌 Visão Geral do Projeto

O **OrbitGuard** é uma solução computacional desenvolvida em linguagem Python para automação do monitoramento, triagem e análise de risco orbital de detritos espaciais situados na Órbita Terrestre Baixa (LEO). 

O acúmulo de lixo espacial — fragmentos de foguetes, satélites inativos e detritos de impacto orbitando a velocidades superiores a 7 km/s — representa uma das principais ameaças operacionais a satélites ativos, telescópios e estações espaciais. O programa fornece uma interface baseada em modo terminal estruturada (TUI/Clipper), aplicando persistência de dados em arquivos CSV, gerenciamento de eventos com estruturas de dados do tipo Pilha (LIFO) e rotinas manuais de busca e ordenação.

---

## 🛠️ Ambiente de Desenvolvimento e Tecnologias

- **Linguagem de Programação:** Python 3 (executável no ambiente padrão, sem dependências externas incompatíveis)
- **Ambiente de Desenvolvimento:** GitHub Codespaces / VS Code Web (Terminal Linux Ubuntu)
- **Controle de Versão:** Git & GitHub
- **Persistência de Dados:** Arquivo de texto no formato CSV (`detritos.csv`)

---

## 📁 Estrutura de Arquivos do Repositório

```text
orbitguard/
│
├── sistema.py           # Menu principal TUI, navegação, cadastros e relatórios estatísticos
├── busca_ordenacao.py   # Algoritmos manuais de busca (Seq/Bin) e ordenação (Inserção/Bolha)
├── pilha_alertas.py     # Estrutura de dados avançada (Pilha LIFO) para gestão de alertas críticos
├── detritos.csv         # Base de dados em disco (valores separados por vírgula)
└── README.md            # Documentação técnica e guia de execução
```

## 💻 Funcionalidades do Sistema

Cadastro Validado de Detritos: Leitura e validação estrita dos campos codigo (inteiro único), nome, altitude_km (> 100 km), velocidade_kms (> 0), tamanho_m (> 0) e nivel_risco (Baixo, Médio, Alto, Crítico).
Listagem Geral: Apresentação formatada da base de dados em tabelas com bordas ASCII.
Consultas Algorítmicas por Código: Busca Sequencial e Busca Binária (iterativa e recursiva), retornando a posição do elemento e o número de comparações efetuadas.
Ranking por Tamanho/Massa: Ordenação manual por Inserção (em ordem decrescente) sem a utilização de atalhos nativos (sort() / sorted()).
Auditoria de Alertas Críticos (Pilha LIFO): Empilhamento (push) e desempilhamento (pop) de eventos de risco iminente para auditoria rápida de segurança.
Relatório de Desempenho Algorítmico: Simulação experimental comparando o consumo de comparações de busca em cenários de 100, 1.000 e 10.000 registros fictícios no pior caso.

## ⚡ Experimento de Desempenho Algorítmico

Para avaliar quantitativamente a eficiência computacional das técnicas de busca, o sistema executa um teste em memória comparando o pior caso (busca por um registro inexistente):
Quantidade de Registros ($N$)	Busca Sequencial ($O(n)$)	Busca Binária ($O(\log n)$)	Redução de Processamento (%)
100	100 comparações	7 comparações	93,00%
1.000	1.000 comparações	10 comparações	99,00%
10.000	10.000 comparações	14 comparações	99,86%
Conclusão Técnica: A Busca Binária demonstra eficiência exponencialmente superior para bases extensas, reduzindo em mais de 99,8% o número de testes lógicos exigidos em relação à Busca Sequencial.

---

## 📋 Tabela de Rastreamento de Desenvolvimento

Etapa	Componente / Foco Técnico	Mensagem de Commit Padrão	Status
Etapa 1	Base inicial em detritos.csv com registros fictícios formatados.	feat: adiciona base de dados inicial em arquivo CSV (detritos.csv)	CONCLUÍDO
Etapa 2	Funções carregar_dados() / salvar_dados() e menu TUI base.	feat: implementa leitura e listagem de dados do arquivo CSV em sistema.py	CONCLUÍDO
Etapa 3	Função cadastrar_detrito() com validação estrita de regras.	feat: adiciona funcao de cadastro de detritos com validacao de regras	CONCLUÍDO
Etapa 4	Algoritmos de Busca Sequencial e Binária (iterativa/recursiva).	feat: implementa busca sequencial e binaria iterativa/recursiva	CONCLUÍDO
Etapa 5	Algoritmos manuais de Ordenação por Inserção e Bolha.	feat: implementa ordenacao por insercao e bolha para ranking	CONCLUÍDO
Etapa 6	Módulo pilha_alertas.py para gestão LIFO de alertas de colisão.	feat: implementa pilha para auditoria de alertas de colisaos recentes	CONCLUÍDO
Etapa 7	Experimento comparativo de desempenho com contagem de comparações.	feat: adiciona relatorio de comparacao de desempenho das buscas	CONCLUÍDO
Etapa 8	Refatoração visual da interface TUI/Clipper com bordas ASCII.	style: finaliza interface TUI estilo Clipper com bordas ASCII e relatorios	CONCLUÍDO
Etapa 9	Elaboração do relatório científico (artigo ABNT em PDF).	docs: finaliza relatorio de artigo cientifico do projeto integrador	CONCLUÍDO
Etapa 10	Gravação do vídeo demonstrativo (3 a 5 min) e publicação de links.	docs: adiciona link do video demonstrativo no README e artigo	Pendente
---

## 🚀 Como Executar o Projeto
Clonar o repositório:
git clone [https://github.com/marciodecarvalho/orbitguard.git](https://github.com/marciodecarvalho/orbitguard.git)
cd orbitguard
Executar a aplicação no terminal:
python sistema.py

---

## 🔗 Links e Recursos
Repositório GitHub: https://github.com/marciodecarvalho/orbitguard
Vídeo Demonstrativo: (Link a ser inserido na Etapa 10)

---

### 📌 Comandos para Salvar e Enviar no Git

Após salvar o conteúdo acima no arquivo `README.md` no seu ambiente do **GitHub Codespaces**, execute os seguintes comandos no terminal:

```bash
git add README.md
git commit -m "docs: finaliza documentacao do README com instruções do projeto"
git push origin main
```