# RUN-CP5-20261122-212810 — Re-execução de reprodutibilidade (CP05)

- Run ID: RUN-CP5-20261122-212810
- Data: 2026-11-22T21:28:11Z
- SO: macOS 27.2.1 (arm64)
- Python: Python 3.12.16
- Comando: /opt/homebrew/bin/python3.12 -E -s run_cases.py <suite>.json (cwd = cópia limpa app/)
- Build: T08-B1.0
- Tester: a confirmar (sessão Claude Code na máquina de Eduardo Dias)

## Isolamento e integridade
- `shipping.py` e `run_cases.py` copiados de `TVSI_T08_Students_B1.0/app/` para `app/` (cópia limpa, sem `__pycache__`); a pasta do docente não foi escrita (o runner grava o `.results.json` ao lado da suite, por isso a suite corre a partir da cópia).
- SHA-256 de `shipping.py` e `run_cases.py` iguais a `9d9f950` antes e depois (`sha256_before.txt`, `sha256_after.txt`).
- Flag `-I` não utilizável: retira a pasta do script do `sys.path` e o runner não importa `shipping` (ver run abortado `RUN-CP5-20261122-212747/ABORTED.md`). Usado `-E -s` (ignora variáveis PYTHON* e site do utilizador).

## Resultados por suite
| Suite | Casos | PASS | FAIL | BLOCKED | Exit code | Ficheiro |
|---|---:|---:|---:|---:|---:|---|
| human_cases_cp4.json (H-ENV + H-01..16) | 17 | 11 | 6 | 0 | 1 | `results/human_cases_cp4.RUN-CP5-20261122-212810.results.json` |
| ai_candidates.json (original, expectativas da IA) | 12 | 10 | 2 | 0 | 1 | `results/ai_candidates.RUN-CP5-20261122-212810.results.json` |
| final_cases.json (H-01..16 + F-17..30) | 30 | 20 | 10 | 0 | 1 | `results/final_cases.RUN-CP5-20261122-212810.results.json` |
| gap_cases.json (F-31..47) | 17 | — | — | **BLOCKED** | — | Não executado: aguarda commit do desenho (design before execution) |

FAILs: humana H-03, H-07, H-10, H-12, H-13, H-14 · IA AI-09 (expectativa errada), AI-12 (deteção de DEF-03) · final H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30.

## Comparação com CP04 (`comparacao_cp4.txt`)
- final_cases vs `Trabalho_CP4/runs/final_cases_execution.py312.json` (3.12.7): sem divergências nos 30 casos.
- human e IA vs execuções CP04 em 3.9.6: sem divergências. (Não existe execução CP04 destas duas suites em 3.10+.)
- `RUN-CP4-20261115-162457/final_cases.results.py312.json` tem 21 casos porque é a suite do CP3 — não é comparável com os 30 casos.

## Reproduções isoladas (`reproducoes_isoladas.txt`)
DEF-01..DEF-04 reproduzidos 3 vezes cada, num processo Python novo por chamada, com output idêntico nas 3 repetições.
