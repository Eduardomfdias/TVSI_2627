# CP02 — Revisão Estática, Modelo e Oráculo Inicial

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27 — T08 — Grupo 5**  
**Build:** T08-B1.0 · **Data de realização:** 2026-10-28 (Data prevista de checkpoint: 2026-11-03)  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa

---

## 1. Revisão Estática — BR-01 a BR-08

| ID | Requisito | Testável? | Técnica |
| --- | --- | --- | --- |
| BR-01/R01 | Validação de inputs: weight inteiro 1–20000 (sem booleans), zone exatamente LOCAL ou REMOTE, express boolean real; inválidos → INVALID/null | Sim | EP + BVA |
| BR-02/R02 | Base fee: 1–1000g→5€, 1001–5000g→8€, 5001–20000g→12€ | Sim | EP + BVA |
| BR-03/R03 | REMOTE +4€; express +6€ após remote; sem arredondamento | Sim | EP |
| BR-04/R04 | REMOTE+express indisponível acima de 5000g → UNAVAILABLE/null; a 5000g exato é disponível; LOCAL+express sempre disponível | Sim | BVA |
| BR-05/R05 | Precedência: validação > disponibilidade > cálculo; sem efeitos laterais; chamadas independentes | Sim | EP |
| BR-06/R06 | Formato JSON; runner `python run_cases.py`; Python 3.10+ | Parcialmente (ambiental) | — |
| BR-07/R07 | Runner compara exatamente; exit codes 0/1/2; preservar reports anteriores | Sim (execução) | — |
| BR-08/R08 | Expectations derivadas independentemente das BRs; classificar candidatos AI; comparar suites | Processual | — |

---

## 2. Ambiguidades e Clarificações Propostas

| ID | Ambiguidade | Clarificação proposta |
| --- | --- | --- |
| AMB-01 | BR-01 exclui booleans como weight, mas em Python `True` e `False` são subclasses de `int` (valor 1 e 0). A exclusão é por tipo ou por valor? | Por tipo: `isinstance(w, bool)` → INVALID, independentemente do valor numérico. Um peso de 1 passado como `int` é válido; passado como `True` é inválido. |
| AMB-02 | BR-01 exige "actual boolean" para express. Os valores `1` e `0` (inteiros) são aceites? | Não: a mesma lógica de tipo aplica-se — `isinstance(e, bool)` com exclusão de int → só `True`/`False` são válidos. |
| AMB-03 | BR-04 diz "above 5000 g". O limiar é exclusivo (>5000) ou inclusivo (≥5000)? A BR refere "At exactly 5000 it is available". | Exclusivo: weight>5000 com REMOTE+express → UNAVAILABLE; weight=5000 com REMOTE+express → OK, fee=18. |
| AMB-04 | BR-01 não especifica o comportamento para weight=None ou weight=string. Cai em INVALID? | Sim: qualquer valor que não seja `int` (excluindo bool) → INVALID/null. |

---

## 3. Condições de Teste Iniciais

### Partições de weight (BR-01 + BR-02)

| ID | Intervalo / Valor | Classe | Expected status |
| --- | --- | --- | --- |
| EP-W1 | weight ≤ 0 | Inválido (fora de intervalo) | INVALID |
| EP-W2 | weight 1–1000 | Válido, base 5€ | OK |
| EP-W3 | weight 1001–5000 | Válido, base 8€ | OK |
| EP-W4 | weight 5001–20000 | Válido, base 12€ | OK |
| EP-W5 | weight > 20000 | Inválido (fora de intervalo) | INVALID |
| EP-W6 | weight float (ex: 500.5) | Inválido (tipo errado) | INVALID |
| EP-W7 | weight bool (True/False) | Inválido (tipo errado) | INVALID |
| EP-W8 | weight None ou string | Inválido (tipo errado) | INVALID |

### Valores de fronteira de weight (BVA)

| Valor | Expected status | Fee base |
| --- | --- | --- |
| 0 | INVALID | null |
| 1 | OK | 5 |
| 1000 | OK | 5 |
| 1001 | OK | 8 |
| 5000 | OK | 8 |
| 5001 | OK | 12 |
| 20000 | OK | 12 |
| 20001 | INVALID | null |

### Partições de zone (BR-01)

| Valor | Classe |
| --- | --- |
| "LOCAL" | Válido |
| "REMOTE" | Válido |
| "local" / "Local" | Inválido (case-sensitive) |
| None, int, outro string | Inválido |

### Partições de express (BR-01)

| Valor | Classe |
| --- | --- |
| True | Válido |
| False | Válido |
| 1, 0 (int) | Inválido |
| None, string | Inválido |

### Partições de disponibilidade (BR-04)

| Condição | Expected |
| --- | --- |
| REMOTE + express=True + weight ≤ 5000 | OK (disponível) |
| REMOTE + express=True + weight 5001–20000 | UNAVAILABLE |
| LOCAL + express=True + qualquer weight válido | OK (sempre disponível) |

---

## 4. Oráculo Independente

Os expected results são derivados exclusivamente de BR-01–BR-05. A implementação (`shipping.py`) **não é usada como oráculo** — qualquer divergência entre o resultado do runner e os valores calculados pelas BRs é tratada como defeito da implementação.

**Algoritmo de derivação:**

1. Verificar tipos e intervalos (BR-01)
   - weight não é int, ou é bool, ou está fora de [1, 20000] → **INVALID, null** (stop)
   - zone não é exatamente "LOCAL" ou "REMOTE" → **INVALID, null** (stop)
   - express não é bool (ou é int) → **INVALID, null** (stop)

2. Verificar disponibilidade (BR-04)
   - zone == "REMOTE" AND express == True AND weight > 5000 → **UNAVAILABLE, null** (stop)

3. Calcular fee (BR-02 + BR-03)
   - base: weight 1–1000 → 5; weight 1001–5000 → 8; weight 5001–20000 → 12
   - se zone == "REMOTE": base += 4
   - se express == True: base += 6
   - → **OK, fee** (inteiro, sem arredondamento)

---

## 5. Plano de Teste Humano Independente

**Técnicas:** Equivalence Partitioning (EP) + Boundary Value Analysis (BVA)  
**Estado:** FROZEN — este plano é fechado antes de abrir `ai_candidates.json`

| TC-ID | weight | zone | express | Expected status | Expected fee | Cobertura |
| --- | --- | --- | --- | --- | --- | --- |
| H-01 | 500 | LOCAL | False | OK | 5 | EP-W2, ambiente check |
| H-02 | 1 | LOCAL | False | OK | 5 | BVA W=1 (mínimo) |
| H-03 | 1000 | LOCAL | False | OK | 5 | BVA W=1000 (fronteira sup. tier 1) |
| H-04 | 1001 | LOCAL | False | OK | 8 | BVA W=1001 (fronteira inf. tier 2) |
| H-05 | 5000 | LOCAL | False | OK | 8 | BVA W=5000 (fronteira sup. tier 2) |
| H-06 | 5001 | LOCAL | False | OK | 12 | BVA W=5001 (fronteira inf. tier 3) |
| H-07 | 20000 | LOCAL | False | OK | 12 | BVA W=20000 (máximo válido) |
| H-08 | 0 | LOCAL | False | INVALID | null | BVA W=0 (abaixo do mínimo) |
| H-09 | 20001 | LOCAL | False | INVALID | null | BVA W=20001 (acima do máximo) |
| H-10 | 500 | REMOTE | False | OK | 9 | EP REMOTE sem express; BR-03 |
| H-11 | 500 | LOCAL | True | OK | 11 | EP express LOCAL; BR-03 |
| H-12 | 500 | REMOTE | True | OK | 15 | EP REMOTE+express; BR-03 |
| H-13 | 5000 | REMOTE | True | OK | 18 | BVA disponibilidade limite (incluído) |
| H-14 | 5001 | REMOTE | True | UNAVAILABLE | null | BVA disponibilidade limite+1 (excluído) |
| H-15 | True | LOCAL | False | INVALID | null | BR-01 bool como weight |
| H-16 | 500 | "local" | False | INVALID | null | BR-01 zone case-sensitive |

**Cálculos dos expected fees (derivados das BRs):**

| TC-ID | Base | +REMOTE | +express | Total |
| --- | --- | --- | --- | --- |
| H-01 | 5 | — | — | 5 |
| H-02 | 5 | — | — | 5 |
| H-03 | 5 | — | — | 5 |
| H-04 | 8 | — | — | 8 |
| H-05 | 8 | — | — | 8 |
| H-06 | 12 | — | — | 12 |
| H-07 | 12 | — | — | 12 |
| H-10 | 5 | +4 | — | 9 |
| H-11 | 5 | — | +6 | 11 |
| H-12 | 5 | +4 | +6 | 15 |
| H-13 | 8 | +4 | +6 | 18 |

---

## 6. Riscos e Prioridades

| ID | Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- | --- |
| R1 | Limiar de disponibilidade REMOTE+express implementado como ≥5000 em vez de >5000 | Alta | Alto | H-13 e H-14 cobrem o limite exacto |
| R2 | Booleans como weight não rejeitados por tipo (aceites como int 1/0) | Média | Médio | H-15 testa explicitamente |
| R3 | Cálculo REMOTE+express com ordem errada (ex: express antes de base) | Baixa | Baixo | Irrelevante (soma comutativa), mas H-12/H-13 verificam o total |
| R4 | Python 3.9.6 instalado (abaixo do mínimo 3.10+) | Confirmado | Médio | Documentado como risco; resolver antes de CP03 |
| R5 | Candidatos AI com expected values derivados da implementação e não das BRs | Alta (by design) | Alto | Oracle independente fixado antes de abrir ai_candidates.json |

**Prioridade de execução:** H-13, H-14 (disponibilidade), H-15 (tipo bool), H-08/H-09 (fronteiras inválidas), restantes.

---

## 7. Registo de Trabalho

**Concluído (CP02):**

- Eduardo Dias: revisão estática BR-01–BR-08, identificação de ambiguidades, definição de partições e fronteiras, derivação do oráculo, plano de 16 casos humanos frozen em `human_cases.json`
- Rui Carneiro: revisão dos casos humanos e verificação dos cálculos de fee
- Érica Moreira: pendente (execução e revisão AI — CP03)
- Beatriz Barbosa: pendente (análise de cobertura — CP03)

**Por resolver:**

- Resolução metodológica de AMB-01/AMB-02: na ausência de esclarecimento formal do professor, adotada a interpretação estrita de tipo (BR-01/BR-05), validada no CP03 via F-20 e F-21
- Upgrade Python 3.9.6 → 3.10+ antes de CP03 (10 nov)

**Próximas ações (CP03 — 10 nov):**

1. Resolver ambiente Python (upgrade ou máquina de laboratório)
2. Executar `human_cases.json` com o runner; registar resultados e evidências
3. Abrir `ai_candidates.json` (apenas após freeze confirmado do human)
4. Classificar cada candidato AI: accept / revise / reject com justificação contra as BRs

---

## 8. Execução dos Casos Humanos — Resultados

**Comando:** `python3 run_cases.py /Trabalho_CP2/human_cases.json`  
**Build:** T08-B1.0 · **Python:** 3.9.6 · **Exit code:** 1 (há FAILs)  
**Resultados:** 10 PASS / 6 FAIL de 16 casos

| TC-ID | Expected status | Expected fee | Actual status | Actual fee | Veredicto |
| --- | --- | --- | --- | --- | --- |
| H-01 | OK | 5 | OK | 5 | **PASS** |
| H-02 | OK | 5 | OK | 5 | **PASS** |
| H-03 | OK | 5 | OK | 8 | **FAIL** |
| H-04 | OK | 8 | OK | 8 | **PASS** |
| H-05 | OK | 8 | OK | 8 | **PASS** |
| H-06 | OK | 12 | OK | 12 | **PASS** |
| H-07 | OK | 12 | INVALID | null | **FAIL** |
| H-08 | INVALID | null | INVALID | null | **PASS** |
| H-09 | INVALID | null | INVALID | null | **PASS** |
| H-10 | OK | 9 | OK | 4 | **FAIL** |
| H-11 | OK | 11 | OK | 11 | **PASS** |
| H-12 | OK | 15 | OK | 10 | **FAIL** |
| H-13 | OK | 18 | OK | 10 | **FAIL** |
| H-14 | UNAVAILABLE | null | OK | 10 | **FAIL** |
| H-15 | INVALID | null | INVALID | null | **PASS** |
| H-16 | INVALID | null | INVALID | null | **PASS** |

---

## 9. Defeitos Encontrados em shipping.py (T08-B1.0)

O oráculo independente (secção 4) foi aplicado a cada FAIL para identificar a causa na implementação. Foram encontrados **4 defeitos distintos**.

### DEF-01 — Fronteira superior de weight usa `>=` em vez de `>`

**TC afetado:** H-07  
**BR violada:** BR-01 (weight válido até 20000 inclusive)  
**Código atual:** `weight >= 20000` → rejeita weight=20000 como INVALID  
**Código correto:** `weight > 20000`  
**Impacto:** weight=20000 deveria retornar `{"status":"OK","fee":12}`; retorna `{"status":"INVALID","fee":null}`

### DEF-02 — Fronteira do tier 1 usa `<` em vez de `<=`

**TC afetado:** H-03  
**BR violada:** BR-02 (1–1000 g → 5 €)  
**Código atual:** `if weight < 1000: fee = 5` → weight=1000 cai no tier 2  
**Código correto:** `if weight <= 1000: fee = 5`  
**Impacto:** weight=1000 retorna fee=8 em vez de fee=5

### DEF-03 — Surcharge REMOTE usa atribuição `=` em vez de incremento `+=`

**TC afetado:** H-10, H-12, H-13  
**BR violada:** BR-03 (REMOTE +4 € sobre base fee)  
**Código atual:** `if zone == "REMOTE": fee = 4` → sobrescreve a base fee  
**Código correto:** `if zone == "REMOTE": fee += 4`  
**Impacto:**  
- H-10: base 5 → fee=4 (devia ser 9)  
- H-12: base 5 → fee=4, +6=10 (devia ser 15)  
- H-13: base 8 → fee=4, +6=10 (devia ser 18)

### DEF-04 — Limiar UNAVAILABLE usa `> 10000` em vez de `> 5000`

**TC afetado:** H-14  
**BR violada:** BR-04 (REMOTE+express indisponível acima de 5000 g)  
**Código atual:** `if zone == "REMOTE" and express and weight > 10000:` → threshold errado  
**Código correto:** `if zone == "REMOTE" and express and weight > 5000:`  
**Impacto:** weight=5001 com REMOTE+express retorna OK/10 em vez de UNAVAILABLE/null

### Resumo dos defeitos

| ID | Linha em shipping.py | BR violada | TCs que detetam |
| --- | --- | --- | --- |
| DEF-01 | `weight >= 20000` | BR-01 | H-07 |
| DEF-02 | `if weight < 1000` | BR-02 | H-03 |
| DEF-03 | `fee = 4` | BR-03 | H-10, H-12, H-13 |
| DEF-04 | `weight > 10000` | BR-04 | H-14 |

**Nota:** H-13 é afetado por DEF-03 e DEF-04 em simultâneo (fee errada e threshold de disponibilidade errado). O veredicto FAIL é o mesmo independentemente da ordem de correção.
