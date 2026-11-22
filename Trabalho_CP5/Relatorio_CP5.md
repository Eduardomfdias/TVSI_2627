# CP05 — Consolidação de Resultados, Cobertura e Riscos Residuais

**Universidade do Minho — Tecnologias e Verificação de Sistemas de Informação 2026/27**
**T08 — Desenho de Testes com Assistência de IA · Build T08-B1.0 · Grupo 5**
Eduardo Dias (pg61456) · Rui Carneiro (pg63791) · Érica Moreira (pg65641) · Beatriz Barbosa (pg63744)
Checkpoint de progresso — 24 de novembro de 2026

---

## 1. Introdução

O presente documento corresponde ao quinto checkpoint (CP05) do trabalho T08, cujo objetivo é consolidar os resultados obtidos até à data, explicar a cobertura alcançada e as lacunas existentes, e identificar o trabalho necessário para o CP06. Não constitui o relatório final.

Além da consolidação, o CP05 incluiu uma revisão crítica do trabalho entregue no CP04. Essa revisão identificou afirmações que a evidência não sustentava e práticas que não cumpriam o enunciado. As correções efetuadas são descritas na secção 3, com o motivo e a evidência de cada uma.

## 2. Evolução do trabalho (CP01–CP04)

| Checkpoint | Trabalho realizado | Resultado |
|---|---|---|
| CP01 — Charter e ambiente | Definição de papéis, âmbito, riscos e prioridades; verificação de ambiente com o caso H-ENV; revisão estática inicial das BR-01 a BR-08 | H-ENV com resultado esperado; ambiente em Python 3.9.6, abaixo do mínimo exigido (3.10+) |
| CP02 — Desenho humano independente | Derivação do oráculo a partir das BR; desenho e congelamento de 16 casos humanos (H-01 a H-16) por partições de equivalência e valores fronteira | 10 PASS / 6 FAIL; quatro defeitos distintos (DEF-01 a DEF-04) |
| CP03 — Revisão dos candidatos IA e suite final | Classificação dos 12 candidatos do docente (2 aceites, 1 revisto, 9 rejeitados); construção da suite final de 21 casos; verificação da independência entre chamadas (BR-05) | 3 expectativas erradas no material IA (AI-05, AI-06, AI-09); suite final com 13 PASS / 8 FAIL |
| CP04 — Execução, evidências e defeitos | Alargamento da suite final para 30 casos; execução das três suites; registo de 68 execuções no workbook; consolidação dos defeitos | Final 20 PASS / 10 FAIL; humana 11/6; IA 10/2 |

## 3. Correções ao trabalho entregue no CP04

*Tabela 1 — Problemas identificados, motivo e correção*

| # | Problema identificado | Motivo da correção | Correção efetuada no CP05 |
|---|---|---|---|
| 1 | Na pasta original do docente, o template do workbook foi substituído pelo workbook do grupo e foi acrescentado texto ao `AI_PROVENANCE.md`. O relatório CP04 afirmava que a baseline tinha sido preservada | O enunciado exige preservar a baseline, trabalhar numa cópia do template ("Save a working copy") e documentar o uso de IA do grupo em separado ("Label that material separately") | Os dois ficheiros foram repostos a partir do ZIP original do docente. O objeto de teste (`shipping.py` e `run_cases.py`) nunca foi alterado: os SHA-256 coincidem com o original. O texto do grupo foi preservado na pasta de evidências e integrado na divulgação de IA. Os ficheiros de resultados gerados em `app/` mantêm-se, por serem saídas previstas do runner (BR-06/BR-07) |
| 2 | O workbook do CP04 tinha referências internas inconsistentes: não abre em leitores OpenXML e o Excel pede reparação, descartando tabelas. O CP04 afirmava que o workbook tinha sido validado | Uma validação não verificada não pode ser apresentada como evidência | Foi criado um novo workbook, `TestResults_T08_CP05.xlsx`, que passa a ser o único workbook do projeto. Os workbooks anteriores mantêm-se como histórico, com a limitação declarada |
| 3 | Grande parte das execuções oficiais correu em Python 3.9.6, incluindo a verificação de ambiente RUN-ENV-01, que o CP04 apresentava como conforme | A BR-06 exige Python 3.10+ | As execuções em 3.9.6 foram preservadas e anotadas como não conformes. As três suites foram re-executadas em Python 3.12.16 (secção 4.2) |
| 4 | Os defect reports indicavam linhas do código-fonte como causa-raiz. O charter declarava uma abordagem black-box sem inspeção do código | O enunciado determina "Do not guess root causes from symptoms" e o T08 é baseado na especificação | Cada defeito passa a conter apenas setup, comando, input e output observado. A inspeção do código realizada após a execução no CP02 é declarada como limitação; não foi usada como oráculo |
| 5 | Na revisão estática, os desfechos de REV-01 a REV-03 citavam a implementação, e as questões Q-02/Q-03 ficaram "a confirmar com o docente" | As questões devem resolver-se pela especificação, não pelo comportamento do código | Todas as questões são resolvidas pelo texto das BR (tipos estritos e sem coerção na BR-01, fronteira de 5000 g na BR-04, precedência na BR-05). Não há questões de especificação em aberto |
| 6 | O CP04 afirmava que nenhum defeito tinha sido detetado por um candidato IA. O candidato AI-12 tem expectativa correta e falha | A afirmação contradiz a evidência de execução | O AI-12 passa a contar como evidência do DEF-03 |
| 7 | O CP04 indicava "9 de 12 candidatos duplicados" e generalizava sobre o comportamento de modelos de IA | A contagem não era exata, e o AI_PROVENANCE proíbe conclusões gerais a partir de um fixture curado | Contagem exata: 7 candidatos com input igual a um caso humano e 2 na mesma partição. As generalizações foram retiradas; as conclusões ficam limitadas a este material |
| 8 | Faltava a comparação entre suites de igual dimensão pedida no enunciado | O enunciado exige comparar "equal-sized suites" | Comparação realizada (secção 5) |
| 9 | A declaração de IA do CP04 tinha texto desatualizado do CP01 e confundia o fixture do docente com a utilização de IA pelo grupo | O AI_PROVENANCE exige o registo de ferramenta, data, finalidade e verificações, separado do fixture | Novo documento `AI_DISCLOSURE.md`, com uma entrada por checkpoint (secção 9) |
| 10 | Existiam no CP04 duas versões diferentes de `final_cases.json` com 30 casos, e uma das execuções em 3.12 correu a versão não oficial | A evidência tem de corresponder à suite descrita no relatório | Foi fixada como oficial a suite descrita no relatório CP04 (H-01 a H-16 e F-17 a F-30). A outra versão é declarada como variante de trabalho |
| 11 | O registo RUN-CTRL-01 indicava 100 chamadas idênticas | A evidência e o procedimento registam 10 chamadas | Registo corrigido |
| 12 | No CP02 e no CP03 o desenho e os resultados entraram no mesmo commit, e um ficheiro de resultados do CP03 foi reescrito no CP04 | O enunciado exige desenho antes da execução e preservação das execuções anteriores | Não é reversível e fica declarado como limitação. No CP05, o desenho dos novos casos foi registado no Git antes de qualquer execução |

## 4. Trabalho realizado no CP05

### 4.1 Verificação do oráculo

As expectativas de todas as suites foram recalculadas a partir das BR-01 a BR-05, sem consulta da implementação. Os 16 casos humanos e os 30 casos da suite final não têm expectativas erradas, e os casos H-01 a H-16 mantêm-se idênticos aos congelados no CP02. No material IA, confirmam-se as três expectativas erradas (AI-05, AI-06 e AI-09) e um duplicado exato (AI-10 = AI-01).

### 4.2 Re-execução em ambiente conforme

As três suites foram re-executadas em Python 3.12.16 (macOS, arm64), a partir de uma cópia limpa da aplicação. Os SHA-256 do objeto de teste foram verificados antes e depois da execução.

*Tabela 2 — Resultados consolidados (RUN-CP5-20261122-212810)*

| Suite | Casos | PASS | FAIL | Casos que falham |
|---|---:|---:|---:|---|
| Humana (H-ENV, H-01 a H-16) | 17 | 11 | 6 | H-03, H-07, H-10, H-12, H-13, H-14 |
| IA original (expectativas do fixture) | 12 | 10 | 2 | AI-09 (expectativa errada), AI-12 (deteta DEF-03) |
| Final (H-01 a H-16, F-17 a F-30) | 30 | 20 | 10 | H-03, H-07, H-10, H-12, H-13, H-14, F-18, F-19, F-29, F-30 |

Os resultados coincidem com as execuções do CP04 em Python 3.12.7 e 3.12.16 e com as execuções em 3.9.6, sem divergências.

### 4.3 Reprodutibilidade dos defeitos

Cada defeito foi reproduzido três vezes, em processos Python independentes e a partir das mesmas condições iniciais, com resultado idêntico em todas as repetições.

### 4.4 Consolidação dos findings

*Tabela 3 — Defeitos de implementação (cada defeito é contado uma vez)*

| ID | Sintoma observado | Regra | Testes que o suportam | Severidade |
|---|---|---|---|---|
| DEF-01 | 20000 g (válido) é rejeitado como INVALID | BR-01 | H-07 | Alta |
| DEF-02 | 1000 g LOCAL é cobrado a 8 € em vez de 5 € | BR-02 | H-03; AI-06 com oráculo corrigido | Média-Alta |
| DEF-03 | Destinos REMOTE devolvem fee errada (500 g: 4 € em vez de 9 €) | BR-03 | H-10, H-12, H-13, F-18, F-29, AI-12; AI-05 com oráculo corrigido | Crítica |
| DEF-04 | REMOTE com express acima de 5000 g devolve OK em vez de UNAVAILABLE | BR-04 | H-14, F-19, F-30; AI-09 com oráculo corrigido | Alta |

**Defeitos de dados (fixture IA):** DATA-01 (AI-05 espera 4 €; falso PASS que mascara o DEF-03), DATA-02 (AI-06 espera 8 €; falso PASS que mascara o DEF-02) e DATA-03 (AI-09 espera OK/22 €; o serviço é indisponível segundo a BR-04). O AI-10 é redundância e não um defeito.

**Questões de especificação em aberto:** nenhuma. As BR definem os tipos, as fronteiras, a precedência e o formato, pelo que todas as expectativas são deriváveis sem consultar a implementação.

### 4.5 Desenho dos casos de lacuna

Foram desenhados 17 novos casos (F-31 a F-47), com expectativa derivada das BR, para cobrir as lacunas da suite final:

- tipos inválidos ainda não testados (weight null e string, zone null e vazia, express null);
- fronteiras de peso REMOTE sem express (1000, 1001, 5000, 5001, 20000) e REMOTE com express dentro da disponibilidade (1000, 1001);
- precedência da BR-05 nas fronteiras ((20000, REMOTE, express) → UNAVAILABLE; (0, REMOTE, express) → INVALID);
- fronteira interior 19999 g;
- dois pontos interiores da zona de indisponibilidade (10000 e 10001 g), cujos valores foram escolhidos com conhecimento do código obtido no CP02, o que se declara.

O desenho foi registado no Git antes de qualquer execução. Os casos ainda não foram executados.

## 5. Cobertura e lacunas na ótica T08

### 5.1 Comparação entre suites de igual dimensão

Para a comparação de igual dimensão, fixou-se à partida a suite humana H-01 a H-12 (ordem de ID), comparada com os 12 candidatos IA. Acrescenta-se a suite humana completa como referência.

*Tabela 4 — Comparação entre suites humana e IA*

| Suite | n | Fronteiras cobertas (de 10) | Expectativas erradas | Duplicados exatos | Defeitos (expectativas originais) | Defeitos (oráculo corrigido) |
|---|---:|---:|---:|---:|---|---|
| Humana H-01 a H-12 | 12 | 8 | 0 | 0 | DEF-01, DEF-02, DEF-03 | DEF-01, DEF-02, DEF-03 |
| IA AI-01 a AI-12 | 12 | 3 | 3 | 1 | DEF-03 | DEF-02, DEF-03, DEF-04 |
| Humana completa | 16 | 10 | 0 | 0 | DEF-01 a DEF-04 | DEF-01 a DEF-04 |

Com as expectativas originais, a suite IA deteta apenas o DEF-03, e dois dos seus PASS são falsos (AI-05 e AI-06). Com o oráculo corrigido, os inputs IA expõem o DEF-02, o DEF-03 e o DEF-04, mas não o DEF-01, por não existir um caso com 20000 g. A suite humana de 12 casos não expõe o DEF-04, porque o H-14 fica fora dos primeiros 12; a suite humana completa expõe os quatro. A IA cobre a partição REMOTE acima de 5000 g com express, ausente dos primeiros 12 casos humanos, mas apenas 3 das 10 fronteiras.

Na suite final, F-19 e F-30 estão na mesma partição que o H-14 para o DEF-04, e o F-28 tem input igual ao AI-03; foram mantidos e marcados como redundantes.

Estas conclusões aplicam-se apenas a este material. O fixture é curado pelo docente e não permite afirmar superioridade de humanos ou de IA. A suite do grupo também não é exclusivamente humana: a revisão dos candidatos no CP03 e o desenho dos casos F-31 a F-47 tiveram assistência de IA.

### 5.2 Rastreabilidade requisito → teste → execução

A Tabela 5 resume a folha Coverage do workbook. Cada ligação corresponde a um par requisito–teste; um teste conta como executado quando tem pelo menos uma execução com veredicto PASS ou FAIL. Todas as execuções contabilizadas são do CP05 (RUN-CP5-20261122-212810, Python 3.12.16): os casos H-ENV e H-01 a H-16 foram executados nas suites humana e final, e os casos F-17 a F-30 na suite final. Os casos F-31 a F-47 estão desenhados mas ainda não executados.

*Tabela 5 — Rastreabilidade R01–R08*

| Requisito | Testes ligados | Executados | Testes executados (RUN-CP5-20261122-212810) | Desenhados, por executar |
|---|---:|---:|---|---|
| R01 / BR-01 — validação | 24 | 15 | H-ENV, H-02, H-03, H-07, H-08, H-09, H-15, H-16, F-20 a F-23, F-25 a F-27 | F-31 a F-35, F-40, F-43 a F-45 |
| R02 / BR-02 — fee base | 25 | 17 | H-ENV, H-01 a H-07, H-10 a H-13, F-17, F-18, F-24, F-28, F-29 | F-36 a F-42, F-45 |
| R03 / BR-03 — suplementos | 17 | 10 | H-01, H-10 a H-13, F-17, F-18, F-24, F-28, F-29 | F-36 a F-42 |
| R04 / BR-04 — disponibilidade | 10 | 5 | H-13, H-14, F-19, F-21, F-30 | F-41 a F-43, F-46, F-47 |
| R05 / BR-05 — precedência e independência | 4 | 2 | F-21, H-ENV ¹ | F-43, F-44 |
| R06 / BR-06 — formato e ambiente | 7 | 7 | H-ENV, H-01, H-07, H-14, F-17, F-21, F-30 ² | — |
| R07 / BR-07 — comparação e exit codes | 5 | 5 | H-ENV, H-01, H-03, F-18, F-21 ² | — |
| R08 / BR-08 — revisão do material IA | 4 | 4 | H-01, F-17, F-18, F-19 ² | — |

¹ A ligação R05–H-ENV foi herdada do CP04 e não exercita precedência; é retirada do workbook. A precedência validação > disponibilidade é exercitada pelo F-21 (e pelos F-43/F-44 por executar); a precedência disponibilidade > cálculo pelos casos UNAVAILABLE sem fee (H-14, F-19, F-30). A independência entre chamadas foi verificada pelos controlos RUN-CTRL-01 a RUN-CTRL-04 (CP04), apenas em Python 3.9.6.

² Os requisitos R06 a R08 não dependem do comportamento da função `quote()`. Os casos indicados servem apenas de evidência de que o processo foi aplicado. A verificação efetiva é de processo:
- **R06:** todas as suites foram aceites pelo runner no formato JSON e executadas em Python 3.12.16.
- **R07:** exit code 1 nas três suites CP05, que têm FAILs, e preservação de cada execução com Run ID próprio; os casos de erro do runner (exit code 2, RUN-ROB-01 a RUN-ROB-05) só têm evidência em 3.9.6.
- **R08:** classificação dos 12 candidatos IA contra o oráculo independente (folha Technique) e comparação da secção 5.1.

A cobertura de requisitos indica apenas que cada regra tem testes ligados e executados; não mede a cobertura de partições, fronteiras ou combinações, que é tratada na secção 5.1.

## 6. Limitações e riscos residuais

- O oráculo foi derivado pelo próprio grupo, com assistência de IA; os casos F-31 a F-47 ainda não têm revisão humana registada.
- A função é testada apenas através do runner e de ficheiros JSON, pelo que tipos Python não exprimíveis em JSON ficam fora do âmbito.
- Todas as execuções correram, até agora, numa única máquina.
- O código foi inspecionado no CP02, após a execução, contrariando o âmbito definido no charter.
- Os controlos de independência (BR-05) e de robustez do runner só têm evidência em Python 3.9.6.
- O fixture IA é curado, pelo que a comparação da secção 5 não generaliza.
- Passar nos testes e ter cobertura de requisitos elevada não prova a correção do software, e os defeitos identificados não são necessariamente todos os existentes.

## 7. Trabalho por fazer até ao CP06 (9 de dezembro)

| Prioridade | Tarefa | Responsável |
|---|---|---|
| 1 | Revisão humana dos casos F-31 a F-47 e respetiva execução em Python 3.10+ | Rui Carneiro (revisão), Érica Moreira (execução) |
| 2 | Repetir em Python 3.10+ os controlos de independência (BR-05) e de robustez do runner | Eduardo Dias |
| 3 | Reprodução das suites noutro computador; cada membro reproduz pelo menos dois testes (preparação da demonstração) | Érica Moreira e todos os membros |
| 4 | Revisão final dos defeitos, da rastreabilidade e da cobertura após a execução dos novos casos | Beatriz Barbosa |
| 5 | Relatório quase final (4–6 páginas) e preparação da demonstração | Eduardo Dias |

## 8. Contribuições individuais

| Membro | Contribuição até à data |
|---|---|
| Eduardo Dias | Coordenação; baseline e charter (CP01); desenho da suite humana (CP02); revisão IA e suite final (CP03); plano do CP04; revisão e correções do CP05, incluindo a reposição da baseline |
| Rui Carneiro | Desenho da suite humana (CP02); auditorias, workbook, evidências e fecho do CP04 |
| Érica Moreira | Revisão IA e execução: supervisão das execuções dos candidatos IA (CP03) e validação das execuções da suite humana (CP04); revisão estática REV-03 |
| Beatriz Barbosa | Defeitos, cobertura e risco residual: validação das execuções dos candidatos IA (CP03) e dos casos F-17 a F-30 (CP04); revisão estática REV-04 |

O trabalho da Érica Moreira e da Beatriz Barbosa entrou no repositório através dos commits dos restantes membros.

## 9. Divulgação da utilização de IA

O ficheiro `ai_candidates.json` é material do docente, gerado com o assistente Codex (identificado como GPT-6 no `AI_PROVENANCE.md`). Independentemente desse material, o grupo utilizou o Claude (Anthropic) no CP01 e o Claude Code nos CP03 a CP05, como apoio à revisão dos candidatos, à construção da suite final, às execuções, aos scripts de verificação e à redação. No CP05 foram usadas duas sessões do Claude Code (uma delas com o modelo Opus 5.5). Todas as expectativas foram conferidas contra as BR. Os prompts dos CP01 a CP04 não foram guardados. O detalhe por checkpoint encontra-se em `AI_DISCLOSURE.md`.

---

## Anexo A — Evidências

| Evidência | Localização |
|---|---|
| Reposição da baseline (SHA-256 antes/depois, texto do grupo retirado do AI_PROVENANCE) | `Trabalho_CP5/evidence/baseline_restauro_20261122/` |
| Workbook consolidado | `Trabalho_CP5/TestResults_T08_CP05.xlsx` |
| Execução CP05 (ambiente, SHA-256, resultados por suite, exit codes) | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/` |
| Comparação com as execuções do CP04 | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/comparacao_cp4.txt` |
| Reprodução isolada dos defeitos (3 × 4) | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/reproducoes_isoladas.txt` |
| Comparação humano vs IA | `Trabalho_CP5/runs/RUN-CP5-20261122-212810/t6_comparacao.md` |
| Casos de lacuna (desenho antes da execução) | `Trabalho_CP5/gap_cases.json`, `Trabalho_CP5/gap_cases.design.json` |
| Divulgação de IA | `Trabalho_CP5/AI_DISCLOSURE.md` |
| Relatório e workbook entregues no CP04 | `relatorio.CP4.md`, `testResults.md` |

---

> **NOTA DE TRABALHO — NÃO INCLUIR NA ENTREGA.** Proposta de integração deste conteúdo no relatório Word cumulativo (base: `relatorio.CP4.md`, que já contém CP01–CP04).

## Proposta de estrutura para o relatório Word (CP05)

O relatório CP04 entregue é cumulativo: Parte I (enquadramento, §1–5), Parte II com uma secção por checkpoint (§6 CP01, §7 CP02, §8 CP03, §9 CP04), §10 Declaração de IA e §11 Anexos, com tabelas numeradas até à **Tabela 34**. O CP05 entra como nova secção da Parte II, mantendo o mesmo estilo de numeração. As secções 6–9 **não se reescrevem** (são o registo do que foi entregue); as afirmações corrigidas recebem uma nota de remissão para o §10.1.

### A. Alterações às partes existentes

| Onde (Word CP04) | Alteração |
|---|---|
| Capa | "Relatório de Checkpoint 5 de 6"; subtítulo "CP05 – Consolidated Findings and Coverage" |
| Resumo | Acrescentar um parágrafo sobre o CP05. Retirar do parágrafo do CP04 as afirmações corrigidas ("validado sem erros de fórmula", conformidade do RUN-ENV-01) ou remeter para o §10.1 |
| Índice e Índice de Tabelas | Regenerar no fim (novas secções 10–13 e Tabelas 35–42) |
| §2 "Excluído do âmbito" (inspeção do código) | Nota: "Ver §10.1.3 — inspeção realizada no CP02 após a execução; declarada como limitação" |
| §4 Tabela 3 e §7.5 (riscos) | Sem alteração; o estado atualizado dos riscos vai para o §10.5 |
| §5 Tabela 4 (plano de trabalho) | Marcar CP01–CP05 como concluídos |
| §7.4 e §9.4.1 (defeitos com linhas de código) | Nota: "Defect reports revistos no CP05 (§10.3.1); causas-raiz pelo código retiradas" |
| §8.5.1–8.5.3, §9.2.2, §9.3.1, §9.3.3, §9.6 | Nota de remissão para a Tabela 36 (§10.1.3) em cada afirmação corrigida |
| §10 Declaração de IA | Passa a §11 e é substituída (ver B) |
| §11 Anexos | Passa a §13 |

### B. Novas secções

| Secção Word | Título | Conteúdo (deste documento) | Tabela |
|---|---|---|---|
| **10.** | **CP05 – Consolidated Findings and Coverage** | Parágrafo introdutório (§1) | — |
| 10.1. | Revisão Crítica do CP04 e Correções | | |
| 10.1.1. | Âmbito e Metodologia da Revisão | Revisão de artefactos, relatório e workbook entregues face ao enunciado e às BR | — |
| 10.1.2. | Reposição da Baseline do Docente | Correção 1 da Tabela 1, com SHA-256 antes/depois | Tabela 35 — Estado da baseline (original vs antes vs depois) |
| 10.1.3. | Correções aos Artefactos e ao Relatório CP04 | Tabela 1 (pontos 2–12) | Tabela 36 — Problemas identificados, motivo e correção |
| 10.2. | Verificação do Oráculo e Re-execução | | |
| 10.2.1. | Verificação Independente das Expectativas | §4.1 | — |
| 10.2.2. | Re-execução em Ambiente Conforme (Python 3.12.16) | §4.2 | Tabela 37 — Resultados consolidados por suite |
| 10.2.3. | Reprodutibilidade dos Defeitos | §4.3 | — |
| 10.3. | Consolidação dos Findings | | |
| 10.3.1. | Defeitos de Implementação | §4.4 | Tabela 38 — Defeitos de implementação |
| 10.3.2. | Defeitos de Dados no Material IA | §4.4 (DATA-01 a DATA-03, AI-10) | — |
| 10.3.3. | Questões de Especificação | §4.4 (nenhuma em aberto) | — |
| 10.4. | Cobertura e Lacunas na Ótica T08 | | |
| 10.4.1. | Comparação entre Suites de Igual Dimensão | §5.1 | Tabela 39 — Comparação humano vs IA |
| 10.4.2. | Redundância na Suite Final | §5.1 (F-19, F-30, F-28) | — |
| 10.4.3. | Rastreabilidade Requisito–Teste–Execução | §5.2 (Tabela 5 e notas ¹ ²) | Tabela 40 — Rastreabilidade R01–R08 |
| 10.4.4. | Casos de Lacuna (F-31 a F-47) | §4.5 | — |
| 10.5. | Limitações e Riscos Residuais | §6 + estado atualizado dos riscos R1–R5 do §4 | Tabela 41 — Riscos residuais (estado CP05) |
| 10.6. | Trabalho por Fazer até ao CP06 | §7 | Tabela 42 — Tarefas, prioridades e responsáveis |
| 10.7. | Conclusões do CP05 | 1 parágrafo: o que ficou consolidado, o que foi corrigido, o que falta | — |
| **11.** | **Declaração de Utilização de IA** (substitui o §10 do CP04) | §9 + resumo do `AI_DISCLOSURE.md`: fixture do docente separado do uso pelo grupo; uma linha por checkpoint | Tabela 43 — Utilização de IA por checkpoint |
| **12.** | **Contribuições Individuais** (nova; exigida pelo enunciado) | §8 | Tabela 44 — Contribuições por membro |
| **13.** | **Anexos** | Entregáveis CP05 + Anexo A (evidências) | Tabela 45 — Entregáveis e evidências CP05 |

### C. Notas para a passagem ao Word

- A Tabela 40 (rastreabilidade) corresponde à Tabela 5 (§5.2), extraída do workbook `TestResults_T08_CP05.xlsx` em 22/11. Se o Excel mudar (por exemplo, ao retirar a ligação R05–H-ENV, que passa R05 para 3 ligações e 1 executada), atualizar os números antes de passar para o Word.
- Manter os títulos das secções dos checkpoints em inglês, como no CP04 ("CP05 – Consolidated Findings and Coverage"), e o resto em português.
- Legendas no formato do CP04: *Tabela N - Título*, em itálico, por cima da tabela.
- Os caminhos de ficheiros (evidências) ficam só no Anexo; no corpo do texto basta referir o Run ID.
