# Relatório CP02 — Revisão Estática, Modelo e Oráculo Inicial

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27 — T08 — Grupo 5**  
**Build:** T08-B1.0 · **Data de realização:** 2026-10-28 (Data prevista de checkpoint: 2026-11-03)  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa

---

## 1. Revisão Estática dos Requisitos (BR-01 a BR-08)

| ID | Requisito | Testável? | Técnica |
|---|---|---|---|
| BR-01/R01 | Validação de inputs: `weight` inteiro 1–20000 (sem booleans), `zone` exatamente `LOCAL` ou `REMOTE`, `express` boolean real; inválidos → `INVALID`/`null` | Sim | EP + BVA |
| BR-02/R02 | Base fee: 1–1000 g → 5 €; 1001–5000 g → 8 €; 5001–20000 g → 12 € | Sim | EP + BVA |
| BR-03/R03 | REMOTE +4 €; express +6 € após remote; sem arredondamento | Sim | EP |
| BR-04/R04 | REMOTE + express indisponível acima de 5000 g → `UNAVAILABLE`/`null`; a 5000 g exato é disponível; LOCAL + express sempre disponível | Sim | BVA |
| BR-05/R05 | Precedência: validação > disponibilidade > cálculo; sem efeitos laterais; chamadas independentes | Sim | EP |
| BR-06/R06 | Formato JSON; runner `python run_cases.py`; Python 3.10+ | Parcialmente (ambiental) | — |
| BR-07/R07 | Runner compara exatamente; exit codes 0/1/2; preservar reports anteriores | Sim (execução) | — |
| BR-08/R08 | Expectations derivadas independentemente das BRs; classificar candidatos AI; comparar suites | Processual | — |

---

## 2. Ambiguidades Identificadas e Clarificações

| ID | Ambiguidade | Clarificação proposta |
|---|---|---|
| AMB-01 | BR-01 exclui booleans como `weight`, mas em Python `True`/`False` são subclasses de `int`. A exclusão é por tipo ou por valor? | Por tipo: `isinstance(w, bool)` → `INVALID`, independentemente do valor numérico. |
| AMB-02 | BR-01 exige "actual boolean" para `express`. Os valores `1` e `0` (inteiros) são aceites? | Não: a mesma lógica de tipo aplica-se — só `True`/`False` são válidos. |
| AMB-03 | BR-04 diz "above 5000 g". O limiar é exclusivo (>5000) ou inclusivo (≥5000)? | Exclusivo: `weight > 5000` com `REMOTE + express` → `UNAVAILABLE`; `weight = 5000` → disponível, fee = 18 €. |
| AMB-04 | BR-01 não especifica o comportamento para `weight = None` ou `weight = string`. | Sim: qualquer valor que não seja `int` (excluindo `bool`) → `INVALID`/`null`. |

> **Nota (Estado histórico no CP02):** AMB-01 e AMB-02 aguardam clarificação do professor antes de CP03.
> *(Ver nota de atualização pós-CP03 na Secção 10 sobre a decisão metodológica autónoma adotada pelo grupo).*

---

## 3. Oráculo Independente

Os expected results são derivados exclusivamente das BRs. O ficheiro `shipping.py` **não é usado como oráculo** — qualquer divergência é tratada como defeito da implementação.

**Algoritmo de derivação:**

1. **Validação de inputs (BR-01)**
   - `weight` não é `int`, ou é `bool`, ou está fora de [1, 20000] → **INVALID, null**
   - `zone` não é exatamente `"LOCAL"` ou `"REMOTE"` → **INVALID, null**
   - `express` não é `bool` → **INVALID, null**

2. **Verificação de disponibilidade (BR-04)**
   - `zone == "REMOTE"` AND `express == True` AND `weight > 5000` → **UNAVAILABLE, null**

3. **Cálculo da fee (BR-02 + BR-03)**
   - base: `weight` 1–1000 → 5 €; 1001–5000 → 8 €; 5001–20000 → 12 €
   - se `zone == "REMOTE"`: base += 4 €
   - se `express == True`: base += 6 €
   - resultado → **OK, fee**

---

## 4. Plano de Teste Humano (FROZEN)

**Técnicas aplicadas:** Equivalence Partitioning (EP) + Boundary Value Analysis (BVA)

| TC-ID | weight | zone | express | Expected status | Expected fee | Cobertura |
|---|---|---|---|---|---|---|
| H-01 | 500 | LOCAL | False | OK | 5 | EP-W2 |
| H-02 | 1 | LOCAL | False | OK | 5 | BVA mínimo |
| H-03 | 1000 | LOCAL | False | OK | 5 | BVA fronteira sup. tier 1 |
| H-04 | 1001 | LOCAL | False | OK | 8 | BVA fronteira inf. tier 2 |
| H-05 | 5000 | LOCAL | False | OK | 8 | BVA fronteira sup. tier 2 |
| H-06 | 5001 | LOCAL | False | OK | 12 | BVA fronteira inf. tier 3 |
| H-07 | 20000 | LOCAL | False | OK | 12 | BVA máximo válido |
| H-08 | 0 | LOCAL | False | INVALID | null | BVA abaixo do mínimo |
| H-09 | 20001 | LOCAL | False | INVALID | null | BVA acima do máximo |
| H-10 | 500 | REMOTE | False | OK | 9 | EP REMOTE sem express |
| H-11 | 500 | LOCAL | True | OK | 11 | EP express LOCAL |
| H-12 | 500 | REMOTE | True | OK | 15 | EP REMOTE + express |
| H-13 | 5000 | REMOTE | True | OK | 18 | BVA disponibilidade limite (incluído) |
| H-14 | 5001 | REMOTE | True | UNAVAILABLE | null | BVA disponibilidade limite+1 |
| H-15 | True (bool) | LOCAL | False | INVALID | null | BR-01 bool como weight |
| H-16 | 500 | "local" | False | INVALID | null | BR-01 zone case-sensitive |

**Verificação dos cálculos de fee:**

| TC-ID | Base fee | + REMOTE (+4) | + express (+6) | Total |
|---|---|---|---|---|
| H-01 | 5 | — | — | **5** |
| H-02 | 5 | — | — | **5** |
| H-03 | 5 | — | — | **5** |
| H-04 | 8 | — | — | **8** |
| H-05 | 8 | — | — | **8** |
| H-06 | 12 | — | — | **12** |
| H-07 | 12 | — | — | **12** |
| H-10 | 5 | +4 | — | **9** |
| H-11 | 5 | — | +6 | **11** |
| H-12 | 5 | +4 | +6 | **15** |
| H-13 | 8 | +4 | +6 | **18** |

---

## 5. Resultados da Execução

**Comando executado:**
```
python3 run_cases.py human_cases.json
```

**Build:** T08-B1.0 · **Python:** 3.9.6 · **Exit code:** 1 (há FAILs)

### Sumário

| Métrica | Valor |
|---|---|
| Total de casos | 16 |
| PASS | 10 |
| FAIL | 6 |
| Taxa de sucesso | 62,5 % |

### Resultados detalhados

| TC-ID | Expected status | Expected fee | Actual status | Actual fee | Veredicto |
|---|---|---|---|---|---|
| H-01 | OK | 5 | OK | 5 | ✅ PASS |
| H-02 | OK | 5 | OK | 5 | ✅ PASS |
| H-03 | OK | 5 | OK | **8** | ❌ FAIL |
| H-04 | OK | 8 | OK | 8 | ✅ PASS |
| H-05 | OK | 8 | OK | 8 | ✅ PASS |
| H-06 | OK | 12 | OK | 12 | ✅ PASS |
| H-07 | OK | 12 | **INVALID** | **null** | ❌ FAIL |
| H-08 | INVALID | null | INVALID | null | ✅ PASS |
| H-09 | INVALID | null | INVALID | null | ✅ PASS |
| H-10 | OK | 9 | OK | **4** | ❌ FAIL |
| H-11 | OK | 11 | OK | 11 | ✅ PASS |
| H-12 | OK | 15 | OK | **10** | ❌ FAIL |
| H-13 | OK | 18 | OK | **10** | ❌ FAIL |
| H-14 | UNAVAILABLE | null | **OK** | **10** | ❌ FAIL |
| H-15 | INVALID | null | INVALID | null | ✅ PASS |
| H-16 | INVALID | null | INVALID | null | ✅ PASS |

---

## 6. Defeitos Encontrados em `shipping.py` (T08-B1.0)

Foram identificados **4 defeitos distintos** comparando os resultados da execução com o oráculo independente.

### DEF-01 — Fronteira superior de `weight` usa `>=` em vez de `>`

| Campo | Detalhe |
|---|---|
| **BR violada** | BR-01 (`weight` válido até 20000 inclusive) |
| **Linha do código** | `weight >= 20000` |
| **Correção** | `weight > 20000` |
| **TCs que detetam** | H-07 |
| **Impacto** | `weight = 20000` retorna `INVALID`/`null`; devia retornar `OK`/`12` |

### DEF-02 — Fronteira do tier 1 usa `<` em vez de `<=`

| Campo | Detalhe |
|---|---|
| **BR violada** | BR-02 (1–1000 g → 5 €) |
| **Linha do código** | `if weight < 1000: fee = 5` |
| **Correção** | `if weight <= 1000: fee = 5` |
| **TCs que detetam** | H-03 |
| **Impacto** | `weight = 1000` é classificado no tier 2 e retorna `fee = 8`; devia retornar `fee = 5` |

### DEF-03 — Surcharge REMOTE usa atribuição `=` em vez de incremento `+=`

| Campo | Detalhe |
|---|---|
| **BR violada** | BR-03 (REMOTE +4 € sobre a base fee) |
| **Linha do código** | `if zone == "REMOTE": fee = 4` |
| **Correção** | `if zone == "REMOTE": fee += 4` |
| **TCs que detetam** | H-10, H-12, H-13 |
| **Impacto** | A base fee é sobrescrita em vez de acrescida: H-10 retorna `fee = 4` (devia ser 9); H-12 retorna `fee = 10` (devia ser 15); H-13 retorna `fee = 10` (devia ser 18) |

### DEF-04 — Limiar de `UNAVAILABLE` usa `> 10000` em vez de `> 5000`

| Campo | Detalhe |
|---|---|
| **BR violada** | BR-04 (REMOTE + express indisponível acima de 5000 g) |
| **Linha do código** | `if zone == "REMOTE" and express and weight > 10000:` |
| **Correção** | `if zone == "REMOTE" and express and weight > 5000:` |
| **TCs que detetam** | H-14 |
| **Impacto** | `weight = 5001` com REMOTE + express retorna `OK`/`10`; devia retornar `UNAVAILABLE`/`null` |

### Tabela de rastreabilidade

| Defeito | Linha em `shipping.py` | BR violada | TCs que detetam |
|---|---|---|---|
| DEF-01 | `weight >= 20000` | BR-01 | H-07 |
| DEF-02 | `if weight < 1000` | BR-02 | H-03 |
| DEF-03 | `fee = 4` | BR-03 | H-10, H-12, H-13 |
| DEF-04 | `weight > 10000` | BR-04 | H-14 |

> **Nota:** H-13 é afetado por DEF-03 e DEF-04 em simultâneo.

---

## 7. Riscos e Prioridades

| ID | Risco | Prob. | Impacto | Estado |
|---|---|---|---|---|
| R1 | Limiar UNAVAILABLE implementado como ≥5000 em vez de >5000 | Alta | Alto | **Confirmado** — DEF-04 |
| R2 | Booleans como `weight` não rejeitados por tipo | Média | Médio | **Não ocorre** — H-15 passa |
| R3 | Cálculo REMOTE+express com ordem errada | Baixa | Baixo | Irrelevante (soma comutativa) |
| R4 | Python 3.9.6 instalado (abaixo do mínimo 3.10+) | Confirmado | Médio | **Ativo** — resolver antes de CP03 |
| R5 | Candidatos AI com expected derivados da implementação | Alta | Alto | A verificar em CP03 |

---

## 8. Distribuição de Trabalho

| Elemento | Contribuição | Estado |
|---|---|---|
| Eduardo Dias | Revisão estática BR-01–BR-08; identificação de ambiguidades; partições e fronteiras; oráculo; plano de 16 casos frozen em `human_cases.json` | ✅ Concluído |
| Rui Carneiro | Revisão dos casos humanos; verificação dos cálculos de fee | ✅ Concluído |
| Érica Moreira | Execução e revisão dos candidatos AI | ⏳ CP03 |
| Beatriz Barbosa | Análise de cobertura | ⏳ CP03 |

---

## 9. Próximas Ações (CP03 — 10 nov)

1. Resolver ambiente Python: upgrade para 3.10+ ou usar máquina de laboratório
2. Clarificar AMB-01/AMB-02 com o professor (comportamento de `bool` como `weight` e `express`)
3. Abrir `ai_candidates.json` (apenas após freeze confirmado do human — já feito)
4. Classificar cada candidato AI: **accept / revise / reject** com justificação contra as BRs
5. Comparar a suite AI com a suite humana e analisar cobertura

---

## 10. Nota de Atualização Posterior (Resolução documentada no CP03)

O registo deste relatório reflete o estado histórico do projeto à data de entrega do **CP02 (28–30 de outubro de 2026)**. No âmbito dos trabalhos do **CP03 (08–10 de novembro de 2026)**, os pontos pendentes foram resolvidos e documentados com evidências no repositório:

1. **Ambiente Python (Risco R4):** Mitigado através da validação da suite em **Python 3.12.7** (conforme o requisito de Python 3.10+), mantendo em simultâneo os resultados na versão **Python 3.9.6** (baseline). Ambas as versões demonstraram paridade estrita de comportamento (13 PASS / 8 FAIL).
2. **Ambiguidades AMB-01 e AMB-02:** Na ausência de esclarecimento formal ou resposta escrita por parte do corpo docente, o grupo adotou uma **decisão metodológica autónoma** baseada na interpretação estrita das regras BR-01 e BR-05 (validação por tipo com rejeição de booleanos como `weight` e de não-booleanos como `express`). Esta resolução foi codificada e empiricamente validada na suite final através dos casos `F-20` e `F-21`.
3. **Distribuição de Trabalho (Érica Moreira e Beatriz Barbosa):** A revisão dos 12 candidatos de IA, a construção da suite final de 21 casos e a matriz de cobertura dos requisitos BR-01 a BR-08 foram integralmente concluídas no CP03.
4. **Risco R5 (Candidatos IA com expected errados):** Confirmado e mitigado no CP03 através da identificação de 3 erros conceituais nos candidatos de IA (AI-05, AI-06 e AI-09), corrigidos com recurso ao oráculo independente.

---

*Ficheiros gerados neste CP:*  
`Trabalho_CP2/human_cases.json` — 16 casos frozen  
`Trabalho_CP2/human_cases.results.json` — resultados da execução (T08-B1.0, Python 3.9.6)
