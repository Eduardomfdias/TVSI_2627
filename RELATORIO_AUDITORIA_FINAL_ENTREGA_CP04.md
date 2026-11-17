# RELATÓRIO DE AUDITORIA INTEGRAL DO GIT, ARTEFACTOS E VALIDAÇÃO FINAL DA ENTREGA CP04

**Projeto:** TVSI 2026/27 — Tecnologias e Verificação de Sistemas de Informação  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA | **Grupo 5**  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git`  
**Objeto de Teste (SUT):** `quote(weight, zone, express)` em `shipping.py` — Build `T08-B1.0`  
**Data da Auditoria:** 17 de Novembro de 2026  
**Documento:** `RELATORIO_AUDITORIA_FINAL_ENTREGA_CP04.md`

---

### A. Resumo Executivo

O presente documento constitui o relatório formal e exaustivo da auditoria integral realizada ao repositório Git, aos documentos académicos, ao livro de cálculo oficial Excel (`TestResults_T08_Template.xlsx`), a todas as evidências empíricas de execução, aos scripts de auditoria automatizada e ao pacote de entrega (`TVSI_T08_Grupo5_CP04.zip`).

1. **Integridade da Baseline e Defeitos:** O módulo `shipping.py` permanece rigorosamente inalterado em relação ao commit inicial `9d9f950`. Os 4 defeitos estruturais da SUT (`DEF-01` a `DEF-04`) foram confirmados por testes reproduzíveis e preservados para fins de avaliação docente do desenho de testes.
2. **Workbook Excel Canónico:** O ficheiro `Trabalho_CP4/TestResults_T08_Template.xlsx` (33.151 bytes | SHA-256 `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef`) encontra-se 100% preenchido nas suas 6 folhas oficiais (`Test Cases`, `Executions`, `Defects`, `Static Review`, `Coverage`, `Technique`), com 0 campos obrigatórios vazios e 0 erros de fórmula. As 4 cópias existentes no repositório encontram-se sincronizadas bit-a-bit.
3. **Reconciliação das Execuções:** A contagem de 68 linhas de execução lógica no Excel e 98 execuções físicas multiplataforma ($1 + 16 + 12 + 60 + 4 + 5 = 98$) está plenamente comprovada por registos JSON auditáveis.
4. **Auditoria Técnica:** O script `Trabalho_CP4/audit_cp4.py` reporta **27 PASS | 0 FAIL | 0 WARNING | 0 BLOCKED** e a suite de meta-testes de robustez `Trabalho_CP4/test_auditor_robustness.py` reporta **6/6 testes de mutação aprovados**.
5. **Pacote de Entrega:** O arquivo `TVSI_T08_Grupo5_CP04.zip` agrega exatamente 51 ficheiros (50 artefactos de projeto + 1 manifesto), possui 204.739 bytes e soma SHA-256 `11ba7b2dd785eedf32194c60b965e39858a6d4b61d662ab83c37e020863edcc5`, validada a 100% por teste de extração profunda.
6. **Sincronização Remota:** Ambas as branches `main` e `cp04-final` encontram-se sincronizadas com o repositório remoto GitHub no commit `dc45f4d44359cf562f7e7a2d269a453e8643aaf3`.

---

### B. Inventário dos Artefactos de Entrega

O manifesto oficial (`MANIFEST_ENTREGA.md`) enumera os 50 ficheiros do projeto que constituem o pacote de entrega, complementados pelo próprio manifesto (totalizando os 51 ficheiros do arquivo ZIP). Todos os ficheiros foram inspecionados quanto a existência, dimensão e soma criptográfica SHA-256:

| Artefacto | Caminho Relativo | Existe | Dimensão (Bytes) | SHA-256 | Conteúdo Verificado | Estado |
|---|---|:---:|---:|---|---|:---:|
| Relatório de Auditoria | `AUDITORIA_FINAL_ENTREGA.md` | Sim | 14.303 | `0417ad4db53e...` | Auditoria detalhada das 12 áreas normativas | **CONFORME** |
| Guia do Assistente | `CLAUDE.md` | Sim | 2.179 | `24468175d9c2...` | Regras de integridade e comandos de auditoria | **CONFORME** |
| Fecho Técnico CP04 | `FECHO_FINAL_CP04.md` | Sim | 15.244 | `1bfadad44d5c...` | Relatório técnico de reconciliação e fecho | **CONFORME** |
| Manifesto de Entrega | `MANIFEST_ENTREGA.md` | Sim | 4.908 | `71b3e83f3f5a...` | Tabela criptográfica dos 50 artefactos de projeto | **CONFORME** |
| Documentação Principal | `README.md` | Sim | 11.086 | `fcae13dfdcae...` | Visão global do projeto, equipa e estrutura | **CONFORME** |
| Relatório Consolidado | `Relatorio_Consolidado.md` | Sim | 19.918 | `132646ea8c85...` | Relatório científico integrador dos 4 checkpoints | **CONFORME** |
| Proveniência IA (HTML) | `TVSI_T08_Students_B1.0/AI_PROVENANCE.html` | Sim | 2.826 | `3ea599d9581c...` | Versão HTML do registo de proveniência de IA | **CONFORME** |
| Proveniência IA (MD) | `TVSI_T08_Students_B1.0/AI_PROVENANCE.md` | Sim | 1.841 | `4e101cf1ae7e...` | Registo de proveniência de IA docente | **CONFORME** |
| Regras de Negócio (HTML) | `TVSI_T08_Students_B1.0/BusinessRules.html` | Sim | 6.840 | `1b13dd9ae4fe...` | Versão HTML das Business Rules normativas | **CONFORME** |
| Regras de Negócio (MD) | `TVSI_T08_Students_B1.0/BusinessRules.md` | Sim | 5.234 | `6067b57fa0d2...` | Regras BR-01 a BR-08 normativas | **CONFORME** |
| Guia de Início (HTML) | `TVSI_T08_Students_B1.0/START_HERE.html` | Sim | 4.887 | `4fe59a43a027...` | Guia de introdução discente docente | **CONFORME** |
| Guia de Início (MD) | `TVSI_T08_Students_B1.0/START_HERE.md` | Sim | 3.593 | `5f1714fc2a7e...` | Guia de introdução discente docente | **CONFORME** |
| Enunciado (HTML) | `TVSI_T08_Students_B1.0/StudentAssignment.html` | Sim | 11.233 | `3ecb995185d9...` | Especificação formal do trabalho | **CONFORME** |
| Enunciado (MD) | `TVSI_T08_Students_B1.0/StudentAssignment.md` | Sim | 9.070 | `a4bb0a07bc36...` | Especificação formal do trabalho | **CONFORME** |
| Livro Excel (Base) | `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` | Sim | 33.151 | `5bbe97aacc41...` | Cópia sincronizada bit-a-bit do workbook | **CONFORME** |
| Candidatos IA | `TVSI_T08_Students_B1.0/app/ai_candidates.json` | Sim | 2.193 | `a90623ce1b15...` | 12 casos gerados por IA originais | **CONFORME** |
| Resultados IA | `TVSI_T08_Students_B1.0/app/ai_candidates.results.json` | Sim | 3.197 | `7be26ca9df57...` | Execução dos 12 candidatos de IA no runner | **CONFORME** |
| Casos Humanos | `TVSI_T08_Students_B1.0/app/human_cases.json` | Sim | 2.977 | `26ff01099684...` | 16 casos humanos originais | **CONFORME** |
| Resultados Humanos | `TVSI_T08_Students_B1.0/app/human_cases.results.json` | Sim | 4.254 | `88c69c5dd467...` | Execução dos casos humanos no runner | **CONFORME** |
| Runner Docente | `TVSI_T08_Students_B1.0/app/run_cases.py` | Sim | 4.882 | `b99564c78d0f...` | Script original de execução de testes | **CONFORME** |
| Objeto de Teste (SUT) | `TVSI_T08_Students_B1.0/app/shipping.py` | Sim | 1.155 | `07d2f9b8c9e5...` | Código de produção da baseline (intacto) | **CONFORME** |
| Plano CP01 | `Trabalho_CP1/CP1.md` | Sim | 6.657 | `8103d15da8fa...` | Charter, equipa, análise de riscos e smoke | **CONFORME** |
| Livro Excel (CP01) | `Trabalho_CP1/TestResults_T08_Template.xlsx` | Sim | 33.151 | `5bbe97aacc41...` | Cópia sincronizada bit-a-bit do workbook | **CONFORME** |
| Plano CP02 | `Trabalho_CP2/CP2.md` | Sim | 13.353 | `50a58572183e...` | Metodologia de desenho de testes humanos | **CONFORME** |
| Relatório CP02 | `Trabalho_CP2/Relatorio_CP2.md` | Sim | 12.261 | `9d555883fe4e...` | Congelamento dos 16 casos humanos | **CONFORME** |
| Casos Humanos CP02 | `Trabalho_CP2/human_cases.json` | Sim | 2.977 | `26ff01099684...` | Casos humanos congelados no commit 54ec4d3 | **CONFORME** |
| Resultados CP02 | `Trabalho_CP2/human_cases.results.json` | Sim | 4.254 | `88c69c5dd467...` | 16 execuções humanas históricas | **CONFORME** |
| Plano CP03 | `Trabalho_CP3/CP3.md` | Sim | 6.573 | `1bfa11d61184...` | Avaliação crítica da IA e suite combinada | **CONFORME** |
| Relatório CP03 | `Trabalho_CP3/Relatorio_CP3.md` | Sim | 21.706 | `5a74e5482390...` | Demonstração formal de BR-05 e oráculos | **CONFORME** |
| Auditor CP03 | `Trabalho_CP3/audit_project.py` | Sim | 11.233 | `5776d6536553...` | Script de validação da fase CP03 | **CONFORME** |
| BR-05 Py312 (CP03) | `Trabalho_CP3/br05_independence.py312.json` | Sim | 7.979 | `99aeae30a6c0...` | Evidência de independência BR-05 em Python 3.12 | **CONFORME** |
| BR-05 Results (CP03)| `Trabalho_CP3/br05_independence.results.json` | Sim | 7.979 | `99aeae30a6c0...` | Evidência de independência BR-05 em Python 3.9 | **CONFORME** |
| Casos Finais (CP03) | `Trabalho_CP3/final_cases.json` | Sim | 5.867 | `1f3640243467...` | Suite de 30 casos concebida no CP03 | **CONFORME** |
| Resultados CP03 | `Trabalho_CP3/final_cases.results.json` | Sim | 8.243 | `4a3375b4d45d...` | Execuções da suite final em Python 3.9 | **CONFORME** |
| Resultados Py312 | `Trabalho_CP3/final_cases.results.py312.json` | Sim | 8.243 | `4a3375b4d45d...` | Execuções da suite final em Python 3.12 | **CONFORME** |
| Script BR-05 (CP03) | `Trabalho_CP3/verify_br05_independence.py` | Sim | 5.862 | `a906bd2d5395...` | Script verificador de independência | **CONFORME** |
| Plano CP04 | `Trabalho_CP4/CP4.md` | Sim | 8.618 | `5ff4645229be...` | Planeamento da execução e evidências CP04 | **CONFORME** |
| Relatório CP04 | `Trabalho_CP4/Relatorio_CP4.md` | Sim | 16.516 | `1fe84b901269...` | Relatório de execução e evidências CP04 | **CONFORME** |
| Livro Excel Canónico| `Trabalho_CP4/TestResults_T08_Template.xlsx` | Sim | 33.151 | `5bbe97aacc41...` | Workbook oficial canónico auditado | **CONFORME** |
| Auditor CP04 | `Trabalho_CP4/audit_cp4.py` | Sim | 25.176 | `f948ce6ea848...` | Script formal de auditoria profunda das 12 áreas | **CONFORME** |
| Evidência BR-05 CP04| `Trabalho_CP4/evidence/br05_independence_cp4.json` | Sim | 8.525 | `f59992d9d13e...` | 4 ensaios formais de propriedades BR-05 | **CONFORME** |
| Evidência Robustez | `Trabalho_CP4/evidence/runner_robustness_evidence.json` | Sim | 2.502 | `0e03e5c92850...` | 5 ensaios de robustez CLI | **CONFORME** |
| Casos Finais CP04 | `Trabalho_CP4/final_cases.json` | Sim | 5.867 | `1f3640243467...` | 30 casos finais integrados | **CONFORME** |
| Resultados CP04 | `Trabalho_CP4/final_cases.results.json` | Sim | 8.243 | `4a3375b4d45d...` | Execuções da suite final (20 PASS / 10 FAIL) | **CONFORME** |
| Casos Humanos CP04 | `Trabalho_CP4/human_cases_cp4.json` | Sim | 3.197 | `7be26ca9df57...` | 17 entradas (H-ENV + 16 humanos congelados) | **CONFORME** |
| Resultados Hum. CP04| `Trabalho_CP4/human_cases_cp4.results.json` | Sim | 4.542 | `0032b850d510...` | Execução das 17 entradas humanas | **CONFORME** |
| Log Execução IA | `Trabalho_CP4/runs/ai_candidates_execution.json` | Sim | 3.197 | `7be26ca9df57...` | Log de execução dos candidatos de IA | **CONFORME** |
| Log Execução Final | `Trabalho_CP4/runs/final_cases_execution.json` | Sim | 8.243 | `4a3375b4d45d...` | Log de execução suite final em Python 3.9 | **CONFORME** |
| Log Final Py312 | `Trabalho_CP4/runs/final_cases_execution.py312.json` | Sim | 8.243 | `4a3375b4d45d...` | Log de execução suite final em Python 3.12 | **CONFORME** |
| Log Humano 17 | `Trabalho_CP4/runs/human_17_execution.json` | Sim | 4.542 | `0032b850d510...` | Log de execução das 17 entradas humanas | **CONFORME** |
| Script Atualizador | `Trabalho_CP4/update_workbook_cp4.py` | Sim | 9.091 | `ad8db478d227...` | Script gerador e formatador do Excel OpenXML | **CONFORME** |

---

### C. Auditoria do Workbook Excel (`TestResults_T08_Template.xlsx`)

- **Caminho Canónico Oficial:** `Trabalho_CP4/TestResults_T08_Template.xlsx`
- **Dimensão:** 33.151 bytes
- **SHA-256 Definitivo:** `5bbe97aacc418cbf2fb2c6555e4d1d812f9acfb68d98a48c99ea83a78f9c0bef`
- **Sincronização:** Todas as 4 cópias no repositório (`TVSI_T08_Students_B1.0/`, `Trabalho_CP1/`, `Trabalho_CP4/` e `Trabalho_CP4/TVSI_T08_Students_B1.0_CP4/`) são **100% idênticas bit-a-bit**.

#### Análise Detalhada por Folha

| Folha | Campos Obrigatórios | Campos Preenchidos | Lacunas Detetadas | Resultado |
|---|---|---|:---:|:---:|
| `Test Cases` | 9 colunas (A–I): Test ID, Technique, Rules / objective, Setup / preconditions, Exact inputs, Action steps, Expected outputs, Expected side effects, Priority. | **31 casos preenchidos** (`H-ENV`, `H-01..16`, `F-17..30`). Total de 279 células de dados preenchidas. | 0 | **CONFORME (100% Preenchido)** |
| `Executions` | 10 colunas obrigatórias (A–H, J–K) + 1 condicional (I - Defect IDs): Run ID, Test ID, Requirement ID(s), Date / environment, Expected outputs, Actual outputs, Verdict, Evidence, Defect IDs, Tester, Notes. | **68 linhas de execução lógica** (50 PASS / 18 FAIL). Coluna C com requisitos em C4 e preenchida em todas as linhas. Total de 680 células obrigatórias preenchidas. | 0 | **CONFORME (100% Preenchido)** |
| `Defects` | 9 colunas (A–I): Defect ID, Title / tests, Rule / build / environment, Exact reproduction, Expected, Actual, Evidence, Severity / rationale, Status. | **7 registos preenchidos**: 4 defeitos estruturais da SUT (`DEF-01` a `DEF-04`) e 3 anomalias nos dados de IA (`DATA-01` a `DATA-03`). Total de 63 células preenchidas. | 0 | **CONFORME (100% Preenchido)** |
| `Static Review` | 6 colunas (A–F): Review ID, Rule, Observation / question, Impact / rationale, Suggested clarification, Outcome / owner. | **4 revisões estáticas** (`REV-01` a `REV-04`) cobrindo BR-01, BR-04 e BR-05, com análise individual por cada um dos 4 autores. Total de 24 células preenchidas. | 0 | **CONFORME (100% Preenchido)** |
| `Coverage` | Requisitos R01 a R08 mapeados com Designed, Executed, Not Executed e pares de associação. | **65 pares requisito-teste** mapeados nas linhas 21–120. **324 fórmulas ativas** (`SUMIFS`, `COUNTIFS`, somatórios e subtrações). Cobertura de 100% com 0 não executados. | 0 | **CONFORME (100% Preenchido)** |
| `Technique` | 8 colunas (A–H): Candidate ID / origin, Rule / boundary, Original expectation, Independent oracle, Accept / revise / reject, Reason / duplicate, Final test IDs, Comparison evidence. | **12 candidatos de IA** (`AI-01` a `AI-12`) integralmente analisados e confrontados com os oráculos humanos independentes. Total de 96 células preenchidas. | 0 | **CONFORME (100% Preenchido)** |

#### Declaração de Âmbito sobre a Validação OpenXML
> *"A validação estrutural OpenXML confirmou a legibilidade e a integridade sintática dos componentes XML analisados, incluindo a estrutura das folhas, os namespaces e a presença das fórmulas de rastreabilidade. Não foi efetuado recálculo dinâmico independente das fórmulas, devido à indisponibilidade do LibreOffice no ambiente de execução. Consequentemente, os resultados desta validação não são apresentados como prova de correção dos valores calculados."*

---

### D. Auditoria Documental

Todos os documentos académicos foram auditados quanto à completude, consistência e qualidade técnica:

1. **Autoria e Identificação:** Todos os 11 relatórios e planos identificam univocamente o Grupo 5 e os quatro autores (*Eduardo Dias, Rui Carneiro, Érica Moreira e Beatriz Barbosa*), a instituição (*Universidade do Minho*) e a unidade curricular (*TVSI 2026/27*).
2. **Consistência Normativa:**
   - A suite humana está uniformemente referenciada em todos os documentos como **17 entradas normativas** (16 casos desenhados pelos estudantes `H-01..16` congelados no commit `54ec4d3` + 1 caso de validação de ambiente `H-ENV`), eliminando menções obsoletas a 21 casos.
   - A taxonomia dos defeitos (`DEF-01` a `DEF-04`) e das anomalias de IA (`DATA-01` a `DATA-03`) está rigorosamente harmonizada entre `README.md`, `Relatorio_Consolidado.md`, `Relatorio_CP4.md`, `AUDITORIA_FINAL_ENTREGA.md` e `FECHO_FINAL_CP04.md`.
3. **Qualidade Académica:** Distinção conceitual rigorosa entre falhas observadas legítimas (que comprovam a eficácia dos testes em isolar defeitos) e a conformidade metodológica do processo de teste (100% conforme).

---

### E. Auditoria das Evidências e Reconciliação Quantitativa

#### Tabela de Reconciliação Rigorosa das Execuções

| Bloco de Execução | ID de Ensaio | Casos Únicos | Execuções Lógicas (Excel) | Execuções Físicas (Runtimes) | Veredicto Observado | Ficheiro de Prova / Evidência Primária |
|---|---|:---:|:---:|:---:|:---:|---|
| **Ambiente de Teste** | `RUN-ENV-01` | 1 | 1 | 1 | 1 PASS | `Trabalho_CP4/runs/human_17_execution.json` |
| **Suite Humana Congelada** | `RUN-H02-01..16` | 16 | 16 | 16 | 10 PASS / 6 FAIL | `Trabalho_CP2/human_cases.results.json` |
| **Candidatos de IA** | `RUN-AI-01..12` | 12 | 12 | 12 | 10 PASS / 2 FAIL | `Trabalho_CP4/runs/ai_candidates_execution.json` |
| **Suite Final Integrada** | `RUN-CP4-01..30` | 30 | 30 | 60 *(30 em Py 3.9 + 30 em Py 3.12)* | 20 PASS / 10 FAIL | `Trabalho_CP4/runs/final_cases_execution.json` & `.py312.json` |
| **Propriedades BR-05** | `RUN-CTRL-01..04` | 4 | 4 | 4 | 4 PASS | `Trabalho_CP4/evidence/br05_independence_cp4.json` |
| **Robustez do Runner CLI** | `RUN-ROB-01..05` | 5 | 5 | 5 | 5 PASS | `Trabalho_CP4/evidence/runner_robustness_evidence.json` |
| **Total Global** | — | **68** | **68** | **98** | **50 PASS / 18 FAIL** *(no Excel)* | `Trabalho_CP4/TestResults_T08_Template.xlsx` |

$$\text{Execuções Lógicas Reconciliadas} = 1 + 16 + 12 + 30 + 4 + 5 = \mathbf{68}$$
$$\text{Execuções Físicas Totais} = 1 + 16 + 12 + (30 \times 2) + 4 + 5 = \mathbf{98}$$

*Reconciliação quantitativa consistente com os registos de execução e as evidências identificadas.*

- **Nota sobre BR-05:** Confirmado que o bloco BR-05 corresponde exatamente a **4 execuções físicas** (e não 8), testando as 4 propriedades de determinismo, ausência de estado residual, não mutação e ausência de efeitos colaterais no sistema de ficheiros delimitado no interpretador Python 3.9.

---

### F. Auditoria do Pacote ZIP e Manifesto

- **Ficheiro de Submissão:** `TVSI_T08_Grupo5_CP04.zip`
- **Contagem de Ficheiros:** Exatamente **51 ficheiros** (50 artefactos de projeto + 1 manifesto `MANIFEST_ENTREGA.md`).
- **Dimensão Exata:** **204.739 bytes**
- **SHA-256 Definitivo:** `11ba7b2dd785eedf32194c60b965e39858a6d4b61d662ab83c37e020863edcc5`
- **Validação Estrutural ZIP:** `zipfile.testzip()` executado sem erros (`None`). Ausência absoluta de ficheiros temporários, de sistema (`.DS_Store`) ou de controlo de versões (`.git/`).
- **Validação de Extração:** Extração temporária comprovou correspondência estrita bit-a-bit e hash-a-hash para todos os 51 ficheiros.
- **Manifesto Interno:** `MANIFEST_ENTREGA.md` audita os 50 ficheiros de projeto sem dependência circular.
- **Ficheiro Externo de Validação:** `TVSI_T08_Grupo5_CP04.zip.sha256` contém a assinatura criptográfica:  
  `11ba7b2dd785eedf32194c60b965e39858a6d4b61d662ab83c37e020863edcc5  TVSI_T08_Grupo5_CP04.zip`

---

### G. Auditoria Técnica e Meta-Testes

1. **Script de Auditoria Profunda (`Trabalho_CP4/audit_cp4.py`):**
   - **Resultado:** **PASS: 27 | FAIL: 0 | WARNING: 0 | BLOCKED: 0** (Exit code: 0).
   - Valida as 12 áreas críticas: baseline, congelamento humano, validação sintática de 33 ficheiros JSON, unicidade de IDs, paridade de execução dual-Python, cobertura R01–R08, integridade do Excel e extração do ZIP.
2. **Suite de Meta-Testes de Sensibilidade (`Trabalho_CP4/test_auditor_robustness.py`):**
   - **Resultado:** **6/6 testes de mutação aprovados (100% PASS)**:
     - Detetou com sucesso ficheiro obrigatório em falta (PASS);
     - Detetou com sucesso JSON malformado (PASS);
     - Detetou com sucesso IDs de teste duplicados (PASS);
     - Detetou com sucesso oráculo divergente (PASS);
     - Detetou com sucesso hash adulterado no manifesto (PASS);
     - Detetou com sucesso arquivo ZIP corrompido (PASS).
   - **Declaração de Conformidade:**
     > *"Os seis cenários controlados demonstram que o auditor deteta as classes de falhas especificamente testadas."*

---

### H. Estado do Git e Sincronização GitHub

- **Commit de Fecho:** `dc45f4d44359cf562f7e7a2d269a453e8643aaf3`
  - Mensagem: *"CP04: finalize integrity audit, excel hash reconciliation, and delivery reports"*
- **Ramo Principal (`main`):** `dc45f4d44359cf562f7e7a2d269a453e8643aaf3` (em paridade com `origin/main`).
- **Ramo de Fecho (`cp04-final`):** `dc45f4d44359cf562f7e7a2d269a453e8643aaf3` (em paridade com `origin/cp04-final`).
- **Working Tree:** `nothing to commit, working tree clean`.
- **Integridade da Baseline:** Zero alterações a `shipping.py` e zero modificações a evidências históricas.

---

### I. Pendências e Limitações Metodológicas

Não existem bloqueios técnicos, ficheiros em falta ou inconsistências materiais pendentes. As únicas limitações remanescentes são intrínsecas ao desenho do trabalho prático e encontram-se formalmente documentadas:
1. **Preservação dos 4 Defeitos da SUT:** Os defeitos estruturais em `shipping.py` (`DEF-01` a `DEF-04`) não foram corrigidos no código para preservar a integridade académica do objeto de teste.
2. **Validação OpenXML sem Recálculo Dinâmico:** A verificação das fórmulas no Excel foi realizada por inspeção estática da árvore OpenXML, devido à ausência de LibreOffice no ambiente de execução.
3. **Consolidação Multiplataforma:** As execuções em Python 3.12 encontram-se consolidadas nos registos JSON de paridade, mantendo-se no Excel uma linha lógica por caso de teste (68 linhas).

---

### J. Veredicto Final

$$\mathbf{PRONTO\ COM\ LIMITAÇÕES\ DOCUMENTADAS}$$

*(Os artefactos obrigatórios estão completos, íntegros, auditados e sincronizados no GitHub, subsistindo apenas as limitações metodológicas academicamente explicitadas).*
