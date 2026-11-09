# Relatório CP03 — Desenho de Testes com Assistência de IA

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27 — T08 — Grupo 5**  
**Build:** T08-B1.0  
**Data de realização:** 2026-11-08 (Data prevista de checkpoint: 2026-11-10, 23:59)  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa  
**Ferramenta de IA utilizada:** Claude Sonnet 4.6 (Anthropic Claude Code)

---

## 1. Contexto e Objetivos

Este relatório documenta a execução do CP03, cuja finalidade é:

1. Rever os **12 candidatos IA** (`ai_candidates.json`) usando o oráculo independente derivado das Business Rules (BR) — sem consultar `shipping.py`.
2. Classificar cada candidato como **aceitar**, **rever** ou **rejeitar**.
3. Construir a **suite final** (`final_cases.json`) com os 16 casos humanos (H-01 a H-16) congelados em CP02 + casos IA aceites/revistos + casos novos para fechar lacunas de cobertura.
4. Executar a suite final com `run_cases.py` e registar resultados.
5. Demonstrar a independência e ausência de efeitos secundários entre chamadas (BR-05).
6. Verificar cobertura BR-01 a BR-08 e atualizar registo de riscos.

**Função sob teste:** `quote(weight, zone, express)` em `shipping.py`

---

## 2. Oráculo Independente (resumo)

| Passo | Regra | Resultado se falhar |
|-------|-------|---------------------|
| 1 — BR-01 | `weight` é `int` não-bool ∈ [1, 20 000]; `zone` ∈ {"LOCAL", "REMOTE"} (case-sensitive); `express` é `bool` real | `INVALID`, `null` |
| 2 — BR-04 | Se `zone=="REMOTE"` e `express==True` e `weight > 5000` | `UNAVAILABLE`, `null` |
| 3 — BR-02 | Fee base: 1–1 000 g → 5 €; 1 001–5 000 g → 8 €; 5 001–20 000 g → 12 € | — |
| 4 — BR-03 | Suplementos acumulativos: +4 € se REMOTE; +6 € se express==True | — |

---

## 3. Revisão dos Candidatos IA

### 3.1 Tabela de Classificação

| ID | Weight | Zone | Express | Oracle Status | Oracle Fee | Candidato Expected | Candidato Fee | Classificação | Justificação |
|----|--------|------|---------|--------------|------------|-------------------|---------------|---------------|--------------|
| AI-01 | 500 | LOCAL | false | OK | 5 | OK | 5 ✓ | **REJEITAR** | Duplicado exato de H-01. Sem cobertura nova. |
| AI-02 | 2000 | LOCAL | false | OK | 8 | OK | 8 ✓ | **REJEITAR** | EP interior de tier2 LOCAL. H-04 (1001) e H-05 (5000) já cobrem as fronteiras. |
| AI-03 | 6000 | LOCAL | false | OK | 12 | OK | 12 ✓ | **REJEITAR** | EP interior de tier3 LOCAL. H-06 (5001) e H-07 (20000) já cobrem as fronteiras. |
| AI-04 | 500 | LOCAL | true | OK | 11 | OK | 11 ✓ | **REJEITAR** | Duplicado exato de H-11. |
| AI-05 | 500 | REMOTE | false | OK | **9** | OK | **4** ✗ | **REJEITAR** | Duplicado de H-10 + expected errado. Fee correto = 5 (tier1) + 4 (BR-03 REMOTE) = 9. O candidato só indicou o suplemento REMOTE sem a fee base. |
| AI-06 | 1000 | LOCAL | false | OK | **5** | OK | **8** ✗ | **REJEITAR** | Duplicado de H-03 + expected errado. weight=1000 ∈ tier1 (1–1000 g) → fee=5 €, não 8 €. Candidato IA confundiu fronteira superior de tier1 com tier2. |
| AI-07 | 0 | LOCAL | false | INVALID | null | INVALID | null ✓ | **REJEITAR** | Duplicado exato de H-08. |
| AI-08 | 20001 | LOCAL | false | INVALID | null | INVALID | null ✓ | **REJEITAR** | Duplicado exato de H-09. |
| AI-09 | 6000 | REMOTE | true | **UNAVAILABLE** | **null** | OK | **22** ✗ | **REVER** | Expected errado: weight=6000 > 5000 + REMOTE + express → BR-04 → UNAVAILABLE, null. Corrigido para UNAVAILABLE/null. Acrescenta EP interior da zona UNAVAILABLE (H-14 cobre só a fronteira BVA 5001). Incluído como F-19. |
| AI-10 | 500 | LOCAL | false | OK | 5 | OK | 5 ✓ | **REJEITAR** | Triplicado de H-01 / AI-01. |
| AI-11 | 10000 | LOCAL | true | OK | **18** | OK | 18 ✓ | **ACEITAR** | Cobre tier3 (5001–20000) com express para LOCAL. Nenhum caso humano cobre este quadrante. Fee = 12 (tier3) + 6 (express BR-03) = 18. Incluído como F-17. |
| AI-12 | 2000 | REMOTE | false | OK | **12** | OK | 12 ✓ | **ACEITAR** | Cobre tier2 + REMOTE sem express. H-10 cobre tier1 REMOTE, mas nenhum humano cobre tier2 REMOTE. Fee = 8 (tier2) + 4 (REMOTE BR-03) = 12. Incluído como F-18. |

### 3.2 Resumo da Revisão

| Classificação | Quantidade | IDs |
|--------------|------------|-----|
| Aceitar | 2 | AI-11, AI-12 |
| Rever (expected corrigido) | 1 | AI-09 |
| Rejeitar | 9 | AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, AI-08, AI-10 |

**Erros encontrados nos candidatos IA:**
- **AI-05**: fee esperada = 4 (omitiu fee base); correto = 9. Viola BR-03.
- **AI-06**: fee esperada = 8 (confundiu fronteira tier1/tier2); correto = 5. Viola BR-02.
- **AI-09**: status esperado = OK (ignorou BR-04); correto = UNAVAILABLE. Viola BR-04.

---

## 4. Suite Final (final_cases.json)

### 4.1 Casos Adicionados para Fechar Lacunas de Cobertura

Após incorporar os casos IA aceites/revistos, foram identificadas lacunas em:

- **BR-01 (express inválido):** nenhum caso humano testa `express` com tipo não-bool (ex: inteiro).
- **BR-05 (validação prevalece sobre disponibilidade):** nenhum caso testa `weight` inválido com `REMOTE + express=True` para confirmar que BR-01 tem prioridade sobre BR-04.

Foram criados dois casos novos:

| ID | Weight | Zone | Express | Expected Status | Expected Fee | BR coberta | Justificação |
|----|--------|------|---------|----------------|-------------|-----------|--------------|
| F-20 | 500 | LOCAL | 1 (int) | INVALID | null | BR-01 | `express=1` não é bool real → validação falha |
| F-21 | 25000 | REMOTE | true | INVALID | null | BR-01, BR-05 | Weight inválido (>20000) com REMOTE+express: BR-01 tem prioridade sobre BR-04 |

### 4.2 Tabela Completa da Suite Final

| TC-ID | Weight | Zone | Express | Expected Status | Expected Fee | Requisitos | Técnica | Prioridade | Raciocínio do Oráculo |
|-------|--------|------|---------|----------------|-------------|-----------|---------|-----------|----------------------|
| H-01 | 500 | LOCAL | false | OK | 5 | BR-02, BR-03 | EP | Média | tier1 (1–1000)=5; LOCAL sem express: sem suplementos |
| H-02 | 1 | LOCAL | false | OK | 5 | BR-01, BR-02 | BVA | Alta | Limite inferior válido; tier1=5 |
| H-03 | 1000 | LOCAL | false | OK | 5 | BR-01, BR-02 | BVA | Alta | Limite superior tier1; 1000 ∈ [1,1000] → fee=5 |
| H-04 | 1001 | LOCAL | false | OK | 8 | BR-01, BR-02 | BVA | Alta | Limite inferior tier2; 1001 ∈ [1001,5000] → fee=8 |
| H-05 | 5000 | LOCAL | false | OK | 8 | BR-01, BR-02 | BVA | Alta | Limite superior tier2; 5000 ∈ [1001,5000] → fee=8 |
| H-06 | 5001 | LOCAL | false | OK | 12 | BR-01, BR-02 | BVA | Alta | Limite inferior tier3; 5001 ∈ [5001,20000] → fee=12 |
| H-07 | 20000 | LOCAL | false | OK | 12 | BR-01, BR-02 | BVA | Alta | Limite superior válido; 20000 ∈ [1,20000] → fee=12 |
| H-08 | 0 | LOCAL | false | INVALID | null | BR-01 | BVA | Alta | weight=0 < 1 → INVALID |
| H-09 | 20001 | LOCAL | false | INVALID | null | BR-01 | BVA | Alta | weight=20001 > 20000 → INVALID |
| H-10 | 500 | REMOTE | false | OK | 9 | BR-02, BR-03 | EP | Alta | tier1=5; REMOTE+4=9 |
| H-11 | 500 | LOCAL | true | OK | 11 | BR-02, BR-03 | EP | Alta | tier1=5; express+6=11 |
| H-12 | 500 | REMOTE | true | OK | 15 | BR-02, BR-03 | EP | Alta | tier1=5; REMOTE+4; express+6=15 |
| H-13 | 5000 | REMOTE | true | OK | 18 | BR-02, BR-03, BR-04 | BVA | Alta | tier2=8; REMOTE+4; express+6=18; weight=5000 ≤ 5000 → OK |
| H-14 | 5001 | REMOTE | true | UNAVAILABLE | null | BR-04 | BVA | Alta | weight=5001 > 5000 + REMOTE + express → UNAVAILABLE |
| H-15 | true | LOCAL | false | INVALID | null | BR-01 | EP | Alta | weight=True é bool → INVALID |
| H-16 | 500 | local | false | INVALID | null | BR-01 | EP | Alta | zone="local" não ∈ {"LOCAL","REMOTE"} → INVALID |
| F-17 | 10000 | LOCAL | true | OK | 18 | BR-02, BR-03 | EP | Média | tier3=12; express+6=18; LOCAL sem suplemento REMOTE |
| F-18 | 2000 | REMOTE | false | OK | 12 | BR-02, BR-03 | EP | Média | tier2=8; REMOTE+4=12 |
| F-19 | 6000 | REMOTE | true | UNAVAILABLE | null | BR-04 | EP | Alta | weight=6000 > 5000 + REMOTE + express → UNAVAILABLE (EP interior, confirma DEF-04) |
| F-20 | 500 | LOCAL | 1 (int) | INVALID | null | BR-01 | EP | Alta | express=1 não é bool real → INVALID |
| F-21 | 25000 | REMOTE | true | INVALID | null | BR-01, BR-05 | EP/BVA | Alta | weight=25000 > 20000 → BR-01 falha primeiro; UNAVAILABLE não chega a ser avaliado |

**Total: 21 casos** (16 humanos + 3 IA + 2 novos para cobertura)

---

## 5. Verificação de Cobertura BR-01 a BR-08

| BR | Descrição | Casos que cobrem | Estado |
|----|-----------|-----------------|--------|
| BR-01 | Validação de tipos e intervalos | H-02, H-03, H-07, H-08, H-09, H-15, H-16, F-20, F-21 | ✅ Coberto |
| BR-02 | Fee base por tier (1–1000 / 1001–5000 / 5001–20000) | H-02, H-03, H-04, H-05, H-06, H-07 (todas as fronteiras BVA) | ✅ Coberto |
| BR-03 | Suplementos acumulativos REMOTE (+4€) e express (+6€) | H-10 (REMOTE), H-11 (express), H-12 (ambos), F-17, F-18 | ✅ Coberto |
| BR-04 | UNAVAILABLE se REMOTE+express+weight>5000 | H-13 (fronteira disponível), H-14 (fronteira UNAVAILABLE), F-19 (EP interior) | ✅ Coberto |
| BR-05 | Precedência validação > disponibilidade > cálculo; independência de chamadas e ausência de efeitos secundários | F-21 (precedência) + Procedimento `BR05-IND` (independência e ausência de efeitos secundários) | ✅ Coberto |
| BR-06 | Formato JSON; runner `python run_cases.py`; Python 3.10+ | Todos os casos executados com `run_cases.py` (validado em Python 3.12.7 e Python 3.9.6) | ✅ Coberto |
| BR-07 | Runner compara exatamente; exit codes 0=PASS, 1=FAILs, 2=erro | Executado; exit code = 1 (há FAILs documentados) | ✅ Coberto |
| BR-08 | Oráculo independente derivado das BRs; classificação crítica da IA | Oráculo derivado exclusivamente de BR-01–BR-05; candidatos IA revistos e justificados | ✅ Coberto |

---

## 6. Resultados da Execução

**Ambiente de Execução:**
- Execução Primária de Conformidade: Python 3.12.7 (cumpre o requisito Python 3.10+ de BR-06).
- Execução Secundária de Compatibilidade: Python 3.9.6 (versão padrão do sistema macOS).
- Em ambos os ambientes, a suite executou sem erros de infraestrutura, produzindo resultados estritamente idênticos.

**Código de saída do runner (`run_cases.py`):** 1 (há 8 FAILs resultantes de defeitos de implementação).

**Resumo da Suite Final (21 casos):** 13 PASS / 8 FAIL (61,9% taxa de sucesso).

| TC-ID | Verdict | Actual Status | Actual Fee | Defeito associado |
|-------|---------|--------------|------------|-------------------|
| H-01 | ✅ PASS | OK | 5 | — |
| H-02 | ✅ PASS | OK | 5 | — |
| H-03 | ❌ FAIL | OK | **8** (esperado 5) | DEF-02 |
| H-04 | ✅ PASS | OK | 8 | — |
| H-05 | ✅ PASS | OK | 8 | — |
| H-06 | ✅ PASS | OK | 12 | — |
| H-07 | ❌ FAIL | **INVALID** (esperado OK/12) | null | DEF-01 |
| H-08 | ✅ PASS | INVALID | null | — |
| H-09 | ✅ PASS | INVALID | null | — |
| H-10 | ❌ FAIL | OK | **4** (esperado 9) | DEF-03 |
| H-11 | ✅ PASS | OK | 11 | — |
| H-12 | ❌ FAIL | OK | **10** (esperado 15) | DEF-03 |
| H-13 | ❌ FAIL | OK | **10** (esperado 18) | DEF-03 |
| H-14 | ❌ FAIL | **OK/10** (esperado UNAVAILABLE) | 10 | DEF-04 |
| H-15 | ✅ PASS | INVALID | null | — |
| H-16 | ✅ PASS | INVALID | null | — |
| F-17 | ✅ PASS | OK | 18 | — |
| F-18 | ❌ FAIL | OK | **4** (esperado 12) | DEF-03 |
| F-19 | ❌ FAIL | **OK/10** (esperado UNAVAILABLE) | 10 | DEF-04 |
| F-20 | ✅ PASS | INVALID | null | — |
| F-21 | ✅ PASS | INVALID | null | — |

### 6.1 Análise dos Defeitos (Alinhamento Rigoroso com CP02)

Nenhum defeito novo foi introduzido em CP03. Os 8 FAILs observados distribuem-se de forma consistente pelos 4 defeitos identificados desde o CP02:

| Defeito | Descrição | Casos CP02 | Casos CP03 (novos) | Estado |
|---------|-----------|-----------|-------------------|--------|
| **DEF-01** | Fronteira superior de `weight`: implementação usa `>= 20000` em vez de `> 20000`, rejeitando indevidamente `weight=20000` como INVALID em vez de OK (fee=12) | H-07 | — | Confirmado |
| **DEF-02** | Fronteira do tier 1: implementação usa `< 1000` em vez de `<= 1000`, calculando indevidamente taxa de tier 2 (fee=8) para `weight=1000` em vez de tier 1 (fee=5) | H-03 | — | Confirmado |
| **DEF-03** | Sobrescrita do suplemento REMOTE: implementação usa atribuição `=` (`fee = 4`) em vez de soma acumulada `+= 4`, sobrescrevendo a fee base | H-10, H-12, H-13 | F-18 (tier2 REMOTE) | Confirmado e alargado |
| **DEF-04** | Limiar de `UNAVAILABLE`: implementação usa `> 10000` em vez de `> 5000` para REMOTE expresso, retornando OK em vez de UNAVAILABLE para pesos 5001–10000 | H-14 | F-19 (peso 6000) | Confirmado e alargado |

**Nota F-20 (express=1):** PASS — a aplicação verifica `type(express) is not bool`, rejeitando inteiros como não-booleanos.  
**Nota F-21 (weight=25000, REMOTE, true):** PASS — validação tem precedência sobre disponibilidade, devolvendo `INVALID` e confirmando a primeira parte de BR-05.

### 6.2 Demonstração da Independência e Ausência de Efeitos Secundários (BR-05)

A regra BR-05 estipula: *"Repeated calls are independent and have no side effects."*  
Como o runner `run_cases.py` executa os casos sequencialmente no mesmo processo Python sem repetições deliberadas de inputs idênticos, foi desenvolvido e executado um procedimento de verificação complementar (`verify_br05_independence.py`).

Para rigor metodológico, foram distinguidas e testadas **quatro propriedades específicas**, delimitando com precisão o âmbito da verificação:

1. **Repetibilidade dos Resultados (Determinismo — `BR05-DET-01`):**
   - *Procedimento:* Execução consecutiva de 10 chamadas com inputs idênticos `{"weight": 500, "zone": "LOCAL", "express": false}` no mesmo processo runtime.
   - *Resultado esperado:* Cada chamada devolve rigorosamente `{"status": "OK", "fee": 5}` sem qualquer flutuação de valor.
   - *Resultado observado:* 10/10 invocações devolveram o resultado idêntico (**PASS**).

2. **Ausência de Estado Residual entre Chamadas (`BR05-RES-02`):**
   - *Procedimento:* Sequência de 9 passos intercalados alternando transições críticas: Válido nominal → Inválido (peso negativo) → Válido de recuperação → Indisponível (peso 15000 REMOTE express) → Válido de recuperação → Inválido (tipo booleano) → Válido de recuperação → Válido de outro tier (Tier 2) → Válido de referência final.
   - *Resultado esperado:* As chamadas executadas após falhas de validação ou indisponibilidade não sofrem contaminação de estado anterior, comportando-se como se fossem a primeira chamada da sessão.
   - *Resultado observado:* Todos os 9 passos devolveram os outputs exatos previstos pelo oráculo independente (**PASS**).

3. **Ausência de Mutações Observáveis (`BR05-MUT-03`):**
   - *Procedimento:*
     - Verificação de não-mutação dos argumentos de entrada (dicionário de parâmetros do chamador).
     - Isolamento de instâncias de retorno: cada invocação gera uma nova instância de dicionário (`id(res_a) != id(res_b)`). A mutação deliberada pelo caller de um retorno anterior (`res_a["fee"] = 9999`) não corrompe o retorno de chamadas subsequentes.
     - Imutabilidade do namespace do módulo: inspeção de `shipping.__dict__` antes e depois das chamadas, comprovando que nenhuma variável global é criada ou modificada.
   - *Resultado observado:* Imutabilidade de inputs, isolamento de objetos e namespace preservados (**PASS**).

4. **Ausência de Efeitos Secundários Externos Delimitados (`BR05-EXT-04`):**
   - *Procedimento:* Monitorização de streams de saída padrão (`sys.stdout`, `sys.stderr`), variáveis de ambiente (`os.environ`) e snapshot dos ficheiros diretamente existentes na diretoria da aplicação (`app_dir`), comparando nome, tamanho e timestamp de modificação (`st_mtime_ns`) antes e após as invocações de `quote()`.
   - *Resultado esperado:* Nenhuma escrita para stdout/stderr, nenhuma alteração em variáveis de ambiente e nenhuma alteração observável nos ficheiros diretamente monitorizados em `app_dir`.
   - *Resultado observado:* Streams de saída completamente limpos, ambiente inalterado e ficheiros diretamente monitorizados em `app_dir` inalterados (**PASS**).

> **Delimitação Rigorosa de Âmbito:** A função `quote()` em `shipping.py` é uma função de cálculo puramente computacional em memória (sem I/O de rede ou base de dados). A verificação realizada observa especificamente:
> 1. Ausência de saída em `sys.stdout` e `sys.stderr`;
> 2. Ausência de alterações nas variáveis de ambiente (`os.environ`);
> 3. Ausência de alterações observáveis nos ficheiros diretamente existentes em `app_dir` (comparando nome, tamanho e timestamp `st_mtime_ns`).
> 
> *Nota de delimitação:* Este teste não realiza varrimento recursivo de subdiretorias, inspeção de conteúdo integral bit a bit, nem monitorização de todo o sistema de ficheiros do sistema operativo. Os resultados obtidos confirmam a repetibilidade, a ausência de estado residual intra-processo, a ausência de mutações em memória e a ausência de efeitos secundários externos nas áreas expressamente delimitadas e testadas.

- **Evidências geradas:**
  - `Trabalho_CP3/br05_independence.results.json` — Execução em Python 3.9.6 (baseline): veredicto **PASS**.
  - `Trabalho_CP3/br05_independence.py312.json` — Execução em Python 3.12.7 (conformidade 3.10+): veredicto **PASS**.

---

## 7. Riscos e Prioridades (atualizado)

| Risco | Descrição | Estado CP02 | Estado CP03 |
|-------|-----------|------------|------------|
| R1 — DEF-04 | Limiar de UNAVAILABLE incorreto (>10000 em vez de >5000) | Identificado | **Confirmado e Alargado** — F-19 reitera com weight=6000 |
| R2 — DEF-01, DEF-02 | Off-by-one no limite superior (DEF-01) e na fronteira de tier 1 (DEF-02) | Identificado | **Confirmado** — sem alteração na aplicação |
| R3 — Versão de Python | Requisito de Python 3.10+ vs Python 3.9.6 | Pendente | **Mitigado e Validado** — suite executada com Python 3.12.7 e Python 3.9.6 com paridade estrita de comportamento |
| R4 — Candidatos IA | Candidatos com expected incorretos | Aberto | **Fechado** — 3 erros corrigidos/rejeitados com base no oráculo |
| R5 — Estado e Efeitos Secundários | Risco de acoplamento entre chamadas na mesma sessão | Não testado | **Fechado** — verificado e comprovado via `verify_br05_independence.py` |

---

## 8. Declaração de Utilização de IA (Tabela 20)

| Atividade | Ferramenta | Utilização | Revisão Humana |
|-----------|-----------|-----------|---------------|
| Revisão dos candidatos IA (`ai_candidates.json`) | Claude Sonnet 4.6 | Classificação aceitar/rever/rejeitar de cada candidato, aplicando oráculo independente das BR | Sim — oráculo verificado manualmente contra as BR antes da execução |
| Construção de `final_cases.json` | Claude Sonnet 4.6 | Integração de H-01–H-16 + casos IA aceites/revistos + casos F-20/F-21 para fechar lacunas BR-01 e BR-05 | Sim — expected de cada caso verificado pelo oráculo antes de gravar ficheiro |
| Execução com `run_cases.py` e scripts de validação | Claude Code (bash) | Execução do runner e script de independência BR-05 em Python 3.12 e 3.9 | Sim — resultados interpretados e mapeados para defeitos DEF-01 a DEF-04 |

---

## 9. Entregáveis CP03

| Ficheiro | Localização | Descrição |
|---------|------------|-----------|
| `final_cases.json` | `Trabalho_CP3/` | Suite final com 21 casos (H-01–H-16 + F-17–F-21) |
| `final_cases.results.json` | `Trabalho_CP3/` | Output do runner em Python 3.9.6 (baseline): 13 PASS / 8 FAIL, exit code 1 |
| `final_cases.results.py312.json` | `Trabalho_CP3/` | Output do runner em Python 3.12.7 (requisito 3.10+): 13 PASS / 8 FAIL, exit code 1 |
| `verify_br05_independence.py` | `Trabalho_CP3/` | Procedimento complementar de validação de independência e efeitos secundários delimitados (BR-05) |
| `br05_independence.results.json` | `Trabalho_CP3/` | Evidência de execução da validação BR-05 em Python 3.9.6: veredicto PASS |
| `br05_independence.py312.json` | `Trabalho_CP3/` | Evidência de execução da validação BR-05 em Python 3.12.7: veredicto PASS |
| `human_cases.json` | `Trabalho_CP2/` | Suite humana congelada em CP02 (16 casos H-01–H-16) |
| `human_cases.results.json` | `Trabalho_CP2/` | Evidência de execução humana CP02 (10 PASS / 6 FAIL) |
| `Relatorio_CP3.md` | `Trabalho_CP3/` | Relatório consolidado e auditado do CP03 |
| `TestResults_T08_Template.xlsx` | `TVSI_T08_Students_B1.0/` | Workbook de testes oficial integralmente preenchido (Test Cases, Executions, Defects, Static Review, Coverage, Technique) |

---

## 10. Conclusão

O CP03 atingiu plenamente os objetivos estabelecidos:

- **12 candidatos IA revistos**: 2 aceites (AI-11, AI-12), 1 revisto (AI-09 com expected corrigido para UNAVAILABLE/null), 9 rejeitados. Foram detetados 3 erros conceituais nos candidatos gerados por IA, comprovando empiricamente a necessidade de revisão crítica humana apoiada em oráculo independente.
- **Suite final com 21 casos**: 16 casos humanos preservados intactos + 3 casos IA integrados (F-17, F-18, F-19) + 2 casos novos para cobertura de requisitos (F-20 para tipo de express e F-21 para precedência de validação sobre disponibilidade).
- **Cobertura de Requisitos BR-01 a BR-08**: integralmente assegurada, incluindo verificação formal da ausência de efeitos secundários e independência entre chamadas (BR-05).
- **Resultados e Rastreabilidade**: 13 PASS / 8 FAIL. Os 4 defeitos reportados no CP02 foram rigorosamente confirmados e mapeados sem ambiguidades: DEF-01 (fronteira superior weight=20000), DEF-02 (fronteira tier 1 weight=1000), DEF-03 (sobrescrita de fee REMOTE), e DEF-04 (limiar de disponibilidade >10000).
- **Conformidade de Ambiente**: Validada a execução em Python 3.12.7 e Python 3.9.6, comprovando estabilidade e eliminando riscos de desvio ambiental.
