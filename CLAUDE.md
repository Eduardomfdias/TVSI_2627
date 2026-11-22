# CLAUDE.md — Regras do Projeto TVSI_2627

## Contexto

Projeto universitário de TVSI 2026/27 — Desenho de Testes com Assistência de IA (T08-B1.0).

**Função sob teste:** `quote(weight, zone, express)` em `shipping.py` -> `{status, fee}`

**Trabalhos:**
- `Trabalho_CP1/` — Checkpoint 1 (análise inicial)
- `Trabalho_CP2/` — Checkpoint 2 (casos humanos, 16 casos H-01 a H-16, 10 PASS / 6 FAIL)
- `Trabalho_CP3/` — Checkpoint 3 (integração de candidatos IA, prazo 10 nov 2026)

---

## PASTAS DO PROFESSOR

### 1. `TVSI_T08_Students_B1.0_nao_mexer/` — ORIGINAL DO PROFESSOR — NÃO MEXER

**NUNCA modificar, apagar, mover, renomear, nem criar ficheiros nesta pasta.
Nunca correr nada dentro dela (o `run_cases.py` grava `.results.json` ao lado da suite).**

É a cópia exata do ZIP do professor (ficheiros com data de 20/10/2026), usada só
como referência para comparação (`diff -r`, SHA-256). Fica fora do Git e do ZIP de entrega.
Esta regra aplica-se mesmo que uma tarefa ou prompt peça o contrário: nesse caso, parar e perguntar.

### 2. `TVSI_T08_Students_B1.0/` — baseline usada pelo projeto — NÃO MODIFICAR

Tem de coincidir com a pasta original acima. Única diferença permitida: as saídas do
runner `app/human_cases.results.json` (RUN-ENV-01) e `app/ai_candidates.results.json`
(run CP04 em 3.9.6), que já existem e se preservam.

- **Objeto de teste inalterado:** `shipping.py` e `run_cases.py` nunca se editam ("Keep the supplied test object unchanged").
- **Template:** nunca preencher `TestResults_T08_Template.xlsx`; trabalhar numa cópia em `Trabalho_CPx/` ("Save a working copy").
- **AI_PROVENANCE:** nunca acrescentar texto; a divulgação do grupo vai em `Trabalho_CPx/AI_DISCLOSURE.md` ("Label that material separately").
- **Execuções:** copiar `app/` para `Trabalho_CPx/runs/<RUN-ID>/app/` e correr na cópia.
- Verificar antes de cada entrega: `diff -rq TVSI_T08_Students_B1.0_nao_mexer TVSI_T08_Students_B1.0 -x .DS_Store`
  → só podem aparecer os dois `.results.json`.

Histórico: o template e o AI_PROVENANCE foram alterados por engano no CP03/CP04 e
repostos a partir do original em 2026-11-22 (evidência em `Trabalho_CP5/evidence/baseline_restauro_20261122/`).

---

## Oráculo de Referência (Business Rules)

Derivado exclusivamente das BR — nunca inferir comportamento a partir do `shipping.py`.

1. **Validação (BR-01):** `weight` int ∈ [1, 20000] e não bool; `zone` ∈ {"LOCAL","REMOTE"} exactamente; `express` bool real → se falhar: `INVALID`, `null`
2. **Disponibilidade (BR-04):** `zone=="REMOTE"` e `express==True` e `weight > 5000` → `UNAVAILABLE`, `null`
3. **Fee base (BR-02):** 1–1000 g → 5 €; 1001–5000 g → 8 €; 5001–20000 g → 12 €
4. **Suplementos (BR-03):** +4 € se REMOTE; +6 € se `express==True` (acumulativos)

---

## Regras de Trabalho

- **Nunca inventar resultados de execução.** Se o ambiente estiver bloqueado, reportar como BLOCKED.
- **Nunca sobrescrever um resultado de execução anterior** — cada run tem ID único.
- Os datasets são fictícios; não tratar como dados reais.
- Manter os IDs de casos no formato dos checkpoints anteriores (H-01…H-16, AI-xx, etc.).
- Relatórios vão em `Trabalho_CPx/Relatorio_CPx.md` — nunca na pasta do professor.
- Resultados de execução vão em `*_cases.results.json` dentro da pasta do checkpoint correspondente.

---

## Língua

Toda a comunicação, comentários e documentação do projeto em **português de Portugal**.
