# AI comparison material provenance
Created on 20 October 2026 for this TVSI package by the Codex assistant in this conversation. The assistant's system identity is GPT-6; no independently recorded model snapshot/version identifier is available. No separate model/API call or external benchmark was run.

`app/ai_candidates.json` is an AI-authored, deliberately curated teaching fixture, not an unedited transcript of an independent model trial. It intentionally contains mixed-quality suggestions, omissions and repetition for critical review. It is not ground truth and does not measure the performance of a named AI product.

Authoring brief used in this package: “Provide an offline set of candidate tests for a parcel fee policy, mixing plausible correct suggestions with errors and coverage gaps so students can independently critique them.” BusinessRules is the normative policy. No real customer data was used.

Freeze your human suite before inspecting this file's candidate data. The starter human case is only an environment example, not a supplied human benchmark. Record who designed each new human case and when. Review all candidates, including apparently passing ones.

No Internet or AI account is required. If you optionally use another AI tool, record exact tool/model as exposed, date, prompt, response, edits, data supplied and independent checks. Label that material separately from this fixture. Do not claim empirical superiority of humans or AI from this small curated comparison.

---

## Registo de Congelamento da Suite Humana e Cronologia Git (T08 — Grupo 5)

Para garantir total conformidade com a regra BR-08 e dissipar qualquer ambiguidade relativa à localização da suite humana congelada:

### 1. Distinção de Ficheiros
- **Caso de Verificação de Ambiente (`H-ENV`):**  
  Localização: `TVSI_T08_Students_B1.0/app/human_cases.json`  
  Conteúdo: Contém unicamente o caso técnico starter (`weight=500, zone="LOCAL", express=false → OK, fee=5`), fornecido na baseline inicial pelo docente para teste de funcionamento do runner (`run_cases.py`). Não constitui a suite de teste humana de avaliação.
- **Suite Humana Desenhada e Congelada (`H-01` a `H-16`):**  
  Localização: `Trabalho_CP2/human_cases.json`  
  Conteúdo: 16 casos de teste desenhados pelo grupo humano (Eduardo Dias e Rui Carneiro) através de Partições de Equivalência (EP) e Análise de Valores de Fronteira (BVA), baseados estritamente nas regras de negócio BR-01 a BR-05, sem inspeção prévia de `ai_candidates.json` ou do código da aplicação.
- **Resultados da Execução da Suite Humana Congelada:**  
  Localização: `Trabalho_CP2/human_cases.results.json`  
  Veredicto: 10 PASS / 6 FAIL (identificando os defeitos DEF-01 a DEF-04).

### 2. Cronologia Sustentada pelo Histórico Git
A integridade do congelamento prévio da suite humana é comprovada pelos registos reais do repositório Git:

1. **Commit `9d9f950` — 2026-10-22 22:43:21 +0100**  
   *Mensagem:* `feat: add student assignment files, test suites, and initial project charter for TVSI T08`  
   *Registo:* Importação da baseline inicial com o starter `TVSI_T08_Students_B1.0/app/human_cases.json` (apenas `H-ENV`) e o fixture não-inspecionado `TVSI_T08_Students_B1.0/app/ai_candidates.json`.

2. **Commit `54ec4d3` — 2026-10-30 21:48:34 +0000**  
   *Mensagem:* `feat: add CP2 documentation, test cases, and test results for Trabalho_CP2`  
   *Registo:* **Congelamento efetivo da suite humana.** Criação e commit de `Trabalho_CP2/human_cases.json` (16 casos `H-01` a `H-16`) e respetiva evidência de execução `Trabalho_CP2/human_cases.results.json` e relatórios CP02. Nesta data, o ficheiro `ai_candidates.json` permaneceu fechado e por analisar.

3. **Commit `5f9567e` — 2026-11-08 17:32:31 +0000**  
   *Mensagem:* `feat: add CP03 test planning, report, and final cases suite with AI candidate review`  
   *Registo:* **Revisão dos candidatos IA e construção da suite final.** Abertura de `ai_candidates.json`, avaliação dos 12 candidatos face ao oráculo independente já estabelecido no CP02, e geração de `Trabalho_CP3/final_cases.json` (21 casos: 16 humanos intactos + 3 IA aproveitados + 2 de fecho de cobertura) e `Trabalho_CP3/final_cases.results.json`.

### 3. Relação Temporal e Independência
A cronologia do Git comprova de forma inequívoca que a suite humana de 16 casos esteve congelada e executada desde 30 de outubro de 2026, 9 dias antes de qualquer abertura ou inspeção da suite candidata de IA a 8 de novembro de 2026, assegurando total independência do desenho de testes humano face às sugestões geradas por IA.
