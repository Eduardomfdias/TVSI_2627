# Divulgação de utilização de IA — T08, Grupo 5 (CP01–CP05)

Este documento substitui, para o grupo, a secção em português que foi acrescentada a `TVSI_T08_Students_B1.0/AI_PROVENANCE.md` (o diff dessa secção está preservado em `evidence/legacy/AI_PROVENANCE_secao_grupo.diff` e o texto integral em `evidence/baseline_restauro_20261122/AI_PROVENANCE_acrescento_grupo.md`; o `AI_PROVENANCE.md` do docente foi reposto ao original em 22/11). Nota: essa secção afirmava que a cronologia Git "comprova de forma inequívoca" o congelamento da suite humana; a cronologia é compatível com o congelamento antes da revisão IA, mas não o prova, porque `ai_candidates.json` está no repositório desde 22/10. O `AI_PROVENANCE.md` do docente descreve só o fixture; o uso de IA pelo grupo fica aqui, separado.

## 1. Material de IA fornecido pelo docente (fixture)

| Item | Origem declarada pelo docente | Uso pelo grupo |
|---|---|---|
| `app/ai_candidates.json` (AI-01..AI-12) | "Codex assistant … system identity GPT-6; no independently recorded model snapshot" (AI_PROVENANCE, 20/10/2026). Fixture curado, com erros intencionais | Revisto no CP03 (aceitar/rever/rejeitar) contra o oráculo das BR; executado sem alterações |

O fixture não mede o desempenho de nenhum produto de IA e não permite afirmar superioridade de humanos ou de IA.

## 2. Utilização de IA pelo grupo

O modelo exato só é conhecível quando a ferramenta o expôs na sessão. Onde isso não ficou registado, escreve-se "não registado" em vez de adivinhar.

| CP | Data | Ferramenta / modelo (como exposto) | Finalidade | Material fornecido à ferramenta | Prompt / resposta guardados | Edições humanas | Verificação independente |
|---|---|---|---|---|---|---|---|
| CP01 | 2026-10-22 | "Claude, Anthropic" (CP1.md §9). Interface e modelo: não registados | Estrutura do charter, apoio à revisão estática | BusinessRules, StudentAssignment | Não guardados | Não registadas | Interpretações conferidas contra BR-01..BR-08 (CP1.md §9) |
| CP02 | 2026-10-28/30 | Não registado no CP02. O README atribui ao grupo "Claude Sonnet 4.6 (Claude Code)" sem data por utilização | Não registado por utilização | Não registado | Não guardados | Não registadas | A confirmar pelo grupo |
| CP03 | 2026-11-08/09 | "Claude Sonnet 4.6 (Anthropic Claude Code)" (Relatorio_CP3.md §8) | Classificação dos 12 candidatos, construção de `final_cases.json`, execução do runner, `verify_br05_independence.py` | BR, `ai_candidates.json`, casos humanos | Não guardados | Não registadas | Expectativas conferidas contra o oráculo (Relatorio_CP3.md §8) |
| CP04 | 2026-11-15/17 | Claude Code (RUN-CP4-20261115-162457/RUN_SUMMARY.md: "Execução: Claude Code"). O Relatorio_CP4 indica "Claude Sonnet 4.6"; não há registo do modelo por sessão | Execuções, scripts (`audit_cp4.py`, `update_workbook_cp4.py`, `tools/`), workbook, relatórios de auditoria | Repositório completo | Não guardados | Não registadas | `audit_cp4.py` foi escrito com a mesma ferramenta e **não detetou** a corrupção do workbook (KeyError `rId1`); não deve ser lido como verificação independente |
| CP05 | 2026-11-22 | Claude Code, duas sessões na máquina de Eduardo Dias. Sessão A (análise CP1–CP4, plano v2 `CP5.md`, reposição da baseline, revisão deste relatório): "Opus 5.5" (`claude-opus-5-5`). Sessão B (oráculo, `gap_cases`, execuções, workbook, T6, primeira versão deste documento): segundo o seu próprio registo, "Sonnet 4.6" (`claude-sonnet-4-6`) e "Opus 5.5" (`claude-opus-5-5`) | Análise de lacunas CP1–CP4, oráculo `tools/oracle.py`, `gap_cases.json`, re-execuções, workbook CP05, T6, este documento e o Relatorio_CP5 | Repositório completo; `Trabalho_CP5/CP5.md` | Prompt: `ai_log/CP5_prompt_claude_code.md`. Resposta: os próprios artefactos do CP05; a transcrição da sessão não está no repositório | A fazer pelo grupo na revisão | Expectativas F-31..F-47 e tabela T6 a conferir à mão por um membro (ver Relatorio_CP5 §6); 4 linhas da T6 conferidas na sessão |

## 3. Limites

- O oráculo `tools/oracle.py` foi escrito com assistência de IA a partir do texto das BR. Um oráculo escrito pelo próprio grupo, com a mesma ferramenta que gerou os casos, não é independente no sentido forte; por isso as expectativas novas exigem conferência manual por um membro.
- Os registos de CP01–CP04 não guardaram prompts nem respostas. Esta lacuna não é recuperável, apenas declarada.
