# RELATÓRIO TÉCNICO DE AUDITORIA, FECHO INTEGRAL E INTEGRAÇÃO DO CP04
## Projeto TVSI 2026/27 — T08 — Grupo 5

- **Instituição:** Universidade do Minho — Escola de Engenharia — Mestrado em Engenharia Informática
- **Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)
- **Trabalho Prático:** T08 — Desenho de Testes com Assistência de IA
- **Objeto de Teste:** Módulo `shipping.py` — Função `quote(weight, zone, express)`
- **Build Sob Teste:** `T08-B1.0`
- **Grupo:** Grupo 5
- **Elementos do Grupo:**
  - Eduardo Dias
  - Rui Carneiro
  - Érica Moreira
  - Beatriz Barbosa
- **Data de Fecho:** 17 de Novembro de 2026
- **Classificação Final:** **FECHADO E VALIDADO A 100% (COM LIMITAÇÕES DOCUMENTADAS)**

---

## 1. INTRODUÇÃO E ENQUADRAMENTO DA INTERVENÇÃO

O presente relatório documenta a auditoria técnica exaustiva, correção de todas as incongruências identificadas, reconciliação matemática de evidências de teste, auditoria do workbook Excel, validação determinística dos oráculos e integração controlada no Git para o encerramento definitivo do **Checkpoint 4 (CP04) — Execução de Testes e Gestão de Evidências**.

Todas as ações respeitam integralmente os princípios inegociáveis de auditoria de software:
1. **Preservação Absoluta da Baseline de Código:** O ficheiro `shipping.py` (`TVSI_T08_Students_B1.0/app/shipping.py`) permanece idêntico bit-a-bit ao commit inicial `9d9f950`. Nenhum defeito foi mascarado ou corrigido no código sob teste.
2. **Preservação da Suite Humana Congelada (CP02):** A suite humana concebida e congelada no commit `54ec4d3` (`H-01` a `H-16`) foi rigorosamente preservada, acompanhada pelo caso técnico de infraestrutura e ambiente `H-ENV` (totalizando 17 entradas normativas).
3. **Preservação das Evidências Empíricas:** Não foram apagados runs nem substituídos resultados observados por esperados; nenhuma falha legítima foi convertida artificialmente em aprovação.
4. **Segregação Rigorosa de Defeitos de Software vs. Erros de IA:** Os defeitos de código da implementação (`DEF-01` a `DEF-04`) foram rigorosamente isolados e distinguidos das anomalias de oráculo e especificação geradas pelos modelos LLM (`DATA-01` a `DATA-03`).

---

## 2. ESTADO INICIAL DO REPOSITÓRIO E DAS BRANCHES

Antes da intervenção de integração e auditoria:
- **`origin/main`** (HEAD no commit `0748b43` por Eduardo Dias):
  - Incluía ficheiros e pastas de suporte ao CP04 preliminar (`TVSI_T08_Students_B1.0_CP4/`, runs empíricos `RUN-CP4-20261115-162457`), mas mantinha a redação preliminar no plano `CP4.md` mencionando "21 testes humanos congelados", contrariando o congelamento oficial de 16 testes em `54ec4d3`.
- **`origin/cp04-final`** (HEAD no commit `0ac8399` por Rui Carneiro):
  - Retificava a menção da suite humana para o texto oficial de 17 entradas normativas (`H-ENV` + `H-01..H-16`).
  - Implementava a suite final de 30 casos (`final_cases.json`) e os seus runners.
  - Reestruturava o workbook Excel com coluna autónoma de requisitos.
  - Implementava o script de auto-auditoria `Trabalho_CP4/audit_cp4.py`.
- **Estratégia de Integração:**
  - Salvaguarda prévia das referências com branches locais `backup/origin-main` (`0748b43`) e `backup/main-local` (`0ac8399`).
  - Fusão no ramo de integração `integration/cp04-merge` através do merge commit `36fd904`, resolvendo os conflitos em `CP4.md` e `Relatorio_CP4.md` com a versão auditada de 17 entradas humanas e 30 casos finais.
  - O ramo `main` foi subsequentemente avançado e sincronizado no commit `022e343`.

---

## 3. INCONGRUÊNCIAS DETETADAS E RESOLUÇÃO TÉCNICA

| # | Incongruência Detetada | Impacto Técnico / Risco | Resolução Adotada e Evidência |
|---|---|---|---|
| **INC-01** | Menção a 21 testes humanos (`H-01..H-20`) no commit `0748b43`. | Inconsistência grave com a suite humana de 16 casos congelada em `54ec4d3`. | Harmonização com o texto normativo oficial: 16 casos de teste (`H-01..H-16`) + 1 caso de ambiente (`H-ENV`) = 17 entradas. |
| **INC-02** | Formato de evidência `br05_independence_cp4.json` continha saída stdout de terminal em vez de JSON estruturado. | Quebrava a validação sintática do script de auditoria. | Substituição pelo relatório JSON válido e completo `br05_independence.results.json`, cobrindo as 4 propriedades. |
| **INC-03** | Ficheiros espúrios gerados pelo macOS/iCloud com sufixo `" 2"` no workspace. | Risco de empacotamento de lixo e duplicação no repositório. | Remoção automática e sanitização de todos os duplicados no workspace. |
| **INC-04** | Célula C4 do workbook original misturava requisitos e inputs. | Dificuldade de rastreabilidade automática no Excel. | Separação estrita: Coluna C para `Requirement ID(s)` autónoma, Coluna D para `Input Data`. Fórmulas de cobertura corrigidas sem `#REF!`. |
| **INC-05** | Descrição desfasada dos 4 defeitos em versão preliminar de `FECHO_FINAL_CP04.md`. | Contradição com as regras de negócio e relatórios de CP02/CP03. | Retificação total: alinhamento com os 4 defeitos reais da baseline (`shipping.py`) identificados nos relatórios CP02/CP03 e no workbook. |
| **INC-06** | Dependência circular de hash SHA-256 se o manifesto tentar registar o hash do ZIP que o contém. | Incoerência matemática impossível de resolver estaticamente. | Arquitetura limpa: `MANIFEST_ENTREGA.md` atesta os 51 ficheiros do projeto; o hash do ZIP final é gerado de forma independente no ficheiro de verificação `TVSI_T08_Grupo5_CP04.zip.sha256`. |

---

## 4. RECONCILIAÇÃO MATEMÁTICA DAS 68 EXECUÇÕES

O workbook oficial [TestResults_T08_Template.xlsx](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx) regista na folha `Executions` exatamente **68 linhas de ensaio**, explicadas pela seguinte decomposição matemática:

$$\text{Total de Execuções Reconciliadas} = 1\ (\text{ENV}) + 16\ (\text{H02}) + 12\ (\text{AI}) + 30\ (\text{CP4}) + 4\ (\text{CTRL}) + 5\ (\text{ROB}) = \mathbf{68}$$

### 4.1. Decomposição Estruturada por Bloco de Execução

1. **RUN-ENV-01 (1 execução):** Caso técnico de arranque `H-ENV` (`weight=500, zone=LOCAL, express=False` $\to$ `OK, fee=5`). Valida a integridade do ambiente e função `quote()` da baseline.  
   - **Resultado:** **1 PASS**.
2. **RUN-H02-01 a RUN-H02-16 (16 execuções):** Suite Humana oficial congelada no CP02 (`H-01` a `H-16`).  
   - **Resultados:** **10 PASS / 6 FAIL**.  
   - **Casos que Falham:** `H-03` (expõe DEF-02), `H-07` (expõe DEF-01), `H-10` (expõe DEF-03), `H-12` (expõe DEF-03), `H-13` (expõe DEF-03) e `H-14` (expõe DEF-04).  
   *(Nota: Considerando o caso técnico H-ENV conjuntamente com os 16 casos humanos, perfazem 17 entradas com 11 PASS e 6 FAIL).*
3. **RUN-AI-01 a RUN-AI-12 (12 execuções):** Suite de candidatos gerados por IA (`AI-01` a `AI-12`).  
   - **Resultados:** **10 PASS / 2 FAIL**.  
   - **Casos que Falham no Runner:** `AI-09` (falha por oráculo inválido gerado por IA) e `AI-12` (falha legítima expondo DEF-03 com oráculo correto).  
   - **Falsos PASS Identificados:** `AI-05` (DATA-01 mascara DEF-03) e `AI-06` (DATA-02 mascara DEF-02).
4. **RUN-CP4-01 a RUN-CP4-30 (30 execuções):** Suite Final Integrada (`H-01..H-16` + `F-17..F-30`).  
   - **Resultados:** **20 PASS / 10 FAIL**.  
   - **Casos que Falham:** `CP4-03`, `CP4-07`, `CP4-10`, `CP4-12`, `CP4-13`, `CP4-14`, `CP4-18`, `CP4-19`, `CP4-29`, `CP4-30`.  
   - **Paridade Multi-Runtime:** A suite foi executada de forma determinística e independente em Python 3.9 (`final_cases_execution.json`) e Python 3.12 (`final_cases_execution.py312.json`), obtendo rigorosamente a mesma distribuição caso a caso (20 PASS / 10 FAIL).
5. **RUN-CTRL-01 a RUN-CTRL-04 (4 execuções):** Verificação de Independência de Execuções e Ausência de Efeitos Secundários (BR-05).  
   - **Resultados:** **4 PASS**.  
   - `BR05-DET-01`: Determinismo e repetibilidade (10 invocações consecutivas idênticas).  
   - `BR05-ISO-02`: Ausência de estado residual mutável entre chamadas.  
   - `BR05-MUT-03`: Imutabilidade de inputs e argumentos em memória.  
   - `BR05-FS-04`: Ausência de efeitos laterais ou escrita indevida no sistema de ficheiros delimitado.
6. **RUN-ROB-01 a RUN-ROB-05 (5 execuções):** Verificação de Robustez do Test Runner CLI (`run_cases.py`).  
   - **Resultados:** **5 PASS** (validação de Exit Code 2 perante ficheiro inexistente, ficheiro corrompido, array JSON vazio, payload sem `test_id` e payload com campos em falta).

---

## 5. TABELA COMPARATIVA DE RESULTADOS DE EXECUÇÃO

| Bloco de Execução | Dimensão | PASS | FAIL | Taxa de Sucesso (%) | Evidência Primária no Repositório |
|---|:---:|:---:|:---:|:---:|---|
| **Human Suite (com H-ENV)** | 17 | 11 | 6 | 64.71% | `Trabalho_CP4/runs/human_17_execution.json` |
| **Human Suite Congelada (H-01..16)** | 16 | 10 | 6 | 62.50% | `Trabalho_CP2/human_cases.results.json` |
| **AI Candidates Suite** | 12 | 10 | 2 | 83.33% | `Trabalho_CP4/runs/ai_candidates_execution.json` |
| **Final Suite CP04 (Python 3.9)** | 30 | 20 | 10 | 66.67% | `Trabalho_CP4/runs/final_cases_execution.json` |
| **Final Suite CP04 (Python 3.12)** | 30 | 20 | 10 | 66.67% | `Trabalho_CP4/runs/final_cases_execution.py312.json` |
| **Propriedades BR-05** | 4 | 4 | 0 | 100.00% | `Trabalho_CP4/evidence/br05_independence_cp4.json` |
| **Robustez do Runner (Exit Code 2)**| 5 | 5 | 0 | 100.00% | `Trabalho_CP4/evidence/runner_robustness_evidence.json` |
| **Total Reconciliado no Excel** | **68** | **50** | **18** | **73.53%** | `TestResults_T08_Template.xlsx` |

---

## 6. MATRIZ DEFINITIVA DOS QUATRO DEFEITOS DE SOFTWARE (DEF-01 A DEF-04)

Os quatro defeitos decorrem de erros estruturais na implementação de `shipping.py` e violam as regras de negócio normativas de `BusinessRules.md`:

| Defeito | Regra Violada | Código na Baseline (`shipping.py`) | Comportamento Incorreto | Resultado Esperado | Resultado Observado | Testes Reveladores | Severidade |
|---|---|---|---|---|---|---|:---:|
| **DEF-01** | BR-01 | Linha 3: `weight >= 20000` | Rejeição indevida da fronteira superior válida (20000g). A condição `>=` exclui o valor limite permitido. | `{"status": "OK", "fee": 12}` | `{"status": "INVALID", "fee": null}` | `H-07` | **Alta** |
| **DEF-02** | BR-02 | Linha 7: `if weight < 1000:` | Fronteira entre Tier 1 e Tier 2. Para peso de 1000g, o código salta para o escalão `<= 5000` cobrando taxa de 8€. | `{"status": "OK", "fee": 5}` | `{"status": "OK", "fee": 8}` | `H-03` | **Média-Alta** |
| **DEF-03** | BR-03 | Linha 14: `fee = 4` | Sobrescrita destrutiva da tarifa base. Usa atribuição `=` em vez de acumulação `+= 4`, apagando a taxa base para `zone="REMOTE"`. | `{"status": "OK", "fee": 9}` | `{"status": "OK", "fee": 4}` | `H-10, H-12, H-13, F-18, F-29` | **Crítica** |
| **DEF-04** | BR-04 | Linha 5: `weight > 10000` | Limiar de indisponibilidade de serviço expresso REMOTE implementado em 10000g em vez de 5000g. Encomendas entre 5001g e 10000g são incorretamente aceites. | `{"status": "UNAVAILABLE", "fee": null}` | `{"status": "OK", "fee": 10}` | `H-14, F-19, F-30` | **Alta** |

---

## 7. MATRIZ DEFINITIVA DAS TRÊS ANOMALIAS DE DADOS DA IA (DATA-01 A DATA-03)

As anomalias de IA resultam de alucinações e erros de interpretação de regras pelo modelo LLM durante a geração do candidato `ai_candidates.json`:

| Anomalia | Caso IA | Regra Envolvida | Proposta da IA (`expected`) | Oráculo Normativo Correto | Comportamento no Runner | Diagnóstico Técnico da Anomalia |
|---|---|---|---|---|---|---|
| **DATA-01** | `AI-05` | BR-03 | `{"status": "OK", "fee": 4}` | `{"status": "OK", "fee": 9}` | **Falso PASS** (baseline devolve 4 devido a `DEF-03`) | A IA omitiu a taxa base (5€) somando apenas a taxa de zona (4€). O teste passou fortuitamente porque a baseline tem o defeito `DEF-03`, mascarando o bug. |
| **DATA-02** | `AI-06` | BR-02 | `{"status": "OK", "fee": 8}` | `{"status": "OK", "fee": 5}` | **Falso PASS** (baseline devolve 8 devido a `DEF-02`) | A IA cometeu um erro de fronteira para 1000g, atribuindo taxa de Tier 2 (8€). O teste passou fortuitamente porque a baseline tem o defeito `DEF-02`. |
| **DATA-03** | `AI-09` | BR-04 | `{"status": "OK", "fee": 22}` | `{"status": "UNAVAILABLE", "fee": null}` | **FAIL** (baseline devolve `OK, fee=10`) | A IA tentou tarifar uma encomenda de 6000g express em REMOTE somando 12 + 4 + 6 = 22€, ignorando a indisponibilidade legal de BR-04. Falha legítima que revelou a alucinação da IA. |

---

## 8. AUDITORIA DO WORKBOOK EXCEL (`TestResults_T08_Template.xlsx`)

O livro de cálculo oficial foi inspecionado estruturalmente via XML:
- **Folhas Preservadas (6 folhas na ordem regulamentar):**
  1. `Test Cases`
  2. `Executions`
  3. `Defects`
  4. `Static Review`
  5. `Coverage`
  6. `Technique`
- **Coluna de Requisitos Autónoma:** Célula `C4` contém `'Requirement ID(s)'`, eliminando contaminações de inputs na coluna de requisitos.
- **Folha `Executions`:** 68 linhas de execução detalhadas com Run ID, Test ID, Requisito, Input, Output Esperado, Output Observado e Verdict.
- **Folha `Coverage`:** 324 fórmulas ativas (`COUNTIFS` e `SUMIFS`) que ligam dinamicamente a folha de Casos de Teste e a folha de Execuções aos requisitos R01 a R08. Cobertura: 100% (diferença entre desenhados e executados = 0).
- **Integridade de Fórmulas:** 0 células com erros (`#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`, `#N/A`).
- **Limitação Declarada:** Devido à ausência do LibreOffice no ambiente headless, o recálculo dinâmico por motor Office externo não foi executado; a validação baseou-se na análise sintática e estrutural do esquema XML OpenXML e avaliação simbólica das expressões.

---

## 9. SCRIPT AUTOMATIZADO DE AUDITORIA (`Trabalho_CP4/audit_cp4.py`)

O script de auditoria foi aprimorado para validar as 12 áreas normativas com verificação semântica real:
1. **Área 1:** Integridade absoluta de `shipping.py` contra o commit inicial `9d9f950`.
2. **Área 2:** Preservação da suite humana congelada (16 casos CP02 em `54ec4d3`).
3. **Área 3:** Validação sintática de todos os 33 ficheiros JSON do repositório.
4. **Área 4:** Unicidade estrita dos `test_id` em todas as suites.
5. **Área 5:** Correspondência 1-para-1 de inputs e saídas na suite final.
6. **Área 6:** Re-execução determinística e verificação de oráculos (20 PASS / 10 FAIL).
7. **Área 7:** Cobertura total de requisitos R01..R08.
8. **Área 8:** Registo e segregação formal de `DEF-01..04` vs. `DATA-01..03`.
9. **Área 9:** Integridade das 6 folhas e 68 execuções do workbook Excel.
10. **Área 10:** Consistência cruzada nos documentos de texto e relatórios.
11. **Área 11:** Integridade estrutural e teste de extração do ZIP (51 ficheiros limpos).
12. **Área 12:** Correspondência criptográfica SHA-256 no `MANIFEST_ENTREGA.md`.

---

## 10. PACOTE DE SUBMISSÃO E HASHES CRIPTOGRÁFICOS

- **Ficheiro de Submissão:** `TVSI_T08_Grupo5_CP04.zip`
- **Dimensão:** 203,578 bytes
- **Hash SHA-256:** `b8b12cad93371cb4fe5968e1b26e844e494e7237de81a2fea5f7048e762605f5`
- **Número de Ficheiros:** 51 ficheiros essenciais
- **Higiene do Pacote:** Isento de diretórios `.git/`, pastas de cache `__pycache__/` e ficheiros temporários `.DS_Store`.
- **Ficheiro de Verificação Externo:** `TVSI_T08_Grupo5_CP04.zip.sha256`
- **Manifesto Interno:** [MANIFEST_ENTREGA.md](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/MANIFEST_ENTREGA.md) contém os hashes SHA-256 e dimensões de todos os ficheiros constituintes do pacote, eliminando dependências circulares de cálculo.

---

## 11. LIMITAÇÕES TÉCNICAS DECLARADAS

1. **Recálculo do Excel:** Não foi possível executar recálculo sob motor LibreOffice headless por não estar instalado no sistema operacional; a integridade foi atestada por validação estática OpenXML.
2. **Publicação Remota Git:** O envio para o repositório remoto GitHub (`git push`) requer credenciais interativas do utilizador no terminal do macOS.

---

## 12. VEREDICTO FINAL

$$\mathbf{VEREDICTO:\ FECHADO\ E\ VALIDADO\ (COM\ LIMITAÇÕES\ DOCUMENTADAS)}$$

O trabalho Checkpoint 4 (CP04) encontra-se tecnicamente consistente, empiricamente reproduzível, documentalmente harmonizado e pronto para submissão académica.
