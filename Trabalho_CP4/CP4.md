# CP04 — Plano de Execução

**Deadline: 17 Nov 2026, 23:59 (PT)**
**Build: T08-B1.0 | Pasta: TVSI_T08_Students_B1.0/app/**

---

## Pré-requisito — Ambiente (Eduardo)

```bash
cd TVSI_T08_Students_B1.0/app
python --version          # deve ser 3.10+
python run_cases.py human_cases.json
```

Se bloqueado → registar BLOCKED no workbook e pedir máquina ao docente.

---

## Tarefa 1 — Completar human_cases.json (Rui)

21 casos derivados independentemente das BRs (H-ENV + H-01..H-20).

Cobertura:

- Partições: [1–1000], [1001–5000], [5001–20000] × LOCAL/REMOTE × std/express
- Boundaries: 1, 1000, 1001, 5000, 5001, 20000
- Inválidos: 0, 20001, weight=true (bool excluído por BR-01)
- REMOTE express: =5000 → OK/18; >5000 → UNAVAILABLE/null

---

## Tarefa 2 — Revisão ai_candidates.json (Érica)

Classificar cada candidato contra as BRs **antes** de executar.

| ID    | Decisão | Justificação |
|-------|---------|--------------|
| AI-01 | ACCEPT  | 500g LOCAL std → fee=5 ✓ (BR-02) |
| AI-02 | ACCEPT  | 2000g LOCAL std → fee=8 ✓ (BR-02) |
| AI-03 | ACCEPT  | 6000g LOCAL std → fee=12 ✓ (BR-02) |
| AI-04 | ACCEPT  | 500g LOCAL express → fee=5+6=11 ✓ (BR-03) |
| AI-05 | REJECT  | 500g REMOTE std: fee correto=9 (5+4), AI diz 4. Viola BR-03. |
| AI-06 | REJECT  | 1000g ∈ [1–1000] → fee=5, AI diz 8. Boundary mistake, viola BR-02. |
| AI-07 | ACCEPT  | weight=0 → INVALID/null ✓ (BR-01) |
| AI-08 | ACCEPT  | weight=20001 → INVALID/null ✓ (BR-01) |
| AI-09 | REJECT  | 6000g REMOTE express → UNAVAILABLE (BR-04: >5000g), AI diz OK/22. |
| AI-10 | REJECT  | Duplicado exato de AI-01. Redundante. |
| AI-11 | ACCEPT  | 10000g LOCAL express → fee=12+6=18 ✓ (BR-02+BR-03) |
| AI-12 | ACCEPT  | 2000g REMOTE std → fee=8+4=12 ✓ (BR-02+BR-03) |

**AI rejeitados com expected corrigido para final_cases.json:**

- AI-05 → fee=9
- AI-06 → fee=5
- AI-09 → status=UNAVAILABLE, fee=null

---

## Tarefa 3 — Executar as 3 suites (Érica)

Criar `final_cases.json` = AI aceites (AI-01..04, 07, 08, 11, 12) + AI revisados (05, 06, 09) + human cases.

```bash
# Preservar runs anteriores antes de cada execução
python run_cases.py human_cases.json       # → human_cases.results.json
python run_cases.py ai_candidates.json     # → ai_candidates.results.json
python run_cases.py final_cases.json       # → final_cases.results.json
```

Guardar evidências com nome único, ex: `run_01_human_20261116.json`.

---

## Tarefa 4 — Preencher workbook (Eduardo + todos)

**Aba Executions** — por cada run:

- Test ID, Requirement ID (R01–R08), Build (T08-B1.0), OS, Python version, data, tester
- Observed output (status + fee exatos), evidence filename, verdict (PASS/FAIL/BLOCKED)

**Aba Test Cases** — expected results derivados independentemente das BRs (não copiar output da app).

---

## Tarefa 5 — Draft defects (Beatriz)

Um defect report por finding distinto e reprodutível:

- **Setup**: Python X.Y.Z, OS, Build T08-B1.0
- **Steps**: comando exato + JSON input
- **Expected** (da BR): o que a regra especifica
- **Actual**: o que o software devolveu
- **Evidence**: nome do ficheiro .results.json
- **Severity + justificação**

Findings prováveis:

1. AI-05: fee=4 vs correto=9 → possível defeito no surcharge REMOTE (BR-03)
2. AI-06: fee=8 para 1000g vs correto=5 → possível defeito no boundary [1–1000] (BR-02)
3. AI-09: OK/22 para REMOTE express >5000g vs UNAVAILABLE → possível defeito em BR-04

Separar: *specification question* vs *data defect* (expectativa AI errada) vs *implementation defect* (bug no shipping.py).

---

## Divisão de trabalho

| Quem     | Tarefa                                              | Quando       |
|----------|-----------------------------------------------------|--------------|
| Rui      | human_cases.json completo (21 casos)                | 15 Nov       |
| Érica    | Revisão AI + executar 3 suites + guardar evidências | 15–16 Nov    |
| Beatriz  | Draft defects no workbook                           | 16 Nov       |
| Eduardo  | Integrar workbook + ZIP final + verificação         | 16 Nov tarde |

---

## Checklist entrega

- [ ] human_cases.json com 21 casos frozen
- [ ] 12 AI candidates classificados no workbook (accept/revise/reject + justificação)
- [ ] final_cases.json criado
- [ ] 3 suites executadas, .results.json com nomes únicos
- [ ] Workbook Executions: build, OS, Python, data, tester, evidence, verdict
- [ ] Workbook Defects: ≥1 draft defect por finding distinto reprodutível
- [ ] ZIP com workbook + JSONs + results + evidence
isto
