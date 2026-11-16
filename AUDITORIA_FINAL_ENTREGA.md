# Relatório de Auditoria Final e Verificação de Entregáveis — CP04
## TVSI_2627 — UMinho | Grupo 5

**Data da Auditoria:** 16 de Novembro de 2026  
**Auditor Técnico:** Senior QA Engineer, Test Manager & Technical Auditor  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5 (*Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa*)  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git` (Ramo `main`)  
**Ficheiro do Relatório:** `AUDITORIA_FINAL_ENTREGA.md`  
**Pacote Oficial de Entrega:** `TVSI_T08_Grupo5_CP04.zip`

---

## 1. Identificação e Âmbito da Auditoria do CP04

A presente intervenção consubstancia uma auditoria técnica independente, profunda e exaustiva sobre o repositório `TVSI_2627`, com o objetivo de executar o **fecho integral do Checkpoint 4 (CP04)**, assegurando a resolução de todas as incongruências identificadas, a validação de todas as suites de testes, a integridade do livro de cálculo oficial e a preparação de um pacote de entrega final tecnicamente irrepreensível, verificável e academicamente defensável.

O âmbito cobriu de forma cumulativa e harmonizada os quatro checkpoints da U.C.:
- **CP01:** Project Charter, papéis dos elementos, análise de riscos e verificação técnica de ambiente com o teste de fumo `H-ENV`.
- **CP02:** Revisão estática, modelação do oráculo independente a partir das regras normativas BR-01 a BR-08, e congelamento formal da suite humana (16 casos: `H-01` a `H-16`) a 30 de outubro de 2026 (commit `54ec4d3`).
- **CP03:** Auditoria crítica dos 12 candidatos de IA, aceitação de `AI-11` (`F-17`) e `AI-12` (`F-18`), revisão de `AI-09` (`F-19`), identificação de falsos positivos na IA, primeira suite combinada e demonstração formal de BR-05.
- **CP04:** Execução sistemática de testes, gestão de evidências de execução reproduzíveis em múltiplos interpretadores Python (3.9 e 3.12), auditoria profunda do workbook oficial com introdução de coluna autónoma de requisitos e separação de resultados esperados e observados, expansão da suite final para 30 casos (20 PASS / 10 FAIL), rastreabilidade rigorosa dos 4 defeitos de software (`DEF-01` a `DEF-04`) e dos 3 problemas de expectativas de IA (`DATA-01` a `DATA-03`), automação da auditoria (`Trabalho_CP4/audit_cp4.py`) e geração do arquivo de submissão do grupo (`TVSI_T08_Grupo5_CP04.zip`).

---

## 2. Incongruências Identificadas e Resoluções Aplicadas

| # | Incongruência Inicial | Resolução Técnica de Auditoria | Impacto / Estado |
|---|---|---|---|
| **1** | **Discrepância no Plano CP04:** O plano apresentava referências obsoletas a 21 testes humanos ou `H-01` a `H-20` como congelados. | O plano `Trabalho_CP4/CP4.md` foi reescrito para harmonizar com a suite efetivamente congelada em CP02: 16 casos (`H-01` a `H-16`) mais o teste técnico `H-ENV` de ambiente, totalizando 17 entradas, sem adições retroativas. | **Resolvido e Alinhado** |
| **2** | **Ausência de Coluna de Requisitos em Executions:** A folha `Executions` do workbook oficial não dispunha de coluna autónoma `Requirement ID(s)`. | Adicionada a coluna autónoma `Requirement ID(s)` (coluna C), associando com rigor cada execução aos requisitos normativos exercitados (R01 a R08). | **Resolvido e Conforme** |
| **3** | **Separação de Resultados Esperados e Observados:** Necessidade de clareza absoluta entre oráculo independente e saídas reais. | Reestruturadas as colunas da folha `Executions` para separar formalmente `Expected outputs (independently derived)` de `Actual outputs`, preservando o veredicto na coluna G para manter 100% íntegras as fórmulas de cobertura. | **Resolvido e Conforme** |
| **4** | **Histórico de Execuções Incompleto:** O workbook continha apenas a suite combinada, omitindo o histórico de execuções humanas de CP02 e dos candidatos de IA no runner. | Consolidado o registo histórico integral com 68 execuções: CP01 (Smoke H-ENV), CP02 (Humana congelada 16 casos), CP03 (Candidatos IA no runner original), CP04 (Suite final de 30 casos), BR-05 (4 propriedades) e Robustez do Runner (5 cenários). | **Resolvido e Rastreável** |
| **5** | **Falsos PASS na Suite de IA Mascarando Defeitos:** O runner reportava 10 PASS e 2 FAIL sobre `ai_candidates.json` devido a expectativas incorretas em `AI-05` e `AI-06`. | Preservados os resultados históricos do runner original (10 PASS / 2 FAIL) sem manipulação forçada, explicitando nas observações e na folha `Defects` que se tratam de erros de dados de teste da IA (`DATA-01` e `DATA-02`) e não de conformidade do software. | **Resolvido e Transparente** |
| **6** | **Discriminação de Testers:** Os registos apresentavam identificação genérica de ferramentas. | Atualizada a identificação de testers com discriminação explícita de papéis funcionais: Executante, Supervisão e Validação por membros humanos do Grupo 5. | **Resolvido e Conforme** |
| **7** | **Cobertura de Casos Limite Operacionais:** Faltava evidência executável para pesos float, whitespace em zonas, tipos não-booleanos e exit code 2. | Concebidos e executados os casos `F-22` a `F-30` na suite final e 5 cenários de robustez do runner, registados com evidências JSON auditáveis. | **Resolvido e Validado** |

---

## 3. Síntese dos Resultados Oficiais de Execução

| Suite de Teste | Entradas | PASS | FAIL | Taxa | Observações de Auditoria |
|---|:---:|:---:|:---:|:---:|---|
| **Humana (com H-ENV)** | **17** | **11** | **6** | 64.7% | 16 casos humanos congelados em CP02 + H-ENV. Isolou preliminarmente os 4 defeitos. |
| **Candidatos Originais IA** | **12** | **10** | **2** | 83.3% | Executados no runner original. 2 casos são falsos PASS por expectativa incorreta da IA (`DATA-01` e `DATA-02`). |
| **Suite Final Combinada** | **30** | **20** | **10** | 66.7% | 16 humanos + 14 complementares (`F-17` a `F-30`). 100% de paridade em Python 3.9 e Python 3.12. |

---

## 4. Matriz de Defeitos de Software vs Problemas de Qualidade IA

### Defeitos Estruturais de Software (`shipping.py`)
1. **`DEF-01` (BR-01):** Linha 3 (`weight >= 20000`). Off-by-one rejeita 20000g como `INVALID`. Detetado por `H-07`. Severidade: **Alta**.
2. **`DEF-02` (BR-02):** Linha 7 (`weight < 1000`). Off-by-one cobra 8€ a 1000g em vez de 5€. Detetado por `H-03`. Severidade: **Média-Alta**.
3. **`DEF-03` (BR-03):** Linha 14 (`fee = 4`). Atribuição simples apaga tarifa base em encomendas `REMOTE`. Detetado por `H-10, H-12, H-13, F-18, F-29`. Severidade: **Crítica**.
4. **`DEF-04` (BR-04):** Linha 5 (`weight > 10000`). Limiar de indisponibilidade em 10kg em vez de 5kg. Detetado por `H-14, F-19, F-30`. Severidade: **Alta**.

### Problemas de Qualidade de Dados de Teste IA
1. **`DATA-01` (BR-03 / AI-05):** Expectativa da IA omitiu a taxa base (esperou 4€ em vez de 9€), replicando o bug `DEF-03`.
2. **`DATA-02` (BR-02 / AI-06):** Expectativa da IA atribuiu taxa de Tier 2 a 1000g (esperou 8€ em vez de 5€), mascarando o bug `DEF-02`.
3. **`DATA-03` (BR-04 / AI-09):** Expectativa da IA tarifou encomenda que a regra BR-04 define como `UNAVAILABLE`. Revisto para `F-19`.

---

## 5. Auditoria das 11 Áreas Normativas (`audit_cp4.py`)

A execução do script formal de auditoria [`Trabalho_CP4/audit_cp4.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP4/audit_cp4.py) reportou:

| # | Área de Auditoria | Verificações Efetuadas | Veredicto |
|---|---|---|:---:|
| **1** | **Integridade da Baseline** | `shipping.py` intacto face ao repositório oficial; todos os documentos normativos presentes. | **PASS** |
| **2** | **Suite Humana Congelada** | `Trabalho_CP2/human_cases.json` idêntico ao commit `54ec4d3` (16 casos); `human_cases_cp4.json` com 17 casos. | **PASS** |
| **3** | **Evidências de Execução** | Todos os ficheiros em `runs/` e `evidence/` presentes, válidos e íntegros. | **PASS** |
| **4** | **Correspondência Test IDs** | Correspondência estrita 1-para-1 entre suite de 30 casos e ficheiro de execução JSON. | **PASS** |
| **5** | **Cobertura de Requisitos** | 100% de cobertura (R01 a R08); todos os testes desenhados foram executados (0 não executados). | **PASS** |
| **6** | **Consistência de Resultados** | Humana (11/6), IA runner (10/2), Final (20/10), Paridade estrita Python 3.9 vs Python 3.12. | **PASS** |
| **7** | **Relatórios de Defeitos** | Registo completo dos 4 defeitos de software e segregação dos 3 problemas de oráculo de IA. | **PASS** |
| **8** | **Integridade do Workbook** | 6 folhas oficiais; coluna autónoma `Requirement ID(s)`; 0 erros de fórmula (`#REF!`, etc.). | **PASS** |
| **9** | **Consistência Documental** | Plano CP04 com texto oficial de referência e 17 entradas humanas; relatórios harmonizados. | **PASS** |
| **10** | **Integridade do Pacote ZIP** | `TVSI_T08_Grupo5_CP04.zip` íntegro (0 erros em `testzip()`); 0 ficheiros temporários ou `.git/`. | **PASS** |
| **11** | **Validação Criptográfica** | Hashes SHA-256 e dimensões rigorosamente alinhados com `MANIFEST_ENTREGA.md`. | **PASS** |

---

## 6. Identificação do Pacote ZIP Oficial de Entrega

- **Ficheiro:** `TVSI_T08_Grupo5_CP04.zip`
- **Caminho Relativo:** `./TVSI_T08_Grupo5_CP04.zip`
- **Dimensão:** 195.167 bytes
- **Hash SHA-256:** `ae73ff12db9c088cb52d8aabb16702fba8a80014aa70bc24637229a89ff08bf9`
- **Ficheiros Incluídos:** 50 ficheiros essenciais
- **Resultado do Teste de Extração:** 100% aprovado sem ficheiros em falta ou corrompidos.

---

## 7. Conclusão Final do Auditor

O Checkpoint 4 (CP04) encontra-se **tecnicamente fechado, auditado e em plena conformidade** com os critérios de avaliação e requisitos normativos da U.C. de Tecnologias e Verificação de Sistemas de Informação 2026/27.
