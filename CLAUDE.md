# CLAUDE.md — Regras do Projeto TVSI_2627

## Contexto

Projeto universitário de TVSI 2026/27 — Desenho de Testes com Assistência de IA (T08-B1.0).

**Função sob teste:** `calculate_shipping(weight: int, zone: str, express: bool) -> {status, fee}`

**Trabalhos:**
- `Trabalho_CP1/` — Checkpoint 1 (análise inicial)
- `Trabalho_CP2/` — Checkpoint 2 (casos humanos, 16 casos H-01 a H-16, 10 PASS / 6 FAIL)
- `Trabalho_CP3/` — Checkpoint 3 (integração de candidatos IA, prazo 10 nov 2026)

---

## PASTA INTOCÁVEL

**`TVSI_T08_Students_B1.0/` — NÃO MODIFICAR, NÃO APAGAR, NÃO MOVER**

Esta pasta contém os ficheiros originais fornecidos pelo professor.
É uma referência imutável. Nunca editar, nunca apagar ficheiros dentro dela,
mesmo que seja pedido implicitamente.

Se uma tarefa exigir usar esses ficheiros, copiar para outra pasta e
trabalhar na cópia — **jamais no original**.

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
