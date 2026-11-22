# CP05 — Resultados consolidados, cobertura e riscos residuais

**TVSI 2026/27 · T08 — AI-Assisted Test Design · Grupo 5 · Build T08-B1.0** · 2026-11-22 · Checkpoint de 24/11 (não é o relatório final)
Autores: Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa · Workbook: `TestResults_T08_CP05.xlsx`

## 1. Estado

As suites humana (17), IA original (12) e final (30) foram re-executadas em Python 3.12.16 (conforme BR-06) a partir de uma cópia limpa da aplicação, com resultados iguais aos do CP04. Os quatro defeitos de implementação reproduzem-se de forma isolada (3/3 cada). O T1 confirma que só as expectativas AI-05, AI-06 e AI-09 divergem das BR. Os 17 casos de lacuna F-31..F-47 estão desenhados com expectativa derivada das BR, mas **ainda não foram executados (BLOCKED)**: aguardam o commit do desenho, que prova que o desenho precedeu a execução. A baseline do docente continua alterada (ver §2, ponto 1).

## 2. O que mudou desde o CP04

| # | Problema | Estado no CP05 |
|---|---|---|
| 1 | Baseline do docente alterada (`AI_PROVENANCE.md`, template `.xlsx`, `app/ai_candidates.results.json`) | **Pendente.** O conteúdo acrescentado foi copiado para `AI_DISCLOSURE.md` e `evidence/legacy/`; SHA-256 atuais vs `9d9f950` em `evidence/legacy/baseline_sha256_estado_atual.txt`. O restauro (`git checkout 9d9f950 -- …` + `git rm`) fica para decisão do grupo |
| 2 | Workbook do CP04 não abre no openpyxl (`KeyError: rId1`); "OpenXML validado" era falso | Novo `TestResults_T08_CP05.xlsx`, gerado por `tools/build_workbook.py` a partir do CP04 com os ids das tabelas corrigidos; abre com `openpyxl.load_workbook()`. Recálculo no Excel: **a confirmar por um membro** (valores esperados em `evidence/coverage_valores_esperados.txt`). Os workbooks do CP1 e do CP4 ficam como estavam, também partidos |
| 3 | Execuções oficiais em 3.9.6 | Preservadas e anotadas "ambiente não conforme com BR-06" na folha Executions. As execuções CP05 são em 3.12.16 |
| 4 | Defect reports com linhas de código como causa | A folha Defects passa a ter setup + comando + input JSON + output observado. A leitura do código no CP02 fica registada como limitação (NOTA-02) |
| 5 | AI-12 omitido | AI-12 (2000, REMOTE, false → esperado 12, observado 4) é um FAIL legítimo e suporta DEF-03 |
| 6 | Falta a comparação de igual dimensão | §6 e folha Technique (linhas 48+) |
| 7 | Divulgação de IA incompleta | `AI_DISCLOSURE.md`, com uma linha por CP e o fixture separado do uso pelo grupo |
| 8 | Links locais absolutos (esquema file com caminho de utilizador) | 9 substituídos por caminhos relativos (FECHO_FINAL_CP04, Relatorio_Consolidado, AUDITORIA_FINAL_ENTREGA). As únicas ocorrências restantes estão no prompt guardado (`CP5.md` e `ai_log/`), como texto citado |
| 9 | Documentos sobrepostos na raiz | **Pendente**: o `git mv` para `Trabalho_CP4/auditoria/` aguarda autorização do grupo |
| 10 | Pontos não listados no CP04, encontrados na revisão | (a) REV-03 e REV-04 da Static Review não eram ambiguidades genuínas: o texto de BR-04 e BR-05 resolve-as. (b) Os desfechos REV-01 e REV-02 citavam a implementação como resposta. (c) `Trabalho_CP1/TestResults_T08_Template.xlsx` foi alterado em 09/11 e 16/11, e `Trabalho_CP3/br05_independence.results.json` foi reescrito no CP04. (d) Desenho e resultados entraram no mesmo commit no CP02 (`54ec4d3`) e no CP03 (`5f9567e`), por isso o Git não prova "design before execution" nesses CPs. (e) O charter excluía a inspeção de código, mas o CP02 inspecionou-o. (f) `audit_cp4.py` deu PASS com o workbook corrompido, por isso não serve como verificação independente |
| 11 | Pontos do relatório CP04 entregue (`relatorio.CP4.md`) | (a) A Tabela 33 afirma "shipping.py não foi inspecionado", mas o §9 cita linhas do código como causa-raiz; corrigido nos defect reports e declarado como limitação. (b) A Tabela 33 mantém texto do CP01 ("ai_candidates.json NÃO foi aberto nesta fase") e mistura o fixture com o uso pelo grupo; substituída por `AI_DISCLOSURE.md`. (c) O §8.5.2 afirma que nenhum defeito foi descoberto por candidatos IA e chama ao desenho humano "estruturalmente mais rigoroso"; o AI-12 deteta DEF-03 com a sua própria expectativa, e o AI_PROVENANCE proíbe conclusões de superioridade, por isso a leitura passa a ser a do §6. (d) O relatório não tinha contribuições individuais (exigidas pelo enunciado); ver §9 |

## 3. Resultados consolidados (RUN-CP5-20261122-212810, Python 3.12.16, macOS 27.2.1 arm64)

| Suite | Casos | PASS | FAIL | BLOCKED | Exit | FAILs |
|---|---:|---:|---:|---:|---:|---|
| Humana (H-ENV + H-01..16) | 17 | 11 | 6 | 0 | 1 | H-03, H-07, H-10, H-12, H-13, H-14 |
| IA original (expectativas da IA) | 12 | 10 | 2 | 0 | 1 | AI-09 (expectativa errada), AI-12 (deteção de DEF-03) |
| Final (H-01..16 + F-17..30) | 30 | 20 | 10 | 0 | 1 | H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30 |
| Lacunas (F-31..47) | 17 | — | — | 17 | — | Por executar após o commit do desenho |

Comparação com o CP04: sem divergências nos 30 casos finais face à execução em 3.12.7, nem nas suites humana e IA face às execuções em 3.9.6. O run `RUN-CP5-20261122-212747` foi abortado (ImportError com a flag `-I`, sem resultados) e está preservado com `ABORTED.md`.

## 4. Findings

**Defeitos de implementação (confirmados; reproduzidos 22/11, RUN-CP5-20261122-212810, tester a confirmar).** Cada defeito conta uma vez.

| ID | Sintoma (black-box) | Regra | Testes de suporte | Severidade |
|---|---|---|---|---|
| DEF-01 | 20000 g válido → INVALID | BR-01 | H-07 | Alta |
| DEF-02 | 1000 g LOCAL → fee 8 (esperado 5) | BR-02 | H-03; AI-06 com oráculo corrigido | Média-Alta |
| DEF-03 | REMOTE devolve fee sem base (500 g → 4; esperado 9) | BR-03 | H-10, H-12, H-13, F-18, F-29, AI-12; AI-05 com oráculo corrigido | Crítica |
| DEF-04 | REMOTE + express > 5000 g → OK (esperado UNAVAILABLE) | BR-04 | H-14, F-19, F-30; AI-09 com oráculo corrigido | Alta |

**Defeitos de dados (fixture IA):** DATA-01 (AI-05 espera 4; falso PASS), DATA-02 (AI-06 espera 8; falso PASS), DATA-03 (AI-09 espera OK/22; FAIL por expectativa errada). AI-10 é redundância (duplicado exato de AI-01), não um defeito.

**Questões de especificação em aberto: nenhuma.** As BR fixam tipos, fronteiras (incluindo "at exactly 5000 it is available"), precedência e formato, e todas as expectativas são deriváveis sem consultar a implementação.

## 5. Rastreabilidade (resumo; detalhe na folha Coverage)

| Req. | Testes (exemplos) | Execuções |
|---|---|---|
| R01 | H-ENV, H-02, H-03, H-07..H-09, H-15, H-16, F-20..F-23, F-25..F-27; F-31..F-35, F-40, F-43..F-45 (BLOCKED) | RUN-CP5-…/final_cases, /human_cases_cp4 |
| R02 | H-ENV, H-01..H-07, H-10..H-13, F-17, F-18, F-24, F-28, F-29; F-36..F-42, F-45 (BLOCKED) | idem |
| R03 | H-01, H-10..H-13, F-17, F-18, F-24, F-28, F-29; F-36..F-42 (BLOCKED) | idem |
| R04 | H-13, H-14, F-19, F-21, F-30; F-41..F-43, F-46, F-47 (BLOCKED) | idem |
| R05 | F-21, H-ENV (ligação herdada do CP04); F-43, F-44 (BLOCKED); BR05-DET/RES/MUT/EXT | RUN-CP5-…/final_cases; RUN-CTRL-01..04 (CP04) |
| R06–R08 | Na Coverage, ligados a casos executados pelo runner (H-ENV, H-01, F-17…) apenas como evidência de processo. A cobertura real vem da verificação de processo e do runner (formato JSON, exit codes 0/1/2, RUN-ROB-01..05, revisão da IA), **não** do comportamento de `quote()` | RUN-CP5 (exit codes), CP04 |

Valores esperados na Coverage após recálculo: Designed/Executed R01 24/15, R02 25/17, R03 17/10, R04 10/5, R05 4/2, R06 7/7, R07 5/5, R08 4/4. Os "não executados" são exatamente os casos F-31+ BLOCKED.

## 6. Cobertura e lacunas na ótica T08

Suite humana de 12 = H-01..H-12, escolhida por ordem de ID e fixada antes do cálculo (`tools/analise_t6.py`; conferida à mão nas linhas de expectativas inválidas, duplicados e defeitos).

| Suite | n | Requisitos | Partições | Fronteiras (de 10) | Expect. inválidas | Duplicados exatos | Defeitos (expect. originais) | Defeitos (oráculo corrigido) |
|---|---:|---|---:|---:|---:|---:|---|---|
| Humano H-01..H-12 | 12 | R01–R04 | 11 | 8 | 0 | 0 | DEF-01, 02, 03 | DEF-01, 02, 03 |
| IA AI-01..AI-12 | 12 | R01–R05 | 11 | 3 | 3 | 1 (AI-10) | DEF-03 (AI-12) | DEF-02, 03, 04 |
| Humano completo | 16 | R01–R05 | 14 | 10 | 0 | 0 | DEF-01..04 | DEF-01..04 |

Leitura limitada ao material: com expectativas originais, a suite IA deteta só DEF-03, e dois dos seus PASS são falsos (AI-05, AI-06). Com o oráculo corrigido, os inputs IA expõem DEF-02..04, mas não DEF-01 (não há input 20000). A suite humana de 12 não expõe DEF-04, porque o H-14 fica fora dos primeiros 12. Os 16 humanos expõem os quatro. A IA cobre a partição REMOTE > 5000 com express, que falta nos primeiros 12 humanos, mas só 3 das 10 fronteiras. O fixture é curado pelo docente; isto não estabelece superioridade de humanos nem de IA. "R05" conta casos de precedência (INVALID com REMOTE+express e UNAVAILABLE sem fee parcial), uma interpretação do grupo.

**Redundância na suite final (nenhum caso apagado):** F-19 e F-30 estão na mesma partição de H-14 para DEF-04; F-28 tem inputs iguais a AI-03. **Lacunas fechadas pelo desenho F-31..F-47:** weight/zone/express null, weight string, zone vazia; fronteiras REMOTE sem express (1000, 1001, 5000, 5001, 20000); REMOTE express 1000/1001; precedência (20000, REMOTE, true) → UNAVAILABLE e (0, REMOTE, true) → INVALID; 19999 LOCAL. Os casos F-46/F-47 (10000/10001 REMOTE express) delimitam o sintoma de DEF-04. Têm expectativa fundamentada na BR-04, mas os valores foram escolhidos com conhecimento do código obtido no CP02, o que se declara.

## 7. Limitações e riscos residuais

- O oráculo foi derivado pelo próprio grupo, com assistência de IA (`tools/oracle.py`); falta a conferência manual independente dos F-31+.
- A função é testada só via runner/JSON: tipos Python não exprimíveis em JSON (float NaN, bytes, subclasses de int) ficam fora.
- Todas as execuções até agora correram numa só máquina (macOS arm64); falta a reprodução noutro portátil.
- O fixture IA é curado; a comparação T6 não generaliza.
- Desenho e execução no mesmo commit nos CP02/CP03; inspeção do código no CP02.
- A baseline do docente continua alterada até o grupo decidir o restauro.
- A cobertura de requisitos alta não prova correção; os defeitos encontrados não são necessariamente todos os existentes.

## 8. Trabalho por fazer até ao CP06 (9 dez)

| Prioridade | Tarefa | Responsável (proposta, a confirmar) | Bloqueio |
|---|---|---|---|
| 1 | Rever e fazer commit de `gap_cases.json` (+ `gap_cases.design.json`) e só depois executar | Rui (desenho), Eduardo (commit) | Aguarda o grupo |
| 2 | Restaurar a baseline (problema 1) e o `git mv` dos documentos da raiz (problema 9) | Eduardo | Aguarda autorização |
| 3 | Reproduzir as 4 suites noutro portátil com Python 3.10+; cada membro reproduz ≥ 2 testes | Érica + todos | — |
| 4 | Confirmar o recálculo da Coverage no Excel contra `evidence/coverage_valores_esperados.txt` | Beatriz | — |
| 5 | Rever Defects/rastreabilidade após a execução dos F-31+ | Beatriz | Depende de 1 |
| 6 | Relatório quase final de 4–6 páginas, demonstração, ZIP do CP05 (T9) | Eduardo | Depende de 1–3 |

## 9. Contribuições até à data (evidência Git)

| Membro | Evidência | Estado |
|---|---|---|
| Eduardo Dias | 5 commits: baseline e charter (22/10), CP02 (30/10), CP03 (08/11), plano CP04 (15/11) | Confirmado pelo Git |
| Rui Carneiro | 19 commits (09/11–17/11): auditorias, workbook, evidências e fecho do CP04 | Confirmado pelo Git |
| Érica Moreira | Sem commits próprios | A confirmar pelo membro |
| Beatriz Barbosa | Sem commits próprios | A confirmar pelo membro |
| CP05 (esta versão) | Preparado em sessão Claude Code na máquina de Eduardo Dias; sem commit ainda | A confirmar |

## 10. Divulgação de IA (resumo)

Fixture `ai_candidates.json`: Codex/GPT-6, segundo o docente. Uso pelo grupo: Claude (CP01), Claude Code com Sonnet 4.6 segundo os relatórios (CP03–CP04, modelo por sessão não registado) e Claude Code com Sonnet 4.6 / Opus 5.5 (CP05). Prompts dos CP01–CP04 não guardados; o prompt do CP05 está em `ai_log/`. Detalhe e verificações em `AI_DISCLOSURE.md`.
