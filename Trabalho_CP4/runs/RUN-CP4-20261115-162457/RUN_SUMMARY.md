# RUN-CP4-20261115-162457 — Execução de final_cases.json (suite CP3, 21 casos) no âmbito do CP4

**Data:** 2026-11-15 · **Build:** T08-B1.0 · **Execução:** Claude Code, a pedido do grupo

## Isolamento
- `shipping.py` e `run_cases.py` copiados de `TVSI_T08_Students_B1.0/app/` para `app/` (cópia de trabalho); execução com `python -B` (sem `__pycache__`).
- SHA-256 de todos os ficheiros da pasta do professor antes/depois: **idênticos** (`professor_sha256.before.txt` / `.after.txt`).
- Execuções anteriores em `Trabalho_CP3/` não foram sobrescritas (a suite executada é `Trabalho_CP3/final_cases.json`, não alterada).

## Resultados
| Execução | Python | Resultado | Exit code |
|---|---|---|---|
| `final_cases.json` | 3.12.16 | 13 PASS / 8 FAIL | 1 |
| `final_cases.json` | 3.9.6 | 13 PASS / 8 FAIL | 1 |
| `verify_br05_independence.py` | 3.12.16 | PASS (4/4 propriedades) | 0 |
| `verify_br05_independence.py` | 3.9.6 | PASS (4/4 propriedades) | 0 |

FAILs: H-03 (DEF-02), H-07 (DEF-01), H-10/H-12/H-13/F-18 (DEF-03), H-14/F-19 (DEF-04). Não surgiram defeitos novos.

## Verificações (`oracle_check.py` → `verificacao.txt`)
- Os 21 `expected` de `final_cases.json` coincidem com o oráculo derivado das BR.
- H-01..H-16 são idênticos a `Trabalho_CP2/human_cases.json`.
- Os resultados são iguais aos da execução anterior (py312) e iguais entre 3.12 e 3.9.

Nota: o interpretador 3.12 do sistema está agora em **3.12.16** (a execução anterior registou 3.12.7). O comportamento é o mesmo.
