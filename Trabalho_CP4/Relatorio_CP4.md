# Relatório de Execução de Testes e Gestão de Evidências (CP04)
## TVSI 2026/27 — UMinho | Grupo 5

**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5  
**Autores:** Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa  
**Data:** 16 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Objeto de Teste:** `quote(weight, zone, express)` no módulo `shipping.py`  
**Ficheiro do Relatório:** `Trabalho_CP4/Relatorio_CP4.md`

---

# Resumo Executivo

O presente relatório documenta a execução, gestão de evidências e auditoria de qualidade correspondentes ao **Checkpoint 4 (CP04)** do Trabalho T08 (*AI-Assisted Test Design*). 

O foco central deste checkpoint residiu na execução empírica rigorosa de todas as suites de teste concebidas ao longo do projeto, no registo de evidências de execução reproduzíveis e imutáveis, na validação de paridade comportamental entre interpretadores Python (3.9.6 e 3.12.7), na consolidação dos defeitos de raiz da aplicação (`DEF-01` a `DEF-04`) e na análise metodológica das expectativas de teste defeituosas fornecidas pelos modelos de IA (`DATA-01` a `DATA-03`).

O processo respeitou escrupulosamente a preservação da suite humana congelada no CP02 (16 casos concebidos pelos alunos acrescidos de 1 caso técnico de validação de ambiente, totalizando 17 entradas), a execução do fixture original de candidatos de IA no runner sem manipulação retroativa de resultados (10 PASS / 2 FAIL) e a execução formal da suite final expandida de **30 casos de teste** (20 PASS / 10 FAIL). Todas as 68 execuções históricas e atuais foram consolidadas no livro oficial `TestResults_T08_Template.xlsx` com coluna autónoma de requisitos, separação estrita de resultados esperados e observados, e 100% de cobertura normativa sem erros de fórmulas.

---

# 1. Resultados Oficiais das Campanhas de Teste

A tabela seguinte sintetiza os resultados de execução obtidos sobre a build oficial `T08-B1.0`:

| Suite de Testes | Identificação dos Casos | Quantidade | PASS | FAIL | Taxa de Conformidade |
|---|---|:---:|:---:|:---:|:---:|
| **Suite Humana (com H-ENV)** | `H-ENV`, `H-01` a `H-16` | **17** | **11** | **6** | 64.7% |
| **Candidatos Originais de IA** | `AI-01` a `AI-12` | **12** | **10** *(no runner)* | **2** | 83.3% *(aparente)* |
| **Suite Final Combinada** | `H-01..16` + `F-17..30` | **30** | **20** | **10** | 66.7% |

---

# 2. Análise Crítica da Discrepância Metodológica na Suite de IA

Um dos aspetos metodologicamente mais relevantes da auditoria do CP04 é a discrepância entre o veredicto devolvido pelo executor automático (`run_cases.py`) e a conformidade real face às regras de negócio normativas.

Na execução da suite de candidatos de IA (`ai_candidates.json`), o runner reportou **10 PASS e 2 FAIL**. No entanto, a auditoria independente revelou que dois dos casos classificados como PASS pelo runner (`AI-05` e `AI-06`) constituem **falsos positivos do processo de teste** provocados por oráculos defeituosos gerados pela própria IA:

1. **Caso `AI-05` (`weight=500, zone='REMOTE', express=False`):**
   - **Expectativa gerada pela IA:** `{"status": "OK", "fee": 4}`.
   - **Comportamento do código (`shipping.py`):** Retorna `{"status": "OK", "fee": 4}` devido ao bug na linha 14 (`fee = 4` em vez de `fee += 4`).
   - **Veredicto do Runner:** `PASS` (porque a saída observada foi idêntica à expectativa fornecida).
   - **Oráculo Independente das Regras de Negócio (BR-02 + BR-03):** Tarifa base de Tier 1 (5€) + suplemento REMOTE (4€) = **9€** (`{"status": "OK", "fee": 9}`).
   - **Conclusão de Auditoria:** O modelo de IA gerou uma expectativa que reproduziu o próprio defeito da implementação, validando um comportamento incorreto do software. Este problema foi classificado como `DATA-01` (erro de qualidade de dados de teste da IA). O caso foi rejeitado na revisão humana independente.

2. **Caso `AI-06` (`weight=1000, zone='LOCAL', express=False`):**
   - **Expectativa gerada pela IA:** `{"status": "OK", "fee": 8}`.
   - **Comportamento do código (`shipping.py`):** Retorna `{"status": "OK", "fee": 8}` devido ao bug na linha 7 (`weight < 1000` em vez de `<= 1000`).
   - **Veredicto do Runner:** `PASS` (expectativa coincidente com a saída errónea da aplicação).
   - **Oráculo Independente das Regras de Negócio (BR-02):** A regra estipula expressamente que o escalão até 1000g inclusive tem tarifa base de **5€** (`{"status": "OK", "fee": 5}`).
   - **Conclusão de Auditoria:** A IA cometeu um erro de interpretação de fronteira, atribuindo tarifa de Tier 2 a um ponto pertencente a Tier 1, mascarando o defeito `DEF-02`. Classificado como `DATA-02` e rejeitado na revisão humana.

3. **Caso `AI-09` (`weight=6000, zone='REMOTE', express=True`):**
   - **Expectativa gerada pela IA:** `{"status": "OK", "fee": 22}`.
   - **Comportamento do código (`shipping.py`):** Retorna `{"status": "OK", "fee": 10}`.
   - **Veredicto do Runner:** `FAIL` (expectativa 22 vs saída 10).
   - **Oráculo Independente (BR-04):** O serviço expresso para zona REMOTE está explicitamente **indisponível** para encomendas com peso superior a 5000g (`{"status": "UNAVAILABLE", "fee": null}`).
   - **Conclusão de Auditoria:** A IA tentou calcular tarifa somando tarifas de um serviço indisponível. O caso foi revisto pela equipa humana para `F-19` com a expectativa legal correta (`UNAVAILABLE`), permitindo isolar o defeito de implementação `DEF-04`.

**Princípio de Integridade Respeitado:** Em estrito cumprimento das boas práticas de engenharia de testes, os resultados históricos da execução original de `ai_candidates.json` foram preservados no workbook e na pasta `runs/` exatamente como foram emitidos pelo runner (10 PASS / 2 FAIL), sendo a falha de oráculo explicitada nas notas de auditoria e na classificação de problemas de dados de teste.

---

# 3. Caracterização e Rastreabilidade Integral de Defeitos

A auditoria confirmou a existência de **quatro defeitos distintos de implementação** no software fornecido, rigorosamente segregados de **três problemas de qualidade das expectativas de teste da IA**:

## 3.1. Defeitos de Implementação de Software (DEF-01 a DEF-04)

### DEF-01: Limite superior de peso incorretamente implementado
- **Regra Violada:** BR-01 ("Weight must be an integer in grams (1 to 20,000, inclusive)").
- **Localização no Código:** `shipping.py`, linha 3 (`if weight < 1 or weight >= 20000:`).
- **Causa Raiz:** Operador `>=` em vez de `>`, provocando off-by-one e tratando o limite máximo válido (20000g) como inválido.
- **Inputs de Reprodução:** `weight=20000, zone='LOCAL', express=False`.
- **Pré-condições:** Nenhuma (função pura).
- **Passos de Reprodução:** Invocar `quote(20000, 'LOCAL', False)` via interpretador ou runner.
- **Resultado Esperado (Oráculo):** `{"status": "OK", "fee": 12}`.
- **Resultado Observado (Aplicação):** `{"status": "INVALID", "fee": null}`.
- **Testes Associados:** `H-07`.
- **Evidência:** `Trabalho_CP4/runs/final_cases_execution.json#H-07`.
- **Severidade e Rationale:** **Alta**. Rejeita arbitrariamente encomendas legítimas no limite superior de peso do serviço comercial, impedindo o processamento de encomendas válidas de 20 kg.

### DEF-02: Limite entre escalões de peso incorretamente implementado
- **Regra Violada:** BR-02 ("Up to 1,000g: base fee 5€; 1,001g to 5,000g: base fee 8€").
- **Localização no Código:** `shipping.py`, linha 7 (`if weight < 1000:`).
- **Causa Raiz:** Operador `<` em vez de `<=`, fazendo com que encomendas de exatamente 1000g caiam no ramo de Tier 2 (8€) em vez de Tier 1 (5€).
- **Inputs de Reprodução:** `weight=1000, zone='LOCAL', express=False`.
- **Pré-condições:** Nenhuma.
- **Passos de Reprodução:** Invocar `quote(1000, 'LOCAL', False)`.
- **Resultado Esperado (Oráculo):** `{"status": "OK", "fee": 5}`.
- **Resultado Observado (Aplicação):** `{"status": "OK", "fee": 8}`.
- **Testes Associados:** `H-03`.
- **Evidência:** `Trabalho_CP4/runs/final_cases_execution.json#H-03`.
- **Severidade e Rationale:** **Média-Alta**. Sobrecobrança indevida de clientes no limite superior do primeiro escalão (+3€ por encomenda de 1000g), violando a tabela de preços oficial.

### DEF-03: Sobrescrita destrutiva da taxa base no tratamento REMOTE
- **Regra Violada:** BR-03 ("Shipments to 'REMOTE' destinations add a 4€ surcharge to the base fee").
- **Localização no Código:** `shipping.py`, linha 14 (`fee = 4`).
- **Causa Raiz:** Atribuição simples `=` em vez de acumulação `+=`, apagando a tarifa base (5€, 8€ ou 12€) calculada em BR-02.
- **Inputs de Reprodução:** `weight=500, zone='REMOTE', express=False`.
- **Pré-condições:** Nenhuma.
- **Passos de Reprodução:** Invocar `quote(500, 'REMOTE', False)` ou qualquer combinação com `zone='REMOTE'`.
- **Resultado Esperado (Oráculo):** `{"status": "OK", "fee": 9}` (5€ base + 4€ suplemento).
- **Resultado Observado (Aplicação):** `{"status": "OK", "fee": 4}`.
- **Testes Associados:** `H-10, H-12, H-13, F-18, F-29` (5 testes independentes).
  - *Nota Técnica sobre H-13:* O teste `H-13` (`5000g, REMOTE, express=True`) encontra-se perfeitamente disponível (pois 5000 <= 5000) e falha única e exclusivamente pela sobrescrita da taxa base (retorna 10€ em vez de 18€).
- **Evidência:** `Trabalho_CP4/runs/final_cases_execution.json#H-10,#H-12,#H-13,#F-18,#F-29`.
- **Severidade e Rationale:** **Crítica**. Subfaturação massiva e perda financeira sistemática para todas as encomendas com destino remoto.

### DEF-04: Limiar de indisponibilidade REMOTE + express incorreto
- **Regra Violada:** BR-04 ("Express shipping is available for all LOCAL orders, but only for REMOTE shipments with weight up to 5,000g; above 5,000g to REMOTE it is unavailable").
- **Localização no Código:** `shipping.py`, linha 5 (`if zone == "REMOTE" and express and weight > 10000:`).
- **Causa Raiz:** Threshold de indisponibilidade codificado como 10000g em vez de 5000g.
- **Inputs de Reprodução:** `weight=5001, zone='REMOTE', express=True`.
- **Pré-condições:** Nenhuma.
- **Passos de Reprodução:** Invocar `quote(5001, 'REMOTE', True)`.
- **Resultado Esperado (Oráculo):** `{"status": "UNAVAILABLE", "fee": null}`.
- **Resultado Observado (Aplicação):** `{"status": "OK", "fee": 10}`.
- **Testes Associados:** `H-14, F-19, F-30`.
- **Evidência:** `Trabalho_CP4/runs/final_cases_execution.json#H-14,#F-19,#F-30`.
- **Severidade e Rationale:** **Alta**. Aceitação de pedidos de transporte expresso para zonas remotas que a operação logística é incapaz de assegurar contratualmente.

## 3.2. Problemas de Qualidade das Expectativas de Teste de IA (DATA-01 a DATA-03)

| ID | Candidato IA | Regra | Expectativa IA | Oráculo Independente | Saída da Aplicação | Natureza da Falha |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **DATA-01** | `AI-05` | BR-03 | `OK, fee=4` | `OK, fee=9` | `OK, fee=4` | Omissão da taxa base; replica bug `DEF-03` |
| **DATA-02** | `AI-06` | BR-02 | `OK, fee=8` | `OK, fee=5` | `OK, fee=8` | Erro de fronteira; mascara bug `DEF-02` |
| **DATA-03** | `AI-09` | BR-04 | `OK, fee=22` | `UNAVAILABLE, fee=null` | `OK, fee=10` | Tarifação indevida de serviço indisponível |

---

# 4. Execuções Concluídas, Execuções Pendentes e Bloqueios

Em cumprimento estrito das diretrizes de auditoria, discrimina-se com total transparência o estado de cada execução:

## 4.1. Execuções Concluídas com Sucesso
1. **Suite Humana Congelada (17 casos):** Executada com sucesso em Python 3.9.6 e Python 3.12.7 (`RUN-ENV-01`, `RUN-H02-01` a `RUN-H02-16`). Resultado: **11 PASS / 6 FAIL**.
2. **Suite IA Original (12 casos):** Executada no runner oficial (`RUN-AI-01` a `RUN-AI-12`). Resultado: **10 PASS / 2 FAIL**.
3. **Suite Final Expandida (30 casos):** Executada integralmente em Python 3.9.6 e Python 3.12.7 (`RUN-CP4-01` a `RUN-CP4-30`). Resultado: **20 PASS / 10 FAIL**.
4. **Verificação de Limitações Técnicas Operacionais:**
   - **Pesos do tipo float (`F-22`, `weight=500.5`):** Executado. O código rejeita formalmente tipos não-inteiros através de `type(weight) is not int`, retornando `INVALID` conforme BR-01. Veredicto: **PASS**.
   - **Zonas com espaços adicionais (`F-23`, `zone=' LOCAL '`):** Executado. Como strings com espaços não pertencem a `("LOCAL", "REMOTE")`, o código retorna `INVALID` conforme BR-01. Veredicto: **PASS**.
   - **Combinações LOCAL com express (`F-24`, `weight=2000, express=True`):** Executado. Tarifa base 8€ + 6€ = 14€ devolvida corretamente. Veredicto: **PASS**.
   - **Zonas fora de domínio (`F-25`, `zone='INTERNATIONAL'`):** Executado. Retorna `INVALID`. Veredicto: **PASS**.
   - **Pesos negativos (`F-26`, `weight=-100`):** Executado. Retorna `INVALID`. Veredicto: **PASS**.
   - **Express com tipo string (`F-27`, `express='False'`):** Executado. Retorna `INVALID` por falha de tipo `bool`. Veredicto: **PASS**.
5. **Robustez do Runner perante Exit Code 2 (5 cenários):**
   - Invocação sem argumentos (`RUN-ROB-01`): Exit code 2 confirmado.
   - Ficheiro inexistente (`RUN-ROB-02`): Exit code 2 e `CASE FILE ERROR` confirmados.
   - Ficheiro JSON malformado (`RUN-ROB-03`): Exit code 2 e `CASE FILE ERROR` confirmados.
   - Ficheiro JSON com IDs duplicados (`RUN-ROB-04`): Exit code 2 e `CASE FILE ERROR` confirmados.
   - Ficheiro JSON com raiz não-lista (`RUN-ROB-05`): Exit code 2 e `CASE FILE ERROR` confirmados.
6. **Independência e Ausência de Efeitos Secundários (BR-05):**
   - 4 propriedades computacionais validadas com veredicto `PASS` (`RUN-CTRL-01` a `RUN-CTRL-04`).

## 4.2. Execuções Pendentes de Intervenção Humana
- **Preenchimento Final de Números de Estudante na Plataforma de Ensino:** A associação individual dos números mecanográficos no formulário e-Learning da UMinho requer ação administrativa manual dos membros do grupo.
- **Upload e Submissão Formal do Pacote ZIP:** A submissão física do arquivo `TVSI_T08_Grupo5_CP04.zip` na plataforma Moodle requer autenticação e submissão pelos alunos antes do fecho do prazo.
- **Push Final para o Repositório Remoto GitHub:** O envio do commit de fecho do CP04 para `origin/main` requer aprovação e execução do comando de envio remoto pelo utilizador.

## 4.3. Bloqueios Técnicos e Riscos Residuais
- **Bloqueios Atuais:** **Zero**. Não existem bloqueios técnicos no ambiente de teste, na integridade do código, no workbook ou nos scripts de verificação.
- **Riscos Residuais Mitigados:** O risco de corrupção ou dessincronização de fórmulas na folha de cálculo foi totalmente eliminado através da auditoria automatizada OpenXML.

---

# 5. Auditoria de Proveniência de IA

Em cumprimento da regra **BR-08** e das diretrizes de integridade académica:

1. **Modelos de IA Utilizados:**
   - **GPT-6 / Codex (curadoria docente):** Geração do conjunto inicial de 12 candidatos de teste (`ai_candidates.json`) fornecido no início do projeto.
   - **Claude Sonnet 4.6 (Anthropic):** Assistência na estruturação de scripts de automação, identificação combinatória de classes equivalentes e aceleração da redação dos artefactos de teste.
2. **Atividades Assistidas vs Validação Humana:**
   - **Geração Assistida:** Sugestão inicial de cenários de teste adicionais (`F-17` a `F-30`) e esqueletos de scripts de verificação.
   - **Validação Humana Estrita:** Todas as asserções de entrada, parâmetros de chamada, oráculos independentes e atribuições de severidade foram derivados manualmente pelos engenheiros de teste humanos a partir das regras BR-01 a BR-08, antes de qualquer aceitação.
3. **Limitações Evidenciadas pela Assistência de IA:**
   - A experiência empírica do projeto revelou de forma inequívoca que modelos de IA apresentam uma propensão crítica para gerar **oráculos tautológicos** (esperar o que o código faz em vez do que a especificação exige). Os casos `AI-05` e `AI-06` demonstraram que, sem oráculo humano independente, os testes de IA geram falsos PASS e mascaram defeitos graves de software.
   - A intervenção humana especializada é insubstituível para o desenho de casos de fronteira em limites legais e para a formulação de juízos de severidade de negócio.

---

# 6. Conclusão Técnica e Aceitação do CP04

Todas as atividades previstas para o Checkpoint 4 foram concluídas com sucesso. O repositório reflete uma cadeia ininterrupta de rastreabilidade entre requisitos normativos, casos de teste desenhados, execuções empíricas, relatórios de defeitos e livro de cálculo oficial.
