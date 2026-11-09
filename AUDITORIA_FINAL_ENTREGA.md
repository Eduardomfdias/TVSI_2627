# Relatório de Auditoria Final e Verificação de Entregáveis — TVSI_2627

**Data da Auditoria:** 09 de Novembro de 2026  
**Auditor Técnico:** Quality Assurance & Senior Test Engineering Auditor  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5 (*Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa*)  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git` (Ramo `main`)  
**Ficheiro do Relatório:** `AUDITORIA_FINAL_ENTREGA.md`

---

## 1. Identificação da Auditoria

A presente intervenção consubstancia uma auditoria técnica exaustiva e independente sobre o repositório `TVSI_2627`, com o objetivo de assegurar que todos os artefactos, entregáveis, scripts, suites de teste, evidências e folhas de cálculo respeitam os requisitos académicos e profissionais da unidade curricular.

A auditoria abrangeu os três primeiros checkpoints do plano de trabalho:
- **CP01:** Project Charter, organização do grupo, riscos, e verificação de ambiente.
- **CP02:** Revisão estática, modelação do oráculo independente, congelamento da suite humana (16 casos: `H-01` a `H-16`) e identificação preliminar dos defeitos `DEF-01` a `DEF-04`.
- **CP03:** Auditoria e revisão crítica dos 12 candidatos de IA, construção da suite final combinada (21 casos), execução dual em interpretadores Python (3.9.6 e 3.12.7), validação formal da regra de independência BR-05, preenchimento integral do workbook oficial e consolidação documental.

---

## 2. Commit e Estado Inicial

- **Ramo Ativo:** `main`
- **Commit Inicial da Intervenção:** `fa938fe` (*fix(audit): correct DEF-04/H-13 defect traceability, update Excel workbook, and add consolidated report*)
- **Estado Inicial da Working Tree:**
  - Repositório sincronizado com `origin/main`.
  - Ausência de ficheiros corrompidos ou com conflito de fusão.
  - Baseline docente `TVSI_T08_Students_B1.0/` preservada sem adulterações de código (`shipping.py` intacto).

---

## 3. Inventário dos Entregáveis

| # | Entregável / Ficheiro | Categoria | Finalidade | Estado de Conformidade |
|---|---|---|---|:---:|
| 1 | `Relatorio_Consolidado.md` | Relatório Principal | Documento consolidado e completo da submissão académica | **Completo e Validado** |
| 2 | `README.md` | Documentação Geral | Visão global do repositório, mapa de ficheiros e guias | **Completo e Validado** |
| 3 | `CLAUDE.md` | Engenharia / Contexto | Diretrizes operacionais e convenções do projeto | **Completo e Validado** |
| 4 | `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` | Workbook Oficial | 6 folhas preenchidas, 51 ligações de cobertura, 0 erros | **Auditado e Íntegro** |
| 5 | `Trabalho_CP1/TestResults_T08_Template.xlsx` | Cópia de Trabalho | Workbook sincronizado com a versão oficial | **Auditado e Íntegro** |
| 6 | `Trabalho_CP1/CP1.md` | Relatório CP01 | Charter de teste, papéis, riscos e teste H-ENV | **Completo e Validado** |
| 7 | `Trabalho_CP2/CP2.md` | Relatório CP02 | Modelação do oráculo, partições e fronteiras | **Completo e Validado** |
| 8 | `Trabalho_CP2/Relatorio_CP2.md` | Relatório CP02 | Resultados da suite humana e caracterização de defeitos | **Completo e Validado** |
| 9 | `Trabalho_CP2/human_cases.json` | Suite Humana Congelada | 16 casos (`H-01` a `H-16`) congelados no commit `54ec4d3` | **100% Intacto (Frozen)** |
| 10 | `Trabalho_CP2/human_cases.results.json` | Evidência CP02 | Resultado da suite humana (10 PASS / 6 FAIL) em Py 3.9 | **Preservado e Validado** |
| 11 | `Trabalho_CP3/CP3.md` | Documentação CP03 | Planeamento da revisão crítica dos candidatos de IA | **Completo e Validado** |
| 12 | `Trabalho_CP3/Relatorio_CP3.md` | Relatório CP03 | Relatório do CP03, suite final, cobertura e BR-05 | **Completo e Validado** |
| 13 | `Trabalho_CP3/final_cases.json` | Suite Final Combinada | 21 casos de teste (`H-01..16` + `F-17..21`) | **Completo e Validado** |
| 14 | `Trabalho_CP3/final_cases.results.json` | Evidência CP03 (Py 3.9) | Execução oficial da suite final em Python 3.9.6 | **13 PASS / 8 FAIL** |
| 15 | `Trabalho_CP3/final_cases.results.py312.json` | Evidência CP03 (Py 3.12) | Execução oficial da suite final em Python 3.12.7 | **13 PASS / 8 FAIL** |
| 16 | `Trabalho_CP3/verify_br05_independence.py` | Automação QA | Procedimento de teste computacional de BR-05 | **Auditado e Validado** |
| 17 | `Trabalho_CP3/br05_independence.results.json` | Evidência BR-05 (Py 3.9) | Teste das 4 propriedades BR-05 em Python 3.9.6 | **PASS (4/4)** |
| 18 | `Trabalho_CP3/br05_independence.py312.json` | Evidência BR-05 (Py 3.12) | Teste das 4 propriedades BR-05 em Python 3.12.7 | **PASS (4/4)** |
| 19 | `Trabalho_CP3/audit_project.py` | Automação QA | Script de auditoria automatizada (29 verificações) | **PASS (29/29)** |
| 20 | `TVSI_T08_Students_B1.0/AI_PROVENANCE.md` | Declaração de IA | Proveniência do fixture e cronologia de congelamento | **Completo e Validado** |
| 21 | `TVSI_T08_Grupo5_CP03.zip` | Arquivo de Submissão | Pacote completo com 28 ficheiros essenciais | **111.231 B (Íntegro)** |
| 22 | `MANIFEST_ENTREGA.md` | Manifesto de Entrega | Registo com tamanhos, funções e hashes SHA-256 | **Completo e Validado** |

---

## 4. Problemas Encontrados na Auditoria

1. **Associação Errónea de `H-13` a `DEF-04`:** Em versões anteriores, documentos e a folha `Executions` do workbook associavam o caso `H-13` cumulativamente a `DEF-03` e `DEF-04`. No entanto, segundo a regra BR-04 (*"Express delivery to REMOTE zones is unavailable above 5000 g. At exactly 5000 it is available"*), a 5000g o serviço é nominalmente **disponível**. Tanto o oráculo como a aplicação (com limiar incorreto de 10000g) tratam 5000g como disponível (`status: OK`). Portanto, `H-13` falha unicamente pelo erro de tarifa de `DEF-03` (`fee=10` em vez de `fee=18`). O defeito `DEF-04` é detetado na fronteira estritamente superior por `H-14` (5001g) e confirmado por `F-19` (6000g).
2. **Evidência BR-05 e Delimitação do Sistema de Ficheiros:** A docstring original e relatórios anteriores aludiam genericamente a "ausência de alterações no sistema de ficheiros", quando o script monitorizava apenas a diretoria local da aplicação (`app_dir`).
3. **Discrepância de Versão Python nas Evidências:** Os relatórios declaravam conformidade com Python 3.10+, mas os ficheiros `.results.json` apenas registavam Python 3.9.6.
4. **Ausência de Documento Consolidado Único:** Faltava um relatório consolidado com narrativa integrada unindo CP01, CP02 e CP03.
5. **Inexistência de Script Automatizado de Auditoria com Saída Legível:** Não existia um utilitário autónomo reproduzível para validar de forma integral os 29 requisitos de integridade do projeto.

---

## 5. Correções Efetuadas

1. **Correção Global de Rastreabilidade (`H-13` e `DEF-04`):**
   - Removida a menção de `H-13` como detetor de `DEF-04` em todos os ficheiros: `README.md`, `Trabalho_CP2/CP2.md`, `Trabalho_CP2/Relatorio_CP2.md`, `Trabalho_CP3/Relatorio_CP3.md` e `Relatorio_Consolidado.md`.
   - Na folha `Executions` do workbook (`TestResults_T08_Template.xlsx`), atualizada a célula `I18` (RUN-14) para `DEF-03` exclusivamente.
2. **Execução Dual de Python e Evidências Independentes:**
   - Criado e gravado `final_cases.results.py312.json` sob Python 3.12.7 (13 PASS / 8 FAIL).
   - Criado e gravado `br05_independence.py312.json` sob Python 3.12.7 (PASS).
   - Preservadas intactas as evidências de baseline em Python 3.9.6.
3. **Refinamento e Delimitação da Propriedade 4 da Regra BR-05:**
   - O procedimento `verify_br05_independence.py` foi atualizado para verificar explicitamente ficheiros diretos em `app_dir` (nome, tamanho e timestamp `st_mtime_ns`), delimitando formalmente o âmbito em relatório e docstring, evitando afirmações inflacionadas.
4. **Criação do Relatório Técnico Consolidado:**
   - Elaborado `Relatorio_Consolidado.md` com estrutura exaustiva em três partes (Enquadramento Geral, Desenvolvimento dos Checkpoints e Conclusões Finais com Matriz de Defeitos e Declaração de IA).
5. **Criação do Script de Auditoria:**
   - Desenvolvido `Trabalho_CP3/audit_project.py` com validação de 29 critérios em tempo real e retorno de código de saída zero.
6. **Construção do Pacote de Entrega e Manifesto:**
   - Gerado `TVSI_T08_Grupo5_CP03.zip` contendo os 28 ficheiros essenciais da entrega.
   - Criado `MANIFEST_ENTREGA.md` com a listagem exaustiva e hashes criptográficos SHA-256.

---

## 6. Documentos Consolidados

- **Relatório Principal de Submissão:** [`Relatorio_Consolidado.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Relatorio_Consolidado.md).
- **Documentação de Enquadramento:** [`README.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/README.md) e [`CLAUDE.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/CLAUDE.md).
- **Relatórios Específicos por Checkpoint:**
  - CP01: [`Trabalho_CP1/CP1.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP1/CP1.md).
  - CP02: [`Trabalho_CP2/CP2.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP2/CP2.md) e [`Trabalho_CP2/Relatorio_CP2.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP2/Relatorio_CP2.md).
  - CP03: [`Trabalho_CP3/CP3.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/CP3.md) e [`Trabalho_CP3/Relatorio_CP3.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/Relatorio_CP3.md).

---

## 7. Estado do Workbook Excel

O ficheiro oficial [`TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx) foi auditado folha a folha:
1. **`Test Cases`:** 22 registos (`H-ENV`, `H-01` a `H-16`, `F-17` a `F-21`), com prioridades, técnicas e oráculo independente.
2. **`Executions`:** 22 registos alinhados com `Test Cases`. A célula `I18` (`H-13`) regista estritamente `DEF-03`.
3. **`Defects`:** 4 defeitos documentados (`DEF-01` a `DEF-04`) com causa raiz, impacto e casos detetores.
4. **`Static Review`:** 4 observações de análise estática e ambiguidades de tipo e fronteira.
5. **`Coverage`:** 51 ligações de requisitos ativas (BR-01 a BR-08), com 324 fórmulas dinâmicas (`SUMIFS`, `COUNTIFS`, `IF`) sem qualquer erro ou célula quebrada.
6. **`Technique`:** 12 candidatos de IA avaliados (2 aceites, 1 revisto, 9 rejeitados) com oráculo e fundamentação.

*Erros de cálculo ou fórmula encontrados:* **Zero**. Todas as fórmulas encontram-se ativas e coerentes.

---

## 8. Scripts Criados ou Corrigidos

1. [`Trabalho_CP3/audit_project.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/audit_project.py): Script de auditoria automatizada sem dependências externas (recorre apenas à biblioteca standard de Python), executando 29 asserções de validação estrita.
2. [`Trabalho_CP3/verify_br05_independence.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/verify_br05_independence.py): Parametrizado para suportar caminho de saída CLI e com snapshot de ficheiros de `app_dir`.
3. [`TVSI_T08_Students_B1.0/app/run_cases.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/TVSI_T08_Students_B1.0/app/run_cases.py): Runner oficial mantido intacto na baseline.

---

## 9. Resultados das Execuções

### Suite Humana (`human_cases.json` — 16 casos)
- **Comando:** `/usr/bin/python3 TVSI_T08_Students_B1.0/app/run_cases.py Trabalho_CP2/human_cases.json`
- **Resultados:** 10 PASS / 6 FAIL (Exit code 1).
- **Defeitos Detetados:** `DEF-01` (`H-07`), `DEF-02` (`H-03`), `DEF-03` (`H-10, H-12, H-13`), `DEF-04` (`H-14`).

### Suite Final (`final_cases.json` — 21 casos)
- **Execução Python 3.9.6:**
  - Veredicto: **13 PASS / 8 FAIL** (Exit code 1).
  - Evidência: `Trabalho_CP3/final_cases.results.json`.
- **Execução Python 3.12.7:**
  - Veredicto: **13 PASS / 8 FAIL** (Exit code 1).
  - Evidência: `Trabalho_CP3/final_cases.results.py312.json`.
- **Paridade:** 100% de paridade bit a bit entre os resultados das duas versões.

---

## 10. Validação da Regra BR-05 (Independência)

Procedimento: `Trabalho_CP3/verify_br05_independence.py`  
Executado em Python 3.9.6 e Python 3.12.7:

| Dimensão Testada | Identificador | Condição | Resultado |
|---|---|---|:---:|
| **Determinismo** | `BR05-DET-01` | 10 invocações consecutivas em memória produzem o mesmo output | **PASS** |
| **Ausência de Estado Residual** | `BR05-RES-02` | Sequência intercalada (válido, inválido, indisponível) sem contaminação | **PASS** |
| **Ausência de Mutações** | `BR05-MUT-03` | Inputs inalterados, retornos isolados em memória e namespace preservado | **PASS** |
| **Efeitos Externos Delimitados** | `BR05-EXT-04` | Ausência de stdout/stderr, ambiente inalterado e ficheiros de app/ intactos | **PASS** |

**Veredicto Geral de BR-05:** **PASS** (reproduzível em Py 3.9 e Py 3.12).

---

## 11. Integridade da Suite Humana Congelada

- **Localização:** `Trabalho_CP2/human_cases.json`.
- **Dimensão:** Exatamente 16 casos (`H-01` a `H-16`).
- **Verificação Git:** `git diff 54ec4d3 -- Trabalho_CP2/human_cases.json` produz saída rigorosamente vazia.
- **Conclusão:** A suite humana permaneceu 100% inalterada desde o momento de congelamento documentado no CP02.

---

## 12. Rastreabilidade Final dos Defeitos

| Defeito | Regra Violada | Linha de Código | Descrição do Problema | Casos Detetores |
|---|:---:|:---:|---|---|
| **DEF-01** | BR-01 | Linha 3 | `weight >= 20000` em vez de `> 20000`, rejeitando 20000g como `INVALID` | **`H-07`** |
| **DEF-02** | BR-02 | Linha 7 | `weight < 1000` em vez de `<= 1000`, cobrando Tier 2 (8€) a 1000g | **`H-03`** |
| **DEF-03** | BR-03 | Linha 14 | `fee = 4` em vez de `fee += 4`, sobrescrevendo a tarifa base em REMOTE | **`H-10, H-12, H-13, F-18`** |
| **DEF-04** | BR-04 | Linha 5 | `weight > 10000` em vez de `> 5000` para disponibilidade de express REMOTE | **`H-14, F-19`** |

*Demarcação de H-13:* A encomenda `H-13` (`weight=5000, zone="REMOTE", express=True`) situa-se no limite em que o serviço expresso para REMOTE é nominalmente **disponível** segundo a especificação legal (BR-04: *"At exactly 5000 it is available"*). Por conseguinte, `H-13` não viola nem deteta `DEF-04`. A sua falha decorre exclusivamente do erro tarifário de `DEF-03` (devolve 10€ em vez de 18€). O defeito `DEF-04` é detetado na fronteira estritamente superior por `H-14` (`weight=5001`) e reiterado por `F-19` (`weight=6000`).

---

## 13. Proveniência e Declaração de IA

- **Origem dos Candidatos:** Fixture `ai_candidates.json` gerado pelo modelo GPT-6/Codex para fins pedagógicos.
- **Classificação:** 2 aceites (`AI-11` → `F-17`, `AI-12` → `F-18`), 1 revisto (`AI-09` → `F-19`), 9 rejeitados.
- **Erros Identificados na IA:** Três erros conceituais graves demonstrados: `AI-05` (replicou a omissão de taxa base da implementação), `AI-06` (confundiu limites de tier alinhando-se com o bug de código), e `AI-09` (ignorou completamente a regra de indisponibilidade BR-04 prevendo `OK` a 6000g).
- **Declaração Formal:** Documentada em detalhe no `AI_PROVENANCE.md` e na Secção 11 do `Relatorio_Consolidado.md`.

---

## 14. Validação do Pacote ZIP

- **Nome do Arquivo:** `TVSI_T08_Grupo5_CP03.zip`.
- **Localização:** Raiz do repositório (`./TVSI_T08_Grupo5_CP03.zip`).
- **Dimensão:** 111.231 bytes.
- **Total de Ficheiros:** 28 ficheiros essenciais.
- **Teste de Integridade:** `zipfile.testzip()` executado com retorno `None` (0 ficheiros corrompidos, 100% íntegro).
- **Hash SHA-256:** `8e7527a5d013229c4e52dcb247181af090bad5abba1b491056d5cbcec46bc83c`.

---

## 15. Manifesto dos Entregáveis

O manifesto completo de submissão encontra-se formalizado em [`MANIFEST_ENTREGA.md`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/MANIFEST_ENTREGA.md), contendo o inventário de cada ficheiro, a categoria, o ambiente de teste, o estado de validação e o respetivo hash criptográfico SHA-256.

---

## 16. Estado Final do Git

- **Branch Ativa:** `main`
- **Último Commit Remoto:** [`fa938fe`](https://github.com/Eduardomfdias/TVSI_2627/commit/fa938fe).
- **Ficheiros Modificados no Espaço de Trabalho Local:**
  - `Relatorio_Consolidado.md` (expansão da estrutura completa e narrativa formal)
  - `README.md` (adição de referências ao manifesto, relatório consolidado e script de auditoria)
- **Ficheiros Novos na Working Tree:**
  - `Trabalho_CP3/audit_project.py`
  - `MANIFEST_ENTREGA.md`
  - `AUDITORIA_FINAL_ENTREGA.md`
- **Ficheiros Locais Ignorados:** `TVSI_T08_Grupo5_CP03.zip` (ignorado via `.gitignore`).
- **Estado de Sincronização:** Nenhuma alteração foi enviada para o servidor remoto (`origin/main`), respeitando a diretiva de aguardar autorização expressa.

---

## 17. Limitações e Pendências

1. **Números Mecanográficos dos Estudantes:**  
   Em cumprimento estrito do princípio de não-invenção de dados académicos, os números mecanográficos dos estudantes (*Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa*) não foram gerados artificialmente. Devem ser indicados pelos alunos no momento do envio formal da submissão no formulário do Moodle da Universidade do Minho.
2. **Ambiente com Código com Defeitos:**  
   A suite final apresenta 8 falhas nominais (13 PASS / 8 FAIL) que decorrem exclusivamente dos quatro defeitos identificados em `shipping.py`. O código da aplicação sob teste não foi modificado, mantendo a autenticidade exigida pela avaliação pedagógica.

---

## 18. Veredicto Final

Com base na execução de todas as verificações automáticas e manuais:

### **PRONTO PARA ENTREGA COM RESSALVAS**

**Fundamentação:**  
Todos os artefactos, relatórios, suites de teste, scripts de validação, evidências duais de Python (3.9.6 e 3.12.7), auditorias de BR-05, o workbook oficial de testes e o pacote de submissão ZIP encontram-se 100% auditados, íntegros e em conformidade estrita com o enunciado da unidade curricular.  
A única ressalva prende-se com o preenchimento dos números de aluno individuais no ato de submissão formal no Moodle.

