# TVSI 2026/27 — Trabalho T08: Desenho de Testes com Assistência de IA

**Universidade do Minho**  
**Mestrado em Engenharia Informática / Tecnologias e Verificação de Sistemas de Informação**  
**Ano Letivo:** 2026/27  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** T08 — Grupo 5  
**Elementos do Grupo:**
- Eduardo Dias (Coordenador / Test Lead)
- Rui Carneiro (Desenhador de Testes & Automação QA)
- Érica Moreira (Revisão IA e Gestão de Evidências)
- Beatriz Barbosa (Analista de Defeitos e Cobertura)

---

## 1. Objetivo do Trabalho

O objetivo deste projeto consiste na aplicação do método de **comparação crítica entre o desenho de testes humano e o desenho assistido por Inteligência Artificial**, tendo como objeto de teste o componente de software `shipping.py` (Build oficial `T08-B1.0`).

O trabalho cobre integralmente os quatro checkpoints (**CP01 a CP04**):
- **CP01 (Charter & Environment):** Definição do charter de testes, papéis dos elementos, avaliação de riscos e verificação técnica de ambiente com o teste de fumo `H-ENV`.
- **CP02 (Static Review & Oracle Model):** Revisão estática das regras BR-01 a BR-08, modelação do oráculo independente e desenho/congelamento formal da suite humana (`H-01` a `H-16`) a 30 de outubro de 2026 (commit `54ec4d3`).
- **CP03 (AI Candidate Review & Final Suite Design):** Auditoria crítica dos 12 candidatos de IA (`AI-01` a `AI-12`), identificação de erros de oráculo na IA, expansão para a suite final combinada e demonstração computacional da regra de independência BR-05.
- **CP04 (Test Execution & Evidence Management):** Execução integral das suites em múltiplos interpretadores Python (3.9 e 3.12), gestão de evidências de execução reproduzíveis em `Trabalho_CP4/`, auditoria profunda do livro de cálculo Excel com coluna autónoma de requisitos, caracterização dos defeitos de implementação (`DEF-01` a `DEF-04`) e dos problemas de dados de IA (`DATA-01` a `DATA-03`), automação de auditoria (`Trabalho_CP4/audit_cp4.py`) e fecho do pacote de entrega.

---

## 2. Estrutura do Repositório

```text
TVSI_2627/
├── README.md                                  # Documentação principal e guia de reprodução
├── Relatorio_Consolidado.md                   # Relatório técnico consolidado do projeto (CP01 a CP04)
├── MANIFEST_ENTREGA.md                        # Manifesto de integridade criptográfica SHA-256
├── AUDITORIA_FINAL_ENTREGA.md                 # Relatório de auditoria técnica profunda
├── CLAUDE.md                                  # Guia de contexto e convenções do projeto
├── .gitignore                                 # Regras de exclusão Git (macOS, Python)
├── TVSI_T08_Grupo5_CP04.zip                   # Arquivo final de submissão do Grupo 5
├── TVSI_T08_Students_B1.0/                    # Pacote baseline oficial fornecido pelo docente
│   ├── BusinessRules.md / .html               # Regras de negócio normativas (BR-01 a BR-08)
│   ├── StudentAssignment.md / .html           # Guião e requisitos de avaliação do trabalho
│   ├── START_HERE.md / .html                  # Instruções de arranque inicial
│   ├── AI_PROVENANCE.md / .html               # Registo de proveniência da IA e cronologia de congelamento
│   ├── TestResults_T08_Template.xlsx          # Livro Excel oficial (6 folhas, coluna Requirement IDs, 0 erros)
│   └── app/                                   # Ambiente de execução da aplicação
│       ├── shipping.py                        # Objeto de teste (função quote) - baseline intocada
│       ├── run_cases.py                       # Runner oficial de testes JSON
│       ├── human_cases.json                   # Caso técnico de verificação de ambiente (H-ENV)
│       ├── human_cases.results.json           # Resultado da verificação técnica de ambiente
│       └── ai_candidates.json                 # 12 candidatos de teste IA fornecidos
├── Trabalho_CP1/                              # Checkpoint 1 — Charter e Ambiente
│   ├── CP1.md                                 # Relatório do CP01 (charter, papéis, riscos, revisão estática)
│   └── TestResults_T08_Template.xlsx          # Cópia sincronizada do workbook oficial
├── Trabalho_CP2/                              # Checkpoint 2 — Revisão Estática, Modelo e Oráculo
│   ├── CP2.md                                 # Especificação técnica e modelo de oráculo independente
│   ├── Relatorio_CP2.md                       # Relatório do CP02 e resultados da suite humana congelada
│   ├── human_cases.json                       # Suite humana congelada (16 casos: H-01 a H-16)
│   └── human_cases.results.json               # Evidência de execução da suite humana (10 PASS / 6 FAIL)
├── Trabalho_CP3/                              # Checkpoint 3 — Revisão IA, Suite Final e Validação
│   ├── CP3.md                                 # Planeamento da revisão dos candidatos IA
│   ├── Relatorio_CP3.md                       # Relatório consolidado e auditado do CP03
│   ├── final_cases.json                       # Suite combinada de 21 casos do CP03
│   ├── final_cases.results.json               # Evidência CP03 em Python 3.9.6 (13 PASS / 8 FAIL)
│   ├── final_cases.results.py312.json         # Evidência CP03 em Python 3.12.7 (13 PASS / 8 FAIL)
│   ├── verify_br05_independence.py            # Procedimento de teste computacional de BR-05
│   ├── br05_independence.results.json         # Evidência BR-05 em Python 3.9.6 (PASS)
│   ├── br05_independence.py312.json          # Evidência BR-05 em Python 3.12.7 (PASS)
│   └── audit_project.py                       # Script preliminar de auditoria do CP03
└── Trabalho_CP4/                              # Checkpoint 4 — Execuções, Evidências e Fecho
    ├── CP4.md                                 # Plano de Execução de Testes e Gestão de Evidências
    ├── Relatorio_CP4.md                       # Relatório Técnico Integral do CP04
    ├── human_cases_cp4.json                   # Suite humana integral (17 casos: H-ENV + H-01..H-16)
    ├── final_cases.json                       # Suite final combinada oficial de 30 casos (H-01..16 + F-17..30)
    ├── audit_cp4.py                           # Automação de auditoria formal das 11 áreas normativas
    ├── update_workbook_cp4.py                 # Script gerador do livro de cálculo oficial OpenXML
    ├── TestResults_T08_Template.xlsx          # Cópia de trabalho do workbook oficial atualizado
    ├── runs/                                  # Registos brutos de execução oficial em formato JSON
    │   ├── human_17_execution.json            # Execução da suite humana de 17 casos (11 PASS / 6 FAIL)
    │   ├── ai_candidates_execution.json       # Execução original dos 12 candidatos IA (10 PASS / 2 FAIL)
    │   ├── final_cases_execution.json         # Execução da suite final de 30 casos em Py 3.9 (20 PASS / 10 FAIL)
    │   └── final_cases_execution.py312.json   # Execução da suite final de 30 casos em Py 3.12 (20 PASS / 10 FAIL)
    └── evidence/                              # Evidências especializadas de controlo e robustez
        ├── br05_independence_cp4.json         # Evidência computacional das 4 propriedades BR-05 (PASS)
        └── runner_robustness_evidence.json    # Evidência dos 5 cenários de robustez do runner (Exit Code 2)
```

---

## 3. Síntese dos Resultados Oficiais de Execução

| Suite de Testes | Ficheiro Fonte | Casos | PASS | FAIL | Taxa de Conformidade |
|---|---|:---:|:---:|:---:|:---:|
| **Humana (com H-ENV)** | `Trabalho_CP4/human_cases_cp4.json` | **17** | **11** | **6** | 64.7% |
| **Candidatos IA Originais** | `TVSI_T08_Students_B1.0/app/ai_candidates.json` | **12** | **10** *(runner)* | **2** | 83.3% *(aparente)* |
| **Suite Final Combinada** | `Trabalho_CP4/final_cases.json` | **30** | **20** | **10** | 66.7% |

> **Nota Metodológica Crucial:** Os casos `AI-05` e `AI-06` obtêm `PASS` no runner original porque as expectativas fornecidas pela IA reproduzem os próprios defeitos do código. A avaliação humana independente das regras de negócio demonstrou que estes casos contêm expectativas inválidas (`DATA-01` e `DATA-02`), tendo sido rejeitados na revisão. O runner histórico foi preservado sem adulteração artificial.

---

## 4. Instruções de Reprodução e Execução

### Requisitos
- **Python:** Versão 3.10 ou superior (ou Python 3.9.6 do macOS, com paridade demonstrada).
- **Sem dependências externas:** O projeto utiliza estritamente módulos padrão do Python.

### Execução da Suite Final do CP04 (30 casos)
```bash
PYTHONPATH=TVSI_T08_Students_B1.0/app python3 TVSI_T08_Students_B1.0/app/run_cases.py Trabalho_CP4/final_cases.json
```
*Gera `Trabalho_CP4/final_cases.results.json` com 20 PASS e 10 FAIL (exit code 1).*

### Execução da Suite Humana do CP04 (17 casos)
```bash
PYTHONPATH=TVSI_T08_Students_B1.0/app python3 TVSI_T08_Students_B1.0/app/run_cases.py Trabalho_CP4/human_cases_cp4.json
```
*Gera `Trabalho_CP4/human_cases_cp4.results.json` com 11 PASS e 6 FAIL (exit code 1).*

### Execução dos Candidatos Originais de IA (12 casos)
```bash
PYTHONPATH=TVSI_T08_Students_B1.0/app python3 TVSI_T08_Students_B1.0/app/run_cases.py TVSI_T08_Students_B1.0/app/ai_candidates.json
```
*Gera 10 PASS e 2 FAIL (exit code 1).*

### Validação da Regra de Independência BR-05 (4 Propriedades)
```bash
python3 Trabalho_CP3/verify_br05_independence.py
```
*Demonstra determinismo, ausência de estado residual, imutabilidade e isolamento de ficheiros (veredicto PASS).*

### Execução da Auditoria Automatizada Completa do CP04
```bash
python3 Trabalho_CP4/audit_cp4.py
```
*Audita as 11 áreas normativas, baseline, integridade do Excel, correspondência de requisitos e conformidade do ZIP.*

---

## 5. Rastreabilidade de Defeitos de Software (`shipping.py`)

A baseline oficial `shipping.py` foi preservada intacta, isolando quatro defeitos de implementação:

| ID | Regra | Localização | Descrição do Defeito | Casos que Falham na Suite Final |
|---|:---:|:---:|---|---|
| **DEF-01** | BR-01 | Linha 3 | `weight >= 20000`: off-by-one rejeita peso máximo válido (20000g) como `INVALID`. | `H-07` |
| **DEF-02** | BR-02 | Linha 7 | `weight < 1000`: off-by-one cobra tarifa de Tier 2 (8€) a 1000g em vez de Tier 1 (5€). | `H-03` |
| **DEF-03** | BR-03 | Linha 14 | `fee = 4`: sobrescrita destrutiva da taxa base em encomendas para zona `REMOTE`. | `H-10, H-12, H-13, F-18, F-29` |
| **DEF-04** | BR-04 | Linha 5 | `weight > 10000`: limiar de indisponibilidade `REMOTE + express` em 10kg em vez de 5kg. | `H-14, F-19, F-30` |

*Total de falhas na suite final: 1 (DEF-01) + 1 (DEF-02) + 5 (DEF-03) + 3 (DEF-04) = 10 casos FAIL.*

---

## 6. Utilização de Inteligência Artificial e Declaração de Autoria

- **Fixture Inicial de IA (`ai_candidates.json`):** Gerado por Codex (GPT-6) no âmbito pedagógico da UC.
- **Ferramenta de Assistência do Grupo:** Claude Sonnet 4.6 (Anthropic Claude Code) utilizado como acelerador de desenvolvimento e testes.
- **Supervisão e Decisão Humana:** 100% das asserções, inputs, resultados esperados e classificações de defeitos foram verificados manualmente pela equipa com base estrita nas regras BR-01 a BR-08.
