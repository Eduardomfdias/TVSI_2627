# Divulgação de Utilização de IA e Contribuições Individuais — T08, Grupo 5 (CP01–CP05)

Este documento constitui o registo oficial e consolidado da proveniência do material e da utilização de ferramentas de Inteligência Artificial pelo Grupo 5 ao longo dos checkpoints CP01 a CP05, bem como o registo das contribuições e papéis de cada elemento do grupo.

Substitui formalmente a secção que havia sido indevidamente acrescentada ao ficheiro original `TVSI_T08_Students_B1.0/AI_PROVENANCE.md` (o qual foi integralmente reposto ao estado original do docente; o histórico das alterações e diffs encontra-se preservado na pasta de evidências `evidence/baseline_restauro_20261122/`).

---

## 1. Material de IA Fornecido pelo Docente (Fixture de Teste)

| Item | Origem Declarada pelo Docente | Utilização pelo Grupo 5 |
|---|---|---|
| `app/ai_candidates.json` (AI-01 a AI-12) | "Codex assistant … system identity GPT-6; no independently recorded model snapshot" (`AI_PROVENANCE.md`, 20/10/2026). Fixture curado pelo docente com erros e inconsistências intencionais | Auditado e classificado no CP03 contra o oráculo independente das BR (2 aceites, 1 revisto, 9 rejeitados). Executado no CP04 e CP05 no seu formato original sem qualquer alteração aos inputs ou expectativas |

> [!NOTE]
> O fixture fornecido não mede o desempenho de nenhum modelo de IA autónomo e não permite extrapolar conclusões gerais sobre a superioridade de humanos ou de modelos de IA. Trata-se estritamente de um artefacto de teste curado para efeitos pedagógicos.

---

## 2. Distinção de Papéis nos Registos de Execução

Em conformidade com as boas práticas de auditoria de software, a documentação e os registos do Grupo 5 distinguem claramente quatro papéis distintos:

1. **Operador da Execução (`Operator` / `Runner`):** O indivíduo ou sessão técnica que invocou o comando do runner no sistema operativo (atualmente pendente de confirmação nominal nos ficheiros `ENVIRONMENT.txt` de CP05, assinalado como `Tester: a confirmar (sessão Claude Code na máquina de Eduardo Dias)`).
2. **Autor do Teste (`Author`):** O responsável pelo desenho conceptual e especificação dos casos de teste (ex.: Eduardo Dias e Rui Carneiro para a suite humana no CP02; equipa conjunta para os casos de lacuna F-31..F-47).
3. **Revisor do Resultado (`Validator` / `Reviewer`):** O elemento humano que inspecionou e atestou a conformidade do veredicto do runner com a especificação (ex.: Érica Moreira para a suite humana; Beatriz Barbosa para os candidatos IA e F-17..F-30; casos F-31..F-47 pendentes de validação nominal).
4. **Assistência de IA (`AI Assistant`):** Ferramenta tecnológica de suporte utilizada na automação, formulação de código de suporte ou rascunhos de documentação.

---

## 3. Utilização de IA pelo Grupo ao Longo dos Checkpoints

O modelo exato só é registado quando a ferramenta o expôs de forma auditável durante a respetiva sessão. Onde isso não ocorreu nos checkpoints iniciais, regista-se "não registado" em vez de especular.

| Checkpoint | Data | Ferramenta / Modelo | Finalidade e Âmbito | Material Fornecido | Prompts / Transcrições | Edições Humanas | Validação Humana Independente |
|---|---|---|---|---|---|---|---|
| **CP01** | 2026-10-22 | Claude (Anthropic). Interface/modelo: não registados | Estruturação inicial do project charter; rascunho da revisão estática | `BusinessRules.md`, `StudentAssignment.md` | Não guardados historicamente | Estruturação e adaptação do charter | Interpretações conferidas manualmente contra BR-01..BR-08 (`CP1.md` §9) |
| **CP02** | 2026-10-28/30 | Claude Sonnet (Claude Code). Modelo exato por sessão não registado | Apoio na sistematização de partições de equivalência e valores fronteira | `BusinessRules.md` | Não guardados | Desenho e seleção dos 16 casos humanos | Casos H-01 a H-16 congelados manualmente e conferidos contra as regras |
| **CP03** | 2026-11-08/09 | Claude Sonnet 4.6 (Claude Code) | Apoio na classificação dos 12 candidatos IA; rascunho de `verify_br05_independence.py` | `BusinessRules.md`, `ai_candidates.json`, suite humana | Não guardados | Ajustes nas justificações de rejeição | Expectativas de todos os casos conferidas contra o oráculo normativo |
| **CP04** | 2026-11-15/17 | Claude Code (sessões de trabalho no repositório) | Scripts de suporte (`audit_cp4.py`, `update_workbook_cp4.py`); apoio na redação de relatórios | Repositório de trabalho | Não guardados | Revisão dos textos de entrega | Auditoria posterior demonstrou que `audit_cp4.py` não detetou corrupção de referências no Excel; validação humana refeita no CP05 |
| **CP05** | 2026-11-22 | Claude Code (duas sessões na máquina de Eduardo Dias): Sessão A ("Opus 5.5"); Sessão B ("Sonnet 4.6" / "Opus 5.5") | Análise de lacunas de CP04; codificação de `tools/oracle.py`; geração do desenho de `gap_cases.json`; re-execução 3.12; `build_workbook.py` | Repositório integral; `Trabalho_CP5/CP5.md` | Rascunho inicial do prompt arquivado em `ai_log/` | Revisão integral do workbook, eliminação de causas-raiz em código e saneamento de rastreabilidade | Oráculo testado contra as BR; tabela de validação humana dos casos F-31..F-47 criada como pendência |

---

## 4. Matriz de Contribuições Individuais dos Elementos do Grupo

Para assegurar rigor académico, a matriz abaixo discrimina as atividades realizadas, a assistência de IA recebida, as revisões humanas conduzidas e as tarefas pendentes de cada membro:

| Membro | Trabalho Efetivamente Realizado | Trabalho Assistido por IA | Trabalho Revisto por Humanos | Trabalho Ainda Pendente |
|---|---|---|---|---|
| **Eduardo Dias** (pg61456) | Coordenação geral; redação do project charter (CP01); reposição da baseline do docente no CP05; plano de auditoria CP05 | Estruturação de documentos e análise de lacunas via Claude Code | Revisão e aprovação das regras de precedência BR-05; acompanhamento das execuções em Python 3.12 | Re-execução dos testes de robustez do runner em Python 3.10+ (CP06) |
| **Rui Carneiro** (pg63791) | Auditoria técnica de integridade; engenharia de rastreabilidade em `TestResults_T08_CP05.xlsx`; eliminação de ligações espúrias em Coverage; preparação e verificação do pacote de submissão CP05 | Apoio na refatoração de `build_workbook.py` e simulação matemática de fórmulas Excel | Verificação manual do oráculo das BR; conferência de casos fronteira | Validação humana independente e registo nominal nos casos F-31 a F-47 (CP06) |
| **Érica Moreira** (pg65641) | Revisão estática REV-03 (análise da fronteira de 5000 g em BR-04); validação de execuções históricas da suite humana | Formulação de rascunhos de interpretação de normas | Verificação de que a regra BR-04 resolve REV-03 sem consulta à implementação | Execução cruzada das suites de teste num computador independente para preparação da demonstração (CP06) |
| **Beatriz Barbosa** (pg63744) | Caracterização dos defeitos de implementação e defeitos de fixture; revisão estática REV-04 (precedência de validação em BR-05) | Apoio na formulação comparativa de sintomas observados | Verificação da separação rigorosa entre dados do fixture (DATA) e defeitos do software (DEF) | Validação final da matriz de cobertura e reconciliação dos resultados após correções (CP06) |

---

## 5. Limitações e Declarações Éticas

1. **Independência do Oráculo:** O oráculo em `tools/oracle.py` foi programado com apoio de IA com base nas BR. Para mitigar o risco de circularidade, as expectativas dos novos casos foram verificadas termo a termo e dependem de confirmação manual independente.
2. **Prompts Históricos:** Os prompts das sessões de trabalho de CP01 a CP04 não foram arquivados na altura em que decorreram as sessões. Esta lacuna histórica é irreversível e encontra-se expressamente declarada.
3. **Não-Atribuição Indevida:** Nenhuma validação humana é dada como concluída sem que tenha existido conferência nominal efetiva. Onde tal confirmação ainda não ocorreu, o registo permanece rigorosamente identificado como "pendente" ou "a confirmar pelo grupo".
