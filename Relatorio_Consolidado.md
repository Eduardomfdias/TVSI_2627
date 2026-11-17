# Tecnologias e Verificação de Sistemas de Informação 2026/27
## T08 — Desenho de Testes com Assistência de IA
### Relatório Técnico Consolidado de Testes e Auditoria (CP01, CP02, CP03 e CP04)

**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5  
**Autores:**  
- Eduardo Dias  
- Rui Carneiro  
- Érica Moreira  
- Beatriz Barbosa  
**Data:** 16 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git` (Ramo `main`)

---

# Resumo Executivo

O presente documento constitui o relatório técnico consolidado do Trabalho T08 (*AI-Assisted Test Design*) no âmbito da unidade curricular de TVSI 2026/27, integrando de forma cumulativa, consistente e auditável as atividades, decisões metodológicas, desenhos de teste, execuções e evidências desenvolvidas ao longo dos quatro checkpoints (**CP01, CP02, CP03 e CP04**).

O objeto de teste é a função `quote(weight, zone, express)` implementada no módulo `shipping.py` (build fornecida `T08-B1.0`), destinada ao cálculo tarifário de expedição de encomendas em gramas com base em 8 regras de negócio normativas (**BR-01 a BR-08**).

A metodologia assentou na derivação rigorosa de um **oráculo independente** ancorado estritamente na especificação legal, no desenho manual prévio de **16 casos de teste humanos** (`H-01` a `H-16`) congelados no CP02 (commit `54ec4d3`) antes de qualquer inspeção da ferramenta de IA, na subsequente avaliação crítica no CP03 de **12 casos candidatos gerados por IA** (`AI-01` a `AI-12`), e na consolidação integral no CP04 da **gestão de evidências e execução sistemática**.

No âmbito do CP04, a suite final expandiu-se de 21 para **30 casos de teste** (`H-01` a `H-16` e `F-17` a `F-30`), integrando os casos humanos originais, os candidatos de IA aceites e revistos, e novos cenários de robustez de tipos (pesos float, express não-booleano), espaços em strings, valores negativos e fronteiras ampliadas de disponibilidade. A execução da suite final foi validada nos interpretadores **Python 3.9.6** (baseline local) e **Python 3.12.7** (requisito formal de conformidade), obtendo-se paridade estrita: **20 PASS / 10 FAIL**.

Os 10 resultados FAIL isolam com exatidão matemática quatro defeitos estruturais na implementação de `shipping.py` (**DEF-01 a DEF-04**). Foi igualmente demonstrada a independência funcional e ausência de efeitos secundários (**BR-05**) nas quatro dimensões computacionais exigidas. A auditoria confirmou que o runner original sobre os 12 candidatos de IA reportou **10 PASS e 2 FAIL**, revelando que os casos `AI-05` e `AI-06` constituem falsos positivos resultantes de oráculos erróneos gerados por IA que mascaram os defeitos do código (**DATA-01 e DATA-02**). O livro de cálculo oficial (`TestResults_T08_Template.xlsx`) foi preenchido com coluna autónoma de requisitos, separação estrita de resultados esperados e observados, 100% de cobertura normativa e estrutura OpenXML validada.

---

# Índice Geral

- [Resumo Executivo](#resumo-executivo)
- [PARTE I – ENQUADRAMENTO GERAL](#parte-i--enquadramento-geral)
  - [1. Identificação e Organização do Grupo](#1-identificação-e-organização-do-grupo)
  - [2. Objetivos e Âmbito do Projeto](#2-objetivos-e-âmbito-do-projeto)
  - [3. Sistema em Teste e Ambiente de Teste](#3-sistema-em-teste-e-ambiente-de-teste)
  - [4. Regras de Negócio e Critérios de Aceitação (BR-01 a BR-08)](#4-regras-de-negócio-e-critérios-de-aceitação-br-01-a-br-08)
  - [5. Estratégia e Plano de Testes](#5-estratégia-e-plano-de-testes)
  - [6. Riscos, Prioridades e Critérios de Conclusão](#6-riscos-prioridades-e-critérios-de-conclusão)
- [PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS](#parte-ii--desenvolvimento-dos-checkpoints)
  - [7. CP01 — Charter and Environment](#7-cp01--charter-and-environment)
  - [8. CP02 — Static Review, Test Model and Oracle](#8-cp02--static-review-test-model-and-oracle)
    - [8.1. Revisão Estática e Ambiguidades](#81-revisão-estática-e-ambiguidades)
    - [8.2. Modelo de Teste e Oráculo Independente](#82-modelo-de-teste-e-oráculo-independente)
    - [8.3. Desenho e Congelamento da Suite Humana](#83-desenho-e-congelamento-da-suite-humana)
    - [8.4. Execução e Identificação de Defeitos](#84-execução-e-identificação-de-defeitos)
    - [8.5. Conclusões do CP02](#85-conclusões-do-cp02)
  - [9. CP03 — AI-Assisted Test Design and Final Validation](#9-cp03--ai-assisted-test-design-and-final-validation)
    - [9.1. Proveniência e Auditoria dos Candidatos IA](#91-proveniência-e-auditoria-dos-candidatos-ia)
    - [9.2. Construção da Suite Combinada (21 Casos)](#92-construção-da-suite-combinada-21-casos)
    - [9.3. Execução Dual Python (3.9.6 e 3.12.7)](#93-execução-dual-python-396-e-3127)
    - [9.4. Rastreabilidade Rigorosa de Defeitos](#94-rastreabilidade-rigorosa-de-defeitos)
    - [9.5. Matriz de Cobertura de Requisitos](#95-matriz-de-cobertura-de-requisitos)
    - [9.6. Demonstração Formal de BR-05](#96-demonstração-formal-de-br-05)
    - [9.7. Avaliação Crítica da Utilização de IA](#97-avaliação-crítica-da-utilização-de-ia)
  - [10. CP04 — Execução de Testes e Gestão de Evidências](#10-cp04--execução-de-testes-e-gestão-de-evidências)
    - [10.1. Planeamento e Preservação da Suite Humana Congelada (17 Entradas)](#101-planeamento-e-preservação-da-suite-humana-congelada-17-entradas)
    - [10.2. Execução dos Candidatos de IA e Discrepâncias de Oráculo](#102-execução-dos-candidatos-de-ia-e-discrepâncias-de-oráculo)
    - [10.3. Suite Final de 30 Casos e Execução Dual-Runtime](#103-suite-final-de-30-casos-e-execução-dual-runtime)
    - [10.4. Matriz Rastreabilidade de Defeitos de Software vs Qualidade IA](#104-matriz-rastreabilidade-de-defeitos-de-software-vs-qualidade-ia)
    - [10.5. Cobertura de Requisitos e Auditoria do Livro de Cálculo Oficial](#105-cobertura-de-requisitos-e-auditoria-do-livro-de-cálculo-oficial)
    - [10.6. Execuções Concluídas, Execuções Pendentes e Bloqueios](#106-execuções-concluídas-execuções-pendentes-e-bloqueios)
    - [10.7. Automação de Auditoria e Validação Criptográfica](#107-automação-de-auditoria-e-validação-criptográfica)
- [PARTE III – CONCLUSÃO E ENTREGA](#parte-iii--conclusão-e-entrega)
  - [11. Conclusões Gerais](#11-conclusões-gerais)
  - [12. Declaração Formal de Utilização de IA](#12-declaração-formal-de-utilização-de-ia)
  - [13. Anexos e Tabelas Consolidadas](#13-anexos-e-tabelas-consolidadas)

---

# PARTE I – ENQUADRAMENTO GERAL

## 1. Identificação e Organização do Grupo

- **Instituição:** Universidade do Minho — Escola de Engenharia
- **U.C.:** Tecnologias e Verificação de Sistemas de Informação (TVSI) — Ano Letivo 2026/27
- **Trabalho:** T08 — AI-Assisted Test Design (Build sob teste: `T08-B1.0`)
- **Grupo:** Grupo 5

| Membro | Papel Principal | Responsabilidades |
|---|---|---|
| **Eduardo Dias** | Test Lead & Architect | Revisão estática BR-01–BR-08, modelação do oráculo independente, definição de partições/fronteiras, desenho de casos humanos, supervisão do CP01 a CP04. |
| **Rui Carneiro** | Test Designer & QA Automation | Desenho de testes de robustez, automação de runners e scripts de auditoria (`audit_cp4.py`), verificação de efeitos secundários (BR-05) e gestão de evidências. |
| **Érica Moreira** | AI Test Evaluator & Runner Lead | Auditoria crítica dos 12 candidatos de IA, classificação accept/revise/reject, execução operacional do runner oficial e catalogação de evidências. |
| **Beatriz Barbosa** | Coverage & Metrics Analyst | Matriz de rastreabilidade de requisitos (BR-01–BR-08), auditoria e verificação do workbook oficial (`TestResults_T08_Template.xlsx`), análise de riscos residuais. |

## 2. Objetivos e Âmbito do Projeto

1. **Avaliação Crítica de IA:** Avaliar o contributo e as falhas do desenho de testes gerado por modelos de inteligência artificial em comparação direta com a engenharia de testes humana independente.
2. **Oráculo Independente:** Estabelecer uma especificação formal de resultados esperados antes da inspeção do código da aplicação ou das sugestões da IA, tratando a implementação como caixa-negra falível.
3. **Preservação de Evidências:** Manter registos imutáveis e auditáveis de cada execução e decisão técnica.
4. **Isolamento de Defeitos:** Identificar e caraterizar com rigor defeitos de software na implementação sem confundir com problemas de dados de teste da IA.

## 3. Sistema em Teste e Ambiente de Teste

- **Objeto:** Função `quote(weight, zone, express)` no ficheiro `shipping.py` da build oficial `T08-B1.0`.
- **Ambiente de Teste:**
  - Python 3.9.6 (ambiente base macOS Darwin 24.1.0)
  - Python 3.12.7 (interpretador formal de referência para validação 3.10+)
  - Runner oficial: `TVSI_T08_Students_B1.0/app/run_cases.py`

## 4. Regras de Negócio e Critérios de Aceitação (BR-01 a BR-08)

- **BR-01 (Validação de Entrada):** `weight` é inteiro em gramas $\in [1, 20\,000]$ (excluindo booleanos). `zone` é string sensível a maiúsculas $\in \{\text{"LOCAL"}, \text{"REMOTE"}\}$. `express` é booleano estrito. Se inválido: `{"status": "INVALID", "fee": null}`.
- **BR-02 (Tarifas Base por Escalão):**
  - $\le 1\,000\text{ g}$: 5€ (Tier 1)
  - $1\,001\text{ g a } 5\,000\text{ g}$: 8€ (Tier 2)
  - $5\,001\text{ g a } 20\,000\text{ g}$: 12€ (Tier 3)
- **BR-03 (Suplementos):** Destino `"REMOTE"` adiciona taxa fixa de 4€ sobre a tarifa base. Serviço expresso adiciona 6€ sobre a tarifa base. As taxas são cumulativas (se aplicáveis ambas: base + 4€ + 6€).
- **BR-04 (Disponibilidade do Serviço Expresso):** Expresso disponível para todas as encomendas `"LOCAL"`. Para `"REMOTE"`, disponível apenas para peso $\le 5\,000\text{ g}$. Para peso $> 5\,000\text{ g}$ em `"REMOTE"` com `express=True`: `{"status": "UNAVAILABLE", "fee": null}`.
- **BR-05 (Independência e Ausência de Efeitos Secundários):** Função pura sem efeitos secundários, determinística e sem mutação de estado.
- **BR-06 (Formato e Runner):** Casos em ficheiro JSON com runner padrão sem dependências `pip`.
- **BR-07 (Avaliação do Runner):** Correspondência exata em todos os campos; exit code 0=PASS, 1=FAIL, 2=blocked/erro.
- **BR-08 (Rastreabilidade e Declaração de IA):** Transparência integral e verificação humana mandatória.

## 5. Estratégia e Plano de Testes

- Caixa-negra estrita assente em Particionamento de Equivalência (EP) e Análise de Valores Limite (BVA).
- Oráculo derivado antes da execução.
- Congelamento prévio da suite humana antes de aceder aos candidatos de IA.
- Paridade dual-runtime e integridade criptográfica.

## 6. Riscos, Prioridades e Critérios de Conclusão

- Risco de contaminação de oráculo mitigado por derivação formal independente.
- Risco de confusão entre defeitos de código e dados de teste de IA mitigado por classificação diferenciada (`DEF` vs `DATA`).

---

# PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS

## 7. CP01 — Charter and Environment
- Charter formal do projeto aprovado.
- Caso de teste `H-ENV` (`weight=500, zone='LOCAL', express=False`) executado com sucesso: `PASS`.

## 8. CP02 — Static Review, Test Model and Oracle
- Revisão estática identificou ambiguidades REV-01 a REV-04.
- Oráculo independente formalizado.
- **Congelamento da Suite Humana:** 16 casos de teste (`H-01` a `H-16`) congelados no commit `54ec4d3` a 30 de outubro de 2026.
- Execução inicial da suite humana revelou os primeiros indícios de 4 defeitos estruturais no código.

## 9. CP03 — AI-Assisted Test Design and Final Validation
- Revisão crítica dos 12 candidatos de IA (`ai_candidates.json`): 2 aceites (`AI-11` → `F-17`, `AI-12` → `F-18`), 1 revisto (`AI-09` → `F-19`), 9 rejeitados por redundância ou oráculo erróneo.
- Primeira versão combinada da suite final (21 casos: 13 PASS / 8 FAIL).
- Validação formal das 4 propriedades computacionais de BR-05.

---

## 10. CP04 — Execução de Testes e Gestão de Evidências

### 10.1. Planeamento e Preservação da Suite Humana Congelada (17 Entradas)

A suite humana utilizada no CP04 preserva integralmente os 16 casos de teste concebidos e congelados no CP02 (H-01 a H-16), sendo acompanhada pelo caso técnico H-ENV para validação do ambiente. O conjunto contém, assim, 17 entradas, sem introdução retroativa de casos apresentados como independentes da revisão dos candidatos de IA.

A execução oficial da suite humana de 17 entradas em Python 3.9 e Python 3.12 devolveu rigorosamente:
- **11 PASS:** `H-ENV, H-01, H-02, H-04, H-05, H-06, H-08, H-09, H-11, H-15, H-16`
- **6 FAIL:** `H-03` (DEF-02), `H-07` (DEF-01), `H-10` (DEF-03), `H-12` (DEF-03), `H-13` (DEF-03), `H-14` (DEF-04)

### 10.2. Execução dos Candidatos de IA e Discrepâncias de Oráculo

A suite original de candidatos de IA (`ai_candidates.json`) foi executada no runner oficial `run_cases.py` com o seguinte resultado:
- **10 PASS:** `AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, AI-08, AI-10, AI-11`
- **2 FAIL:** `AI-09, AI-12`

**Auditoria de Qualidade das Expectativas de IA:**  
Conforme demonstrado na auditoria, o resultado aparentemente elevado (10 PASS) oculta falhas conceituais graves:
1. `AI-05` (500g, REMOTE, False) devolve PASS no runner porque a expectativa da IA omitiu a tarifa base (`fee: 4`), coincidindo com o bug da linha 14 (`fee = 4`). O oráculo independente determina 9€ (`DATA-01`).
2. `AI-06` (1000g, LOCAL, False) devolve PASS porque a IA atribuiu 8€ de Tier 2 a 1000g, coincidindo com o bug da linha 7 (`weight < 1000`). O oráculo independente determina 5€ (`DATA-02`).
3. `AI-09` (6000g, REMOTE, True) devolve FAIL porque a IA calculou tarifa para serviço indisponível. Revisto para oráculo legal `UNAVAILABLE` (`DATA-03`).

### 10.3. Suite Final de 30 Casos e Execução Dual-Runtime

Para o encerramento do CP04, a suite final combinada foi formalmente expandida para **30 casos de teste** (`Trabalho_CP4/final_cases.json`), integrando:
- Os 16 casos humanos congelados (`H-01` a `H-16`).
- Os 5 casos derivados do CP03 (`F-17` a `F-21`).
- Nove casos complementares de robustez, limites e classes de equivalência (`F-22` a `F-30`):
  - `F-22`: Rejeição de peso float (`weight=500.5` $\to$ `INVALID`).
  - `F-23`: Rejeição de zona com espaços (`zone=' LOCAL '` $\to$ `INVALID`).
  - `F-24`: Combinação nominal Tier 2 express LOCAL (`weight=2000, express=True` $\to$ `OK, fee=14`).
  - `F-25`: Rejeição de zona fora de domínio (`zone='INTERNATIONAL'` $\to$ `INVALID`).
  - `F-26`: Rejeição de peso negativo (`weight=-100` $\to$ `INVALID`).
  - `F-27`: Rejeição de express em formato string (`express='False'` $\to$ `INVALID`).
  - `F-28`: Ponto interior Tier 3 LOCAL (`weight=6000, express=False` $\to$ `OK, fee=12`).
  - `F-29`: Ponto interior Tier 3 REMOTE (`weight=6000, express=False` $\to$ `OK, fee=16`, expondo `DEF-03`).
  - `F-30`: Limiar interior de indisponibilidade express REMOTE (`weight=8000, express=True` $\to$ `UNAVAILABLE`, expondo `DEF-04`).

**Resultados da Execução da Suite Final (Python 3.9.6 e Python 3.12.7):**
- **20 PASS:** `H-01, H-02, H-04, H-05, H-06, H-08, H-09, H-11, H-15, H-16, F-17, F-20, F-21, F-22, F-23, F-24, F-25, F-26, F-27, F-28`
- **10 FAIL:** `H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30`
- **Paridade:** 100% de paridade entre ambos os ambientes.

### 10.4. Matriz Rastreabilidade de Defeitos de Software vs Qualidade IA

| Defeito de Software | Regra | Localização | Casos Detetores na Suite Final | Severidade |
|---|:---:|:---:|---|:---:|
| **DEF-01** | BR-01 | Linha 3 (`>= 20000`) | `H-07` | Alta |
| **DEF-02** | BR-02 | Linha 7 (`< 1000`) | `H-03` | Média-Alta |
| **DEF-03** | BR-03 | Linha 14 (`fee = 4`) | `H-10, H-12, H-13, F-18, F-29` | Crítica |
| **DEF-04** | BR-04 | Linha 5 (`> 10000`) | `H-14, F-19, F-30` | Alta |

| Problema de Dados de Teste IA | Regra | Candidato | Expectativa IA | Oráculo Independente | Classificação |
|---|:---:|:---:|:---:|:---:|:---:|
| **DATA-01** | BR-03 | `AI-05` | `OK, 4` | `OK, 9` | Omissão de taxa base (replica DEF-03) |
| **DATA-02** | BR-02 | `AI-06` | `OK, 8` | `OK, 5` | Erro de fronteira (mascara DEF-02) |
| **DATA-03** | BR-04 | `AI-09` | `OK, 22` | `UNAVAILABLE, null` | Tarifação indevida de serviço indisponível |

### 10.5. Cobertura de Requisitos e Auditoria do Livro de Cálculo Oficial

O livro oficial `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` foi integralmente atualizado e auditado:
- **Folha Executions:** Contém coluna autónoma `Requirement ID(s)` (coluna C), separação formal de Expected Result e Observed Result, identificação completa de testers com papéis de Execução, Supervisão e Validação, e histórico consolidado de 68 execuções (CP01, CP02, CP03, CP04, BR-05 e Robustez).
- **Folha Coverage:** 100% de cobertura alcançada nas 8 regras (R01: 15 testes, R02: 17 testes, R03: 10 testes, R04: 5 testes, R05: 2 testes, R06: 7 testes, R07: 5 testes, R08: 4 testes). Zero testes não-executados. Zero erros `#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`, `#N/A`.
- **Folhas Test Cases, Defects, Static Review e Technique:** Integralmente sincronizadas.

### 10.6. Execuções Concluídas, Execuções Pendentes e Bloqueios

- **Execuções Concluídas:** Suite humana (17 casos: 11 PASS / 6 FAIL); Suite IA original (12 casos: 10 PASS / 2 FAIL no runner); Suite final (30 casos: 20 PASS / 10 FAIL em Py 3.9 e Py 3.12); Controlo de robustez do runner perante exit code 2 (5 cenários: PASS); Independência BR-05 (4 propriedades: PASS).
- **Execuções Pendentes:** Ações de submissão externa humana (registo de números mecanográficos no formulário da UMinho, submissão do ZIP no Moodle e push do commit de fecho).
- **Bloqueios:** **Zero bloqueios técnicos.**

### 10.7. Automação de Auditoria e Validação Criptográfica

Foi desenvolvido e executado o script [`Trabalho_CP4/audit_cp4.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP4/audit_cp4.py), que valida automaticamente as 11 áreas normativas do projeto, confirmando zero falhas críticas.

---

# PARTE III – CONCLUSÃO E ENTREGA

## 11. Conclusões Gerais

1. **Eficácia Analítica:** O projeto demonstrou que a engenharia de testes humana independente, suportada por oráculos deduzidos de regras formais de negócio, é a única garantia contra defeitos subtis de software que modelos generativos tendem a replicar ou mascarar.
2. **Conformidade Normativa:** Todos os requisitos da U.C. e dos documentos normativos docentes foram respeitados integralmente.
3. **Estado de Fecho:** O Checkpoint 4 encontra-se tecnicamente concluído, validado e pronto para entrega académica.

## 12. Declaração Formal de Utilização de IA

- **Codex (GPT-6):** Geração do fixture inicial de candidatos de IA (`ai_candidates.json`) fornecido pelo docente.
- **Claude Sonnet 4.6 (Claude Code):** Assistência na automação de testes, manipulação OpenXML e suporte à redação técnica.
- **Supervisão Humana:** 100% dos parâmetros de teste, oráculos e classificações de defeitos foram verificados e validados pelos quatro autores humanos do Grupo 5.

---

## 13. Anexos e Tabelas Consolidadas

### Tabela Consolidada de Defeitos de Software (`shipping.py`)

| Defeito | BR | Linha | Descrição da Causa Raiz | Impacto | Casos Detetores |
|---|:---:|:---:|---|---|---|
| **DEF-01** | BR-01 | Linha 3 | `weight >= 20000` em vez de `> 20000` | Rejeição indevida do limite superior válido (20000g). | `H-07` |
| **DEF-02** | BR-02 | Linha 7 | `weight < 1000` em vez de `<= 1000` | Cobrança excessiva de tarifa de Tier 2 a 1000g. | `H-03` |
| **DEF-03** | BR-03 | Linha 14 | `fee = 4` em vez de `fee += 4` | Sobrescrita destrutiva da tarifa base em REMOTE. | `H-10, H-12, H-13, F-18, F-29` |
| **DEF-04** | BR-04 | Linha 5 | `weight > 10000` em vez de `> 5000` | Limiar incorreto de indisponibilidade REMOTE express. | `H-14, F-19, F-30` |
