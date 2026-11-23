# CP05 — Consolidação de Resultados, Cobertura e Riscos Residuais

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27**
**T08 — Desenho de Testes com Assistência de IA · Build T08-B1.0 · Grupo 5**
Eduardo Dias (pg61456) · Rui Carneiro (pg63791) · Érica Moreira (pg65641) · Beatriz Barbosa (pg63744)
Checkpoint de progresso — 24 de novembro de 2026

---

## 1. Identificação da Entrega e Estado Atual

O presente documento corresponde à entrega oficial do quinto checkpoint (**CP05 — Consolidated findings and coverage**), no âmbito do trabalho prático T08. O objetivo central é consolidar os resultados das execuções realizadas, auditar e corrigir a rastreabilidade requisito–teste–execução, explicar a cobertura alcançada e as respetivas lacunas, auditar os relatórios de defeitos em modo estritamente black-box, e preparar com rigor os artefactos e prioridades para a entrega final (CP06). Este documento não constitui o relatório final de projeto, mas sim um relatório de progresso e consolidação técnica.

### 1.1 Estado do Projeto por Categorias de Trabalho

Para garantir total transparência metodológica, o estado atual do trabalho reparte-se da seguinte forma:

- **Trabalho concluído:**
  - Reposição e verificação criptográfica da baseline original do docente (`TVSI_T08_Students_B1.0/`, SHA-256 intactos conforme commit original `9d9f950`).
  - Re-execução das três suites oficiais (`human_cases_cp4.json`, `ai_candidates.json`, `final_cases.json`) em ambiente conforme (Python 3.12.16, macOS arm64, `RUN-CP5-20261122-212810`), sob flags isoladas `-E -s`, com integridade criptográfica verificada antes e depois.
  - Reprodução isolada dos quatro defeitos confirmados (3 repetições independentes em processos novos por defeito).
  - Oráculo independente formalizado em `tools/oracle.py`, derivado exclusivamente do texto normativo de BR-01 a BR-05.
  - Consolidação dos defect reports (DEF-01 a DEF-04) sem especulação de código-fonte (estritamente black-box), e separação inequívoca de defeitos de dados do fixture (`DATA-01` a `DATA-03`) e de redundâncias (`AI-10`, `F-19`, `F-30`, `F-28`).
  - Correção integral da rastreabilidade na folha Coverage de `TestResults_T08_CP05.xlsx`: remoção da ligação espúria R05–H-ENV e remoção das associações artificiais de casos da função `quote()` aos requisitos processuais R06–R08.
  - Análise comparativa humano vs. IA em suites de igual dimensão (T6).
- **Trabalho em curso:**
  - Revisão crítica documental e consolidação dos registos históricos de CP01 a CP04.
  - Elaboração da estrutura cumulativa para o relatório final.
- **Trabalho ainda não iniciado:**
  - Correção da implementação de `shipping.py` e respetiva regressão completa (tarefa de CP06).
- **Trabalho bloqueado:**
  - Execução dos 17 casos de lacuna (`F-31` a `F-47`): bloqueada aguardando validação humana independente antes da execução formal no runner, respeitando o princípio *design before execution*.
  - Re-execução formal em Python 3.10+ dos testes de processo e independência (`P-BR05-01..04` e `P-ROB-01..05`): bloqueada localmente no ambiente de auditoria por restrição de interpretador Python (disponibilidade local de Python 3.9.6, pendente de execução no ambiente 3.12 do grupo).
- **Questões por confirmar:**
  - Registo nominal do operador de execução (`Tester: a confirmar`) nos ficheiros `ENVIRONMENT.txt` de CP05.
  - Validação humana independente (revisor e data) da tabela de expectativas dos casos `F-31` a `F-47`.

---

## 2. Evolução Histórica do Projeto (CP01–CP04)

| Checkpoint | Trabalho realizado | Resultado e Evidência |
|---|---|---|
| **CP01 — Charter e ambiente** | Definição de papéis, âmbito black-box, riscos e prioridades; verificação de ambiente com H-ENV; revisão estática inicial de BR-01 a BR-08 | H-ENV funcionalmente aprovado; limitação: ambiente original em Python 3.9.6 (abaixo de 3.10+) |
| **CP02 — Desenho humano independente** | Derivação do modelo de partições e fronteiras; desenho e congelamento de 16 casos humanos (H-01 a H-16); primeira execução | 10 PASS / 6 FAIL; descoberta dos quatro defeitos fundamentais (DEF-01 a DEF-04) |
| **CP03 — Revisão IA e suite final** | Classificação dos 12 candidatos do fixture IA (2 aceites, 1 revisto, 9 rejeitados); construção da suite final de 21 casos; testes de independência BR-05 | Identificação de 3 expectativas erradas no fixture IA (AI-05, AI-06, AI-09); suite final 13 PASS / 8 FAIL |
| **CP04 — Execução e defeitos** | Expansão da suite final para 30 casos; execução das suites; registo no workbook; consolidação de defeitos | Final: 20 PASS / 10 FAIL; humana: 11 PASS / 6 FAIL; IA: 10 PASS / 2 FAIL |

---

## 3. Correções ao Trabalho Entregue no CP04

*Tabela 1 — Problemas identificados na auditoria, motivo e correção efetuada no CP05*

| # | Problema identificado | Motivo da correção | Correção efetuada no CP05 |
|---|---|---|---|
| 1 | Template do docente substituído na pasta original e texto adicionado a `AI_PROVENANCE.md` | O enunciado exige estrita preservação da baseline do docente ("Save a working copy") | Reposição integral dos ficheiros da baseline a partir do commit original `9d9f950`. SHA-256 conferidos. O texto do grupo foi arquivado em `evidence/baseline_restauro_20261122/` e integrado no `AI_DISCLOSURE.md` |
| 2 | O workbook de CP04 apresentava inconsistências de referências OpenXML (KeyError `rId1`) | Integridade e auditabilidade dos artefactos de teste | Construção de `TestResults_T08_CP05.xlsx` a partir do fluxo reparado, com tabelas e intervalos de fórmulas estendidos até à linha 300, sem erros |
| 3 | Execuções em Python 3.9.6 no CP04, incluindo RUN-ENV-01 | BR-06 exige estritamente Python 3.10+ | Execuções em 3.9.6 preservadas no histórico e anotadas como não conformes. Re-execução oficial em Python 3.12.16 (`RUN-CP5-20261122-212810`) |
| 4 | Defect reports com indicação de linhas de código-fonte como causa-raiz | O charter estabelece uma abordagem puramente black-box baseada na especificação | Remoção de todas as referências ao código-fonte nos defeitos. Relatórios reformulados exclusivamente em torno de setup, input, resultado esperado e sintoma observado |
| 5 | Questões de revisão estática REV-01 a REV-03 citavam a implementação | As ambiguidades resolvem-se pelo texto normativo das BR | Todas as questões foram encerradas com base exclusiva no texto das BR (tipos estritos em BR-01, fronteira de 5000 g em BR-04, precedência em BR-05). Zero questões em aberto |
| 6 | Afirmação de que nenhum defeito fora detetado por candidato IA | Contradição com os resultados de execução | O candidato AI-12 possui expectativa correta segundo as BR e deteta com sucesso o DEF-03 |
| 7 | Afirmações genéricas sobre desempenho de modelos de IA | O fixture é curado pelo docente com defeitos intencionais e não reflete capacidade geral de IA | Conclusões estritamente circunscritas ao material fornecido |
| 8 | Ausência de comparação entre suites de dimensão idêntica | Exigência explícita do enunciado T08 | Execução da análise comparativa T6 fixando H-01..H-12 vs. AI-01..AI-12 |
| 9 | Comparação histórica com CP04 imprecisa | A evidência de 3.12.16 do CP04 cobria apenas 21 casos e não 30 | Esclarecimento explícito da discrepância: divergência de 9 casos sem correspondência por uso de variante prévia no CP04 |
| 10 | Associação espúria de R05–H-ENV e de casos quote() a R06–R08 | H-ENV não testa precedência; testes da função quote() não validam o runner nem o processo | R05–H-ENV removido do workbook; desassociação de quote() de R06–R08; cobertura recalculada estritamente sobre evidências reais |

---

## 4. Resultados Consolidados e Findings (CP05)

### 4.1 Verificação do Oráculo

O oráculo independente (`tools/oracle.py`) deriva exclusivamente de BR-01 a BR-05, sem importar nem inspecionar `shipping.py`. Todas as expectativas das suites humana (H-01..H-16) e final (F-17..F-30) coincidem com o oráculo. No material IA, confirmam-se 3 expectativas incorretas no fixture (`AI-05`, `AI-06`, `AI-09`) e 1 caso redundante (`AI-10`).

### 4.2 Re-execução Oficial em Ambiente Conforme

As três suites foram executadas em ambiente Python 3.12.16 (macOS arm64) no run oficial `RUN-CP5-20261122-212810`. O run imediatamente anterior (`RUN-CP5-20261122-212747`) abortou por invocação com a flag `-I` (que remove o diretório de trabalho de `sys.path`), tendo sido preservado na íntegra com a respetiva explicação (`ABORTED.md`), em cumprimento das regras de integridade.

*Tabela 2 — Resultados consolidados (RUN-CP5-20261122-212810)*

| Suite | Casos | PASS | FAIL | BLOCKED | Exit Code | Casos com FAIL |
|---|---:|---:|---:|---:|---:|---|
| Humana (`human_cases_cp4.json`) | 17 | 11 | 6 | 0 | 1 | H-03, H-07, H-10, H-12, H-13, H-14 |
| IA original (`ai_candidates.json`) | 12 | 10 | 2 | 0 | 1 | AI-09 (expectativa errada), AI-12 (deteta DEF-03) |
| Final (`final_cases.json`) | 30 | 20 | 10 | 0 | 1 | H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30 |
| Lacunas (`gap_cases.json`) | 17 | — | — | 17 | — | Não executados (desenho congelado; pendentes de validação humana e execução em CP06) |

**Análise da Comparação Histórica com CP04 (`comparacao_cp4.txt`):**
1. Face à execução CP04 em Python 3.12.7 (`final_cases_execution.py312.json`): Coincidência absoluta nos 30 casos da suite final, sem qualquer divergência.
2. Face à execução CP04 em Python 3.12.16 (`RUN-CP4-20261115-162457`): A suite então executada continha apenas 21 casos (variante de transição do CP03). Consequentemente, existem 9 casos (`F-22` a `F-30`) sem resultado correspondente no histórico dessa execução específica. Não há divergência nos casos comuns (H-01..H-16 e F-17..F-21).
3. Face às execuções CP04 em Python 3.9.6 das suites humana e IA: Coincidência integral nos resultados funcionais, mas sob ambiente que violava a norma BR-06.

### 4.3 Defeitos Confirmados de Implementação

Todos os defeitos foram reproduzidos isoladamente 3 vezes em processos interpretadores novos (`python -E -s`), a partir de condições limpas, com 100% de consistência.

*Tabela 3 — Defeitos confirmados da aplicação (visão black-box)*

| ID | Sintoma Observado | Regra Violada | Input de Teste | Esperado (BR) | Observado | Severidade | Testes de Suporte |
|---|---|---|---|---|---|---|---|
| **DEF-01** | Limite superior válido de 20000 g rejeitado como inválido | BR-01, BR-02 | `{"weight": 20000, "zone": "LOCAL", "express": false}` | `{"status": "OK", "fee": 12}` | `{"status": "INVALID", "fee": null}` | Alta | H-07 |
| **DEF-02** | Fronteira de 1000 g cobrada no escalão de 8 € em vez de 5 € | BR-02 | `{"weight": 1000, "zone": "LOCAL", "express": false}` | `{"status": "OK", "fee": 5}` | `{"status": "OK", "fee": 8}` | Média-Alta | H-03 (e AI-06 com oráculo corrigido) |
| **DEF-03** | Zona REMOTE omite a taxa base na fee final (subcobrança) | BR-03 | `{"weight": 500, "zone": "REMOTE", "express": false}` | `{"status": "OK", "fee": 9}` | `{"status": "OK", "fee": 4}` | Crítica | H-10, H-12, H-13, F-18, F-29, AI-12 (e AI-05 sob oráculo corrigido) |
| **DEF-04** | REMOTE express acima de 5000 g aceite com fee parcial em vez de indisponível | BR-04, BR-05 | `{"weight": 5001, "zone": "REMOTE", "express": true}` | `{"status": "UNAVAILABLE", "fee": null}` | `{"status": "OK", "fee": 10}` | Alta | H-14, F-19, F-30 (e AI-09 sob oráculo corrigido) |

### 4.4 Defeitos de Dados no Material IA e Redundâncias

Para evitar contaminação dos indicadores de qualidade da aplicação, mantêm-se estritamente separados:
- **DATA-01 (AI-05):** O fixture IA espera `fee=4` para `weight=500, REMOTE, express=false`. Esta expectativa omite a taxa base (5 €) e coincide com o comportamento defeituoso da aplicação, gerando um falso PASS no runner.
- **DATA-02 (AI-06):** O fixture IA espera `fee=8` para `weight=1000, LOCAL, express=false`. Coincide com o defeito DEF-02, gerando um falso PASS.
- **DATA-03 (AI-09):** O fixture IA espera `status=OK, fee=22` para `weight=6000, REMOTE, express=true`. A regra BR-04 determina indisponibilidade do serviço (`UNAVAILABLE`). O FAIL emitido pelo runner decorre de expectativa errada da IA e não de capacidade de deteção do teste.
- **Redundâncias:**
  - `AI-10`: Duplicado exato de `AI-01` (`{"weight": 500, "zone": "LOCAL", "express": false}`). Redundância interna do fixture, não constitui defeito.
  - `F-19` e `F-30`: Casos na mesma partição que `H-14` (`> 5000 g, REMOTE, express=true`) para o DEF-04. Mantidos por integridade histórica, assinalados como redundantes.
  - `F-28`: Input idêntico ao rejeitado `AI-03`.

### 4.5 Casos de Lacuna (F-31 a F-47) e Tabela de Revisão

Foram desenhados 17 casos adicionais em `gap_cases.json` e `gap_cases.design.json` para fechar lacunas de cobertura de partições e fronteiras. Em estrito cumprimento do princípio de integridade, estes casos **não foram executados**, permanecendo identificados como pendentes de validação humana independente.

*Tabela 4 — Tabela de revisão formal dos casos de lacuna (F-31 a F-47)*

| ID | Input | Resultado Esperado | BR Aplicável | Justificação Independente | Revisor Humano | Data Validação | Estado |
|---|---|---|---|---|---|---|---|
| F-31 | `weight: null, zone: 'LOCAL', express: false` | `INVALID / null` | BR-01 | Tipo inválido (peso null não coercível) | A confirmar pelo grupo | A confirmar | Pendente |
| F-32 | `weight: '500', zone: 'LOCAL', express: false` | `INVALID / null` | BR-01 | Tipo inválido (string sem coerção) | A confirmar pelo grupo | A confirmar | Pendente |
| F-33 | `weight: 500, zone: null, express: false` | `INVALID / null` | BR-01 | Tipo inválido (zona null) | A confirmar pelo grupo | A confirmar | Pendente |
| F-34 | `weight: 500, zone: '', express: false` | `INVALID / null` | BR-01 | Domínio inválido (zona string vazia) | A confirmar pelo grupo | A confirmar | Pendente |
| F-35 | `weight: 500, zone: 'LOCAL', express: null` | `INVALID / null` | BR-01 | Tipo inválido (express null) | A confirmar pelo grupo | A confirmar | Pendente |
| F-36 | `weight: 1000, zone: 'REMOTE', express: false` | `OK / 9` | BR-02, BR-03 | BVA: limite superior tier 1 (5 €) + REMOTE (4 €) | A confirmar pelo grupo | A confirmar | Pendente |
| F-37 | `weight: 1001, zone: 'REMOTE', express: false` | `OK / 12` | BR-02, BR-03 | BVA: limite inferior tier 2 (8 €) + REMOTE (4 €) | A confirmar pelo grupo | A confirmar | Pendente |
| F-38 | `weight: 5000, zone: 'REMOTE', express: false` | `OK / 12` | BR-02, BR-03 | BVA: limite superior tier 2 (8 €) + REMOTE (4 €) | A confirmar pelo grupo | A confirmar | Pendente |
| F-39 | `weight: 5001, zone: 'REMOTE', express: false` | `OK / 16` | BR-02, BR-03 | BVA: limite inferior tier 3 (12 €) + REMOTE (4 €) | A confirmar pelo grupo | A confirmar | Pendente |
| F-40 | `weight: 20000, zone: 'REMOTE', express: false` | `OK / 16` | BR-01..BR-03 | BVA: peso máximo válido (12 €) + REMOTE (4 €) | A confirmar pelo grupo | A confirmar | Pendente |
| F-41 | `weight: 1000, zone: 'REMOTE', express: true` | `OK / 15` | BR-02..BR-04 | BVA: tier 1 (5 €) + REMOTE (4 €) + express (6 €); disponível | A confirmar pelo grupo | A confirmar | Pendente |
| F-42 | `weight: 1001, zone: 'REMOTE', express: true` | `OK / 18` | BR-02..BR-04 | BVA: tier 2 (8 €) + REMOTE (4 €) + express (6 €); disponível | A confirmar pelo grupo | A confirmar | Pendente |
| F-43 | `weight: 20000, zone: 'REMOTE', express: true` | `UNAVAILABLE / null` | BR-01, BR-04, BR-05 | Precedência: peso válido > 5000 g → disponibilidade antes de fee | A confirmar pelo grupo | A confirmar | Pendente |
| F-44 | `weight: 0, zone: 'REMOTE', express: true` | `INVALID / null` | BR-01, BR-05 | Precedência: validação precede disponibilidade | A confirmar pelo grupo | A confirmar | Pendente |
| F-45 | `weight: 19999, zone: 'LOCAL', express: false` | `OK / 12` | BR-01, BR-02 | BVA: ponto interior fronteira superior (tier 3) | A confirmar pelo grupo | A confirmar | Pendente |
| F-46 | `weight: 10000, zone: 'REMOTE', express: true` | `UNAVAILABLE / null` | BR-04 | Ponto interior de indisponibilidade (⚠ ver nota metodológica) | A confirmar pelo grupo | A confirmar | Pendente |
| F-47 | `weight: 10001, zone: 'REMOTE', express: true` | `UNAVAILABLE / null` | BR-04 | Ponto interior de indisponibilidade (⚠ ver nota metodológica) | A confirmar pelo grupo | A confirmar | Pendente |

**Avaliação Metodológica dos Casos F-46 e F-47:**
A seleção dos valores 10000 e 10001 foi informada pela leitura do código-fonte realizada no CP02 (onde existia um desvio na condição de disponibilidade). Sob a especificação estritamente black-box (BR-04), a única fronteira normativa é 5000 g; os valores 10000 e 10001 não possuem estatuto de fronteira na especificação. A manutenção destes valores no conjunto exploratório permite delimitar o sintoma de DEF-04, mas constitui uma limitação metodológica que se declara abertamente. Para o CP06, avalia-se a introdução de valores interiores neutros (como 12500 e 15000) para complementar a regressão.

---

## 5. Cobertura e Rastreabilidade na Ótica T08

### 5.1 Comparação entre Suites de Igual Dimensão (T6)

Para cumprir o enunciado T08, comparou-se a suite humana truncada aos primeiros 12 casos (H-01 a H-12, por ordem de ID fixada à partida) com os 12 candidatos do fixture IA. Inclui-se a suite humana completa como referência.

*Tabela 5 — Comparação humano vs. IA (T6)*

| Suite | n | Requisitos Cobertos | Fronteiras (de 10) | Expectativas Erradas | Duplicados / Mesma Partição | Defeitos (Expectativa Original) | Defeitos (Oráculo Corrigido) |
|---|---:|---|---:|---:|---|---|---|
| Humana H-01..H-12 | 12 | R01, R02, R03, R04 | 8 | 0 | 0 / 0 | DEF-01, DEF-02, DEF-03 | DEF-01, DEF-02, DEF-03 |
| IA original AI-01..AI-12 | 12 | R01, R02, R03, R04, R05 | 3 | 3 | 1 / 1 | DEF-03 | DEF-02, DEF-03, DEF-04 |
| Humana completa (H-01..H-16) | 16 | R01, R02, R03, R04, R05 | 10 | 0 | 0 / 0 | DEF-01 a DEF-04 | DEF-01 a DEF-04 |

**Conclusões da Comparação:**
- Sob expectativas originais, o fixture IA apenas deteta o DEF-03 (via AI-12), apresentando dois falsos PASS (AI-05 e AI-06) que mascaram defeitos graves.
- Sob oráculo corrigido, os inputs da IA expõem DEF-02, DEF-03 e DEF-04, mas falham a deteção de DEF-01 por ausência de testes no limite máximo (20000 g).
- A suite humana de 12 casos cobre 8 das 10 fronteiras mas falha DEF-04 por o caso H-14 estar na posição 14. A suite humana completa cobre as 10 fronteiras e todos os 4 defeitos.
- Estas conclusões são restritas ao material do trabalho e não autorizam generalizações sobre a competência intrínseca de humanos ou de modelos de IA.

### 5.2 Rastreabilidade Requisito → Teste → Execução

A folha Coverage do workbook consolida a rastreabilidade entre requisitos e testes. Cada par requisito–teste conta como executado apenas se possuir registo com veredicto PASS ou FAIL em `Executions`.

Na auditoria CP05, foi eliminada a ligação espúria R05–H-ENV (pois H-ENV é uma verificação de fee base que não exercita precedência) e foram removidas as associações arbitrárias de testes de `quote()` aos requisitos processuais R06, R07 e R08.

*Tabela 6 — Rastreabilidade dos requisitos R01 a R08*

| Requisito | Ligações Desenhadas | Ligações Executadas | Testes Executados (RUN-CP5-20261122-212810) | Desenhados, Pendentes de Execução |
|---|---:|---:|---|---|
| **R01 / BR-01 — Validação** | 24 | 15 | H-ENV, H-02, H-03, H-07, H-08, H-09, H-15, H-16, F-20..F-23, F-25..F-27 | F-31 a F-35, F-40, F-43 a F-45 |
| **R02 / BR-02 — Fee base** | 25 | 17 | H-ENV, H-01 a H-07, H-10 a H-13, F-17, F-18, F-24, F-28, F-29 | F-36 a F-42, F-45 |
| **R03 / BR-03 — Suplementos** | 17 | 10 | H-01, H-10 a H-13, F-17, F-18, F-24, F-28, F-29 | F-36 a F-42 |
| **R04 / BR-04 — Disponibilidade** | 10 | 5 | H-13, H-14, F-19, F-21, F-30 | F-41 a F-43, F-46, F-47 |
| **R05 / BR-05 — Precedência e independência** | 3 | 1 | F-21 (validação > disponibilidade: PASS) | F-43, F-44 |
| **R06 / BR-06 — Formato e ambiente** | 0 | 0 | — (verificação processual pelo runner em Python 3.12.16) | P-ROB-01..05 pendentes |
| **R07 / BR-07 — Comparação e exit codes** | 0 | 0 | — (verificação processual por exit code 1 do runner) | P-ROB-01..05 pendentes |
| **R08 / BR-08 — Revisão do material IA** | 0 | 0 | — (verificação documental na folha Technique e AI_DISCLOSURE) | — |
| **TOTAL FUNCIONAL** | **79** | **48** | **48 pares executados (32 PASS, 16 FAIL)** | **31 pares pendentes** |

**Detalhamento dos Resultados por Requisito Funcional:**
- **R01:** 15 executados (10 PASS; 5 FAIL suportados por H-03 e H-07 em combinações de validação/fee).
- **R02:** 17 executados (11 PASS; 6 FAIL associados a DEF-01, DEF-02 e DEF-03).
- **R03:** 10 executados (4 PASS; 6 FAIL demonstrando a subfaturação sistemática de DEF-03 em destinos REMOTE).
- **R04:** 5 executados (2 PASS; 3 FAIL expondo a quebra de indisponibilidade de DEF-04 para peso > 5000 g com express).
- **R05:** 1 executado (1 PASS: F-21 valida que input inválido precede verificação de disponibilidade). Casos de precedência availability > fee (F-43) e validação em fronteira nula (F-44) encontram-se desenhados e pendentes.
- **R06–R08:** Requisitos normativos de formato JSON, ambiente Python 3.10+, exit codes de erro do runner e proveniência de IA. A auditoria determinou a remoção das ligações artificiais a testes da função `quote()`, passando a ser tratados como controlos processuais.

> [!IMPORTANT]
> **Ressalva Metodológica de Cobertura:** A obtenção de cobertura elevada de requisitos ou de partições **não demonstra a correção da aplicação**, nem prova a ausência de defeitos adicionais. A cobertura mede apenas a abrangência dos testes desenhados e executados face às regras normativas.

---

## 6. Limitações Metodológicas, Riscos Residuais e Bloqueios

1. **Validação do Oráculo:** O oráculo foi derivado com assistência de IA pelo próprio grupo; os casos F-31 a F-47 aguardam conferência manual e independente por um elemento do grupo.
2. **Âmbito de Tipos:** O runner apenas processa ficheiros JSON. Tipos nativos de Python incompatíveis com JSON (ex.: floats não finitos, tuplos, objetos) não são testados via CLI.
3. **Execução Monomáquina:** As execuções em Python 3.12 decorreram numa única máquina macOS arm64; a reprodução cruzada pelos restantes elementos do grupo constitui prioridade para o CP06.
4. **Viés Residual de Código:** A seleção dos casos F-46 e F-47 foi informada pela leitura do código-fonte em CP02, o que constitui um desvio ao princípio black-box, expressamente assumido e documentado.
5. **Controlos de Independência e Robustez:** Os testes de processo `P-BR05-01..04` e `P-ROB-01..05` apenas foram executados em Python 3.9.6 no CP04, encontrando-se pendentes de re-execução formal em Python 3.10+.

---

## 7. Prioridades e Plano de Ação para o CP06

*Tabela 7 — Matriz de prioridades e critérios de conclusão para o fecho do projeto (CP06)*

| Prioridade | Trabalho Pendente | Responsável | Critério de Conclusão Objetivo |
|---|---|---|---|
| **P0** | Confirmar formalmente responsáveis de execução e revisões | A confirmar pelo grupo | Campos `Tester` e revisores nominais integralmente preenchidos |
| **P0** | Executar testes de cobertura pendentes (F-31 a F-47) | A definir pelo grupo | Execução via runner em Python 3.10+ com `.results.json` e evidências |
| **P0** | Resolver os quatro defeitos confirmados na aplicação | A definir pelo grupo | Correção em `shipping.py` sem regressão nos casos PASS existentes |
| **P1** | Re-executar suites completas após correções | A definir pelo grupo | 100% PASS nas suites humana, corrigida e final; saída exit code 0 |
| **P1** | Rever regressão, redundâncias e casos neutros de DEF-04 | A definir pelo grupo | Avaliação de casos neutros 12500 e 15000 documentada |
| **P1** | Re-executar controlos de robustez e independência em 3.10+ | Eduardo Dias | Evidência reproduzível de `P-BR05-01..04` e `P-ROB-01..05` em Python 3.10+ |
| **P1** | Consolidar cobertura final e fecho do workbook | Beatriz Barbosa | Workbook consistente com todas as execuções reconciliadas |
| **P2** | Redigir relatório final e preparar demonstração | Grupo 5 | Relatório final (4–6 páginas) e guião de apresentação de 15 minutos |

---

## 8. Responsabilidades e Contribuições Individuais

Em conformidade com as regras de auditoria e com o enunciado do trabalho prático, as contribuições individuais dos elementos do Grupo 5 distinguem o trabalho efetivamente realizado, a assistência por IA, a revisão humana e o trabalho pendente:

### Eduardo Dias (pg61456)
- **Trabalho efetivamente realizado:** Coordenação geral do grupo; redação do project charter (CP01); reposição da baseline do docente e verificação de integridade no CP05; conceção do plano de auditoria CP05.
- **Trabalho assistido por IA:** Apoio na estruturação inicial do charter e análise de lacunas através de sessões Claude Code.
- **Trabalho revisto por humanos:** Revisão das regras de precedência BR-05 e acompanhamento das re-execuções.
- **Trabalho pendente:** Re-execução dos controlos de robustez do runner em Python 3.10+ no CP06.

### Rui Carneiro (pg63791)
- **Trabalho efetivamente realizado:** Auditoria dos artefactos de teste; engenharia de rastreabilidade do workbook `TestResults_T08_CP05.xlsx`; correção das fórmulas de Coverage e eliminação de ligações espúrias; preparação do pacote de entrega e verificação criptográfica.
- **Trabalho assistido por IA:** Apoio de assistente de IA na refatoração do script `build_workbook.py` e simulação matemática das fórmulas Excel.
- **Trabalho revisto por humanos:** Revisão manual do oráculo das BR e conferência individual de casos fronteira.
- **Trabalho pendente:** Validação formal dos casos de lacuna F-31 a F-47 antes da execução em CP06.

### Érica Moreira (pg65641)
- **Trabalho efetivamente realizado:** Revisão estática REV-03 (análise da fronteira de 5000 g em BR-04); validação das execuções históricas da suite humana; supervisão da integridade dos resultados dos candidatos IA.
- **Trabalho assistido por IA:** Apoio na formulação da interpretação de texto normativo.
- **Trabalho revisto por humanos:** Verificação de que as ambiguidades de REV-03 se resolvem pelo texto de BR-04 sem consultar a implementação.
- **Trabalho pendente:** Execução cruzada das suites de teste num segundo computador independente para preparação da demonstração.

### Beatriz Barbosa (pg63744)
- **Trabalho efetivamente realizado:** Caracterização de defeitos de implementação e defeitos de fixture no CP03/CP04; revisão estática REV-04 (análise de precedência de validação em BR-05).
- **Trabalho assistido por IA:** Apoio na formulação comparativa de sintomas observados.
- **Trabalho revisto por humanos:** Verificação da separação estrita entre DATA-01..DATA-03 e os defeitos da aplicação DEF-01..DEF-04.
- **Trabalho pendente:** Validação final da matriz de cobertura e reconciliação dos resultados após a correção de defeitos em CP06.

---

## 9. Divulgação da Utilização de Inteligência Artificial

A utilização de IA no projeto divide-se em duas categorias mutuamente exclusivas e perfeitamente delimitadas:

1. **Fixture Normativo Fornecido pelo Docente (`ai_candidates.json`):**
   - Fornecido no pacote original do docente `TVSI_T08_Students_B1.0/`, gerado originalmente pelo assistente Codex (designado no histórico como GPT-6).
   - Não foi produzido pelo grupo e constitui o objeto de teste da comparação T08.
2. **Assistência de IA nas Tarefas do Grupo:**
   - Ferramentas utilizadas: Claude (Anthropic) no CP01; Claude Code nos CP03 a CP05 (com sessões operando modelos Sonnet 4.6 e Opus 5.5).
   - Finalidade: Apoio à redação de relatórios, conceção do oráculo em Python (`tools/oracle.py`), scripts de construção de workbooks (`build_workbook.py`) e automação de verificações.
   - Validação humana: Todas as expectativas foram verificadas independentemente contra as regras normativas BR-01 a BR-05.
   - O registo detalhado de proveniência por checkpoint encontra-se arquivado em `Trabalho_CP5/AI_DISCLOSURE.md`.

---

## Anexo A — Inventário de Evidências Oficiais CP05

| Evidência | Ficheiro / Localização | Descrição |
|---|---|---|
| Reposição da Baseline | `Trabalho_CP5/evidence/baseline_restauro_20261122/` | Hashes SHA-256 antes e depois, confirmando integridade com commit original `9d9f950` |
| Workbook Consolidado | `Trabalho_CP5/TestResults_T08_CP05.xlsx` | Workbook oficial de CP05 com fórmulas ativas e rastreabilidade corrigida |
| Simulação de Cobertura | `Trabalho_CP5/evidence/coverage_valores_esperados.txt` | Evidência independente com cálculo simulado das fórmulas da folha Coverage |
| Execução Oficial CP05 | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/` | Ambiente Python 3.12.16, exit codes, hashes pré/pós e ficheiros `.results.json` |
| Run Abortado Preservado | `Trabalho_CP5/runs/RUN-CP5-20261122-212747/` | Registo de invocação falhada com flag `-I`, preservada com ficheiro `ABORTED.md` |
| Comparação Histórica | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/comparacao_cp4.txt` | Diferenciação entre execuções 3.12.7 (30 casos) e 3.12.16 (21 casos) |
| Reprodução de Defeitos | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/reproducoes_isoladas.txt` | Registo de 3 repetições independentes em processos novos para DEF-01 a DEF-04 |
| Análise Comparativa T6 | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/t6_comparacao.md` | Dados quantitativos da comparação entre suites de igual dimensão |
| Casos de Lacuna Desenhados | `Trabalho_CP5/gap_cases.json`, `gap_cases.design.json` | 17 casos F-31..F-47 congelados em Git antes de qualquer execução |
| Registo de Divulgação IA | `Trabalho_CP5/AI_DISCLOSURE.md` | Registo integral de proveniência de ferramentas de IA por checkpoint |
