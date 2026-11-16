# Checkpoint 4 (CP04) — Plano de Execução de Testes e Gestão de Evidências
## TVSI 2026/27 — UMinho | Grupo 5

**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5  
**Elementos:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa  
**Data:** 16 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Objeto de Teste:** `quote(weight, zone, express)` em `shipping.py`  
**Documento:** Plano de Execução de Testes e Gestão de Evidências (CP04)

---

## 1. Identificação e Objetivos do CP04

O **Checkpoint 4 (CP04)** tem como objetivo primordial a execução sistemática das suites de teste, a gestão rigorosa e rastreável de todas as evidências de teste, a validação empírica do comportamento do software em múltiplos ambientes de execução e o fecho dos relatórios de defeitos e discrepâncias de oráculo.

### Objetivos Específicos:
1. **Preservação Integral da Suite Humana Congelada:** Executar e validar a suite humana congelada no CP02 sem adulterações retroativas. A suite humana utilizada no CP04 preserva integralmente os 16 casos de teste concebidos e congelados no CP02 (H-01 a H-16), sendo acompanhada pelo caso técnico H-ENV para validação do ambiente. O conjunto contém, assim, 17 entradas, sem introdução retroativa de casos apresentados como independentes da revisão dos candidatos de IA.
2. **Execução Histórica dos Candidatos de IA:** Executar o conjunto original de 12 candidatos de IA (`AI-01` a `AI-12`) no runner oficial `run_cases.py` sem alteração de expectativas, registando os resultados históricos observados e discriminando metodologicamente os falsos PASS causados por oráculo erróneo da IA (`DATA-01` e `DATA-02`).
3. **Execução Integral da Suite Final Combinada:** Executar a suite final combinada composta por **30 casos de teste** (`H-01` a `H-16` e `F-17` a `F-30`), integrando casos humanos, casos derivados da auditoria de IA e casos complementares de robustez de limites, tipos e domínio (pesos float, whitespace em zonas, strings em booleanos e fronteiras de indisponibilidade).
4. **Isolamento e Rastreabilidade de Defeitos de Software:** Mapear cada falha observada contra os 4 defeitos estruturais da implementação (`DEF-01`, `DEF-02`, `DEF-03`, `DEF-04`), distinguindo-os com rigor dos problemas de qualidade das expectativas da IA (`DATA-01`, `DATA-02`, `DATA-03`).
5. **Auditoria e Atualização do Workbook Oficial:** Preencher e validar o livro de cálculo central `TestResults_T08_Template.xlsx` em todas as suas 6 folhas, adicionando coluna autónoma `Requirement ID(s)` na folha `Executions`, separando os resultados esperados derivados independentemente dos resultados observados, registando a discriminação de papéis dos testers e assegurando integridade total das fórmulas de cobertura (0 erros).
6. **Demonstração de Ausência de Efeitos Secundários (BR-05):** Executar bateria de verificação computacional para demonstrar determinismo, ausência de estado residual, imutabilidade em memória e isolamento delimitado de ficheiros e variáveis de ambiente.

---

## 2. Estratégia de Execução e Suites sob Teste

A estratégia assenta no princípio de caixa-negra estrita, no qual as regras de negócio normativas (**BR-01 a BR-08**) funcionam como oráculo independente supremo. Nenhuma expectativa é ajustada para se conformar ao comportamento anómalo do código.

### 2.1. Quantidade e Caracterização das Suites

| Suite | Identificador dos Casos | Quantidade | Finalidade Metodológica |
|---|---|:---:|---|
| **Ambiente & Smoke** | `H-ENV` | 1 | Validação técnica prévia do ambiente de execução, interpretador Python e runner. |
| **Humana Congelada (CP02)** | `H-01` a `H-16` | 16 | Avaliação do software pelo desenho humano independente, congelado no commit `54ec4d3`. |
| **Humana Total CP04** | `H-ENV` + `H-01` a `H-16` | **17** | **Total da suite humana e de controlo de ambiente para CP04.** |
| **Candidatos Originais IA** | `AI-01` a `AI-12` | **12** | Avaliação do runner sobre o fixture de IA não modificado, expondo vieses e oráculos erróneos. |
| **Suite Final Combinada** | `H-01..16` + `F-17..30` | **30** | Suite de aceitação final do sistema com cobertura total de requisitos, robustez e fronteiras. |
| **Controlo BR-05** | `BR05-DET` a `BR05-EXT` | 4 | Verificação computacional das 4 propriedades de independência funcional. |
| **Robustez do Runner** | `ROB-CLI-01` a `05` | 5 | Verificação do tratamento de exceções e exit code 2 perante anomalias de invocação e formato. |

---

## 3. Ambiente e Procedimentos de Execução

### 3.1. Requisitos Técnicos
- Interpretador primário: Python 3.9.6 (ambiente local macOS).
- Interpretador secundário formal: Python 3.12.7 (verificação de paridade de comportamento da linguagem).
- Runner oficial: `TVSI_T08_Students_B1.0/app/run_cases.py`.
- Formato de entrada: Ficheiros JSON codificados em UTF-8 com chaves obrigatórias `id`, `input` e `expected`.

### 3.2. Procedimento Operacional Padrão
1. Limpeza de artefactos residuais e cache de compilação Python (`__pycache__`).
2. Execução da suite através da invocação via linha de comandos:
   ```bash
   PYTHONPATH=TVSI_T08_Students_B1.0/app python3 TVSI_T08_Students_B1.0/app/run_cases.py <caminho_suite.json>
   ```
3. Verificação do código de saída (`exit code`):
   - `0`: Todos os casos obtiveram `PASS`.
   - `1`: Pelo menos um caso obteve `FAIL`.
   - `2`: Erro de sintaxe, ficheiro inexistente ou formato inválido.
4. Armazenamento imutável do ficheiro `.results.json` gerado na diretoria `Trabalho_CP4/runs/`.
5. Comparação manual e automatizada entre `expected` (oráculo) e `actual` (observado).
6. Mapeamento de discrepâncias para registo formal na folha `Defects` do workbook.

---

## 4. Checklists de Validação de Evidências

Para assegurar conformidade total com as normas da UC, cada evidência deve cumprir a seguinte checklist:

- [x] **Identificador Inequívoco de Teste (`Test ID`):** Correspondência estrita aos identificadores oficiais (`H-ENV`, `H-01..16`, `AI-01..12`, `F-17..30`).
- [x] **Mapeamento de Requisitos (`Requirement ID(s)`):** Ligação explícita às regras normativas exercitadas (`R01` a `R08`).
- [x] **Identificador de Execução (`Run ID`):** Prefixo determinístico que distingue as campanhas (`RUN-ENV`, `RUN-H02`, `RUN-AI`, `RUN-CP4`, `RUN-CTRL`, `RUN-ROB`).
- [x] **Identificação da Build e Ambiente:** Registo explícito da build `T08-B1.0`, versão do interpretador Python e sistema operativo.
- [x] **Data Real de Execução:** Registo cronológico genuíno das campanhas (CP01 em Outubro, CP02 em 30/10, CP03 em 08/11, CP04 em 16/11).
- [x] **Discriminação de Testers:** Identificação clara dos papéis humanos (Executante, Supervisão, Validação) e indicação expressa de assistência por ferramentas.
- [x] **Separação Rigorosa de Oráculo e Saída:** Expected Result derivado das regras vs Observed Result retornado pelo sistema.
- [x] **Veredicto Inviolável:** Classificação estrita em `PASS` ou `FAIL` sem adulteração artificial.
- [x] **Referência de Evidência Auditável:** Caminho relativo para ficheiros de registo JSON existentes no repositório.

---

## 5. Critérios de Conclusão e Aceitação do CP04

O CP04 é considerado formalmente concluído quando todos os seguintes critérios forem verificados com sucesso:

1. **Suite Humana Intacta:** A suite de 17 entradas (`H-ENV` + `H-01..16`) apresenta 11 PASS e 6 FAIL, confirmando a preservação da baseline congelada no CP02.
2. **Suite IA Auditada:** Os 12 candidatos de IA foram executados no runner (10 PASS / 2 FAIL), com os falsos positivos de oráculo devidamente documentados como `DATA-01` e `DATA-02`.
3. **Suite Final Validada:** A suite final de 30 casos (`H-01..16` + `F-17..30`) apresenta 20 PASS e 10 FAIL em Python 3.9 e Python 3.12, cobrindo integralmente as classes de equivalência, fronteiras, limitações operacionais e precedências.
4. **Quatro Defeitos Estruturais Isolados:** Defeitos `DEF-01` a `DEF-04` documentados com passos de reprodução, inputs exatos, evidências e severidade fundamentada.
5. **Demonstração Formal de BR-05:** 4 propriedades de independência validadas com veredicto `PASS`.
6. **Workbook Oficial Auditado:** Folha de cálculo oficial `TestResults_T08_Template.xlsx` com 6 folhas consistentes, coluna `Requirement ID(s)` adicionada em `Executions`, 100% de cobertura e 0 erros de fórmula.
7. **Automação de Auditoria Conforme:** Execução do script `Trabalho_CP4/audit_cp4.py` com resultado global `PASS` em todas as verificações.
