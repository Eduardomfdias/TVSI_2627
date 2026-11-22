# Plano CP05 — TVSI T08, Grupo 5 (versão 2, revista)

> Versão 2 do plano, revista em 2026-11-22 após verificação do estado real do repositório (commit `a26b0f8`) e da **base entregue no CP04** (`relatorio.CP4.md` + `testResults.md`, exportação do workbook).
> A versão 1 (prompt original) está preservada sem alterações em `ai_log/CP5_prompt_v1_original.md`.
> Prazo CP05: **24 nov 2026, 23:59 (hora de Portugal)**. Não é o relatório final (CP06: 9 dez; entrega final: 15 dez).

---

## 0. Contexto e fontes

Ler primeiro: `CLAUDE.md`, `TVSI_T08_Students_B1.0/StudentAssignment.md`, `BusinessRules.md`, `AI_PROVENANCE.md` **na versão do commit `9d9f950`** (`git show 9d9f950:TVSI_T08_Students_B1.0/AI_PROVENANCE.md`), e a base entregue no CP04:

| Fonte | O que é | Estado |
|---|---|---|
| `relatorio.CP4.md` (raiz) | Relatório CP04 **efetivamente entregue** | Fora do Git; difere de `Trabalho_CP4/Relatorio_CP4.md` |
| `testResults.md` (raiz) | Exportação do workbook atual (6 folhas) | Fora do Git |
| `Trabalho_CP4/TestResults_T08_Template.xlsx` | Workbook binário CP04 | Estruturalmente corrompido (ver P2) |

**Objetivo do CP05:** resultados consolidados até agora — workbook atualizado e que abre, evidência de execução em Python 3.10+, defect reports revistos (black-box), rastreabilidade requisito → teste → execução, comparação humano vs IA de igual dimensão, questões em aberto separadas de defeitos, limitações, riscos residuais e trabalho em falta para o CP06. **Inclui uma secção explícita de correções ao CP04 entregue.**

## 1. Regras invioláveis

1. O oráculo são as BR-01..BR-05. Nunca derivar expectativas do output da aplicação nem do código de `shipping.py`.
2. Nunca inventar resultados. Interpretador ou passo indisponível → **BLOCKED** (BLOCKED não é PASS).
3. Nunca apagar nem sobrescrever runs anteriores. Cada execução nova tem Run ID novo (`RUN-CP5-…`) e ficheiro de evidência novo.
4. Trabalhar em `Trabalho_CP5/`. Nada novo/editado em `TVSI_T08_Students_B1.0/`, exceto o restauro de P1.
5. Novos testes: expected escrito e **commitado antes** de qualquer execução (commit separado).
6. Sem `git push`. Commits locais pequenos e claros; o Eduardo revê e faz push.
7. Linguagem factual. Proibido "100% validado", "zero riscos", "eliminado totalmente", "concluído com sucesso", "cadeia ininterrupta" e equivalentes. Passar testes e cobertura alta não provam correção.
8. Não generalizar sobre IA: o fixture é curado pelo docente e o AI_PROVENANCE proíbe afirmar superioridade empírica de humanos ou de IA.

---

## 2. Problemas verificados no estado atual (a corrigir no CP05)

Todos os pontos abaixo foram **verificados por comando** em 2026-11-22. Registar no relatório o que mudou e porquê.

### 2.1 Repositório e artefactos

| # | Problema | Evidência verificada | Ação |
|---|---|---|---|
| P1 | Baseline do docente alterada | `git diff --stat 9d9f950 -- TVSI_T08_Students_B1.0`: `AI_PROVENANCE.md` (+35 linhas), `TestResults_T08_Template.xlsx` (25 604 → 33 151 B), `app/ai_candidates.results.json` (novo). **O template do docente tem o mesmo SHA-256 (`5bbe97aa…`) que o workbook CP04** — foi sobrescrito pelo workbook de trabalho | ✅ **Feito em 2026-11-22.** Repostos `AI_PROVENANCE.md` e `TestResults_T08_Template.xlsx` a partir do original do professor (`TVSI_T08_Students_B1.0_nao_mexer/`, que não se mexe). Os dois `app/*.results.json` ficam: são saídas previstas do runner (BR-06/BR-07). Acrescento do grupo guardado em `evidence/baseline_restauro_20261122/` (a integrar no `AI_DISCLOSURE.md`); SHA-256 antes/depois no mesmo sítio. Falta commit |
| P2 | Workbooks corrompidos | `openpyxl.load_workbook()` → `KeyError: 'Unknown relationship: rId1'` em **CP4 e CP1** (folhas 1–3 referenciam `rId1`, os `.rels` usam `R9ec27…`, `R5b834…`, `Rf5dab…`). Folhas 4 e 6 estão coerentes. O original de `9d9f950` abre sem erro | Gerar `Trabalho_CP5/TestResults_T08_CP05.xlsx` **a partir do template de `9d9f950`**, reinserindo os dados de `testResults.md`/CP04. Não alterar os ficheiros CP1/CP4 (são históricos); declarar no relatório que estão corrompidos |
| P3 | Ambiente abaixo do mínimo | Execuções CP02, RUN-AI, `runs/final_cases_execution.json`, BR-05 CP4 e RUN-ROB em **3.9.6**. Evidência 3.10+ existente: `runs/final_cases_execution.py312.json` (**3.12.7**, outra máquina) e `evidence/run_0x_*` (**3.12.16**, Mac do Eduardo). O Mac atual tem `python3.12` = 3.12.16 | Runs 3.9.6 preservados e marcados "ambiente não conforme com BR-06". Execuções CP05 em 3.10+; sem 3.10+ → BLOCKED |
| P4 | Duas `final_cases.json` diferentes com 30 casos | `Trabalho_CP4/final_cases.json` = H-01..H-16 + F-17..F-30. `Trabalho_CP4/TVSI_T08_Students_B1.0_CP4/app/final_cases.json` = H-ENV + H-01..H-16 + F-17..F-21 + AI-01..AI-08 (AI-05/06 corrigidos). **`evidence/run_03_final_20261115` (3.12.16) correu a segunda** — não contém F-29/F-30 | A suite final oficial é `Trabalho_CP4/final_cases.json` (a do relatório entregue). Declarar a segunda como variante de trabalho; o run_03 fica preservado mas não é evidência da suite oficial |
| P5 | Caminhos locais expostos | 9 links absolutos `file:` para `/Users/rui.carneiro/…` (7 em `FECHO_FINAL_CP04.md`, 1 em `Relatorio_Consolidado.md`, 1 em `AUDITORIA_FINAL_ENTREGA.md`) | Substituir por caminhos relativos ao repositório |
| P6 | Documentos sobrepostos na raiz | `AUDITORIA_FINAL_ENTREGA.md`, `FECHO_FINAL_CP04.md`, `RELATORIO_AUDITORIA_FINAL_ENTREGA_CP04.md`, `MANIFEST_ENTREGA.md`, `Relatorio_Consolidado.md` | `git mv` para `Trabalho_CP4/auditoria/` (conteúdo inalterado exceto P5); README passa a apontar para o CP05 |
| P7 | Base entregue fora do Git | `relatorio.CP4.md` e `testResults.md` na raiz, untracked | Guardar sem alterações em `Trabalho_CP4/entregue/` (commit próprio, registo do que foi entregue) |

### 2.2 Afirmações do relatório CP04 entregue contraditas pela evidência

Estas vão para a secção "Correções ao CP04 entregue" do Relatório CP05 (tabela afirmação → evidência → correção).

| # | Secção CP04 | Afirmação | Evidência | Correção |
|---|---|---|---|---|
| C1 | §2 (excluído do âmbito), §10 | "shipping.py não foi inspecionado" | §9.4.1 cita "linha 3/5/7/14" e "causa raiz"; Tab. 27, Tab. 20 e nota de §8.3.3 descrevem o código | Declarar que houve inspeção de código após a execução; retirar causas-raiz dos defect reports (ver T2). As expectativas não dependem do código (verificado pelo oráculo independente) |
| C2 | §9.1.3 | Baseline preservada | P1 | Corrigido no CP05 (restauro) |
| C3 | §9.3.1, §9.3.3, §11 | "Eliminando o risco de corrupção", "324 fórmulas, 0 erros" | P2 | Workbook novo, verificado com openpyxl |
| C4 | §9.2.2 | RUN-ENV-01 "confirmou a conformidade com BR-06" | Evidência `app/human_cases.results.json` é 3.9.6 | RUN-ENV-01 é não conforme; nova verificação de ambiente RUN-CP5 em 3.10+ |
| C5 | §8.5.2 | "Nenhum dos defeitos… foi descoberto por um candidato IA" | AI-12 (2000, REMOTE, false; expected 12 correto) → FAIL, actual 4 | AI-12 deteta DEF-03 com a expectativa original |
| C6 | §8.5.1 | "9 dos 12 duplicados exatos ou quase-exatos" | Input igual a um caso humano: AI-01, 04, 05, 06, 07, 08, 10 (7); mesma partição: AI-02, AI-03 (2); AI-10 = AI-01 | Usar a contagem exata |
| C7 | §8.5.3, §10 | "Modelos de IA apresentam uma propensão crítica…", "IA mais fiável a sugerir onde testar" | AI_PROVENANCE: fixture curado, proibido generalizar | Retirar; conclusões limitadas a este fixture |
| C8 | §10 | IA do grupo usada para "geração do conjunto inicial de 12 candidatos" | Fixture do docente (Codex, "GPT-6" segundo o AI_PROVENANCE) | Separar fixture do docente vs uso do grupo |
| C9 | §10 | "ai_candidates.json NÃO foi aberto nesta fase"; "Claude, assistente conversacional"; IA sugeriu "F-17 a F-30" | Texto do CP01 por atualizar; outros docs dizem "Claude Sonnet 4.6 (Claude Code)"; `Relatorio_CP3.md:239-241` diz que o Claude fez a classificação, a suite final e as execuções | `AI_DISCLOSURE.md` com uma linha por utilização (T7) |
| C10 | §9.6 | "Concluídas com sucesso", "0 bloqueios", "cadeia ininterrupta" | Regra 7 | Linguagem factual |
| C11 | §6.2 / §7.1.2 | Q-02 (float) e Q-03 (None) "a confirmar com o docente" | BR-01: "actual integer… no trimming/coercion" resolve ambas | Fechar como resolvidas pela BR (ver T2) |

### 2.3 Problemas no workbook (`testResults.md`)

| # | Folha | Problema | Ação no CP05 |
|---|---|---|---|
| W1 | Executions | RUN-CP4-xx e RUN-CTRL-xx dizem "Python 3.9.6 & 3.12.7" numa linha; evidência indicada é 3.9.6 | Não alterar as linhas; acrescentar nota "evidência indicada é 3.9.6 — não conforme BR-06". Linhas RUN-CP5: um ambiente por linha |
| W2 | Executions | RUN-CTRL-01: "100 chamadas" | Script e evidência: `reps = 10`. Nota de correção |
| W3 | Executions | RUN-AI-xx: "Exec: Claude Code assistido" | Manter (é factual) e refletir no AI_DISCLOSURE |
| W4 | Defects | Reprodução com linhas de código; evidência aponta para run 3.9.6; Status "Open" | Ver T2 |
| W5 | Defects | DATA-01..03: coluna Actual = output da app | Para defeito de dados: "expectativa do fixture" vs "oráculo BR" |
| W6 | Static Review | REV-01..04 ≠ Q-01..Q-05 do relatório; REV-01/02 citam a implementação; REV-03 não é ambiguidade | Unificar (T2) |
| W7 | Coverage | R05 ligado a H-ENV; controlos BR05-xx e ROB-CLI-xx não existem em Test Cases; R06–R08 ligados a casos `quote()` arbitrários | Ver T5 |
| W8 | Test Cases | Sem autor/data de desenho (AI_PROVENANCE: "Record who designed each new human case and when") | Coluna/nota de autoria em F-31+; para os antigos só onde o Git o comprova, senão "a confirmar" |
| W9 | Technique | AI-03 "Reject (redundante)", mas F-28 tem o mesmo input | Marcar F-28 como redundante com H-06 (mesma partição) e igual a AI-03 |
| W10 | Test Cases | F-26 (-100) e F-21 (25000) marcados BVA | Corrigir para EP (não são fronteiras) — nota, sem alterar expected |

---

## 3. Tarefas

### T1 — Verificar oráculo e consolidar  ✅ verificado em 2026-11-22

Oráculo independente (script a partir das BR) sobre todas as suites:

| Suite | N | Expected errados | Duplicados de input |
|---|---|---|---|
| `Trabalho_CP2/human_cases.json` | 16 | 0 | 0 |
| `ai_candidates.json` | 12 | 3 (AI-05, AI-06, AI-09) | AI-10 = AI-01 |
| `Trabalho_CP3/final_cases.json` | 21 | 0 | 0 |
| `Trabalho_CP4/final_cases.json` | 30 | 0 | 0 |
| `Trabalho_CP4/human_cases_cp4.json` | 17 | 0 | H-ENV = H-01 |

H-01..H-16 são idênticos entre CP02 e a suite final CP04 (frozen preservado). Repetir o script no CP05 e guardá-lo em `Trabalho_CP5/tools/oracle_check.py`.

### T2 — Findings: fundir duplicados e classificar

**Defeitos de implementação** (reprodução = setup + comando exato + input + output observado; **sem referências ao código**):

| ID | Sintoma (black-box) | Regra | Testes que o suportam (contar uma vez) |
|---|---|---|---|
| DEF-01 | 20000 g (válido) → INVALID | BR-01 | H-07 |
| DEF-02 | 1000 g LOCAL → fee 8 em vez de 5 | BR-02 | H-03; AI-06 com oráculo corrigido |
| DEF-03 | REMOTE → fee errado (observado 4 sem express, 10 com express, em todos os pesos testados) | BR-03 | H-10, H-12, H-13, F-18, F-29, AI-12 (AI-12 e F-18 têm o mesmo input) |
| DEF-04 | REMOTE express > 5000 g → OK em vez de UNAVAILABLE | BR-04 | H-14, F-19, F-30, AI-09 com oráculo corrigido (AI-09 e F-19 têm o mesmo input) |

Status: `Confirmed` (detetado e com evidência 3.10+) / `Reproduced (data, Run ID, quem)` / `Open question`. Uma eventual nota "observação de inspeção de código pós-execução, não usada como oráculo" fica numa coluna/anexo separado.

**Defeitos de dados (fixture IA):** DATA-01 (AI-05: expected 4, oráculo 9), DATA-02 (AI-06: 8 vs 5), DATA-03 (AI-09: OK/22 vs UNAVAILABLE/null). **AI-10 é redundância, não defeito.**

**Classificação dos candidatos — manter a do CP04 entregue:** Accept AI-11 (→ F-17), AI-12 (→ F-18); Revise AI-09 (→ F-19); Reject os restantes 9. (A v1 deste plano dizia "AI-06 revisto": errado face ao entregue.) Notas: AI-05 e AI-06 com expected corrigido têm o mesmo input que H-10 e H-03; nota de que a variante de trabalho do P4 os incluía.

**Questões de especificação:** unificar Q-01..Q-05 (relatório) e REV-01..REV-04 (workbook) numa única lista. Todas são resolvidas pelo texto das BR (bool → BR-01; float e None → BR-01 "actual integer… no coercion"; precedência → BR-05; 5000 → BR-04 "At exactly 5000 it is available"). **Resultado: 0 questões em aberto**, com explicação de testabilidade. Retirar dos Outcomes as frases sobre a implementação.

### T3 — Fechar lacunas de cobertura (design antes da execução)

`Trabalho_CP5/gap_cases.json`, IDs F-31+, expected derivado das BR. Mostrar a tabela ao Eduardo **antes do commit**; commit antes de qualquer execução.

| ID | weight | zone | express | Expected | Fundamento BR | Técnica |
|---|---|---|---|---|---|---|
| F-31 | null | LOCAL | false | INVALID / null | BR-01 | EP (tipo) |
| F-32 | "500" | LOCAL | false | INVALID / null | BR-01 (sem coerção) | EP (tipo) |
| F-33 | 500 | null | false | INVALID / null | BR-01 | EP (tipo) |
| F-34 | 500 | "" | false | INVALID / null | BR-01 | EP |
| F-35 | 500 | LOCAL | null | INVALID / null | BR-01 | EP (tipo) |
| F-36 | 1000 | REMOTE | false | OK / 9 | BR-02, BR-03 | BVA |
| F-37 | 1001 | REMOTE | false | OK / 12 | BR-02, BR-03 | BVA |
| F-38 | 5000 | REMOTE | false | OK / 12 | BR-02, BR-03 | BVA |
| F-39 | 5001 | REMOTE | false | OK / 16 | BR-02, BR-03 | BVA |
| F-40 | 20000 | REMOTE | false | OK / 16 | BR-01, BR-02, BR-03 | BVA |
| F-41 | 1000 | REMOTE | true | OK / 15 | BR-02..BR-04 | BVA |
| F-42 | 1001 | REMOTE | true | OK / 18 | BR-02..BR-04 | BVA |
| F-43 | 20000 | REMOTE | true | UNAVAILABLE / null | BR-01, BR-04, BR-05 | BVA (precedência) |
| F-44 | 0 | REMOTE | true | INVALID / null | BR-01, BR-05 | BVA (precedência) |
| F-45 | 19999 | LOCAL | false | OK / 12 | BR-01, BR-02 | BVA (interior) |
| F-46 | ⚠ ver nota | REMOTE | true | UNAVAILABLE / null | BR-04 | EP |
| F-47 | ⚠ ver nota | REMOTE | true | UNAVAILABLE / null | BR-04 | EP |

**Nota F-46/F-47 (decisão do Eduardo):** a v1 propunha 10000 e 10001. O expected sai das BR, mas **a escolha de 10000 não tem fundamento nas BR**: vem do conhecimento do código (o CP02 já titulava DEF-04 com "`> 10000`"). Opções: (a) usar pontos neutros da partição 5001–20000 (p. ex. 12500 e 15000) — recomendado; (b) manter 10000/10001 e declarar explicitamente que a escolha foi informada por inspeção de código pós-execução, usada só para delimitar o sintoma.

Notas de execução previsíveis (não alteram o expected): F-40 e F-43 combinam DEF-01 com outros defeitos; registar o output observado sem atribuir causa.

Depois de executar: marcar na Technique o que é redundante e o que acrescenta — F-19 (6000) e F-30 (8000) estão na mesma partição que H-14 para DEF-04; F-28 está na mesma partição que H-06 e tem o mesmo input que AI-03; F-18 tem o mesmo input que AI-12. Não apagar casos.

### T4 — Reprodutibilidade

Em `Trabalho_CP5/runs/RUN-CP5-<AAAAMMDD-HHMMSS>/`:

1. SHA-256 de `shipping.py` e `run_cases.py` antes e depois; têm de bater com `9d9f950` (`693d5db5…` e `36e1f231…`).
2. Cópia limpa de `app/` (sem `__pycache__`); correr a partir da cópia.
3. Python 3.10+ (registar `python --version`, SO, data, tester). Correr separadamente, com exit code registado e `.results.json` com nome único: `human_cases_cp4.json`, `ai_candidates.json` original, `Trabalho_CP4/final_cases.json` (a oficial, ver P4), `gap_cases.json`.
4. Para cada DEF: reprodução isolada em interpretador novo (`python -I -c "from shipping import quote; print(quote(...))"`), 3 vezes, a partir das mesmas condições iniciais.
5. Re-executar `verify_br05_independence.py` (cópia) em 3.10+ e os controlos ROB-CLI-01..05, para substituir as evidências 3.9.6 de R05–R07.
6. Comparar com os runs CP04 em **3.12.7** (`runs/final_cases_execution.py312.json`) e **3.12.16** (`evidence/run_0x_*`, lembrando P4) e reportar qualquer divergência.
7. `RUN_SUMMARY.md` com PASS/FAIL/BLOCKED por suite.

Reprodução noutras máquinas: cada membro indicado em T8 corre pelo menos uma suite no próprio portátil e entrega o results.json + `python --version`. Se não for entregue até 24 nov às 18h00, registar "a confirmar" — nunca preencher por eles.

### T5 — Workbook `Trabalho_CP5/TestResults_T08_CP05.xlsx`

Base: **template de `9d9f950`** (abre sem erro) + dados de `testResults.md`.

- **Test Cases:** linhas existentes sem alteração de expected; acrescentar F-31+ com autor e data de desenho; acrescentar linhas de processo `P-BR05-01..04` (controlos BR-05) e `P-ROB-01..05` (runner), com setup/ação/expected, para a Coverage de R05–R07 poder ligar a testes reais. W10 como nota.
- **Executions:** linhas CP01–CP04 preservadas (com as notas W1/W2); acrescentar RUN-CP5 (build, SO, versão Python exata, data, tester, output observado exato, ficheiro de evidência, verdict, Defect IDs). Estimativa: cerca de 76 linhas de suites + 12 reproduções + 9 de processo → **ultrapassa a linha 84**: alargar a tabela `ExecutionsTable` e os intervalos `Executions!$B$5:$B$84` / `$G$5:$G$84` nas fórmulas da Coverage.
- **Defects:** versão de T2.
- **Static Review:** lista unificada de T2.
- **Coverage:** retirar R05→H-ENV; R06–R08 ligados a P-xx e não a casos `quote()` arbitrários (ou, se se mantiverem, nota "ligação processual"); acrescentar F-31+. Há 65 ligações e capacidade para 100 (linhas 21–120): alargar se necessário (intervalos `$21:$120` e `'Test Cases'!$A$5:$A$84`).
- **Technique:** manter a classificação dos 12 candidatos e acrescentar a tabela T6 e as marcas de redundância de T3.
- **Verificação:** `openpyxl.load_workbook()` sem `read_only`. O LibreOffice **não está instalado** e nenhum Python do sistema tem openpyxl: usar um venv fora do repositório (declarar) ou BLOCKED. O recálculo das fórmulas é verificado manualmente por um membro (nome, data) ou fica declarado como não verificado.

### T6 — Comparação humano vs IA (núcleo T08)  ✅ valores verificados

Suites de igual dimensão declaradas à partida: humano **H-01..H-12** (ordem de ID) vs **AI-01..AI-12**, mais uma linha com o humano completo (H-01..H-16). Recalcular por script (`tools/compare_suites.py`) e conferir à mão pelo menos 4 linhas.

| Métrica | Humano 12 | IA 12 | Humano 16 |
|---|---|---|---|
| Expectativas erradas | 0 | 3 (AI-05, 06, 09) | 0 |
| Duplicados exatos internos | 0 | 1 (AI-10) | 0 |
| Defeitos com expectativas originais | DEF-01, 02, 03 | DEF-03 (AI-12); AI-09 falha por expectativa errada | DEF-01..04 |
| Defeitos expostos com oráculo corrigido | DEF-01, 02, 03 (não DEF-04) | DEF-02, 03, 04 (não DEF-01: sem 20000) | DEF-01..04 |
| Falsos PASS que mascaram defeitos | 0 | 2 (AI-05 → DEF-03; AI-06 → DEF-02) | 0 |

Completar por script: R01–R05 cobertos, partições, fronteiras (0, 1, 1000, 1001, 5000, 5001, 20000, 20001 e 5000/5001 REMOTE express), redundância por partição.

Conclusão limitada ao material: fixture curado pelo docente; não se afirma superioridade de humanos ou de IA. Declarar que a revisão dos candidatos foi assistida por IA (C9).

### T7 — `Trabalho_CP5/Relatorio_CP5.md` (resumo de progresso, ≤ 3 páginas + anexos)

1. Estado em 1 parágrafo.
2. O que mudou desde o CP04: P1–P7 e W1–W10.
3. **Correções ao CP04 entregue** (tabela C1–C11).
4. Resultados consolidados por suite (tabela, com Run IDs e versão Python).
5. Findings: defeitos confirmados, defeitos de dados, questões de especificação (0 em aberto, com justificação), separados.
6. Rastreabilidade compacta R01–R08 → testes → Run IDs. R06–R08 cobertos por verificação de processo/runner (P-xx), não por casos `quote()`.
7. Cobertura e lacunas na ótica T08 (tabela T6).
8. Limitações e riscos residuais: oráculo derivado pelo próprio grupo; função testada só via runner/JSON (tipos Python não exprimíveis em JSON ficam fora: float NaN, tuplos, subclasses de str, etc.); inspeção de código pós-execução (C1); reprodução maioritariamente numa máquina; fixture IA curado; revisão IA assistida por IA; cobertura alta não prova correção.
9. Trabalho por fazer até ao CP06 (9 dez: relatório quase final de 4–6 páginas e demonstração), bloqueios, prioridades, responsáveis.
10. Contribuições individuais com evidência (commits, Run IDs, folhas). Git: só Rui Carneiro (19 commits) e Eduardo Dias (5). Érica e Beatriz → "a confirmar pelo membro", salvo evidência entregue.
11. Divulgação de IA (resumo; detalhe em `AI_DISCLOSURE.md`).

**`Trabalho_CP5/AI_DISCLOSURE.md`:** uma linha por utilização CP01–CP05 (ferramenta/modelo como exposto, data, finalidade, prompt ou referência, material fornecido, edições, verificação independente, quem verificou). Separar: (a) fixture do docente `ai_candidates.json` (Codex, "GPT-6" segundo o AI_PROVENANCE); (b) uso pelo grupo (Claude via Claude Code; onde o modelo exato não for conhecível, escrever "não registado à data" em vez de "Sonnet 4.6"). Incluir como anexo histórico a secção movida do AI_PROVENANCE (P1). Prompts em `ai_log/`.

### T8 — Distribuição proposta (**confirmar antes de escrever no relatório**)

| Membro | CP05 | Reprodução própria |
|---|---|---|
| Eduardo Dias | Coordenação, restauro da baseline (P1), workbook (T5), Relatório CP05, ZIP | Suite final + 2 testes |
| Rui Carneiro | Casos de lacuna F-31+ (T3: design e expected antes da execução); P4–P6 | `gap_cases.json` no portátil próprio + 2 testes |
| Érica Moreira | Re-execução de reprodutibilidade no portátil próprio (T4), gestão de evidências | `human_cases_cp4.json` e `ai_candidates.json` + 2 testes |
| Beatriz Barbosa | Defect reports e fusão de duplicados (T2), Static Review, rastreabilidade e cobertura | Reproduções isoladas DEF-01..04 + 2 testes |

Cada membro reproduz pelo menos 2 testes e regista-os (preparação da demonstração).

### T9 — Pacote

`TVSI_T08_Grupo5_CP05.zip` com `Trabalho_CP1..CP5/`, baseline intacta, README atualizado e `MANIFEST_CP05.md` (lista de ficheiros + SHA-256, sem auditorias redundantes), mais um `.sha256` externo. O `.gitignore` já exclui `*.zip` (verificado).

---

## 4. Critérios de aceitação (mostrar o output de cada um)

1. `diff -rq TVSI_T08_Students_B1.0_nao_mexer TVSI_T08_Students_B1.0 -x .DS_Store` mostra só `app/ai_candidates.results.json` e `app/human_cases.results.json`; SHA-256 antes/depois registados. A pasta `_nao_mexer` nunca é alterada.
2. `python -c "import openpyxl; openpyxl.load_workbook('Trabalho_CP5/TestResults_T08_CP05.xlsx')"` sem erro (ambiente de verificação declarado).
3. Todas as execuções CP05 em Python 3.10+, com evidência por Run ID.
4. Nenhum results.json anterior alterado: `git diff --stat` sobre `Trabalho_CP2..CP4` vazio, exceto os `git mv` de P6, as substituições de P5 e a adição de `Trabalho_CP4/entregue/` (P7).
5. `gap_cases.json` commitado antes do primeiro results.json que o usa (`git log` com as duas datas).
6. Nenhum link absoluto `file:` nos `.md` **fora de `Trabalho_CP5/CP5.md` e `Trabalho_CP5/ai_log/`** (o plano cita o padrão).
7. Defect reports e Static Review sem referências a linhas ou construções do código.
8. Tabela T6 recalculada por script e conferida à mão em pelo menos 4 linhas.
9. Relatório CP05 contém a secção "Correções ao CP04 entregue" (C1–C11).
10. Nenhuma frase proibida pela regra 7 (`grep -niE "100% valid|zero riscos|eliminad[oa] totalmente|conclu[ií]d[oa]s? com sucesso|cadeia ininterrupta"` vazio em `Trabalho_CP5/`).

No fim: lista de commits, tabela de resultados por suite, findings consolidados, pendentes para o CP06, e tudo o que ficou BLOCKED ou "a confirmar".

## 5. Decisões pendentes do Eduardo

1. F-46/F-47: pontos neutros (recomendado) ou 10000/10001 com declaração (T3).
2. Confirmar a distribuição T8 e quem corre cada suite no próprio portátil.
3. Verificação do workbook: autorizar o venv com openpyxl fora do repositório, ou verificação manual.
4. Confirmar que `Trabalho_CP4/final_cases.json` é a suite final oficial (P4).

## 6. Ordem de execução sugerida (2 dias)

| Quando | Passos |
|---|---|
| 22–23 nov | P7 (guardar entregue) → P1 (restauro) → P5/P6 → T1 (script) → T3 (tabela → aprovação → commit) |
| 23 nov | T4 (runs CP5 no Mac + pedido aos membros) → T2 |
| 24 nov manhã | T5 (workbook) → T6 (script + conferência manual) |
| 24 nov tarde | T7 (relatório + AI_DISCLOSURE) → critérios de aceitação → T9 (ZIP) até às 23:59 |
