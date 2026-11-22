## Test Cases

| | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Test Cases — T08 | | | | | | | | |
| Derive expected results from BusinessRules BEFORE execution. One scenario per row. | | | | | | | | |
| | | | | | | | | |
| Test ID | Technique | Rules / objective | Setup / preconditions | Exact inputs | Action steps | Expected outputs | Expected side effects | Priority |
| H-ENV | Smoke / Environment | Ambiente: weight=500, zone=LOCAL, express=false -> OK, fee=5 | Build T08-B1.0, Python 3.10+, terminal na pasta app | {"weight": 500, "zone": "LOCAL", "express": false} | Executar quote(500, 'LOCAL', False) via runner | {"status": "OK", "fee": 5} | Nenhum (função pura) | Alta |
| H-01 | EP | BR-02, BR-03: Caso nominal Tier 1 (1–1000g), zona LOCAL sem express | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "LOCAL", "express": false} | Executar quote(500, 'LOCAL', False) | {"status": "OK", "fee": 5} | Nenhum | Alta |
| H-02 | BVA | BR-01, BR-02: Limite inferior mínimo válido de peso (weight=1g), Tier 1 | Build T08-B1.0, Python 3.10+ | {"weight": 1, "zone": "LOCAL", "express": false} | Executar quote(1, 'LOCAL', False) | {"status": "OK", "fee": 5} | Nenhum | Alta |
| H-03 | BVA | BR-01, BR-02: Limite superior da fronteira do Tier 1 (weight=1000g) | Build T08-B1.0, Python 3.10+ | {"weight": 1000, "zone": "LOCAL", "express": false} | Executar quote(1000, 'LOCAL', False) | {"status": "OK", "fee": 5} | Nenhum | Alta |
| H-04 | BVA | BR-01, BR-02: Limite inferior da fronteira do Tier 2 (weight=1001g) | Build T08-B1.0, Python 3.10+ | {"weight": 1001, "zone": "LOCAL", "express": false} | Executar quote(1001, 'LOCAL', False) | {"status": "OK", "fee": 8} | Nenhum | Alta |
| H-05 | BVA | BR-01, BR-02: Limite superior da fronteira do Tier 2 (weight=5000g) | Build T08-B1.0, Python 3.10+ | {"weight": 5000, "zone": "LOCAL", "express": false} | Executar quote(5000, 'LOCAL', False) | {"status": "OK", "fee": 8} | Nenhum | Alta |
| H-06 | BVA | BR-01, BR-02: Limite inferior da fronteira do Tier 3 (weight=5001g) | Build T08-B1.0, Python 3.10+ | {"weight": 5001, "zone": "LOCAL", "express": false} | Executar quote(5001, 'LOCAL', False) | {"status": "OK", "fee": 12} | Nenhum | Alta |
| H-07 | BVA | BR-01, BR-02: Limite superior máximo válido de peso (weight=20000g), Tier 3 | Build T08-B1.0, Python 3.10+ | {"weight": 20000, "zone": "LOCAL", "express": false} | Executar quote(20000, 'LOCAL', False) | {"status": "OK", "fee": 12} | Nenhum | Alta |
| H-08 | BVA | BR-01: Limite inferior inválido abaixo do mínimo (weight=0) | Build T08-B1.0, Python 3.10+ | {"weight": 0, "zone": "LOCAL", "express": false} | Executar quote(0, 'LOCAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Alta |
| H-09 | BVA | BR-01: Limite superior inválido acima do máximo (weight=20001) | Build T08-B1.0, Python 3.10+ | {"weight": 20001, "zone": "LOCAL", "express": false} | Executar quote(20001, 'LOCAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Alta |
| H-10 | EP | BR-02, BR-03: Suplemento de zona REMOTE (+4€) em Tier 1 sem express | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "REMOTE", "express": false} | Executar quote(500, 'REMOTE', False) | {"status": "OK", "fee": 9} | Nenhum | Alta |
| H-11 | EP | BR-02, BR-03: Suplemento de envio express (+6€) para zona LOCAL em Tier 1 | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "LOCAL", "express": true} | Executar quote(500, 'LOCAL', True) | {"status": "OK", "fee": 11} | Nenhum | Alta |
| H-12 | EP | BR-02, BR-03: Suplementos acumulativos REMOTE (+4€) e express (+6€) em Tier 1 | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "REMOTE", "express": true} | Executar quote(500, 'REMOTE', True) | {"status": "OK", "fee": 15} | Nenhum | Alta |
| H-13 | BVA | BR-02, BR-03, BR-04: Limite exato de disponibilidade express REMOTE (5000g disponível) | Build T08-B1.0, Python 3.10+ | {"weight": 5000, "zone": "REMOTE", "express": true} | Executar quote(5000, 'REMOTE', True) | {"status": "OK", "fee": 18} | Nenhum | Crítica |
| H-14 | BVA | BR-04: Limite imediato de indisponibilidade express REMOTE (5001g indisponível) | Build T08-B1.0, Python 3.10+ | {"weight": 5001, "zone": "REMOTE", "express": true} | Executar quote(5001, 'REMOTE', True) | {"status": "UNAVAILABLE", "fee": null} | Nenhum | Crítica |
| H-15 | EP | BR-01: Rejeição de tipo booleano no peso (weight=True excluído de int) | Build T08-B1.0, Python 3.10+ | {"weight": true, "zone": "LOCAL", "express": false} | Executar quote(True, 'LOCAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| H-16 | EP | BR-01: Validação estrita case-sensitive da zona (zone='local' inválido) | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "local", "express": false} | Executar quote(500, 'local', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-17 | EP | BR-02, BR-03: Tier 3 (10000g) com express para zona LOCAL (12+6=18€) | Build T08-B1.0, Python 3.10+ | {"weight": 10000, "zone": "LOCAL", "express": true} | Executar quote(10000, 'LOCAL', True) | {"status": "OK", "fee": 18} | Nenhum | Média |
| F-18 | EP | BR-02, BR-03: Tier 2 (2000g) para zona REMOTE sem express (8+4=12€) | Build T08-B1.0, Python 3.10+ | {"weight": 2000, "zone": "REMOTE", "express": false} | Executar quote(2000, 'REMOTE', False) | {"status": "OK", "fee": 12} | Nenhum | Alta |
| F-19 | EP | BR-04: Ponto interior da classe de indisponibilidade REMOTE express (weight=6000g) | Build T08-B1.0, Python 3.10+ | {"weight": 6000, "zone": "REMOTE", "express": true} | Executar quote(6000, 'REMOTE', True) | {"status": "UNAVAILABLE", "fee": null} | Nenhum | Alta |
| F-20 | EP | BR-01: Rejeição de tipo inteiro no parâmetro express (express=1 não é bool real) | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "LOCAL", "express": 1} | Executar quote(500, 'LOCAL', 1) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-21 | EP/BVA | BR-01, BR-04, BR-05: Precedência de validação (weight=25000 > 20000) sobre disponibilidade | Build T08-B1.0, Python 3.10+ | {"weight": 25000, "zone": "REMOTE", "express": true} | Executar quote(25000, 'REMOTE', True) | {"status": "INVALID", "fee": null} | Nenhum | Alta |
| F-22 | EP | BR-01: Robustez de tipo numérico — rejeição de float no peso (weight=500.5) | Build T08-B1.0, Python 3.10+ | {"weight": 500.5, "zone": "LOCAL", "express": false} | Executar quote(500.5, 'LOCAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-23 | EP | BR-01: Robustez de zona com espaços — rejeição de whitespace em zone (' LOCAL ') | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": " LOCAL ", "express": false} | Executar quote(500, ' LOCAL ', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-24 | EP | BR-02, BR-03: Combinação nominal de Tier 2 com serviço express LOCAL (8+6=14€) | Build T08-B1.0, Python 3.10+ | {"weight": 2000, "zone": "LOCAL", "express": true} | Executar quote(2000, 'LOCAL', True) | {"status": "OK", "fee": 14} | Nenhum | Média |
| F-25 | EP | BR-01: Rejeição de zona inválida fora do domínio permitido ('INTERNATIONAL') | Build T08-B1.0, Python 3.10+ | {"weight": 1000, "zone": "INTERNATIONAL", "express": false} | Executar quote(1000, 'INTERNATIONAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-26 | BVA | BR-01: Limite inferior negativo de peso (weight=-100) fora do intervalo | Build T08-B1.0, Python 3.10+ | {"weight": -100, "zone": "LOCAL", "express": false} | Executar quote(-100, 'LOCAL', False) | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-27 | EP | BR-01: Rejeição de express como string em vez de booleano real ('False') | Build T08-B1.0, Python 3.10+ | {"weight": 500, "zone": "LOCAL", "express": "False"} | Executar quote(500, 'LOCAL', 'False') | {"status": "INVALID", "fee": null} | Nenhum | Média |
| F-28 | EP | BR-02, BR-03: Ponto interior Tier 3 nominal para zona LOCAL sem express (12€) | Build T08-B1.0, Python 3.10+ | {"weight": 6000, "zone": "LOCAL", "express": false} | Executar quote(6000, 'LOCAL', False) | {"status": "OK", "fee": 12} | Nenhum | Média |
| F-29 | EP | BR-02, BR-03: Tier 3 para zona REMOTE sem express (12+4=16€) expondo DEF-03 | Build T08-B1.0, Python 3.10+ | {"weight": 6000, "zone": "REMOTE", "express": false} | Executar quote(6000, 'REMOTE', False) | {"status": "OK", "fee": 16} | Nenhum | Alta |
| F-30 | EP | BR-04: Limiar interior de indisponibilidade express REMOTE (weight=8000g) expondo DEF-04 | Build T08-B1.0, Python 3.10+ | {"weight": 8000, "zone": "REMOTE", "express": true} | Executar quote(8000, 'REMOTE', True) | {"status": "UNAVAILABLE", "fee": null} | Nenhum | Alta |

## Executions

| | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Executions — T08 | | | | | | | | | | |
| Manual verdict: compare ALL expected outcomes. Preserve prior runs; BLOCKED is not PASS. | | | | | | | | | | |
| | | | | | | | | | | |
| Run ID | Test ID | Requirement ID(s) | Date / environment | Expected outputs (independently derived) | Actual outputs | Verdict | Evidence | Defect IDs | Tester (Role: Exec / Sup / Val) | Actual side effects / Notes |
| RUN-ENV-01 | H-ENV | R01, R02, R06, R07 | 2026-10-27 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | app/human_cases.results.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Grupo 5) | Nenhum (função pura sem efeitos secundários) |
| RUN-H02-01 | H-01 | R02, R03 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-02 | H-02 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-03 | H-03 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 8} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-02 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (violou BR-02: 1000g cobrado como tier 2) |
| RUN-H02-04 | H-04 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-05 | H-05 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-06 | H-06 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 12} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-07 | H-07 | R01, R02 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "INVALID", "fee": null} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-01 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (violou BR-01: 20000g rejeitado como INVALID) |
| RUN-H02-08 | H-08 | R01 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-09 | H-09 | R01 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-10 | H-10 | R02, R03 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 9} | {"status": "OK", "fee": 4} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-03 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (violou BR-03: taxa base sobrescrita por fee=4) |
| RUN-H02-11 | H-11 | R02, R03 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 11} | {"status": "OK", "fee": 11} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-12 | H-12 | R02, R03 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 15} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-03 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (violou BR-03: taxa base sobrescrita por fee=4) |
| RUN-H02-13 | H-13 | R02, R03, R04 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 18} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-03 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (disponível a 5000g; violou estritamente DEF-03) |
| RUN-H02-14 | H-14 | R04 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP2/human_cases.results.json | DEF-04 | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum (violou BR-04: aceitou 5001g REMOTE express) |
| RUN-H02-15 | H-15 | R01 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-H02-16 | H-16 | R01 | 2026-10-30 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP2/human_cases.results.json | - | Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5) | Nenhum |
| RUN-AI-01 | AI-01 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-02 | AI-02 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-03 | AI-03 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 12} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-04 | AI-04 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 11} | {"status": "OK", "fee": 11} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-05 | AI-05 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 4} | {"status": "OK", "fee": 4} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | DATA-01 | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS (Nota: expectativa da IA incorreta omite base 5€, replicando bug DEF-03) |
| RUN-AI-06 | AI-06 | R02 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | DATA-02 | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS (Nota: expectativa da IA incorreta assume 8€ a 1000g, mascarando DEF-02) |
| RUN-AI-07 | AI-07 | R01 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-08 | AI-08 | R01 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-09 | AI-09 | R04 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 22} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/ai_candidates_execution.json | DATA-03 | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: FAIL (Nota: IA tentou tarifar 6000g REMOTE express que é UNAVAILABLE; revisto para F-19) |
| RUN-AI-10 | AI-10 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS |
| RUN-AI-11 | AI-11 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 18} | {"status": "OK", "fee": 18} | PASS | Trabalho_CP4/runs/ai_candidates_execution.json | - | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: PASS (Aceite para suite final como F-17) |
| RUN-AI-12 | AI-12 | R02, R03 | 2026-11-08 / macOS, Python 3.9.6, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 4} | FAIL | Trabalho_CP4/runs/ai_candidates_execution.json | DEF-03 | Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa) | Runner original: FAIL (Aceite com oráculo independente como F-18) |
| RUN-CP4-01 | H-01 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-02 | H-02 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 5} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-03 | H-03 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 8} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-02 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Violou BR-02: 1000g cobrado como Tier 2 |
| RUN-CP4-04 | H-04 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-05 | H-05 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 8} | {"status": "OK", "fee": 8} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-06 | H-06 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 12} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-07 | H-07 | R01, R02 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "INVALID", "fee": null} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-01 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Violou BR-01: limite 20000g rejeitado como INVALID |
| RUN-CP4-08 | H-08 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-09 | H-09 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-10 | H-10 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 9} | {"status": "OK", "fee": 4} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-03 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Violou BR-03: taxa base sobrescrita por fee=4 |
| RUN-CP4-11 | H-11 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 11} | {"status": "OK", "fee": 11} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-12 | H-12 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 15} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-03 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Violou BR-03: taxa base sobrescrita por fee=4 (+ express 6 = 10) |
| RUN-CP4-13 | H-13 | R02, R03, R04 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 18} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-03 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Disponível a 5000g; falha estritamente por DEF-03 |
| RUN-CP4-14 | H-14 | R04 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-04 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Violou BR-04: aceitou 5001g REMOTE express |
| RUN-CP4-15 | H-15 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-16 | H-16 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira) | Nenhum |
| RUN-CP4-17 | F-17 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 18} | {"status": "OK", "fee": 18} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum |
| RUN-CP4-18 | F-18 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 4} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-03 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Violou BR-03: taxa base sobrescrita por fee=4 |
| RUN-CP4-19 | F-19 | R04 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-04 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Violou BR-04: aceitou 6000g REMOTE express |
| RUN-CP4-20 | F-20 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum |
| RUN-CP4-21 | F-21 | R01, R04, R05 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum |
| RUN-CP4-22 | F-22 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (robustez peso float) |
| RUN-CP4-23 | F-23 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (robustez zona com espaços) |
| RUN-CP4-24 | F-24 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 14} | {"status": "OK", "fee": 14} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (combinação LOCAL express) |
| RUN-CP4-25 | F-25 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (zona inválida 'INTERNATIONAL') |
| RUN-CP4-26 | F-26 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (peso negativo -100) |
| RUN-CP4-27 | F-27 | R01 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "INVALID", "fee": null} | {"status": "INVALID", "fee": null} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (express como string) |
| RUN-CP4-28 | F-28 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 12} | {"status": "OK", "fee": 12} | PASS | Trabalho_CP4/runs/final_cases_execution.json | - | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Nenhum (Tier 3 nominal) |
| RUN-CP4-29 | F-29 | R02, R03 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "OK", "fee": 16} | {"status": "OK", "fee": 4} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-03 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Violou BR-03: taxa base sobrescrita por fee=4 |
| RUN-CP4-30 | F-30 | R04 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | FAIL | Trabalho_CP4/runs/final_cases_execution.json | DEF-04 | Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa) | Violou BR-04: aceitou 8000g REMOTE express |
| RUN-CTRL-01 | BR05-DET-01 | R05 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | Determinismo estrito em 100 chamadas idênticas | Determinismo estrito em 100 chamadas idênticas | PASS | Trabalho_CP4/evidence/br05_independence_cp4.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Nenhum (determinismo comprovado) |
| RUN-CTRL-02 | BR05-RES-02 | R05 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | Ausência de estado residual inter-chamadas | Ausência de estado residual inter-chamadas | PASS | Trabalho_CP4/evidence/br05_independence_cp4.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Nenhum (ordem não afeta saídas) |
| RUN-CTRL-03 | BR05-MUT-03 | R05 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | Imutabilidade de módulos e memória global | Imutabilidade de módulos e memória global | PASS | Trabalho_CP4/evidence/br05_independence_cp4.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Nenhum (memória inalterada) |
| RUN-CTRL-04 | BR05-EXT-04 | R05 | 2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0 | Isolamento de I/O, stdout/stderr, ambiente e filesystem | Isolamento de I/O, stdout/stderr, ambiente e filesystem | PASS | Trabalho_CP4/evidence/br05_independence_cp4.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Nenhum (sistema de ficheiros intocado) |
| RUN-ROB-01 | ROB-CLI-01 | R06, R07 | 2026-11-16 / macOS, Python 3.9.6, T08-B1.0 | Exit code 2 e mensagem de uso sem argumentos | Exit code 2 e mensagem de uso sem argumentos | PASS | Trabalho_CP4/evidence/runner_robustness_evidence.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Runner robusto sem argumentos |
| RUN-ROB-02 | ROB-CLI-02 | R06, R07 | 2026-11-16 / macOS, Python 3.9.6, T08-B1.0 | Exit code 2 e CASE FILE ERROR para ficheiro inexistente | Exit code 2 e CASE FILE ERROR para ficheiro inexistente | PASS | Trabalho_CP4/evidence/runner_robustness_evidence.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Runner robusto ficheiro inexistente |
| RUN-ROB-03 | ROB-CLI-03 | R06, R07 | 2026-11-16 / macOS, Python 3.9.6, T08-B1.0 | Exit code 2 e CASE FILE ERROR para JSON malformado | Exit code 2 e CASE FILE ERROR para JSON malformado | PASS | Trabalho_CP4/evidence/runner_robustness_evidence.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Runner robusto sintaxe JSON inválida |
| RUN-ROB-04 | ROB-CLI-04 | R06, R07 | 2026-11-16 / macOS, Python 3.9.6, T08-B1.0 | Exit code 2 e CASE FILE ERROR para case IDs duplicados | Exit code 2 e CASE FILE ERROR para case IDs duplicados | PASS | Trabalho_CP4/evidence/runner_robustness_evidence.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Runner robusto IDs duplicados |
| RUN-ROB-05 | ROB-CLI-05 | R06, R07 | 2026-11-16 / macOS, Python 3.9.6, T08-B1.0 | Exit code 2 e CASE FILE ERROR para raiz não-lista | Exit code 2 e CASE FILE ERROR para raiz não-lista | PASS | Trabalho_CP4/evidence/runner_robustness_evidence.json | - | Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5) | Runner robusto raiz JSON inválida |

## Defects

| | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Defects — T08 | | | | | | | | |
| One report per reproducible issue; distinguish source data issues, specification questions and software defects. | | | | | | | | |
| | | | | | | | | |
| Defect ID | Title / tests | Rule / build / environment | Exact reproduction | Expected | Actual | Evidence | Severity / rationale | Status |
| DEF-01 | Off-by-one limite superior de peso: weight=20000 tratado como INVALID (H-07) | BR-01 / Build T08-B1.0 / Python 3.12 & 3.9 | quote(20000, 'LOCAL', False) -> linha 3 usa 'weight >= 20000' | {"status": "OK", "fee": 12} | {"status": "INVALID", "fee": null} | final_cases_execution.json#H-07 | Alta / Rejeição indevida do limite máximo legal permitido em BR-01 | Open |
| DEF-02 | Off-by-one na transição entre Tier 1 e Tier 2: weight=1000 cobrado a 8€ (H-03) | BR-02 / Build T08-B1.0 / Python 3.12 & 3.9 | quote(1000, 'LOCAL', False) -> linha 7 usa 'weight < 1000' | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 8} | final_cases_execution.json#H-03 | Média-Alta / Cobrança excessiva de tarifa de escalão superior em fronteira válida | Open |
| DEF-03 | Sobrescrita destrutiva da taxa base no processamento da zona REMOTE (H-10, H-12, H-13, F-18, F-29) | BR-03 / Build T08-B1.0 / Python 3.12 & 3.9 | quote(500, 'REMOTE', False) -> linha 14 usa 'fee = 4' em vez de 'fee += 4' | {"status": "OK", "fee": 9} | {"status": "OK", "fee": 4} | final_cases_execution.json#H-10,#H-12,#H-13,#F-18,#F-29 | Crítica / Perda de receita e subfaturação sistemática de expedições para zona REMOTE | Open |
| DEF-04 | Limiar incorreto de indisponibilidade de express para REMOTE: 10000g em vez de 5000g (H-14, F-19, F-30) | BR-04 / Build T08-B1.0 / Python 3.12 & 3.9 | quote(5001, 'REMOTE', True) -> linha 5 usa 'weight > 10000' | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | final_cases_execution.json#H-14,#F-19,#F-30 | Alta / Aceitação de encomendas express remotas em pesos não suportados operacionalmente | Open |
| DATA-01 | Expectativa incorreta gerada por IA no candidato AI-05 (omite taxa base, replica DEF-03) | BR-03 / ai_candidates.json#AI-05 | Runner executa AI-05 com expected fee=4 em vez de 9 -> gera falso PASS no runner original | {"status": "OK", "fee": 9} | {"status": "OK", "fee": 4} | ai_candidates_execution.json#AI-05 | Média / Falha de oráculo da IA (rejeitado na revisão humana independente) | Rejected (AI Data) |
| DATA-02 | Expectativa incorreta gerada por IA no candidato AI-06 (off-by-one em 1000g, replica DEF-02) | BR-02 / ai_candidates.json#AI-06 | Runner executa AI-06 com expected fee=8 em vez de 5 -> gera falso PASS no runner original | {"status": "OK", "fee": 5} | {"status": "OK", "fee": 8} | ai_candidates_execution.json#AI-06 | Média / Falha de oráculo da IA (rejeitado na revisão humana independente) | Rejected (AI Data) |
| DATA-03 | Tentativa de tarifação de serviço indisponível gerada por IA no candidato AI-09 (revisto para F-19) | BR-04 / ai_candidates.json#AI-09 | Runner executa AI-09 com expected fee=22 em vez de UNAVAILABLE -> falha no runner | {"status": "UNAVAILABLE", "fee": null} | {"status": "OK", "fee": 10} | ai_candidates_execution.json#AI-09 | Alta / Erro conceitual de oráculo da IA (revisto para oráculo correto na suite final) | Revised to F-19 |

## Static Review

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Static Review — T08 |  |  |  |  |  |
| Record supported observations. If no ambiguity is found, explain testability. |  |  |  |  |  |
|  |  |  |  |  |  |
| Review ID | Rule | Observation / question | Impact / rationale | Suggested clarification | Outcome / owner |
| REV-01 | BR-01 | Em Python bool é subclasse de int (True==1). O requisito 'excluindo booleans' deve rejeitar explicitamente por tipo? | Risco de True/False serem processados como inteiros numéricos 1g e 0g sem validação de tipo. | Validar expressamente com \`type(w) is int\` ou \`not isinstance(w, bool)`. | Confirmado; implementação usa \`type(weight) is not int`. Caso H-15 passa. / Eduardo Dias |
| REV-02 | BR-01 | BR-01 exige 'actual boolean' para express. Inteiros 1 e 0 ou strings devem ser rejeitados sem coerção? | Risco de coerção implícita de tipos aceitar inputs não conformes com a especificação. | Rejeitar qualquer valor que não seja do tipo bool (\`type(express) is bool`). | Confirmado; implementação valida tipo estrito. Caso F-20 passa. / Rui Carneiro |
| REV-03 | BR-04 | Limiar de indisponibilidade 'above 5000g' com express REMOTE: o valor 5000g é inclusivo ou exclusivo? | Risco de off-by-one na disponibilidade do serviço expresso. | A regra explicita 'At exactly 5000 it is available'. Logo indisponível apenas para peso > 5000g. | Confirmado; revelou DEF-04 na implementação (que usava erroneamente > 10000). / Érica Moreira |
| REV-04 | BR-05 | Precedência de validação sobre disponibilidade: input inválido (>20000g) com REMOTE express deve ser INVALID ou UNAVAILABLE? | Risco de inversão de prioridade entre validação e disponibilidade. | Validação ocorre primeiro: se peso > 20000, deve retornar INVALID e null imediatamente. | Confirmado; coberto por F-21 (retorna INVALID com sucesso). / Beatriz Barbosa |

## Coverage

| | | | | |
| --- | --- | --- | --- | --- |
| Requirement coverage — T08 | | | | |
| Unique valid test links; executed = at least one PASS or FAIL. This is not technique coverage. | | | | |
| | | | | |
| Requirement | Business rule | Designed | Executed | Not executed |
| R01 | BR-01 | 15 | 15 | 0 |
| R02 | BR-02 | 17 | 17 | 0 |
| R03 | BR-03 | 10 | 10 | 0 |
| R04 | BR-04 | 5 | 5 | 0 |
| R05 | BR-05 | 2 | 2 | 0 |
| R06 | BR-06 | 7 | 7 | 0 |
| R07 | BR-07 | 5 | 5 | 0 |
| R08 | BR-08 | 4 | 4 | 0 |
| | | | | |
| | | | | |
| Amber = editable. White = formula. Add one requirement–test pair per row below. | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| Requirement ID | Test ID | Valid unique link | Executed (0/1) | Link check |
| R01 | H-ENV | 1 | 1 | Linked |
| R01 | H-02 | 1 | 1 | Linked |
| R01 | H-03 | 1 | 1 | Linked |
| R01 | H-07 | 1 | 1 | Linked |
| R01 | H-08 | 1 | 1 | Linked |
| R01 | H-09 | 1 | 1 | Linked |
| R01 | H-15 | 1 | 1 | Linked |
| R01 | H-16 | 1 | 1 | Linked |
| R01 | F-20 | 1 | 1 | Linked |
| R01 | F-21 | 1 | 1 | Linked |
| R01 | F-22 | 1 | 1 | Linked |
| R01 | F-23 | 1 | 1 | Linked |
| R01 | F-25 | 1 | 1 | Linked |
| R01 | F-26 | 1 | 1 | Linked |
| R01 | F-27 | 1 | 1 | Linked |
| R02 | H-ENV | 1 | 1 | Linked |
| R02 | H-01 | 1 | 1 | Linked |
| R02 | H-02 | 1 | 1 | Linked |
| R02 | H-03 | 1 | 1 | Linked |
| R02 | H-04 | 1 | 1 | Linked |
| R02 | H-05 | 1 | 1 | Linked |
| R02 | H-06 | 1 | 1 | Linked |
| R02 | H-07 | 1 | 1 | Linked |
| R02 | H-10 | 1 | 1 | Linked |
| R02 | H-11 | 1 | 1 | Linked |
| R02 | H-12 | 1 | 1 | Linked |
| R02 | H-13 | 1 | 1 | Linked |
| R02 | F-17 | 1 | 1 | Linked |
| R02 | F-18 | 1 | 1 | Linked |
| R02 | F-24 | 1 | 1 | Linked |
| R02 | F-28 | 1 | 1 | Linked |
| R02 | F-29 | 1 | 1 | Linked |
| R03 | H-01 | 1 | 1 | Linked |
| R03 | H-10 | 1 | 1 | Linked |
| R03 | H-11 | 1 | 1 | Linked |
| R03 | H-12 | 1 | 1 | Linked |
| R03 | H-13 | 1 | 1 | Linked |
| R03 | F-17 | 1 | 1 | Linked |
| R03 | F-18 | 1 | 1 | Linked |
| R03 | F-24 | 1 | 1 | Linked |
| R03 | F-28 | 1 | 1 | Linked |
| R03 | F-29 | 1 | 1 | Linked |
| R04 | H-13 | 1 | 1 | Linked |
| R04 | H-14 | 1 | 1 | Linked |
| R04 | F-19 | 1 | 1 | Linked |
| R04 | F-21 | 1 | 1 | Linked |
| R04 | F-30 | 1 | 1 | Linked |
| R05 | F-21 | 1 | 1 | Linked |
| R05 | H-ENV | 1 | 1 | Linked |
| R06 | H-ENV | 1 | 1 | Linked |
| R06 | H-01 | 1 | 1 | Linked |
| R06 | H-07 | 1 | 1 | Linked |
| R06 | H-14 | 1 | 1 | Linked |
| R06 | F-17 | 1 | 1 | Linked |
| R06 | F-21 | 1 | 1 | Linked |
| R06 | F-30 | 1 | 1 | Linked |
| R07 | H-ENV | 1 | 1 | Linked |
| R07 | H-01 | 1 | 1 | Linked |
| R07 | H-03 | 1 | 1 | Linked |
| R07 | F-18 | 1 | 1 | Linked |
| R07 | F-21 | 1 | 1 | Linked |
| R08 | H-01 | 1 | 1 | Linked |
| R08 | F-17 | 1 | 1 | Linked |
| R08 | F-18 | 1 | 1 | Linked |
| R08 | F-19 | 1 | 1 | Linked |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |
| | | 0 | 0 | |

## Technique

| | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Technique — T08 | | | | | | | |
| Critical comparison of human and AI test designs — See assignment for required topic-specific analysis. | | | | | | | |
| | | | | | | | |
| Candidate ID / origin | Rule / boundary | Original expectation | Independent oracle | Accept / revise / reject | Reason / duplicate | Final test IDs | Comparison evidence |
| AI-01 | BR-02 (Tier 1 base fee) | OK, fee=5 | OK, fee=5 | Reject | Duplicado exato de H-01; sem cobertura nova | H-01 | ai_candidates.json#AI-01 vs human_cases.json#H-01 |
| AI-02 | BR-02 (Tier 2 interior) | OK, fee=8 | OK, fee=8 | Reject | Ponto interior redundante com H-04 (1001) e H-05 (5000) | - | ai_candidates.json#AI-02 |
| AI-03 | BR-02 (Tier 3 interior) | OK, fee=12 | OK, fee=12 | Reject | Ponto interior redundante com H-06 (5001) e H-07 (20000) | - | ai_candidates.json#AI-03 |
| AI-04 | BR-03 (Express LOCAL) | OK, fee=11 | OK, fee=11 | Reject | Duplicado exato de H-11; sem valor adicional | H-11 | ai_candidates.json#AI-04 vs human_cases.json#H-11 |
| AI-05 | BR-03 (REMOTE suplemento) | OK, fee=4 | OK, fee=9 | Reject | Expected errado: omitiu fee base (5+4=9); duplica inputs de H-10 | H-10 | ai_candidates.json#AI-05 reproduz defeito DEF-03 |
| AI-06 | BR-02 (Fronteira sup. Tier 1) | OK, fee=8 | OK, fee=5 | Reject | Expected errado: confundiu tier 1 com tier 2 a 1000g; duplica H-03 | H-03 | ai_candidates.json#AI-06 reproduz defeito DEF-02 |
| AI-07 | BR-01 (Peso zero inválido) | INVALID, fee=null | INVALID, fee=null | Reject | Duplicado exato de H-08 | H-08 | ai_candidates.json#AI-07 vs human_cases.json#H-08 |
| AI-08 | BR-01 (Peso acima max) | INVALID, fee=null | INVALID, fee=null | Reject | Duplicado exato de H-09 | H-09 | ai_candidates.json#AI-08 vs human_cases.json#H-09 |
| AI-09 | BR-04 (REMOTE express indisponível) | OK, fee=22 | UNAVAILABLE, fee=null | Revise | Expected errado (ignorou BR-04); corrigido para UNAVAILABLE/null; adiciona ponto interior | F-19 | ai_candidates.json#AI-09 reproduz defeito DEF-04 |
| AI-10 | BR-02 (Tier 1 base) | OK, fee=5 | OK, fee=5 | Reject | Triplicado de H-01 e AI-01 | H-01 | ai_candidates.json#AI-10 |
| AI-11 | BR-02, BR-03 (Tier 3 LOCAL express) | OK, fee=18 | OK, fee=18 | Accept | Cobre lacuna da suite humana: Tier 3 com express para LOCAL (12+6=18) | F-17 | ai_candidates.json#AI-11 integrado como F-17 |
| AI-12 | BR-02, BR-03 (Tier 2 REMOTE padrão) | OK, fee=12 | OK, fee=12 | Accept | Cobre lacuna da suite humana: Tier 2 para REMOTE sem express (8+4=12) | F-18 | ai_candidates.json#AI-12 integrado como F-18 |
