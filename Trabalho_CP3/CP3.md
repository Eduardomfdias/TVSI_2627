# CP03 — Plano de Execução para Claude

## T08 · Desenho de Testes com Assistência de IA · Build T08-B1.0

**Due:** 10 novembro 2026, 23:59 (hora de Portugal)

---

## Contexto

O grupo já tem:

- **16 casos humanos congelados** em `human_cases.json` (H-01 a H-16) — feitos em CP02
- **Oráculo independente** derivado exclusivamente das BR (sem consultar shipping.py nem ai_candidates.json)
- **Resultados de execução CP02:** 10 PASS / 6 FAIL — defeitos DEF-01 a DEF-04 identificados
- **ai_candidates.json** — NÃO foi aberto em CP02; pode ser aberto agora em CP03

**Função sob teste:** `calculate_shipping(weight: int, zone: str, express: bool) -> {status, fee}`

**Oráculo (resumo):**

1. Validação (BR-01): weight int ∈ [1,20000] e não bool; zone ∈ {"LOCAL","REMOTE"} exactamente; express bool real → se falhar: INVALID, null
2. Disponibilidade (BR-04): zone==REMOTE e express==True e weight > 5000 → UNAVAILABLE, null
3. Fee base (BR-02): 1–1000g → 5€; 1001–5000g → 8€; 5001–20000g → 12€
4. Suplementos (BR-03): +4€ se REMOTE; +6€ se express==True (acumulativos)

---

## Passos a executar

### PASSO 1 — Ler ai_candidates.json

```
Read("ai_candidates.json")
```

Para cada candidato, registar:

- `id`, `weight`, `zone`, `express`, `expected_status`, `expected_fee`

---

### PASSO 2 — Classificar cada candidato IA

Para **cada candidato**, aplicar o oráculo independente e classificar:

| Classificação | Critério |
| --- | --- |
| **aceitar** | Inputs e expected corretos segundo as BR; não duplica caso humano existente com cobertura equivalente |
| **rever** | Inputs válidos mas expected errado — corrigir expected antes de incluir |
| **rejeitar** | Input inválido como caso, duplicate sem valor adicional, ou expected irrecuperável |

Registar para cada candidato:

- Classificação (aceitar / rever / rejeitar)
- Expected correto segundo oráculo (se diferir do candidato)
- Justificação com referência à BR violada ou confirmada
- Cobertura que acrescenta (ou não) face aos 16 casos humanos

---

### PASSO 3 — Construir final_cases.json

Regras:

- Começar pelos 16 casos humanos (H-01 a H-16) — **mantê-los todos, sem alterar**
- Acrescentar candidatos IA classificados como "aceitar" ou "rever" (com expected corrigido) que adicionem cobertura nova
- Alvo mínimo: **≥ 16 casos** no total (já garantido pelos humanos; IA aumenta o número)
- Atribuir IDs aos casos IA aceites: prefixo `F-xx` (ex: F-17, F-18…) ou manter IDs originais do ficheiro AI se já existirem
- Garantir que a suite final cobre todas as BR (R01–R08)

Formato de cada caso em final_cases.json (seguir estrutura de human_cases.json):

```json
{
  "id": "F-17",
  "weight": ...,
  "zone": "...",
  "express": ...,
  "expected_status": "...",
  "expected_fee": ...
}
```

---

### PASSO 4 — Preencher TestResults_T08_Template.xlsx

Verificar quais os separadores/colunas existentes no template antes de preencher.

Dados a registar por caso de teste (humano e final):

- **TC-ID** — identificador único
- **Requisito(s) coberto(s)** — BR-01, BR-02, etc.
- **Técnica** — EP, BVA, combinação
- **Prioridade** — Alta/Média/Baixa (os casos de fronteira e os que detetaram defeitos = Alta)
- **Inputs** — weight, zone, express (valores exactos)
- **Pré-condições** — ambiente Python, ficheiro de entrada
- **Expected status** — OK / INVALID / UNAVAILABLE
- **Expected fee** — valor inteiro ou null
- **Raciocínio do oráculo** — frase curta que reproduz o cálculo

Para separador de revisão dos candidatos IA, registar:

- ID do candidato, classificação, expected original, expected corrigido (se revisto), justificação com BR

---

### PASSO 5 — Verificar cobertura R01–R08

Confirmar que a suite final tem pelo menos um caso por cada requisito:

| BR | Cobertura esperada |
| --- | --- |
| BR-01 | Casos INVALID: weight=0, weight=20001, weight=bool, zone inválida, express inválido |
| BR-02 | Fronteiras de cada tier: 1, 1000, 1001, 5000, 5001, 20000 |
| BR-03 | LOCAL sem express, REMOTE sem express, LOCAL+express, REMOTE+express |
| BR-04 | REMOTE+express em weight=5000 (disponível), weight=5001 (UNAVAILABLE) |
| BR-05 | Peso inválido com REMOTE+express (validação prevalece sobre disponibilidade) |
| BR-06 | Verificado por execução com runner |
| BR-07 | Verificado por execução (exit codes) |
| BR-08 | Verificado pelo processo (oráculo independente, revisão AI) |

Se existirem lacunas, criar casos adicionais para fechar a cobertura.

---

### PASSO 6 — Executar final_cases.json

```bash
python3 run_cases.py final_cases.json
```

Registar:

- Código de saída (0 = tudo PASS, 1 = há FAILs, 2 = erro de formato)
- PASS / FAIL por caso
- Novos FAILs (além dos já conhecidos de CP02) → abrir DEF-05, DEF-06… se aplicável
- Manter evidências: `final_cases.results.json`

> Nota: Ambiente ainda em Python 3.9.6 (abaixo do mínimo 3.10+). Registar versão utilizada. Conformidade do ambiente permanece pendente — confirmar se foi resolvido desde CP02.

---

### PASSO 7 — Atualizar secção de Riscos e Prioridades

Com base nos resultados do CP03, actualizar:

- R1 (DEF-04 confirmado): estado → Confirmado / Corrigido (dependendo de novo resultado)
- R3 (Python 3.9.6): estado actual
- R4 (candidatos IA): estado → Avaliado em CP03

---

## Entregáveis CP03

| Ficheiro | Descrição |
| --- | --- |
| `final_cases.json` | Suite final ≥ 16 casos (humanos + IA aceites/revistos) |
| `final_cases.results.json` | Output do runner sobre a suite final |
| `TestResults_T08_Template.xlsx` | Workbook actualizado com casos, oracle reasoning, revisão IA |
| `human_cases.json` | Mantido sem alterações (congelado em CP02) |
| `human_cases.results.json` | Mantido (evidência de CP02) |

Submeter ZIP por grupo conforme instruções do Moodle.

---

## Notas para o agente

- O oráculo é a **única referência de verdade** — qualquer divergência da implementação é defeito, não erro do oráculo
- Ao rever candidatos IA: tratar os `expected` do candidato como **hipótese a validar**, não como resultado correcto
- Não alterar `human_cases.json` nem os resultados de CP02
- Registar na Declaração de Utilização de IA (Tabela 20 do relatório) que em CP03 o Claude auxiliou na revisão dos candidatos e construção do final_cases.json
- Se o template xlsx tiver separadores específicos para CP03 (ex: "AI Review", "Final Suite"), preencher esses em vez de criar estrutura nova
