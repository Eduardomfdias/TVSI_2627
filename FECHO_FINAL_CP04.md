# RELATÓRIO TÉCNICO DE AUDITORIA, RECONCILIAÇÃO E FECHO DEFINITIVO DO CP04
## Projeto TVSI 2026/27 — T08 — Grupo 5

- **Instituição:** Universidade do Minho — Escola de Engenharia — Mestrado em Engenharia Informática
- **Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)
- **Trabalho Prático:** T08 — Desenho de Testes com Assistência de IA
- **Objeto de Teste (SUT):** Módulo `shipping.py` — Função `quote(weight, zone, express)`
- **Build Sob Teste:** `T08-B1.0`
- **Grupo:** Grupo 5
- **Elementos do Grupo:**
  - Eduardo Dias
  - Rui Carneiro
  - Érica Moreira
  - Beatriz Barbosa
- **Data de Fecho:** 17 de Novembro de 2026
- **Veredicto Técnico:** **FECHADO E VALIDADO TECNICAMENTE (COM LIMITAÇÕES DOCUMENTADAS)**

---

## 1. INTRODUÇÃO E ENQUADRAMENTO DA INTERVENÇÃO

O presente documento constitui o registo final da auditoria técnica exaustiva, reconciliação de evidências e fecho definitivo do **Checkpoint 4 (CP04) — Execução de Testes e Gestão de Evidências**.

Todas as verificações obedecem aos princípios fundamentais de engenharia de software e integridade académica:
1. **Preservação Absoluta da Baseline:** O ficheiro `shipping.py` (`TVSI_T08_Students_B1.0/app/shipping.py`) permanece idêntico bit-a-bit ao commit inicial `9d9f950`. A implementação de referência sob teste **contém quatro defeitos estruturais intencionais** e não foi alterada para fazer os testes passar.
2. **Preservação da Suite Humana Congelada (CP02):** A componente humana compreende 16 casos de teste concebidos pelos estudantes (`H-01..H-16`), preservados desde o CP02, e um controlo técnico de ambiente (`H-ENV`). No total, são 17 entradas de execução, das quais 16 correspondem a casos de teste normativos.
3. **Preservação das Evidências Empíricas:** Não foram apagados runs nem substituídos resultados observados por esperados; as falhas legítimas foram registadas como evidência primária da presença dos defeitos.
4. **Segregação Categórica de Defeitos vs. Erros de IA:** Os defeitos de software na implementação (`DEF-01` a `DEF-04`) foram isolados e distinguidos das anomalias de especificação dos modelos LLM (`DATA-01` a `DATA-03`).

---

## 2. ESTADO DO REPOSITÓRIO GIT E RASTREABILIDADE

- **Branch Principal de Trabalho:** `main`
- **Branches Sincronizadas no Remoto:** `origin/main` e `origin/cp04-final`
- **Histórico de Commits Preservado:**
  - Commit inicial de referência: `9d9f950`
  - Congelamento da suite humana CP02: `54ec4d3`
  - Consolidação CP03: `8a525c2`
  - Integração inicial CP04: `0748b43` (Eduardo Dias) e `0ac8399` (Rui Carneiro)
  - Merge commit de integração: `36fd904` (*"merge: integrate CP04 validated test execution, evidence management and workbook audit"*)
  - Refinamentos finais de auditoria: commits `022e343` e `c03417f`.

---

## 3. DISTINÇÃO FUNDAMENTAL: VALIDAÇÃO DO PROCESSO VS. CONFORMIDADE DA IMPLEMENTAÇÃO

É crucial distinguir tecnicamente:
1. **Validação do Processo e dos Entregáveis (100% Validado):** O processo de conceção de casos de teste, execução empírica, registo de evidências, auditoria automatizada, estruturação do workbook Excel e empacotamento de submissão encontra-se plenamente validado e em conformidade estrita com os normativos docentes (`BusinessRules.md`, `StudentAssignment.md`, `START_HERE.md` e `AI_PROVENANCE.md`).
2. **Conformidade da Implementação Sob Teste (Não Conforme / Defeituosa):** A aplicação de ensino `shipping.py` **NÃO está conforme com as regras de negócio**. A baseline contém 4 defeitos de software demonstrados empiricamente pelos testes humanos e finais (`DEF-01` a `DEF-04`), confirmando a eficácia do desenho de testes.

---

## 4. RECONCILIAÇÃO RIGOROSA DAS EXECUÇÕES DE TESTE

Para garantir absoluta clareza conceptual, distinguem-se:
1. **Casos de Teste Únicos:** Entidades de teste distintas concebidas nas suites (`H-ENV`, `H-01..16`, `AI-01..12`, `F-17..30`, `BR05-01..04`, `ROB-01..05`).
2. **Linhas de Execução Lógica no Workbook (68):** Linhas formais de registo no livro de cálculo oficial [TestResults_T08_Template.xlsx](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx) (folha `Executions`), correspondendo a um ensaio por caso de teste lógico.
3. **Execuções Físicas Totais Multiplataforma (98):** Invocações efetivas do interpretador Python em runtime, incluindo a execução paralela de paridade da suite final (30 em Python 3.9 + 30 em Python 3.12 = 60 execuções físicas), perfazendo um total de 98 execuções físicas comprovadas por evidências JSON ($1 + 16 + 12 + 60 + 4 + 5 = 98$).

### Tabela de Reconciliação Metodológica das Execuções

| Bloco de Execução | ID de Ensaio | Registos Lógicos (Excel) | Execuções Físicas (Runtimes) | Veredicto Observado | Evidência Primária no Repositório |
|---|---|:---:|:---:|:---:|---|
| **Ambiente de Teste** | `RUN-ENV-01` | 1 | 1 | 1 PASS | `Trabalho_CP4/runs/human_17_execution.json` |
| **Suite Humana Congelada** | `RUN-H02-01..16` | 16 | 16 | 10 PASS / 6 FAIL | `Trabalho_CP2/human_cases.results.json` |
| **Candidatos de IA** | `RUN-AI-01..12` | 12 | 12 | 10 PASS / 2 FAIL | `Trabalho_CP4/runs/ai_candidates_execution.json` |
| **Suite Final Integrada** | `RUN-CP4-01..30` | 30 | 60 *(30 em Py 3.9 + 30 em Py 3.12)* | 20 PASS / 10 FAIL | `Trabalho_CP4/runs/final_cases_execution.json` & `.py312.json` |
| **Propriedades BR-05** | `RUN-CTRL-01..04` | 4 | 4 | 4 PASS | `Trabalho_CP4/evidence/br05_independence_cp4.json` |
| **Robustez do Runner CLI** | `RUN-ROB-01..05` | 5 | 5 | 5 PASS | `Trabalho_CP4/evidence/runner_robustness_evidence.json` |
| **Total Global** | — | **68** | **98** | **50 PASS / 18 FAIL** *(no Excel)* | `TestResults_T08_Template.xlsx` |

$$\text{Registos Lógicos Reconciliados} = 1 + 16 + 12 + 30 + 4 + 5 = \mathbf{68}$$
$$\text{Execuções Físicas Totais} = 1 + 16 + 12 + (30 \times 2) + 4 + 5 = \mathbf{98}$$

*Nota: O catálogo contém 31 identificadores de teste únicos: H-ENV, H-01..H-16 e F-17..F-30. As 68 execuções lógicas representam registos de execução, incluindo repetições dos mesmos casos em diferentes fases ou contextos, não correspondendo a 68 casos de teste únicos.*  
*Reconciliação quantitativa consistente com os registos de execução e as evidências identificadas.*

---

## 5. RECONCILIAÇÃO DO INVENTÁRIO: 50 ENTRADAS NO MANIFESTO VS. 51 FICHEIROS NO ZIP

A contagem entre o manifesto e o arquivo ZIP encontra-se estritamente reconciliada:
- **Tabela de Conteúdo de [MANIFEST_ENTREGA.md](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/MANIFEST_ENTREGA.md):** Enumera exatamente **50 ficheiros de projeto** (códigos-fonte, documentação, evidências JSON e workbooks Excel), fornecendo a sua dimensão em bytes e o respetivo hash SHA-256.
- **Arquivo ZIP Consolidado (`TVSI_T08_Grupo5_CP04.zip`):** Contém exatamente **51 ficheiros**, correspondendo aos 50 ficheiros de projeto atestados acrescidos do próprio ficheiro `MANIFEST_ENTREGA.md`.
- **Eliminação de Dependência Circular:** O manifesto contido dentro do arquivo ZIP não inclui o hash do próprio ZIP. O hash SHA-256 do arquivo ZIP final é atestado no ficheiro externo de verificação [TVSI_T08_Grupo5_CP04.zip.sha256](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Grupo5_CP04.zip.sha256).

---

## 6. MATRIZ DEFINITIVA DOS QUATRO DEFEITOS DE SOFTWARE (DEF-01 A DEF-04)

Os defeitos decorrem de erros estruturais no código fornecido de `shipping.py` e foram comprovados por execução reproduzível:

| Defeito | Regra Violada | Condição de Desvio no Código | Comportamento Observado | Comportamento Normativo Esperado | Casos Reveladores | Severidade |
|---|:---:|---|---|---|---|:---:|
| **DEF-01** | BR-01 | Linha 3: `weight >= 20000` | Rejeita indevidamente o limite superior permitido (20000g). | `{"status": "OK", "fee": 12}` | `{"status": "INVALID", "fee": null}` | `H-07` | **Alta** |
| **DEF-02** | BR-02 | Linha 7: `if weight < 1000:` | Para peso de 1000g, salta para o escalão `<= 5000` cobrando taxa de 8€ (Tier 2). | `{"status": "OK", "fee": 5}` | `{"status": "OK", "fee": 8}` | `H-03` | **Média-Alta** |
| **DEF-03** | BR-03 | Linha 14: `fee = 4` | Atribuição destrutiva `=` em vez de acumulação `+= 4`, apagando a taxa base em `REMOTE`. | `{"status": "OK", "fee": 9}` | `{"status": "OK", "fee": 4}` | `H-10, H-12, H-13, F-18, F-29` | **Crítica** |
| **DEF-04** | BR-04 | Linha 5: `weight > 10000` | Limiar de indisponibilidade de express para REMOTE implementado em 10kg em vez de 5kg. | `{"status": "UNAVAILABLE", "fee": null}` | `{"status": "OK", "fee": 10}` | `H-14, F-19, F-30` | **Alta** |

---

## 7. MATRIZ DEFINITIVA DAS TRÊS ANOMALIAS DE DADOS DA IA (DATA-01 A DATA-03)

| Anomalia | Caso IA | Regra Envolvida | Proposta da IA (`expected`) | Oráculo Normativo Correto | Comportamento Observado no Runner | Diagnóstico Técnico da Falha de IA |
|---|:---:|:---:|---|---|---|---|
| **DATA-01** | `AI-05` | BR-03 | `{"status": "OK", "fee": 4}` | `{"status": "OK", "fee": 9}` | **Falso PASS** (baseline devolve 4 devido a `DEF-03`) | A IA omitiu a taxa base (5€), somando apenas a taxa de zona (4€). O teste passou fortuitamente porque a baseline tem o defeito `DEF-03`, mascarando a falha. |
| **DATA-02** | `AI-06` | BR-02 | `{"status": "OK", "fee": 8}` | `{"status": "OK", "fee": 5}` | **Falso PASS** (baseline devolve 8 devido a `DEF-02`) | A IA cometeu erro de fronteira para 1000g, atribuindo taxa de Tier 2 (8€). O teste passou fortuitamente devido ao bug `DEF-02`. |
| **DATA-03** | `AI-09` | BR-04 | `{"status": "OK", "fee": 22}` | `{"status": "UNAVAILABLE", "fee": null}` | **FAIL** (baseline devolve `OK, fee=10`) | A IA tentou tarifar 6000g express em REMOTE somando 12 + 4 + 6 = 22€, ignorando a indisponibilidade legal de BR-04. Falha legítima que revelou a alucinação do modelo. |

---

## 8. AUDITORIA E SINCRONIZAÇÃO DO WORKBOOK EXCEL ([TestResults_T08_Template.xlsx](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP4/TestResults_T08_Template.xlsx))

- **Caminho Canónico Oficial:** `Trabalho_CP4/TestResults_T08_Template.xlsx`
- **Dimensão:** 33.151 bytes
- **SHA-256 Definitivo:** `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef`
- **Esclarecimento Criptográfico (Hash A vs Hash B):** O hash real calculado diretamente sobre o ficheiro final canónico e sobre as réplicas é `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef` (anteriormente referido como Hash B). O valor anteriormente referido como Hash A (`5bbe97aacc418cbfec21b66df825b42d54e26eb86a9782cfbf534ae8e8071861`) constituiu um lapso de transcrição textual num rascunho anterior de relatório.
- **Sincronização Bit-a-Bit das 4 Cópias no Repositório:**

| Caminho da Cópia | Dimensão (Bytes) | SHA-256 | Folhas | Status |
|---|:---:|---|:---:|:---:|
| `Trabalho_CP4/TestResults_T08_Template.xlsx` (Canónico) | 33.151 | `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef` | 6 | **Referência Canónica** |
| `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` | 33.151 | `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef` | 6 | **100% Idêntico (Bit-a-bit)** |
| `Trabalho_CP1/TestResults_T08_Template.xlsx` | 33.151 | `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef` | 6 | **100% Idêntico (Bit-a-bit)** |
| `Trabalho_CP4/TVSI_T08_Students_B1.0_CP4/TestResults_T08_Template.xlsx` | 33.151 | `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef` | 6 | **100% Idêntico (Bit-a-bit)** |

- **Folhas Preservadas (6 folhas):** `Test Cases`, `Executions`, `Defects`, `Static Review`, `Coverage`, `Technique`.
- **Coluna de Requisitos Autónoma:** Célula `C4` contém `'Requirement ID(s)'`.
- **Fórmulas de Cobertura R01..R08:** 324 fórmulas na folha `Coverage` ligam dinamicamente casos e execuções aos requisitos (Diferença entre desenhados e executados = 0).
- **Inspeção Estrutural OpenXML:** A inspeção estrutural OpenXML identificou as fórmulas de rastreabilidade previstas e não detetou problemas estruturais nos componentes XML analisados. Não foi efetuado recálculo dinâmico independente das fórmulas, devido à indisponibilidade do LibreOffice no ambiente de execução. Consequentemente, esta validação não constitui prova independente da correção dos valores calculados.

---

## 9. SCRIPT DE AUDITORIA E META-TESTES DE SENSIBILIDADE

- **Script Principal:** [Trabalho_CP4/audit_cp4.py](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP4/audit_cp4.py) — 12 áreas de auditoria com **27 PASS | 0 FAIL | 0 WARNING | 0 BLOCKED**.
- **Meta-Testes de Mutação:** [Trabalho_CP4/test_auditor_robustness.py](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP4/test_auditor_robustness.py) — 6 testes com fixtures temporárias:
  - Ficheiro em falta: detetado (PASS);
  - JSON malformado: detetado (PASS);
  - IDs duplicados: detetado (PASS);
  - Oráculos divergentes: detetado (PASS);
  - Hashes adulterados: detetado (PASS);
  - ZIP corrompido: detetado (PASS).
- **Formulação Metodológica:** *Os seis cenários controlados demonstram que o auditor deteta as classes de falhas especificamente testadas.*

---

## 10. INTEGRIDADE DO PACOTE ZIP DE ENTREGA

- **Nome do Arquivo:** `TVSI_T08_Grupo5_CP04.zip`
- **Total de Ficheiros:** 51 ficheiros essenciais (50 artefactos de projeto + 1 manifesto)
- **Ficheiro Externo de Validação:** [TVSI_T08_Grupo5_CP04.zip.sha256](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Grupo5_CP04.zip.sha256) (contém a soma criptográfica SHA-256 e dimensão exata do arquivo consolidado, eliminando qualquer dependência circular de cálculo)
- **Validação CRC:** `zipfile.testzip()` executado com veredicto `None` (0 erros).
- **Validação por Extração:** Extração temporária confirmou 100% de correspondência byte a byte e hash a hash com o repositório.

---

## 11. LIMITAÇÕES TÉCNICAS DECLARADAS

1. **Validação do Excel sem Recálculo Independente:** A validação estrutural OpenXML confirmou a legibilidade e a integridade sintática dos componentes XML analisados, incluindo a estrutura das folhas, os namespaces e a presença das fórmulas de rastreabilidade. Não foi efetuado recálculo dinâmico independente das fórmulas, devido à indisponibilidade do LibreOffice no ambiente de execução. Consequentemente, os resultados desta validação não são apresentados como prova de correção dos valores calculados.
2. **Ambiente Multiplataforma:** As execuções em Python 3.12 foram consolidadas nos registos JSON de paridade, mantendo-se no workbook Excel a convenção de uma linha de ensaio lógica por caso de teste (68 linhas).
3. **Preservação dos Defeitos da SUT:** Os 4 defeitos conhecidos de `shipping.py` permanecem inalterados por imperativo metodológico de integridade dos testes.

---

## 12. VEREDICTO FINAL

$$\mathbf{CP04\ —\ FECHADO\ E\ VALIDADO,\ COM\ LIMITAÇÕES\ DOCUMENTADAS}$$

O Checkpoint 4 (CP04) encontra-se tecnicamente consistente, empiricamente reproduzível, documentalmente harmonizado e pronto para submissão académica formal.
