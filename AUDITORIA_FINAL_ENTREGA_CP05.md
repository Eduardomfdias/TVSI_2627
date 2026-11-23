# Relatório de Auditoria Final e Verificação de Entregáveis — CP05
## TVSI 2026/27 — UMinho | Grupo 5

**Data da Auditoria:** 23 de Novembro de 2026  
**Auditor Técnico:** Senior QA Engineer, Lead Auditor & Academic Integrity Specialist  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA (Build T08-B1.0)  
**Grupo:** Grupo 5 (*Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa*)  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git` (Ramo `main`)  
**Arquivo de Entrega:** `TVSI_T08_Grupo5_CP05.zip`  
**Ficheiro de Checksum:** `TVSI_T08_Grupo5_CP05.zip.sha256`  

---

## A. Estado Inicial do Repositório

- **Branch ativo:** `main` (sincronizado com `origin/main` após incorporação do commit `0119e2d`).
- **Commit inicial de auditoria:** `0119e2d208d918d0ba7875a1a274c19a3c6d60de` ("docs: add requirement traceability section and table to report").
- **Alterações locais preexistentes:** Preservada a alteração local em `TVSI_T08_Grupo5_CP04.zip.sha256` (recalculado para refletir o hash real do arquivo existente em disco), mantendo o princípio de preservação de evidências históricas.
- **Histórico recente:** Incorporação dos módulos `Trabalho_CP5/`, histórico de commits CP01–CP04 preservado intacto sem reescrita de árvore.

---

## B. Alterações Realizadas na Operação CP05

1. **Correção da Rastreabilidade e Cobertura (`Trabalho_CP5/tools/build_workbook.py` e `TestResults_T08_CP05.xlsx`):**
   - Eliminada a ligação espúria entre R05 e H-ENV, porquanto H-ENV não exercita precedência nem independência funcional.
   - Desassociados todos os casos da função `quote()` dos requisitos processuais R06, R07 e R08, eliminando associações fictícias herdadas do CP04.
   - Saneada e reconstruída a folha `Coverage`, garantindo intervalos dinâmicos de fórmulas estendidos até à linha 300 (`$5:$300` e `$21:$300`) sem referências circulares ou tabelas corrompidas.
   - Total de ligações funcionais recalculadas: 79 pares desenhados (48 executados e 31 por executar).

2. **Evidência Independente de Cobertura (`Trabalho_CP5/evidence/coverage_valores_esperados.txt`):**
   - Atualizado o documento de cálculo independente para refletir a simulação exata das fórmulas Excel: R01 (24/15/9), R02 (25/17/8), R03 (17/10/7), R04 (10/5/5), R05 (3/1/2) e R06..R08 (0/0/0 na matriz funcional de `quote()`).

3. **Revisão e Consolidação do Relatório CP05 (`Trabalho_CP5/Relatorio_CP5.md`):**
   - Reconciliação numérica de todas as tabelas com o workbook e os ficheiros `.results.json`.
   - Correção da descrição da comparação histórica com o CP04: identificação explícita de que a execução de 3.12.16 do CP04 continha apenas 21 casos, apresentando 9 casos sem resultado correspondente (`F-22` a `F-30`).
   - Introdução da tabela formal de revisão dos 17 casos de lacuna (`F-31` a `F-47`), identificando inputs, expectativas das BR, justificações e estado de validação humana como "Pendente".
   - Avaliação metodológica transparente dos casos F-46 e F-47 (10000 e 10001), assumindo o viés de inspeção de código de CP02 e recomendando pontos neutros (12500 e 15000) para o CP06.
   - Estruturação formal das prioridades CP06 (P0, P1, P2) com responsáveis e critérios de conclusão objetivos.
   - Discriminação das contribuições individuais por membro, separando trabalho realizado, assistido por IA, revisto por humanos e pendente.

4. **Registo de Divulgação de IA (`Trabalho_CP5/AI_DISCLOSURE.md`):**
   - Atualização da separação estrita entre o fixture do docente (`ai_candidates.json`) e a utilização de ferramentas pelo grupo.
   - Definição explícita dos 4 papéis de processo: Operador da Execução, Autor do Teste, Revisor do Resultado e Assistência de IA.
   - Declaração de limitação de registos históricos de prompts nos checkpoints iniciais.

5. **Geração do Arquivo Consolidado de Entrega e Checksum:**
   - Criação de `TVSI_T08_Grupo5_CP05.zip` e geração de `TVSI_T08_Grupo5_CP05.zip.sha256`.

---

## C. Validações Técnicas e de Integridade

- **Integridade da Baseline Original (Commit `9d9f950`):**
  - Verificação criptográfica completa de todos os 15 ficheiros de `TVSI_T08_Students_B1.0/`.
  - Hashes SHA-256 de `shipping.py` (`693d5db565...`) e `run_cases.py` (`36e1f23173...`) 100% idênticos à baseline oficial do docente.
- **Workbook Oficial (`TestResults_T08_CP05.xlsx`):**
  - Abertura sem erros através da biblioteca `openpyxl`.
  - Folhas validadas: `Test Cases` (48 casos únicos, 0 duplicados), `Executions` (127 registos lógicos), `Defects` (4 defeitos de código, 3 defeitos de dados IA, 2 notas), `Static Review` (REV-01..04 reavaliadas, REV-CP05 adicionada), `Coverage` (fórmulas ativas, 0 links inválidos), `Technique` (Tabela T6 e redundâncias).
  - Ausência de tabelas órfãs ou corrompidas (correção de `rId1`).
- **Oráculo Independente (`tools/oracle.py`):**
  - 100% de concordância entre as expectativas de `gap_cases.json` e a função oráculo derivada exclusivamente de BR-01 a BR-05.
- **Execuções e Evidências:**
  - Preservação da execução oficial `RUN-CP5-20261122-212810` (Python 3.12.16) com exit codes e stdout registados.
  - Preservação do run abortado `RUN-CP5-20261122-212747` com a respetiva justificação técnica (`ABORTED.md`).
  - Confirmação de 3 reproduções isoladas independentes para cada um dos defeitos DEF-01 a DEF-04 em `reproducoes_isoladas.txt`.

---

## D. Síntese dos Resultados Oficiais

| Dimensão | Métrica | Detalhe |
|---|:---:|---|
| **Casos de Teste na Suite Oficial** | **48** | 17 Humanos (H-ENV + H-01..16), 14 Complementares (F-17..30), 17 Lacunas (F-31..47) |
| **Casos Executados (RUN-CP5)** | **31** | 1 H-ENV, 16 H-01..16, 14 F-17..30 (executados em suites de 17, 12 e 30 casos) |
| **Casos com Veredicto PASS** | **21** | 20 na suite final + H-ENV |
| **Casos com Veredicto FAIL** | **10** | H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30 |
| **Defeitos Confirmados da Aplicação** | **4** | DEF-01 (BR-01), DEF-02 (BR-02), DEF-03 (BR-03), DEF-04 (BR-04, BR-05) |
| **Defeitos de Dados no Fixture IA** | **3** | DATA-01 (AI-05), DATA-02 (AI-06), DATA-03 (AI-09) |
| **Casos Desenhados Pendentes** | **17** | F-31 a F-47 (desenhados, oráculo validado, aguardam execução em CP06) |
| **Ligações de Cobertura Funcional** | **79** | 48 executadas (60.8%), 31 por executar (39.2%) |

---

## E. Limitações e Pendências Declaradas

1. **Confirmação Nominal do Operador de Execução:** O campo `Tester` nos ficheiros `ENVIRONMENT.txt` permanece como `a confirmar (sessão Claude Code na máquina de Eduardo Dias)`. A atribuição nominal definitiva será ratificada pelo grupo no CP06.
2. **Revisão Humana dos Casos F-31 a F-47:** A validação humana independente dos 17 novos casos encontra-se assinalada como pendente na tabela de revisão, aguardando assinatura e data de validação por um elemento do grupo.
3. **Controlos de Robustez e Independência:** Os testes de processo `P-BR05-01..04` e `P-ROB-01..05` foram executados no CP04 apenas em Python 3.9.6, aguardando execução oficial em Python 3.10+ no CP06.
4. **Valores Exploratórios de F-46 e F-47:** A seleção dos valores 10000 e 10001 assenta em inspeção anterior de código; serão complementados por pontos neutros (12500 e 15000) no CP06.

---

## F. Pacote Oficial de Entrega

- **Ficheiro:** `TVSI_T08_Grupo5_CP05.zip`
- **Conteúdo:** 148 ficheiros (baseline do docente, checkpoints CP01 a CP04 históricos, módulo CP05 integral, relatórios de auditoria e manifestos).
- **Integridade do Ficheiro ZIP:** Testada com sucesso (`zipfile.testzip() == None`).
- **Checksum SHA-256:** Registado no ficheiro homónimo `TVSI_T08_Grupo5_CP05.zip.sha256`.

---

## G. Decisão Final da Auditoria

Com base na evidência coligida, na preservação absoluta da baseline do docente (`9d9f950`), na ausência de invenção de resultados ou falsificação de execuções, na coerência interna de toda a cadeia de rastreabilidade e na transparência total relativamente às pendências existentes, a entrega CP05 é classificada como:

### **APROVADA COM PENDÊNCIAS EXPLICITAMENTE IDENTIFICADAS**

A entrega encontra-se consolidada, tecnicamente auditada, academicamente defensável e pronta para submissão no âmbito do Checkpoint 5.
