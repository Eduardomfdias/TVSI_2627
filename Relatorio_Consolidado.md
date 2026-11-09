# Tecnologias e Verificação de Sistemas de Informação 2026/27
## T08 — Desenho de Testes com Assistência de IA
### Relatório Técnico Consolidado de Testes e Auditoria (CP01, CP02 e CP03)

**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5  
**Data:** 09 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Repositório Oficial:** `https://github.com/Eduardomfdias/TVSI_2627.git` (Ramo `main`)

---

# Resumo Executivo

O presente documento constitui o relatório técnico consolidado do Trabalho T08 (*AI-Assisted Test Design*) no âmbito da unidade curricular de TVSI 2026/27, integrando as atividades, decisões metodológicas, desenhos de teste, execuções e evidências desenvolvidas ao longo dos três checkpoints iniciais (**CP01, CP02 e CP03**).

O objeto de teste é a função `quote(weight, zone, express)` implementada no módulo `shipping.py` (build fornecida `T08-B1.0`), destinada ao cálculo tarifário de expedição de encomendas em gramas com base em 8 regras de negócio normativas (**BR-01 a BR-08**).

A metodologia assentou na derivação rigorosa de um **oráculo independente** ancorado estritamente na especificação legal, no desenho manual prévio de **16 casos de teste humanos** (`H-01` a `H-16`) congelados no CP02 antes de qualquer inspeção da ferramenta de IA, e na subsequente avaliação crítica no CP03 de **12 casos candidatos gerados por IA** (`AI-01` a `AI-12`). Dessa análise resultaram 2 candidatos aceites (`AI-11` → `F-17`, `AI-12` → `F-18`), 1 revisto com correção de oráculo (`AI-09` → `F-19`) e 9 rejeitados por redundância ou erro concetual da IA. A suite final combinada, composta por **21 casos de teste** (acrescida de `F-20` e `F-21` para garantia integral de cobertura normativa), foi executada sobre os interpretadores **Python 3.9.6** (baseline) e **Python 3.12.7** (requisito formal de conformidade), obtendo-se paridade estrita: **13 PASS / 8 FAIL**.

Os 8 resultados FAIL não representam falhas do processo de verificação, mas sim a capacidade analítica da suite para isolar com precisão quatro defeitos de raiz na implementação (`DEF-01` a `DEF-04`). Adicionalmente, a regra de independência e ausência de efeitos secundários (**BR-05**) foi formalmente demonstrada através de procedimento computacional dedicado nas quatro dimensões exigidas (determinismo, estado residual, mutação de memória e isolamento delimitado de I/O, ambiente e ficheiros diretos da aplicação).

---

# PARTE I – ENQUADRAMENTO GERAL

## 1. Identificação e Organização do Grupo

| Elemento | Papel Principal | Responsabilidades Chave |
|---|---|---|
| **Eduardo Dias** | Test Lead & Architect | Revisão estática BR-01–BR-08, modelação do oráculo independente, definição de partições/fronteiras, desenho de casos humanos, consolidação do CP01 e CP02. |
| **Rui Carneiro** | Quality Engineer & Auditor | Revisão dos cálculos do oráculo, auditoria de código, desenvolvimento e validação do script de efeitos secundários BR-05, automação e gestão de repositório. |
| **Érica Moreira** | AI Test Specialist | Análise comparativa e classificação crítica dos candidatos IA (`ai_candidates.json`), derivação de correções de oráculo para casos revistos no CP03. |
| **Beatriz Barbosa** | Coverage & Metrics Analyst | Matriz de rastreabilidade de requisitos (BR-01–BR-08), auditoria e verificação do workbook oficial (`TestResults_T08_Template.xlsx`), análise de riscos residuais. |

*Nota de salvaguarda de integridade:* Em estrito cumprimento das diretrizes de auditoria, os números de estudante individuais são preenchidos diretamente no formulário de submissão do Moodle/e-Learning.

## 2. Objetivos e Âmbito

### Objetivos do Projeto:
1. Avaliar criticamente o contributo e as limitações do desenho de testes assistido por Inteligência Artificial face à engenharia de testes humana independente.
2. Derivar um oráculo de teste formal baseado unicamente nas regras de negócio da especificação, tratando o código como *black-box* e oráculo falível.
3. Assegurar rastreabilidade bidirecional total entre requisitos, casos de teste, execuções, defeitos e métricas de cobertura.
4. Preservar o histórico real de execução sem manipular artificialmente os resultados para inflacionar a taxa de PASS.

### Âmbito do Sistema em Teste:
- **Componente:** Módulo `shipping.py` / Função `quote(weight, zone, express)`.
- **Inputs:**
  - `weight`: peso em gramas inteiras (tipo `int`, intervalo nominal `[1, 20000]`).
  - `zone`: zona de entrega em string (`"LOCAL"` ou `"REMOTE"`).
  - `express`: booleano (`True` ou `False`).
- **Outputs:** Dicionário com chaves `"status"` (`"OK"`, `"INVALID"`, `"UNAVAILABLE"`) e `"fee"` (`int` ou `None`).

## 3. Estratégia e Prioridades

A estratégia de testes seguiu a norma de boas práticas de teste de software:
1. **Prioridade Máxima:** Condições de fronteira de disponibilidade (BR-04) e validação de tipos e integridade de fronteiras (BR-01).
2. **Prioridade Média:** Combinações tarifárias nominais e sobretaxas acumuladas (BR-02, BR-03).
3. **Prioridade Baixa:** Variações nominais dentro de classes de equivalência já cobertas.
4. **Isolamento de Efeitos Secundários:** Demonstração empírica da ausência de estado persistente e garantia de repetibilidade (BR-05).

## 4. Riscos e Mitigações

| ID | Risco Identificado | Prob. | Impacto | Estratégia de Mitigação |
|---|---|---|---|---|
| **R1** | Limiar de indisponibilidade implementado incorretamente | Alta | Alto | Desenho de pares de fronteira estrita em torno de 5000g (`H-13` a 5000g e `H-14` a 5001g). |
| **R2** | Coerção implícita de tipos booleanos em inteiros em Python | Média | Médio | Caso específico `H-15` com `weight=True` e `F-20` com `express=1`. |
| **R3** | Divergência de versão de interpretador Python (requisito 3.10+ vs 3.9.6) | Confirmado | Médio | Execução dual e gravação de evidências separadas em Python 3.9.6 e Python 3.12.7. |
| **R4** | Contaminação do desenho humano por inspeção prematura da IA | Alta | Crítico | Congelamento formal no Git da suite humana antes da abertura de `ai_candidates.json`. |
| **R5** | Oráculo erróneo gerado pela IA por alinhamento com a implementação | Alta | Alto | Derivação estrita do oráculo antes da avaliação das sugestões da IA. |

## 5. Plano de Trabalho

- **CP01 (27 Out 2026):** Project Charter, especificação de ambiente, análise estática inicial e execução do probe `H-ENV`.
- **CP02 (03 Nov 2026):** Modelação do oráculo independente, desenho e congelamento de 16 casos humanos (`H-01` a `H-16`) e deteção dos defeitos iniciais.
- **CP03 (10 Nov 2026):** Avaliação crítica dos 12 candidatos IA, construção da suite final de 21 casos, demonstração de BR-05 e auditoria integral do workbook Excel.
- **CP04 (17 Nov 2026):** Consolidação de evidências e preparação de análise de regressão.

---

# PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS

## 6. CP01 – Charter and Environment

No CP01 foi formalizado o compromisso de trabalho do grupo e configurado o ambiente operacional:
- **Sistema Operativo:** macOS (Apple Silicon).
- **Interpretadores:** Python 3.9.6 (interpretador de sistema) e Python 3.12.7 (interpretador de desenvolvimento conforme BR-06).
- **Folha de Cálculo:** Folha de cálculo compatível com a especificação internacional OpenXML (`.xlsx`).
- **Verificação de Baseline:** Execução nominal do caso starter fornecido pelo docente (`H-ENV`: `{"weight": 500, "zone": "LOCAL", "express": False}` devolvendo `{"status": "OK", "fee": 5}`), confirmando a integridade do runner `run_cases.py`.

---

## 7. CP02 – Independent Human Test Design

### 7.1. Revisão Estática, Modelo e Oráculo Inicial
O oráculo foi estabelecido com base nas regras normativas sem consultar o código:
- **BR-01 (Validação de Inputs):** O peso deve ser estritamente `int` (excluindo booleano por tipo), no intervalo inclusivo `[1, 20000]`. Zona deve ser `"LOCAL"` ou `"REMOTE"`. Expresso deve ser estritamente `bool`. Qualquer violação resulta em `{"status": "INVALID", "fee": None}`.
- **BR-02 (Tarifa Base):**
  - Tier 1: 1 a 1000 g → 5 €
  - Tier 2: 1001 a 5000 g → 8 €
  - Tier 3: 5001 a 20000 g → 12 €
- **BR-03 (Sobretaxas Acumuladas):** Destino `"REMOTE"` adiciona +4 € à taxa base; envio `"express"` adiciona +6 €.
- **BR-04 (Restrição de Disponibilidade):** Encomendas com `zone == "REMOTE"` e `express == True` com peso estritamente superior a 5000 g são indisponíveis: `{"status": "UNAVAILABLE", "fee": None}`. No limite exato de 5000 g, o serviço está disponível.
- **BR-05 (Precedência e Independência):** Validação tem precedência sobre disponibilidade, que tem precedência sobre cálculo tarifário.

### 7.2. Plano de Teste Humano (Frozen)
A suite humana foi desenhada aplicando Análise de Valores de Fronteira (BVA) e Partições de Equivalência (EP), totalizando **16 casos de teste** (`H-01` a `H-16`), congelados em `Trabalho_CP2/human_cases.json` no commit `54ec4d3` de 30 de outubro de 2026.

### 7.3. Resultados da Execução
A execução da suite congelada produziu **10 PASS e 6 FAIL**:

| TC-ID | Input (`weight`, `zone`, `express`) | Expected | Actual | Veredicto | Defeito Detetado |
|---|---|---|---|:---:|:---:|
| **H-01** | `500, "LOCAL", False` | `OK, 5` | `OK, 5` | **PASS** | — |
| **H-02** | `1, "LOCAL", False` | `OK, 5` | `OK, 5` | **PASS** | — |
| **H-03** | `1000, "LOCAL", False` | `OK, 5` | `OK, 8` | **FAIL** | **DEF-02** |
| **H-04** | `1001, "LOCAL", False` | `OK, 8` | `OK, 8` | **PASS** | — |
| **H-05** | `5000, "LOCAL", False` | `OK, 8` | `OK, 8` | **PASS** | — |
| **H-06** | `5001, "LOCAL", False` | `OK, 12` | `OK, 12` | **PASS** | — |
| **H-07** | `20000, "LOCAL", False` | `OK, 12` | `INVALID, null` | **FAIL** | **DEF-01** |
| **H-08** | `0, "LOCAL", False` | `INVALID, null` | `INVALID, null` | **PASS** | — |
| **H-09** | `20001, "LOCAL", False` | `INVALID, null` | `INVALID, null` | **PASS** | — |
| **H-10** | `500, "REMOTE", False` | `OK, 9` | `OK, 4` | **FAIL** | **DEF-03** |
| **H-11** | `500, "LOCAL", True` | `OK, 11` | `OK, 11` | **PASS** | — |
| **H-12** | `500, "REMOTE", True` | `OK, 15` | `OK, 10` | **FAIL** | **DEF-03** |
| **H-13** | `5000, "REMOTE", True` | `OK, 18` | `OK, 10` | **FAIL** | **DEF-03** |
| **H-14** | `5001, "REMOTE", True` | `UNAVAILABLE, null` | `OK, 10` | **FAIL** | **DEF-04** |
| **H-15** | `True, "LOCAL", False` | `INVALID, null` | `INVALID, null` | **PASS** | — |
| **H-16** | `500, "local", False` | `INVALID, null` | `INVALID, null` | **PASS** | — |

### 7.4. Discrepâncias Identificadas na Execução
A análise dos 6 casos com veredicto FAIL permitiu caracterizar univocamente os quatro defeitos originais da aplicação (`DEF-01` a `DEF-04`).  
*Clarificação fundamental de rastreabilidade:* O caso `H-13` testa o peso de 5000g, que é nominalmente permitido pela regra BR-04 (*"At exactly 5000 it is available"*). Logo, a expectativa de estado de `H-13` é `OK`. A falha em `H-13` decorre exclusivamente da substituição indevida da tarifa base na zona REMOTE (`DEF-03`), não detetando o defeito `DEF-04` (que se manifesta apenas a partir de 5001g, detetado por `H-14`).

### 7.5. Riscos e Prioridades
Identificou-se a necessidade de clarificar autonomamente as questões de tipo em `weight` e `express` (AMB-01 e AMB-02) e de garantir a execução da suite sob Python 3.10+ no CP03.

---

## 8. CP03 – AI-Assisted Test Design and Final Test Suite

### 8.1. Revisão e Seleção dos Candidatos Gerados por IA
Após o congelamento comprovado da suite humana, o grupo procedeu à abertura e auditoria crítica do ficheiro `TVSI_T08_Students_B1.0/app/ai_candidates.json` (12 sugestões):

| ID IA | Inputs Propostos | Oráculo IA | Oráculo Independente | Decisão | Fundamentação Técnica |
|---|---|---|---|:---:|---|
| **AI-01** | `500, "LOCAL", False` | `OK, 5` | `OK, 5` | **Reject** | Duplicado exato de `H-01`. |
| **AI-02** | `2500, "LOCAL", False` | `OK, 8` | `OK, 8` | **Reject** | Ponto interior redundante com `H-04` e `H-05`. |
| **AI-03** | `10000, "LOCAL", False`| `OK, 12` | `OK, 12` | **Reject** | Ponto interior redundante com `H-06` e `H-07`. |
| **AI-04** | `500, "LOCAL", True` | `OK, 11` | `OK, 11` | **Reject** | Duplicado exato de `H-11`. |
| **AI-05** | `500, "REMOTE", False` | `OK, 4` | `OK, 9` | **Reject** | **Erro da IA:** Gerou a expectativa com base no bug de código (`fee=4`), omitindo a tarifa base (5+4=9). |
| **AI-06** | `1000, "LOCAL", False` | `OK, 8` | `OK, 5` | **Reject** | **Erro da IA:** Alinhou a expectativa com o bug de código do tier 2 a 1000g. |
| **AI-07** | `0, "LOCAL", False` | `INVALID, null` | `INVALID, null` | **Reject** | Duplicado exato de `H-08`. |
| **AI-08** | `25000, "LOCAL", False`| `INVALID, null` | `INVALID, null` | **Reject** | Ponto exterior redundante com `H-09`. |
| **AI-09** | `6000, "REMOTE", True` | `OK, 22` | `UNAVAILABLE, null`| **Revise** | **Erro grave da IA:** Ignorou a regra de indisponibilidade BR-04. Caso revisto e aproveitado como `F-19`. |
| **AI-10** | `500, "LOCAL", False` | `OK, 5` | `OK, 5` | **Reject** | Triplicado de `H-01` e `AI-01`. |
| **AI-11** | `10000, "LOCAL", True` | `OK, 18` | `OK, 18` | **Accept** | Cobre lacuna: Tier 3 expresso para zona LOCAL (12+6=18). Integrado como `F-17`. |
| **AI-12** | `2000, "REMOTE", False`| `OK, 12` | `OK, 12` | **Accept** | Cobre lacuna: Tier 2 padrão para REMOTE (8+4=12). Integrado como `F-18`. |

*Conclusão da revisão de IA:* 3 dos 12 candidatos gerados por IA continham erros conceituais graves, demonstrando empiricamente o risco da dependência cega em modelos generativos sem um oráculo independente.

### 8.2. Construção da Suite Final
A suite final consolidou **21 casos de teste** (`final_cases.json`):
- 16 casos humanos preservados intactos (`H-01` a `H-16`).
- 2 casos IA aceites (`F-17` e `F-18`).
- 1 caso IA revisto com oráculo corrigido (`F-19`).
- 2 casos novos para fecho integral de requisitos:
  - `F-20` (`weight=500, zone="LOCAL", express=1`): validação estrita do tipo de `express` contra inteiros (`BR-01`).
  - `F-21` (`weight=25000, zone="REMOTE", express=True`): precedência absoluta da validação sobre disponibilidade (`BR-05`).

### 8.3. Execução e Análise dos Resultados
A suite final foi executada sobre os interpretadores **Python 3.9.6** e **Python 3.12.7** com o runner oficial:
- **Resultado:** **13 PASS / 8 FAIL** (exit code 1).
- **Paridade entre versões:** 100% estrita e reprodutível.
- **Distribuição dos 8 FAILs:**
  - `H-03`: `DEF-02`
  - `H-07`: `DEF-01`
  - `H-10`: `DEF-03`
  - `H-12`: `DEF-03`
  - `H-13`: `DEF-03`
  - `H-14`: `DEF-04`
  - `F-18`: `DEF-03`
  - `F-19`: `DEF-04`

### 8.4. Cobertura e Verificação dos Requisitos
A matriz de cobertura cobre 100% dos requisitos BR-01 a BR-08:
- **BR-01:** 10 casos (tipos, limites numéricos de peso, zonas válidas e invalidas).
- **BR-02:** 14 casos (todas as fronteiras e classes de peso dos três tiers).
- **BR-03:** 7 casos (combinações de sobretaxa REMOTE e express).
- **BR-04:** 3 casos (`H-13` no limiar disponível, `H-14` na fronteira indisponível e `F-19` no ponto interior indisponível).
- **BR-05:** 2 casos na suite combinada (`F-21` para precedência e `H-01` para ausência de taxa parcial) complementados pelo procedimento formal `verify_br05_independence.py`.
- **BR-06:** 7 casos executados sob Python 3.12.7 e 3.9.6.
- **BR-07:** 5 casos documentando inputs, outputs e mensagens de erro sem omissões.
- **BR-08:** 3 casos derivados exclusivamente do oráculo independente.

### 8.5. Demonstração de BR-05 (Independência e Efeitos Secundários)
O procedimento dedicado [`verify_br05_independence.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/verify_br05_independence.py) confirmou o cumprimento integral de BR-05 através de 4 testes em memória e ambiente:
1. `BR05-DET-01` (Determinismo): 10 execuções idênticas consecutivas com resultado imutável (**PASS**).
2. `BR05-RES-02` (Estado residual): 9 chamadas sequenciais alternando válido, inválido e indisponível sem contaminação (**PASS**).
3. `BR05-MUT-03` (Mutações observáveis): imutabilidade dos dicionários de entrada, isolamento de memória de instâncias devolvidas e integridade do namespace global (**PASS**).
4. `BR05-EXT-04` (Efeitos externos delimitados): ausência de emissão em `stdout`/`stderr`, variáveis de ambiente inalteradas e ausência de alterações observáveis nos ficheiros diretamente existentes em `TVSI_T08_Students_B1.0/app/` (**PASS**).

### 8.6. Conclusões do CP03
O CP03 permitiu comprovar que a IA acrescenta valor na identificação de lacunas de combinação (como demonstrado pelos casos aceites `F-17` e `F-18`), mas falha frequentemente na interpretação de restrições de fronteira e regras de exceção, exigindo sempre validação rigorosa por um oráculo humano.

---

# PARTE III – CONCLUSÕES FINAIS

## 9. Conclusões Gerais e Trabalho Futuro

1. **Eficácia da Suite de Testes:** A suite de 21 casos concebida demonstrou 100% de capacidade para isolar e documentar os defeitos da aplicação, alcançando cobertura exaustiva de todas as regras normativas.
2. **Qualidade do Software em Teste (Build T08-B1.0):** Foram isolados 4 defeitos distintos de código que violam as regras BR-01, BR-02, BR-03 e BR-04. A implementação apresenta deficiências estruturais na atribuição de taxas acumuladas e off-by-one em fronteiras críticas.
3. **Trabalho Futuro (CP04 em diante):** Re-execução da suite caso seja disponibilizada uma nova build corrigida (`T08-B1.1`), análise de robustez e estabilização para o relatório final de submissão.

## 10. Declaração de Utilização de IA

Em conformidade com a política académica da Universidade do Minho e a regra BR-08:
- **Geração de Candidatos:** O ficheiro `ai_candidates.json` fornecido no pacote docente foi gerado pelo modelo GPT-6/Codex com curadoria pedagógica.
- **Revisão e Classificação de Candidatos:** Assistida por Claude Sonnet 4.6, aplicando como oráculo estrito as regras BR-01 a BR-08.
- **Construção da Suite e Scripts:** Scripts auxiliares de auditoria e validação de efeitos secundários desenvolvidos com apoio de ferramentas LLM e validados linha a linha pelos engenheiros de teste humanos.
- **Validação Humana:** Todas as asserções, inputs, saídas esperadas e classificações de defeitos foram verificadas e auditadas manualmente pela equipa.

---

## 11. Anexos e Tabelas Consolidadas

### Tabela Consolidada de Defeitos (DEF-01 a DEF-04)

| Defeito | BR | Linha em `shipping.py` | Causa Raiz | Impacto Real | Casos Detetores |
|---|:---:|:---:|---|---|---|
| **DEF-01** | BR-01 | Linha 3 | `weight >= 20000` em vez de `> 20000` | Rejeição indevida do peso máximo legal permitido (20000g) como `INVALID` em vez de aceitar como Tier 3 (12€). | **`H-07`** |
| **DEF-02** | BR-02 | Linha 7 | `weight < 1000` em vez de `<= 1000` | Sobrecobrança indevida a 1000g (taxado a 8€ de Tier 2 em vez de 5€ de Tier 1). | **`H-03`** |
| **DEF-03** | BR-03 | Linha 14 | `fee = 4` em vez de `fee += 4` | Sobrescrita da tarifa base em destinos REMOTE: encomenda cobrada a 4€ (ou 10€ com expresso), perdendo a tarifa base calculada. | **`H-10, H-12, H-13, F-18`** |
| **DEF-04** | BR-04 | Linha 5 | `weight > 10000` em vez de `> 5000` | Falha na rejeição de indisponibilidade de express para REMOTE entre 5001g e 10000g, devolvendo tarifa `OK` em vez de `UNAVAILABLE`. | **`H-14, F-19`** |

*Nota explicativa de isolamento:*  
- O caso `H-13` (`weight=5000, zone="REMOTE", express=True`) situa-se no limite em que o serviço expresso para REMOTE é **disponível** segundo a especificação legal. Por conseguinte, `H-13` falha unicamente devido ao cálculo incorreto de taxa em `DEF-03` (recebe 10€ em vez de 18€).
- O caso `H-14` (`weight=5001, zone="REMOTE", express=True`) situa-se na fronteira de **indisponibilidade**, revelando `DEF-04` ao ser incorretamente aceite como `OK`.
- O caso `F-19` (`weight=6000, zone="REMOTE", express=True`) confirma e alarga `DEF-04` no interior da classe de indisponibilidade.

