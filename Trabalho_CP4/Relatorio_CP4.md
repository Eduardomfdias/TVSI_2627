# Relatório CP04 — Execuções, Evidência Reprodutível e Draft Defects

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27 — T08 — Grupo 5**  
**Build:** T08-B1.0 · **Data de execução:** 2026-11-15 · **Checkpoint:** 17 nov 2026, 23:59  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa  
**Ambiente:** macOS 27.2.1 · Python 3.12.16 (cumpre BR-06, 3.10+)

---

## 1. Organização e integridade dos dados

- A pasta original do professor (`TVSI_T08_Students_B1.0/`) **não foi alterada**. O SHA-256 dos 14 ficheiros é idêntico antes e depois de todas as execuções (`runs/RUN-CP4-20261115-162457/professor_sha256.*.txt`).
- Todo o trabalho do CP4 foi feito numa cópia: `Trabalho_CP4/TVSI_T08_Students_B1.0_CP4/`.
- Os relatórios de execução anteriores foram preservados antes de qualquer nova execução (BR-07). O relatório H-ENV de 2026-10-22 está guardado como `evidence/run_00_human_HENV_20261022.results.json`.

| Pasta / ficheiro | Conteúdo |
| --- | --- |
| `TVSI_T08_Students_B1.0_CP4/app/human_cases.json` | Suite humana congelada (17 casos) |
| `TVSI_T08_Students_B1.0_CP4/app/final_cases.json` | Suite final do CP4 (30 casos) |
| `TVSI_T08_Students_B1.0_CP4/TestResults_T08_Template.xlsx` | Workbook atualizado (cópia de trabalho) |
| `evidence/run_0X_*.results.json` | Evidências das execuções com nomes únicos |
| `evidence/exit_codes.txt` | Códigos de saída do runner |
| `tools/build_suites.py` | Constrói as suites e valida cada expected contra o oráculo BR |
| `tools/update_workbook.py` | Regista Test Cases, Executions, Defects, Technique e Coverage no workbook |
| `runs/RUN-CP4-20261115-162457/` | Reexecução de controlo da suite do CP3 (21 casos), igual ao CP3 |

---

## 2. Decisões tomadas em relação ao plano `CP4.md`

| Ponto do plano | Decisão do grupo | Motivo |
| --- | --- | --- |
| Tarefa 1: `human_cases.json` com 21 casos (H-ENV + H-01..H-20) | **Mantidos 17 casos** (H-ENV + H-01..H-16, congelados no CP2) | Criar H-17..H-20 depois de abrir o `ai_candidates.json` faria com que esses casos deixassem de ser humanos e independentes da IA (StudentAssignment §2) |
| Tarefa 2: tabela de revisão IA | **Seguida, com correção da classificação** | AI-05, AI-06 e AI-09 entram na suite final com expected corrigido, portanto são **Revise**, não Reject. AI-10 é **Reject** (duplicado) |
| Tarefa 3: `final_cases.json` | Humanos + F-17..F-21 do CP3 + AI-01..AI-08 | AI-09, AI-11 e AI-12 já estavam na suite como F-19, F-17 e F-18 (mesmos inputs), por isso mantêm-se esses IDs para não duplicar testes. F-20 e F-21 mantêm-se porque fecham lacunas de BR-01 (express não-bool) e BR-05 (precedência) |
| Tarefa 5: defeitos | Reprodução reescrita como **comando + input JSON** | O enunciado pede passos exatos e diz para não adivinhar causas a partir de sintomas. As referências a linhas de código foram retiradas |

Esta revisão substitui a do CP3 (que rejeitava os candidatos duplicados). A versão do CP3 continua no workbook original e no `Relatorio_CP3.md`.

---

## 3. Revisão dos candidatos IA (oráculo BR-01..BR-05)

| ID | Input | Expected IA | Oráculo BR | Decisão | ID final | Nota |
| --- | --- | --- | --- | --- | --- | --- |
| AI-01 | 500, LOCAL, false | OK/5 | OK/5 | Accept | AI-01 | Mesmos inputs que H-01 |
| AI-02 | 2000, LOCAL, false | OK/8 | OK/8 | Accept | AI-02 | Ponto interior Tier 2 |
| AI-03 | 6000, LOCAL, false | OK/12 | OK/12 | Accept | AI-03 | Ponto interior Tier 3 |
| AI-04 | 500, LOCAL, true | OK/11 | OK/11 | Accept | AI-04 | Mesmos inputs que H-11 |
| AI-05 | 500, REMOTE, false | OK/**4** | OK/**9** | **Revise** | AI-05 | Omitiu a fee base (BR-02+BR-03) |
| AI-06 | 1000, LOCAL, false | OK/**8** | OK/**5** | **Revise** | AI-06 | 1000 g pertence ao Tier 1 (BR-02) |
| AI-07 | 0, LOCAL, false | INVALID/null | INVALID/null | Accept | AI-07 | Mesmos inputs que H-08 |
| AI-08 | 20001, LOCAL, false | INVALID/null | INVALID/null | Accept | AI-08 | Mesmos inputs que H-09 |
| AI-09 | 6000, REMOTE, true | **OK/22** | **UNAVAILABLE/null** | **Revise** | F-19 | Ignorou BR-04 |
| AI-10 | 500, LOCAL, false | OK/5 | OK/5 | **Reject** | — | Duplicado exato de AI-01 / H-01 |
| AI-11 | 10000, LOCAL, true | OK/18 | OK/18 | Accept | F-17 | Lacuna humana: Tier 3 LOCAL express |
| AI-12 | 2000, REMOTE, false | OK/12 | OK/12 | Accept | F-18 | Lacuna humana: Tier 2 REMOTE |

**Resumo:** 8 Accept, 3 Revise, 1 Reject. Há 3 expectativas incorretas em 12 (25%).

---

## 4. Execuções

Todas as execuções foram feitas a partir de `app/` com `python3.12 -B run_cases.py <suite>.json`. O veredicto manual compara o output observado com o **oráculo BR**, não com o expected do ficheiro.

| Run | Suite | Casos | Runner (vs. expected do ficheiro) | Manual (vs. oráculo BR) | Exit | Evidência |
| --- | --- | --- | --- | --- | --- | --- |
| run_01 | `human_cases.json` | 17 | 11 PASS / 6 FAIL | 11 PASS / 6 FAIL | 1 | `run_01_human_20261115.results.json` |
| run_02 | `ai_candidates.json` | 12 | **10 PASS / 2 FAIL** | **8 PASS / 4 FAIL** | 1 | `run_02_ai_20261115.results.json` |
| run_03 | `final_cases.json` | 30 | 20 PASS / 10 FAIL | 20 PASS / 10 FAIL | 1 | `run_03_final_20261115.results.json` |

No workbook, as execuções estão registadas como RUN-23 a RUN-81, uma linha por teste. A tabela Executions foi estendida de 80 para 86 linhas e as fórmulas da Coverage foram ajustadas, como o template prevê.

**Observação principal (BR-07):** na suite IA sem revisão, o runner dá **PASS** a AI-05 e AI-06. Isto acontece porque o expected errado da IA coincide com o output defeituoso da aplicação. Estes dois falsos PASS escondem o DEF-03 e o DEF-02. O AI-09 dá FAIL, mas contra um expected errado (OK/22). Só o oráculo BR-04 mostra que o resultado correto é UNAVAILABLE (DEF-04).

### FAILs por defeito (run_03, suite final)

| Defeito | Casos em FAIL |
| --- | --- |
| DEF-01 | H-07 |
| DEF-02 | H-03, AI-06 |
| DEF-03 | H-10, H-12, H-13, F-18, AI-05 |
| DEF-04 | H-14, F-19 |

Os 10 FAILs correspondem a **4 defeitos distintos**. Nenhum defeito é contado duas vezes.

---

## 5. Draft defects

| ID | Tipo | Regra | Reprodução | Expected (BR) | Actual | Severidade |
| --- | --- | --- | --- | --- | --- | --- |
| DEF-01 | Implementação | BR-01 | `{"weight": 20000, "zone": "LOCAL", "express": false}` | OK/12 | INVALID/null | Alta |
| DEF-02 | Implementação | BR-02 | `{"weight": 1000, "zone": "LOCAL", "express": false}` | OK/5 | OK/8 | Média |
| DEF-03 | Implementação | BR-03 | `{"weight": 500, "zone": "REMOTE", "express": false}` | OK/9 | OK/4 | Alta |
| DEF-04 | Implementação | BR-04 | `{"weight": 5001, "zone": "REMOTE", "express": true}` | UNAVAILABLE/null | OK/10 | Alta |
| DEF-05 | Dados (`ai_candidates.json`) | BR-08/BR-03 | AI-05 expected fee=4 | OK/9 | — | Média (falso PASS) |
| DEF-06 | Dados (`ai_candidates.json`) | BR-08/BR-02 | AI-06 expected fee=8 | OK/5 | — | Média (falso PASS) |
| DEF-07 | Dados (`ai_candidates.json`) | BR-08/BR-04 | AI-09 expected OK/22 | UNAVAILABLE/null | — | Baixa |

Setup comum: Build T08-B1.0, macOS 27.2.1, Python 3.12.16. Comando: `cd app && python run_cases.py final_cases.json` (ou `ai_candidates.json` para DEF-05..07).  
**Questões de especificação:** não surgiram novas. As REV-01..REV-04 do Static Review continuam válidas.

---

## 6. Comparação entre a suite humana e a suite IA

| Critério | Humana (17) | IA (12) |
| --- | --- | --- |
| Fronteiras de peso (0, 1, 1000, 1001, 5000, 5001, 20000, 20001) | 8/8 | 3/8 (0, 1000, 20001) |
| Fronteira BR-04 (5000/5001 REMOTE express) | Sim (H-13, H-14) | Não (só o ponto interior 6000) |
| Inválidos de tipo e formato (bool, zona case-sensitive) | Sim (H-15, H-16) | Não |
| Expectativas incorretas | 0 | 3 |
| Redundância | 0 duplicados | 1 duplicado interno (AI-10) + 6 com os mesmos inputs que casos humanos |
| Inputs novos face à suite humana | — | 5 (AI-02, AI-03, AI-09, AI-11, AI-12) |
| Defeitos distintos expostos pelo runner, tal como está | 4 | 2 (DEF-03 via AI-12, DEF-04 via AI-09), mais 2 falsos PASS |
| Defeitos distintos expostos com oráculo corrigido | 4 | 3 (DEF-02, DEF-03, DEF-04) |

As suites têm tamanhos diferentes (17 contra 12), por isso a comparação não é entre suites de igual tamanho. O conjunto IA fornecido não permite tirar conclusões sobre a capacidade da IA em geral (BusinessRules, *Comparison method*).

---

## 7. Cobertura de requisitos (aba Coverage)

| Req. | Testes ligados (desenhados = executados) |
| --- | --- |
| R01 | 13 |
| R02 | 18 |
| R03 | 9 |
| R04 | 3 |
| R05 | 2 (+ procedimento `verify_br05_independence.py` do CP3, PASS) |
| R06 | 7 |
| R07 | 7 |
| R08 | 11 |

Isto é cobertura de requisitos, não cobertura de fronteiras nem de decisão. Os 30 casos da suite final correspondem a 24 inputs distintos, porque 6 casos IA aceites repetem inputs humanos. Um número alto de testes não demonstra correção.

**Riscos residuais:**
- BR-04 com LOCAL express acima de 5000 g só é coberto por F-17 (10000 g).
- Não há caso para `zone` com espaços, nem para `weight` float (ex. 500.0).
- BR-06 e BR-07 são verificados pela execução, não por casos dedicados a ficheiros malformados (exit code 2).

---

## 8. Pendentes

- [ ] Abrir o workbook no Excel e confirmar o recálculo das fórmulas da aba Coverage. O workbook foi gerado com openpyxl e as fórmulas só são recalculadas quando o ficheiro é aberto.
- [x] Coluna Priority (aba Test Cases) uniformizada em inglês (`High/Medium/Low`), conforme a validação do template: 20 High, 9 Medium, 1 Low.
- [ ] Rever e assumir individualmente as entradas (tester e owner) antes da entrega.
- [ ] Gerar o ZIP de entrega (workbook, JSONs, resultados e evidência).

---

## 9. Declaração de utilização de IA

| Atividade | Ferramenta | Utilização | Verificação independente |
| --- | --- | --- | --- |
| Construção das suites CP4 e validação dos expected | Claude Code (Opus 5.5) | Script `tools/build_suites.py`: oráculo BR-01..BR-05 aplicado a todos os casos | O script rejeita qualquer expected que divirja do oráculo. As decisões de revisão foram tomadas pelo grupo |
| Execução das 3 suites | Claude Code (bash) | `run_cases.py` em Python 3.12.16, com evidências de nome único | Códigos de saída e outputs guardados em `evidence/` |
| Registo no workbook e redação deste relatório | Claude Code | `tools/update_workbook.py` e este documento | Por rever pelo grupo (ver §8) |

Nota de transparência: ao inspecionar o pacote, o agente apresentou no ecrã o conteúdo de `shipping.py`. Esse conteúdo **não** foi usado para derivar expectativas, que vêm exclusivamente das BR. As causas dos defeitos não são inferidas a partir do código.
