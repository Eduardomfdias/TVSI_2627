# Prompt para Claude Code — CP05 (TVSI T08, Grupo 5)

Cola tudo abaixo da linha numa sessão Claude Code aberta na raiz do repositório `TVSI_2627`.

---

Estás no repositório `TVSI_2627` (TVSI 2026/27, T08 — AI-Assisted Test Design, Grupo 5, build T08-B1.0). Lê primeiro `CLAUDE.md`, `TVSI_T08_Students_B1.0/StudentAssignment.md`, `BusinessRules.md`, `AI_PROVENANCE.md` (versão do commit `9d9f950`) e `Trabalho_CP4/Relatorio_CP4.md`. Responde e escreve tudo em português de Portugal.

## Objetivo

Preparar o checkpoint CP05 (prazo 24 nov 2026, 23:59, hora de Portugal): resultados consolidados até agora, com workbook atualizado, evidência de execução, defect reports revistos, rastreabilidade requisito → teste → execução e um resumo de progresso conciso. Duplicados fundidos, reprodutibilidade verificada, questões em aberto separadas de defeitos confirmados, cobertura e lacunas explicadas na ótica T08 (qualidade do desenho humano vs IA, redundância, expectativas verificadas), limitações e riscos residuais, e trabalho em falta para o CP06 (9 dez). Não é o relatório final.

## Regras invioláveis

1. O oráculo são as BR-01..BR-05. Nunca derivar expectativas do output da aplicação nem do código de `shipping.py`.
2. Nunca inventar resultados. Se um interpretador ou passo não estiver disponível, regista BLOCKED (BLOCKED não é PASS).
3. Nunca apagar nem sobrescrever runs anteriores. Cada nova execução tem Run ID novo (`RUN-CP5-…`) e ficheiro de evidência novo.
4. Trabalha em `Trabalho_CP5/`. Nada de ficheiros novos ou editados em `TVSI_T08_Students_B1.0/`, exceto o restauro do ponto 1 abaixo.
5. Novos testes têm o expected escrito e commitado ANTES de qualquer execução (commit separado), para o histórico Git provar design before execution.
6. Não faças `git push`. Faz commits locais pequenos e com mensagem clara; eu reviso e faço push.
7. Linguagem factual. Proibido "100% validado", "zero riscos", "eliminado totalmente" e equivalentes. Passar testes e ter cobertura alta não prova correção.

## Problemas encontrados no estado atual (commit `a26b0f8`) que o CP05 tem de corrigir

Verifica cada um antes de corrigir e regista no relatório o que mudou e porquê.

1. **Baseline do docente alterada.** Desde `9d9f950` foram alterados/adicionados em `TVSI_T08_Students_B1.0/`: `AI_PROVENANCE.md` (secção em português acrescentada), `TestResults_T08_Template.xlsx` (25 604 → 33 151 bytes) e `app/ai_candidates.results.json`. O enunciado exige preservar a baseline. Ação: mover o conteúdo acrescentado ao AI_PROVENANCE para `Trabalho_CP5/AI_DISCLOSURE.md`, mover o results.json para `Trabalho_CP5/evidence/legacy/` e repor os três caminhos exatamente como em `9d9f950` (`git checkout 9d9f950 -- <ficheiro>` e `git rm` do que não existia). Confirmar com `git diff 9d9f950 -- TVSI_T08_Students_B1.0` vazio e registar SHA-256 antes/depois.
2. **Workbook do CP04 estruturalmente corrompido.** Em `Trabalho_CP4/TestResults_T08_Template.xlsx` as folhas referenciam `<tablePart r:id="rId1"/>` mas os `.rels` usam IDs como `R9ec27faca5a24723`. O openpyxl recusa abrir (`KeyError: Unknown relationship: rId1`) e o Excel deverá pedir reparação e descartar as tabelas. A afirmação "OpenXML validado" é falsa. Ação: criar `Trabalho_CP5/TestResults_T08_CP05.xlsx` a partir do conteúdo do CP04 com os rels consistentes (ou regenerar a partir do template original de `9d9f950` e reinserir os dados), e provar que abre com `openpyxl.load_workbook()` sem `read_only` e que as fórmulas da folha Coverage recalculam (por exemplo com LibreOffice headless, se existir; senão declarar que o recálculo foi verificado manualmente por um membro).
3. **Ambiente abaixo do mínimo.** Muitas execuções oficiais estão em Python 3.9.6, mas BR-06 exige 3.10+. As execuções 3.9.6 ficam preservadas, mas marcadas como ambiente não conforme. As execuções que contam para o CP05 têm de ser em 3.10+ (há evidência de 3.12.7 no Mac). Se não houver 3.10+, BLOCKED.
4. **Defect reports com causa-raiz pelo código.** A folha Defects tem, na coluna de reprodução, coisas como "linha 3 usa `weight >= 20000`". O enunciado pede "Do not guess root causes from symptoms" e o T08 é black-box. Ação: a reprodução passa a ter só setup + comando exato + input JSON + output observado. As referências a linhas de código saem dos defect reports (no máximo, uma nota separada "observação de inspeção de código, não usada como oráculo").
5. **AI-12 omitido na narrativa.** O runner deu 10 PASS / 2 FAIL na suite IA; os FAIL são AI-09 e AI-12. AI-12 (2000, REMOTE, false → 12) tem expectativa correta e falha por deteção genuína do defeito REMOTE (DEF-03). Os relatórios só discutem AI-05, AI-06 e AI-09. Ação: incluir AI-12 como evidência de suporte a DEF-03.
6. **Comparação humano vs IA de igual dimensão em falta.** A folha Technique só tem a classificação dos 12 candidatos. Falta a comparação pedida no enunciado (equal-sized suites, rule/boundary coverage, invalid expectations, redundancy, confirmed defects).
7. **Divulgação de IA incompleta e possivelmente imprecisa.** Os documentos dizem "Claude Sonnet 4.6", mas grande parte dos artefactos (scripts, relatórios de auditoria, workbook) foi produzida via Claude Code. O AI_PROVENANCE exige ferramenta/modelo exatamente como exposto, data, prompt, resposta, edições, dados fornecidos e verificações independentes. Ação: `Trabalho_CP5/AI_DISCLOSURE.md` com uma tabela por utilização (CP01–CP05), separando o fixture do docente (`ai_candidates.json`) do uso de IA pelo grupo. Onde o modelo exato não for conhecível, escrever isso mesmo em vez de adivinhar. Guardar este prompt em `Trabalho_CP5/ai_log/`.
8. **Caminhos locais expostos.** Há 9 links `file:///Users/rui.carneiro/...` em ficheiros `.md`. Trocar por caminhos relativos ao repositório.
9. **Excesso de documentos sobrepostos na raiz** (`AUDITORIA_FINAL_ENTREGA.md`, `FECHO_FINAL_CP04.md`, `RELATORIO_AUDITORIA_FINAL_ENTREGA_CP04.md`, `MANIFEST_ENTREGA.md`, `Relatorio_Consolidado.md`). Mover com `git mv` para `Trabalho_CP4/auditoria/` (sem alterar conteúdo) e atualizar o README para apontar para o CP05 como estado atual.

## Tarefas do CP05

### T1 — Verificar oráculo e consolidar

Recalcula à mão, a partir das BR, o expected de cada caso de `Trabalho_CP4/final_cases.json` e dos 12 AI candidates, e confirma contra o que está no workbook. Valores que verifiquei e tens de confirmar de forma independente: expectativas de AI-05, AI-06 e AI-09 erradas, as restantes 9 corretas; nenhuma expectativa errada nos 30 casos finais. Se houver discrepância com isto, para e reporta-ma antes de continuar.

### T2 — Fundir duplicados e classificar findings

Uma linha por problema distinto e reprodutível, com três categorias separadas:

- **Defeitos de implementação (confirmados)**: DEF-01 (20000 g válido → INVALID; H-07), DEF-02 (1000 g → 8 em vez de 5; H-03, AI-06 revisto), DEF-03 (REMOTE devolve fee errado; H-10, H-12, H-13, F-18, F-29, AI-12), DEF-04 (REMOTE express > 5000 g devolve OK; H-14, F-19, F-30, AI-09 revisto). Vários testes suportam um defeito; não contar o mesmo defeito duas vezes.
- **Defeitos de dados (fixture IA)**: DATA-01 (AI-05), DATA-02 (AI-06), DATA-03 (AI-09). AI-10 é redundância (duplicado exato de AI-01), não defeito.
- **Questões de especificação em aberto**: só as genuínas, com origem na Static Review. Não inventar questões para encher. Se não houver nenhuma por resolver, diz isso e explica a testabilidade.

Coluna Status em cada defeito: Confirmed / Reproduced (data, Run ID, quem) / Open question.

### T3 — Fechar lacunas de cobertura (novos casos, design antes da execução)

Criar `Trabalho_CP5/gap_cases.json` com IDs a partir de F-31, expected derivado das BR, linhas novas em Test Cases (técnica, prioridade, R-IDs, setup separado da ação). Commit antes de executar. Lacunas identificadas na suite final atual:

- Tipos inválidos ainda não testados: `weight` null e string `"500"`; `zone` null e `""`; `express` null.
- Fronteiras REMOTE sem express: 1000, 1001, 5000, 5001, 20000.
- REMOTE express dentro da disponibilidade: 1000 e 1001.
- Precedência BR-05 com input válido nas fronteiras: (20000, REMOTE, true) → UNAVAILABLE e (0, REMOTE, true) → INVALID.
- Fronteira interior 19999 LOCAL.
- Caracterização black-box do intervalo de DEF-04: (10000, REMOTE, true) e (10001, REMOTE, true) → ambos UNAVAILABLE pelas BR. Serve para delimitar o sintoma, não para atribuir causa.

Calcula o expected de cada um e mostra-me a tabela antes do commit. Se alguma linha da lista acima te parecer não ter fundamento nas BR, diz-mo em vez de a incluir.

Depois de executar, reavalia a redundância da suite final: F-19 (6000) e F-30 (8000) estão na mesma partição de H-14 para DEF-04; F-28 equivale a AI-03. Não apagar casos, mas marcar na Technique o que é redundante e o que acrescenta.

### T4 — Reprodutibilidade

Em `Trabalho_CP5/runs/RUN-CP5-<AAAAMMDD-HHMMSS>/`:

1. SHA-256 de `shipping.py` e `run_cases.py` antes e depois; têm de bater com `9d9f950`.
2. Cópia limpa de `app/` (sem `__pycache__`), corrida a partir dessa cópia.
3. Executar com Python 3.10+ (regista `python --version`, SO e data): `human_cases_cp4.json`, `ai_candidates.json` original, `final_cases.json` e `gap_cases.json`, cada um separadamente, com exit code registado e o `.results.json` renomeado com nome único.
4. Para cada DEF, reprodução isolada num interpretador novo (`python -I -c "from shipping import quote; print(quote(...))"`) três vezes, a partir das mesmas condições iniciais.
5. Comparar com os resultados CP04 em 3.12.7 e reportar qualquer divergência sem a esconder.
6. Gerar `RUN_SUMMARY.md` com contagens PASS/FAIL/BLOCKED por suite.

Indica-me qual o membro que deve executar cada suite no próprio portátil (ver T8), para a reprodução não depender de uma só máquina. Se eu não confirmar, regista o tester como "a confirmar".

### T5 — Workbook `Trabalho_CP5/TestResults_T08_CP05.xlsx`

- Test Cases: acrescentar F-31+; não alterar expected de casos frozen.
- Executions: acrescentar linhas RUN-CP5 (build T08-B1.0, SO, versão Python, data, tester, output observado exato, ficheiro de evidência, verdict, Defect IDs). As linhas CP01–CP04 ficam como estão, com nota "ambiente 3.9.6 não conforme com BR-06" onde aplicável.
- Defects: versão revista do T2.
- Coverage: links requisito–teste para todos os casos novos; confirmar que as fórmulas cobrem as linhas usadas (alargar os intervalos `$5:$84` se Executions passar a linha 84).
- Technique: manter a classificação dos 12 candidatos e acrescentar a comparação do T6.
- Verificar abertura sem erros (ver problema 2).

### T6 — Comparação humano vs IA (núcleo do T08)

Tabela de suites de igual dimensão: humano H-01..H-12 (escolhido por ordem de ID, declarado à partida para evitar escolha à medida) vs AI-01..AI-12, e uma linha adicional com o humano completo (16). Métricas: requisitos cobertos (R01–R05), partições cobertas, fronteiras cobertas (0, 1, 1000, 1001, 5000, 5001, 20000, 20001 e a fronteira REMOTE express 5000/5001), expectativas inválidas, redundância (duplicados exatos e mesma partição), defeitos detetados com as expectativas originais e com o oráculo corrigido.

Valores que obtive e tens de confirmar de forma independente:

- IA com expectativas originais: FAIL em AI-09 (expectativa errada) e AI-12 (deteção real de DEF-03).
- IA com oráculo corrigido: os inputs expõem DEF-02, DEF-03 e DEF-04, mas não DEF-01 (não há input 20000).
- Humano H-01..H-12: expõe DEF-01, DEF-02 e DEF-03, mas não DEF-04 (H-14 está fora dos primeiros 12).
- Humano completo (16): expõe os quatro.
- Expectativas inválidas: humano 0, IA 3. Redundância exata: humano 0, IA 1 (AI-10).

Conclusão limitada ao que o material permite: o fixture é curado pelo docente e o AI_PROVENANCE proíbe afirmar superioridade empírica de humanos ou de IA.

### T7 — `Trabalho_CP5/Relatorio_CP5.md` (resumo de progresso, no máximo 3 páginas)

Secções:

1. Estado em 1 parágrafo.
2. O que mudou desde o CP04, incluindo as correções dos problemas 1–9.
3. Resultados consolidados por suite (tabela).
4. Findings: defeitos confirmados, defeitos de dados e questões em aberto, separados.
5. Rastreabilidade: tabela compacta R01–R08 → testes → Run IDs.
6. Cobertura e lacunas (ótica T08, com a tabela do T6). R06–R08 são cobertos por verificação de processo e do runner, não por casos `quote()`; dizer isso explicitamente.
7. Limitações e riscos residuais: oráculo derivado pelo próprio grupo; a função é testada só via runner/JSON (tipos Python não exprimíveis em JSON ficam fora); máquina única até agora; fixture IA curado; cobertura alta não prova correção.
8. Trabalho por fazer, bloqueios, prioridades e responsáveis até ao CP06 (9 dez: relatório quase final de 4–6 páginas e demonstração).
9. Contribuições individuais até à data, por membro, com evidência (commits, Run IDs, folhas do workbook). Se o histórico Git não refletir o trabalho de alguém, não inventes: deixa "a confirmar pelo membro".
10. Divulgação de IA (resumo; o detalhe fica no AI_DISCLOSURE.md).

### T8 — Distribuição proposta (confirmar comigo antes de escrever no relatório)

- Eduardo: coordenação, restauro da baseline, workbook, relatório CP05, ZIP.
- Rui: casos de lacuna F-31+ (design e expected antes da execução).
- Érica: re-execução de reprodutibilidade no portátil próprio e gestão de evidências.
- Beatriz: revisão dos defect reports, fusão de duplicados, rastreabilidade e cobertura.
- Todos: cada membro reproduz pelo menos 2 testes à sua escolha e regista-o (preparação da demonstração).

### T9 — Pacote

`TVSI_T08_Grupo5_CP05.zip` contendo `Trabalho_CP1..CP5/`, a baseline intacta, README atualizado e um `MANIFEST_CP05.md` simples (lista de ficheiros + SHA-256, sem auditorias redundantes), mais um `.sha256` externo do ZIP. O ZIP não vai para o Git se o `.gitignore` o excluir.

## Critérios de aceitação (verifica e mostra-me o output de cada um)

- `git diff 9d9f950 -- TVSI_T08_Students_B1.0` vazio.
- `python -c "import openpyxl; openpyxl.load_workbook('Trabalho_CP5/TestResults_T08_CP05.xlsx')"` sem erro.
- Todas as execuções CP05 em Python 3.10+, com evidência por Run ID, e nenhum results.json anterior alterado (`git diff --stat` sobre `Trabalho_CP2..CP4` vazio, exceto os `git mv` do problema 9).
- `gap_cases.json` commitado antes do primeiro results.json que o usa (mostrar `git log` com as duas datas).
- Nenhum `file:///` nos `.md`.
- Defect reports sem referências a linhas de código como causa.
- Tabela T6 recalculada por script e conferida à mão em pelo menos 4 linhas.

No fim dá-me: lista de commits, tabela de resultados por suite, findings consolidados, pendentes para o CP06 e tudo o que ficou BLOCKED ou "a confirmar".
