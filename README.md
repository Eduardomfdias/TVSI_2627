# TVSI 2026/27 — Trabalho T08: Desenho de Testes com Assistência de IA

**Universidade do Minho**  
**Mestrado em Engenharia Informática / Tecnologias e Verificação de Sistemas de Informação**  
**Ano Letivo:** 2026/27  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** T08 — Grupo 5  
**Elementos do Grupo:**
- Eduardo Dias (Coordenador / Test Lead)
- Rui Carneiro (Desenhador de Testes)
- Érica Moreira (Revisão IA e Execução)
- Beatriz Barbosa (Analista de Defeitos e Cobertura)

---

## 1. Objetivo do Trabalho

O objetivo deste projeto consiste na aplicação do método de **comparação crítica entre o desenho de testes humano e o desenho assistido por Inteligência Artificial**, tendo como objeto de teste o componente de software `shipping.py` (Build T08-B1.0).

O trabalho foi desenvolvido estritamente a partir de um **oráculo de teste independente**, derivado das Regras de Negócio normativas (`BusinessRules.md` v1.0, BR-01 a BR-08), sem consulta prévia ao código-fonte ou às sugestões da IA para a definição dos resultados esperados.

---

## 2. Estrutura do Repositório

```text
TVSI_2627/
├── README.md                                  # Documentação principal do repositório
├── CLAUDE.md                                  # Guia de contexto do projeto
├── .gitignore                                 # Regras de exclusão Git (macOS, Python)
├── TVSI_T08_Students_B1.0/                    # Pacote baseline oficial fornecido pelo docente
│   ├── BusinessRules.md / .html               # Regras de negócio normativas (BR-01 a BR-08)
│   ├── StudentAssignment.md / .html           # Guião e requisitos de avaliação do trabalho
│   ├── START_HERE.md / .html                  # Instruções de arranque inicial
│   ├── AI_PROVENANCE.md / .html               # Registo de proveniência da IA e cronologia de congelamento
│   ├── TestResults_T08_Template.xlsx          # Folha de cálculo oficial integralmente preenchida
│   └── app/                                   # Ambiente de execução da aplicação
│       ├── shipping.py                        # Objeto de teste (função quote) - baseline não alterada
│       ├── run_cases.py                       # Runner oficial de testes JSON
│       ├── human_cases.json                   # Caso de verificação técnica de ambiente (H-ENV)
│       ├── human_cases.results.json           # Resultado da verificação técnica de ambiente
│       └── ai_candidates.json                 # Candidatos de teste IA para revisão crítica
├── Trabalho_CP1/                              # Checkpoint 1 — Charter e Ambiente
│   ├── CP1.md                                 # Relatório do CP01 (charter, papéis, riscos, revisão estática)
│   └── TestResults_T08_Template.xlsx          # Cópia de trabalho do workbook
├── Trabalho_CP2/                              # Checkpoint 2 — Revisão Estática, Modelo e Oráculo
│   ├── CP2.md                                 # Especificação técnica e modelo de oráculo independente
│   ├── Relatorio_CP2.md                       # Relatório do CP02 e resultados da suite humana congelada
│   ├── human_cases.json                       # Suite humana congelada (16 casos: H-01 a H-16)
│   └── human_cases.results.json               # Evidência de execução da suite humana (10 PASS / 6 FAIL)
└── Trabalho_CP3/                              # Checkpoint 3 — Revisão IA, Suite Final e Validação
    ├── CP3.md                                 # Planeamento da revisão dos candidatos IA
    ├── Relatorio_CP3.md                       # Relatório consolidado e auditado do CP03
    ├── final_cases.json                       # Suite final combinada (21 casos: H-01 a H-16 + F-17 a F-21)
    ├── final_cases.results.json               # Evidência de execução em Python 3.9.6 (13 PASS / 8 FAIL)
    ├── final_cases.results.py312.json         # Evidência de execução em Python 3.12.7 (13 PASS / 8 FAIL)
    ├── verify_br05_independence.py            # Procedimento complementar de validação da regra BR-05
    ├── br05_independence.results.json         # Evidência BR-05 em Python 3.9.6 (PASS)
    └── br05_independence.py312.json          # Evidência BR-05 em Python 3.12.7 (PASS)
```

---

## 3. Descrição dos Checkpoints

### CP01 — Charter e Configuração de Ambiente (Data: 2026-10-22)
- Constituição da equipa e distribuição de responsabilidades.
- Definição do âmbito, riscos iniciais e mitigação técnica.
- Revisão estática preliminar de BR-01 a BR-08 e registo de questões de clarificação (Q-01 a Q-04).
- Execução com sucesso do caso técnico de ambiente `H-ENV` (`TVSI_T08_Students_B1.0/app/human_cases.json`).

### CP02 — Revisão Estática, Modelo e Suite Humana Congelada (Data: 2026-10-28)
- Especificação formal do oráculo independente baseado exclusivamente nas regras normativas.
- Aplicação das técnicas de Partições de Equivalência (EP) e Análise de Valores de Fronteira (BVA).
- Desenho de 16 casos de teste humanos (`H-01` a `H-16`) e **congelamento formal** em `Trabalho_CP2/human_cases.json` (comprovado no commit `54ec4d3` de 30/10/2026), antes de qualquer inspeção da suite IA.
- Execução inicial revelando 10 PASS e 6 FAIL, permitindo identificar quatro defeitos de raiz na aplicação (`DEF-01` a `DEF-04`).

### CP03 — Revisão dos Candidatos IA, Suite Final e Auditoria (Data: 2026-11-08)
- Abertura e análise crítica dos 12 candidatos de IA em `ai_candidates.json`:
  - **2 Aceites** (`AI-11` → `F-17`, `AI-12` → `F-18`): adicionaram cobertura relevante.
  - **1 Revisto** (`AI-09` → `F-19`): expected corrigido de `OK, fee=22` para `UNAVAILABLE, fee=null` (violação da regra BR-04 pela IA).
  - **9 Rejeitados**: duplicados de casos humanos existentes ou com expectativas erróneas (`AI-05`, `AI-06`).
- Construção da suite final com **21 casos de teste** (`final_cases.json`): 16 casos humanos preservados + 3 IA aproveitados + 2 casos novos (`F-20` para express não-booleano e `F-21` para precedência de validação BR-05).
- Execução da suite final com veredicto: **13 PASS / 8 FAIL**.
- Demonstração empírica da ausência de efeitos secundários e independência entre chamadas da regra BR-05 através de script dedicado (`verify_br05_independence.py`).
- Preenchimento integral de todas as folhas do workbook de testes oficial (`TestResults_T08_Template.xlsx`).

---

## 4. Localização dos Artefactos e Evidências

| Artefacto | Localização | Descrição |
|---|---|---|
| **Relatório CP01** | `Trabalho_CP1/CP1.md` | Charter de teste, papéis e verificação de ambiente |
| **Relatório CP02** | `Trabalho_CP2/Relatorio_CP2.md` | Oráculo, suite humana e primeiros 4 defeitos |
| **Relatório CP03** | `Trabalho_CP3/Relatorio_CP3.md` | Revisão IA, suite de 21 casos, cobertura e riscos |
| **Suite Humana Congelada** | `Trabalho_CP2/human_cases.json` | 16 casos desenhados por humanos (H-01 a H-16) |
| **Resultados Humanos** | `Trabalho_CP2/human_cases.results.json` | 10 PASS / 6 FAIL (evidência CP02) |
| **Candidatos IA** | `TVSI_T08_Students_B1.0/app/ai_candidates.json` | 12 sugestões de teste geradas por IA |
| **Suite Final Combinada** | `Trabalho_CP3/final_cases.json` | 21 casos finais (H-01 a H-16 + F-17 a F-21) |
| **Resultados Finais (Py 3.9)** | `Trabalho_CP3/final_cases.results.json` | 13 PASS / 8 FAIL (baseline) |
| **Resultados Finais (Py 3.12)** | `Trabalho_CP3/final_cases.results.py312.json` | 13 PASS / 8 FAIL (requisito 3.10+) |
| **Validação BR-05 (Py 3.9)** | `Trabalho_CP3/br05_independence.results.json` | Evidência BR-05 em Python 3.9.6 (PASS) |
| **Validação BR-05 (Py 3.12)** | `Trabalho_CP3/br05_independence.py312.json` | Evidência BR-05 em Python 3.12.7 (PASS) |
| **Workbook Oficial** | `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` | Workbook Excel oficial com 6 separadores completos |

---

## 5. Instruções de Execução

### Requisitos de Ambiente
- **Versão de Python:** Python 3.10 ou superior (exigido por BR-06).
- **Dependências:** Nenhuma dependência externa `pip` é necessária. O runner utiliza apenas a biblioteca padrão (`json`, `pathlib`, `sys`).
- O projeto foi testado e validado em **Python 3.12.7** (em estrita conformidade) e em **Python 3.9.6** (versão base macOS), com paridade absoluta de resultados.

### Executar a Suite Final Oficial (21 casos)
A partir da pasta da aplicação:
```bash
cd TVSI_T08_Students_B1.0/app
python3 run_cases.py ../../Trabalho_CP3/final_cases.json
```
*O runner devolverá exit code 1 (devido aos 8 FAILs resultantes de defeitos na aplicação) e gravará `final_cases.results.json`.*

### Executar a Suite Humana Congelada (16 casos)
```bash
cd TVSI_T08_Students_B1.0/app
python3 run_cases.py ../../Trabalho_CP2/human_cases.json
```

### Executar a Validação de Independência e Ausência de Efeitos Secundários (BR-05)
```bash
python3 Trabalho_CP3/verify_br05_independence.py
```
*Gera o ficheiro de evidência `Trabalho_CP3/br05_independence.results.json` com veredicto `PASS`.*

---

## 6. Utilização de IA e Proveniência

- **Fixture de IA fornecido (`ai_candidates.json`):** Criado a 20 de outubro de 2026 pelo assistente Codex (GPT-6) como material pedagógico deliberadamente curado com erros e lacunas.
- **Assistente IA do grupo:** Claude Sonnet 4.6 (Anthropic Claude Code) utilizado sob supervisão humana para suporte na redação técnica, automação de execução e cruzamento de dados.
- **Garantia de Independência:**
  - O congelamento da suite humana (`H-01` a `H-16`) ocorreu a **30 de outubro de 2026** (commit `54ec4d3`).
  - A revisão dos candidatos de IA decorreu apenas a **8 de novembro de 2026** (commit `5f9567e`).
  - Todas as expectativas foram derivadas analiticamente das regras BR-01 a BR-05, o que permitiu detetar 3 erros nos candidatos de IA (`AI-05`, `AI-06` e `AI-09`).

---

## 7. Defeitos Confirmados na Aplicação (`shipping.py`)

A baseline original fornecida pelo docente foi intencionalmente preservada sem modificações de código, mantendo os 4 defeitos identificados para avaliação:

| ID | Regra | Localização | Comportamento Observado | Comportamento Esperado | Casos Afetados |
|---|---|---|---|---|---|
| **DEF-01** | BR-01 | `shipping.py:3` | Usa `>= 20000`, rejeitando indevidamente `weight = 20000` como `INVALID` | `weight = 20000` é o limite superior válido (deve retornar `OK`, fee=12) | H-07 |
| **DEF-02** | BR-02 | `shipping.py:7` | Usa `< 1000` em vez de `<= 1000`, cobrando taxa de tier 2 (8€) a `weight = 1000` | `weight = 1000` pertence ao tier 1 (deve retornar `OK`, fee=5) | H-03 |
| **DEF-03** | BR-03 | `shipping.py:14` | Atribuição simples `fee = 4` substitui a fee base para entregas `REMOTE` | Suplemento `REMOTE` deve acumular sobre a fee base (`fee += 4`) | H-10, H-12, H-13, F-18 |
| **DEF-04** | BR-04 | `shipping.py:5` | Limiar de indisponibilidade `REMOTE + express` usa `> 10000` | Deve retornar `UNAVAILABLE` para pesos estritamente superiores a 5000 g | H-14, F-19 (e threshold de H-13) |
