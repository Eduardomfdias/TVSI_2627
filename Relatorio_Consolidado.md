# Tecnologias e Verificação de Sistemas de Informação 2026/27
## T08 — Desenho de Testes com Assistência de IA
### Relatório Técnico Consolidado de Testes e Auditoria (CP01, CP02 e CP03)

**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação (TVSI 2026/27)  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5  
**Autores:**  
- Eduardo Dias  
- Rui Carneiro  
- Érica Moreira  
- Beatriz Barbosa  
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

# Índice Geral

- [Resumo Executivo](#resumo-executivo)
- [PARTE I – ENQUADRAMENTO GERAL](#parte-i--enquadramento-geral)
  - [1. Identificação e Organização do Grupo](#1-identificação-e-organização-do-grupo)
  - [2. Objetivos e Âmbito do Projeto](#2-objetivos-e-âmbito-do-projeto)
  - [3. Sistema em Teste e Ambiente de Teste](#3-sistema-em-teste-e-ambiente-de-teste)
  - [4. Regras de Negócio e Critérios de Aceitação (BR-01 a BR-08)](#4-regras-de-negócio-e-critérios-de-aceitação-br-01-a-br-08)
  - [5. Estratégia e Plano de Testes](#5-estratégia-e-plano-de-testes)
  - [6. Riscos, Prioridades e Critérios de Conclusão](#6-riscos-prioridades-e-critérios-de-conclusão)
- [PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS](#parte-ii--desenvolvimento-dos-checkpoints)
  - [7. CP01 — Charter and Environment](#7-cp01--charter-and-environment)
  - [8. CP02 — Static Review, Test Model and Oracle](#8-cp02--static-review-test-model-and-oracle)
    - [8.1. Revisão Estática e Ambiguidades](#81-revisão-estática-e-ambiguidades)
    - [8.2. Modelo de Teste e Oráculo Independente](#82-modelo-de-teste-e-oráculo-independente)
    - [8.3. Desenho e Congelamento da Suite Humana](#83-desenho-e-congelamento-da-suite-humana)
    - [8.4. Execução e Identificação de Defeitos](#84-execução-e-identificação-de-defeitos)
    - [8.5. Conclusões do CP02](#85-conclusões-do-cp02)
  - [9. CP03 — AI-Assisted Test Design and Final Validation](#9-cp03--ai-assisted-test-design-and-final-validation)
    - [9.1. Proveniência e Auditoria dos Candidatos IA](#91-proveniência-e-auditoria-dos-candidatos-ia)
    - [9.2. Construção da Suite Final (21 Casos)](#92-construção-da-suite-final-21-casos)
    - [9.3. Execução Dual Python (3.9.6 e 3.12.7)](#93-execução-dual-python-396-e-3127)
    - [9.4. Rastreabilidade Rigorosa de Defeitos](#94-rastreabilidade-rigorosa-de-defeitos)
    - [9.5. Matriz de Cobertura de Requisitos](#95-matriz-de-cobertura-de-requisitos)
    - [9.6. Demonstração Formal de BR-05](#96-demonstração-formal-de-br-05)
    - [9.7. Avaliação Crítica da Utilização de IA](#97-avaliação-crítica-da-utilização-de-ia)
- [PARTE III – CONCLUSÃO E ENTREGA](#parte-iii--conclusão-e-entrega)
  - [10. Conclusões Gerais e Trabalho Futuro](#10-conclusões-gerais-e-trabalho-futuro)
  - [11. Declaração Formal de Utilização de IA](#11-declaração-formal-de-utilização-de-ia)
  - [12. Anexos e Tabelas Consolidadas](#12-anexos-e-tabelas-consolidadas)

---

# PARTE I – ENQUADRAMENTO GERAL

## 1. Identificação e Organização do Grupo

O Grupo 5 é constituído por quatro estudantes do Mestrado em Engenharia Informática da Universidade do Minho:

| Elemento | Papel Principal | Responsabilidades Chave |
|---|---|---|
| **Eduardo Dias** | Test Lead & Architect | Revisão estática BR-01–BR-08, modelação do oráculo independente, definição de partições/fronteiras, desenho de casos humanos, consolidação do CP01 e CP02. |
| **Rui Carneiro** | Quality Engineer & Auditor | Revisão dos cálculos do oráculo, auditoria de código, desenvolvimento e validação do script de efeitos secundários BR-05, automação e gestão de repositório Git. |
| **Érica Moreira** | AI Test Specialist | Análise comparativa e classificação crítica dos candidatos IA (`ai_candidates.json`), derivação de correções de oráculo para casos revistos no CP03. |
| **Beatriz Barbosa** | Coverage & Metrics Analyst | Matriz de rastreabilidade de requisitos (BR-01–BR-08), auditoria e verificação do workbook oficial (`TestResults_T08_Template.xlsx`), análise de riscos residuais. |

*Nota de salvaguarda de integridade:* Em estrito cumprimento das diretrizes de auditoria (não fabricação de dados), os números de estudante individuais são preenchidos diretamente pelos alunos no formulário de submissão do Moodle/e-Learning.

## 2. Objetivos e Âmbito do Projeto

### Objetivos Principais:
1. **Avaliação Crítica de IA:** Avaliar o contributo e as falhas do desenho de testes gerado por modelos de inteligência artificial em comparação direta com a engenharia de testes humana independente.
2. **Oráculo Independente:** Estabelecer uma especificação formal de resultados esperados antes da inspeção do código da aplicação ou das sugestões da IA, tratando a implementação como caixa-negra falível.
3. **Rastreabilidade Bidirecional Exaustiva:** Garantir mapeamento sem falhas entre regras normativas, casos de teste, registos de execução, defeitos de software e matrizes de cobertura.
4. **Verificação de Não-Contaminação e Independência:** Demonstrar computacionalmente a ausência de estado residual e efeitos secundários entre invocações repetidas (regra BR-05).

### Âmbito do Sistema em Teste:
- **Objeto sob Teste:** Módulo `shipping.py` / Função `quote(weight, zone, express)`.
- **Entradas:**
  - `weight`: peso em gramas inteiras (tipo `int`, intervalo nominal `[1, 20000]`).
  - `zone`: zona geográfica de entrega (string `"LOCAL"` ou `"REMOTE"`).
  - `express`: modalidade de envio expresso (booleano `True` ou `False`).
- **Saídas:** Estrutura de dicionário com chaves `"status"` (`"OK"`, `"INVALID"`, `"UNAVAILABLE"`) e `"fee"` (`int` ou `None`).

## 3. Sistema em Teste e Ambiente de Teste

A execução e validação do sistema foram conduzidas sob as seguintes especificações de ambiente:
- **Hardware / Sistema Operativo:** macOS (Apple Silicon).
- **Interpretador de Sistema (Baseline):** Python 3.9.6 (`/usr/bin/python3`).
- **Interpretador de Conformidade (Requisito BR-06):** Python 3.12.7 (`/usr/local/bin/python3`).
- **Ferramentas de Execução:** Script oficial `run_cases.py` (fornecido na baseline docente, não modificado).
- **Folha de Cálculo Oficial:** Ficheiro em formato standard OpenXML (`.xlsx`), compatível com Microsoft Excel e LibreOffice Calc.

## 4. Regras de Negócio e Critérios de Aceitação (BR-01 a BR-08)

O comportamento do sistema é regido estritamente pelo documento normativo `BusinessRules.md` (v1.0):

1. **BR-01 (Validação de Inputs):** O peso deve ser um inteiro válido entre 1 g e 20000 g (inclusive), excluindo tipos booleanos. A zona deve ser exatamente `"LOCAL"` ou `"REMOTE"`. A opção express deve ser um booleano estrito. Se qualquer entrada for inválida, a função deve retornar `{"status": "INVALID", "fee": None}`.
2. **BR-02 (Tarifa Base):**
   - Tier 1: 1 g a 1000 g inclusive → 5 €
   - Tier 2: 1001 g a 5000 g inclusive → 8 €
   - Tier 3: 5001 g a 20000 g inclusive → 12 €
3. **BR-03 (Sobretaxas Acumuladas):**
   - Sobretaxa de zona: `"REMOTE"` adiciona +4 € à taxa base.
   - Sobretaxa de serviço: `"express"` adiciona +6 € à taxa base.
   - Ambas as sobretaxas acumulam quando aplicáveis em simultâneo.
4. **BR-04 (Restrição de Disponibilidade):**
   - Envio expresso para zona `"REMOTE"` é **indisponível** para encomendas com peso estritamente superior a 5000 g (`weight > 5000`), devendo retornar `{"status": "UNAVAILABLE", "fee": None}`.
   - No limite exato de 5000 g, o serviço está disponível (*"At exactly 5000 it is available"*).
5. **BR-05 (Precedência e Independência):**
   - A validação de entradas tem precedência sobre disponibilidade, que por sua vez tem precedência sobre o cálculo tarifário.
   - Nenhum valor de tarifa é calculado em situações `INVALID` ou `UNAVAILABLE`.
   - Chamadas repetidas são independentes e não produzem efeitos secundários.
6. **BR-06 (Ambiente Python):** O código deve ser executável em ambiente Python 3.10 ou superior.
7. **BR-07 (Completude de Saída):** A resposta deve conter sempre os campos `status` e `fee`.
8. **BR-08 (Processo Metodológico):** Os resultados esperados devem ser derivados antes da inspeção dos candidatos de IA; os candidatos IA devem ser classificados criticamente em *accept*, *revise* ou *reject*.

## 5. Estratégia e Plano de Testes

A abordagem metodológica baseou-se em:
- **Técnicas Caixa-Negra:** Partições de Equivalência (EP) e Análise de Valores de Fronteira (BVA) aplicadas a todos os domínios de entrada.
- **Isolamento de Fases:** Congelamento obrigatório da suite de testes humana no CP02 antes de aceder aos candidatos gerados por IA.
- **Oráculo Independente:** Determinação manual de cada valor esperado a partir das BRs, tratando divergências como defeitos da implementação.
- **Priorização de Riscos:** Foco prioritário nas fronteiras de disponibilidade (5000g vs 5001g) e validação de tipos booleanos.

## 6. Riscos, Prioridades e Critérios de Conclusão

| ID | Risco Identificado | Severidade | Ação Preventiva / Mitigação |
|---|---|:---:|---|
| **R1** | Erro de limiar de disponibilidade (>10000 em vez de >5000) | Alta | Desenho dos casos `H-13` (5000g) e `H-14` (5001g) para isolar a fronteira exata. |
| **R2** | Coerção implícita de tipos (True avaliado como 1) | Média | Casos específicos `H-15` (`weight=True`) e `F-20` (`express=1`). |
| **R3** | Divergência ambiental de Python (3.9 vs 3.10+) | Média | Validação dual e gravação de evidências separadas em Python 3.9.6 e Python 3.12.7. |
| **R4** | Contaminação do desenho humano por sugestões de IA | Crítica | Congelamento no commit Git `54ec4d3` antes da abertura de `ai_candidates.json`. |
| **R5** | Oráculo erróneo na suite de IA | Alta | Auditoria manual de todos os 12 candidatos de IA face ao oráculo independente. |

*Critérios de Conclusão:* 100% dos requisitos cobertos, paridade de resultados entre versões Python comprovada, defeitos caracterizados com evidência reproduzível e ausência de efeitos secundários demonstrada.

---

# PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS

## 7. CP01 — Charter and Environment

O Checkpoint 1 (concluído a 22 de outubro de 2026) estabeleceu as fundações do projeto:
- **Project Charter:** Definição formal de objetivos, membros, papéis e riscos do grupo.
- **Verificação de Ambiente:** Teste com sucesso do runner oficial `run_cases.py` através do caso starter `H-ENV` (`weight=500, zone="LOCAL", express=False → {"status": "OK", "fee": 5}`), confirmando a operacionalidade do ambiente.
- **Revisão Estática Preliminar:** Registo das questões de clarificação inicial sobre interpretação de tipos em Python e limites inclusivos de fronteira.

---

## 8. CP02 — Static Review, Test Model and Oracle

### 8.1. Revisão Estática e Ambiguidades
Durante o CP02, o grupo identificou quatro ambiguidades potenciais na especificação:
- **AMB-01 (Booleano em weight):** Em Python, `bool` herda de `int` (`isinstance(True, int) == True`). A regra BR-01 exige "excluding booleans". O grupo adotou a interpretação estrita por tipo: `isinstance(w, bool)` deve resultar em `INVALID`.
- **AMB-02 (Inteiro em express):** A regra BR-01 exige "actual boolean". O grupo estabeleceu que valores numéricos como `1` ou `0` não devem ser aceites por coerção implícita.
- **AMB-03 (Limiar de indisponibilidade):** A regra BR-04 explicita *"above 5000 g"*, confirmando que o limite é exclusivo (`> 5000`). A 5000 g o serviço está disponível.
- **AMB-04 (Inputs nulos ou strings em peso):** Devem resultar invariavelmente em `INVALID, fee=None`.

### 8.2. Modelo de Teste e Oráculo Independente
O oráculo derivou as classes de equivalência e valores de fronteira para cada variável:
- `weight`: Inválidos negativos (≤0), Tier 1 ([1, 1000]), Tier 2 ([1001, 5000]), Tier 3 ([5001, 20000]), Inválidos excessivos (>20000).
- `zone`: Válidas (`"LOCAL"`, `"REMOTE"`), Inválidas (minúsculas, outras strings, tipos inválidos).
- `express`: Válidos (`True`, `False`), Inválidos (inteiros, strings, None).

### 8.3. Desenho e Congelamento da Suite Humana
Foram concebidos **16 casos de teste humanos** (`H-01` a `H-16`), cobrindo valores nominais, limites de classe e entradas inválidas.  
A suite foi formalmente congelada em `Trabalho_CP2/human_cases.json` no commit `54ec4d3` em 30 de outubro de 2026.

### 8.4. Execução e Identificação de Defeitos
A execução de `Trabalho_CP2/human_cases.json` produziu **10 PASS e 6 FAIL**:

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

### 8.5. Conclusões do CP02
O CP02 isolou com precisão os quatro defeitos originais da aplicação (`DEF-01` a `DEF-04`), confirmando a total eficácia do desenho humano independente.

---

## 9. CP03 — AI-Assisted Test Design and Final Validation

### 9.1. Proveniência e Auditoria dos Candidatos IA
No CP03, após verificação do congelamento no Git, abriu-se o ficheiro `TVSI_T08_Students_B1.0/app/ai_candidates.json` (12 sugestões de teste):

| ID IA | Inputs Propostos | Oráculo IA | Oráculo Independente | Decisão | Fundamentação Técnica |
|---|---|---|---|:---:|---|
| **AI-01** | `500, "LOCAL", False` | `OK, 5` | `OK, 5` | **Reject** | Duplicado exato de `H-01`. |
| **AI-02** | `2500, "LOCAL", False` | `OK, 8` | `OK, 8` | **Reject** | Ponto interior redundante com `H-04` e `H-05`. |
| **AI-03** | `10000, "LOCAL", False`| `OK, 12` | `OK, 12` | **Reject** | Ponto interior redundante com `H-06` e `H-07`. |
| **AI-04** | `500, "LOCAL", True` | `OK, 11` | `OK, 11` | **Reject** | Duplicado exato de `H-11`. |
| **AI-05** | `500, "REMOTE", False` | `OK, 4` | `OK, 9` | **Reject** | **Erro grave da IA:** Expectativa alinhada com o código bugado (`fee=4`), omitindo a taxa base. |
| **AI-06** | `1000, "LOCAL", False` | `OK, 8` | `OK, 5` | **Reject** | **Erro da IA:** Confundiu Tier 1 com Tier 2 a 1000g, alinhando com o bug de código. |
| **AI-07** | `0, "LOCAL", False` | `INVALID, null` | `INVALID, null` | **Reject** | Duplicado exato de `H-08`. |
| **AI-08** | `25000, "LOCAL", False`| `INVALID, null` | `INVALID, null` | **Reject** | Ponto exterior redundante com `H-09`. |
| **AI-09** | `6000, "REMOTE", True` | `OK, 22` | `UNAVAILABLE, null`| **Revise** | **Erro crítico da IA:** Ignorou a regra de indisponibilidade BR-04. Corrigido para `F-19`. |
| **AI-10** | `500, "LOCAL", False` | `OK, 5` | `OK, 5` | **Reject** | Triplicado de `H-01` e `AI-01`. |
| **AI-11** | `10000, "LOCAL", True` | `OK, 18` | `OK, 18` | **Accept** | Cobre lacuna: Tier 3 com expresso para LOCAL (12+6=18). Integrado como `F-17`. |
| **AI-12** | `2000, "REMOTE", False`| `OK, 12` | `OK, 12` | **Accept** | Cobre lacuna: Tier 2 padrão para REMOTE (8+4=12). Integrado como `F-18`. |

### 9.2. Construção da Suite Final (21 Casos)
A suite final (`final_cases.json`) integrou 21 casos:
- 16 casos humanos (`H-01` a `H-16`) preservados intactos.
- 2 casos IA aceites (`F-17` e `F-18`).
- 1 caso IA revisto com oráculo corrigido (`F-19`).
- 2 casos novos para fecho de requisitos: `F-20` (tipo de `express`) e `F-21` (precedência de validação sobre disponibilidade).

### 9.3. Execução Dual Python (3.9.6 e 3.12.7)
A suite final foi executada com o runner oficial em ambos os interpretadores:
- **Python 3.9.6:** 13 PASS / 8 FAIL (`Trabalho_CP3/final_cases.results.json`).
- **Python 3.12.7:** 13 PASS / 8 FAIL (`Trabalho_CP3/final_cases.results.py312.json`).
- **Paridade de Resultados:** 100% estrita entre interpretadores.

### 9.4. Rastreabilidade Rigorosa de Defeitos
Os 8 FAILs da suite final correspondem estritamente aos quatro defeitos conhecidos:
- `DEF-01`: `H-07`
- `DEF-02`: `H-03`
- `DEF-03`: `H-10, H-12, H-13, F-18`
- `DEF-04`: `H-14, F-19`

*Nota explicativa de isolamento:*  
O caso `H-13` (`weight=5000, zone="REMOTE", express=True`) situa-se no limite em que o serviço expresso para REMOTE é **disponível** segundo a especificação legal (BR-04). Por conseguinte, `H-13` falha unicamente devido ao cálculo incorreto de taxa em `DEF-03` (recebe 10€ em vez de 18€), não detetando `DEF-04`. O defeito `DEF-04` é detetado na fronteira estritamente superior por `H-14` (`weight=5001`) e reiterado por `F-19` (`weight=6000`).

### 9.5. Matriz de Cobertura de Requisitos
A matriz de cobertura cobre 100% das regras normativas BR-01 a BR-08 (51 ligações de requisitos ativas na folha `Coverage` do workbook oficial, sem qualquer ligação quebrada ou pendente).

### 9.6. Demonstração Formal de BR-05
O procedimento dedicado [`verify_br05_independence.py`](file:///Users/rui.carneiro/Library/Mobile%20Documents/com~apple~CloudDocs/Desktop/Mestrado/TVSI/TVSI_2627/Trabalho_CP3/verify_br05_independence.py) confirmou o cumprimento de BR-05 através de 4 dimensões (com veredicto **PASS** em Python 3.9 e Python 3.12):
1. `BR05-DET-01` (Determinismo): 10 invocações consecutivas em memória com saídas rigorosamente idênticas.
2. `BR05-RES-02` (Estado residual): 9 chamadas sequenciais alternando válido, inválido e indisponível sem contaminação.
3. `BR05-MUT-03` (Mutações observáveis): imutabilidade de dicionários de entrada, isolamento de objetos devolvidos e integridade do namespace do módulo.
4. `BR05-EXT-04` (Efeitos externos delimitados): ausência de output em `stdout`/`stderr`, variáveis de ambiente inalteradas e ausência de alterações observáveis nos ficheiros diretamente existentes em `TVSI_T08_Students_B1.0/app/` (nome, tamanho e timestamp).

### 9.7. Avaliação Crítica da Utilização de IA
A experiência empírica do CP03 demonstrou que a IA é valiosa para identificar lacunas combinatórias de classes equivalentes (ex.: `AI-11` e `AI-12`), mas apresenta uma tendência perigosa para replicar os defeitos da implementação quando o oráculo não é derivado independentemente (ex.: `AI-05`, `AI-06`, `AI-09`), reiterando a imprescindibilidade da intervenção humana em engenharia de testes.

---

# PARTE III – CONCLUSÃO E ENTREGA

## 10. Conclusões Gerais e Trabalho Futuro

1. **Eficácia da Suite de Testes:** A suite de 21 casos concebida demonstrou 100% de capacidade para isolar e documentar os defeitos da aplicação, alcançando cobertura exaustiva de todas as regras normativas.
2. **Qualidade do Software em Teste (Build T08-B1.0):** Foram isolados 4 defeitos distintos de código que violam as regras BR-01, BR-02, BR-03 e BR-04. A implementação apresenta deficiências estruturais na atribuição de taxas acumuladas e off-by-one em fronteiras críticas.
3. **Trabalho Futuro (CP04 em diante):** Re-execução da suite caso seja disponibilizada uma nova build corrigida (`T08-B1.1`), análise de robustez e estabilização para o relatório final de submissão.

### 10.1. Estado dos Artefactos, Evidências e Limitações de Entrega

Para transparência e rigor metodológico absoluto, discrimina-se o estado exato de cada componente do projeto:

1. **Ficheiros Publicados no GitHub:**
   - O repositório remoto (`origin/main`) encontra-se estabilizado no commit `fa938fe`, contendo todo o histórico de desenvolvimento dos checkpoints CP01, CP02 e CP03, a baseline de software intocada, as suites de testes, os resultados históricos e as versões base da documentação.
2. **Ficheiros Existentes Apenas Localmente:**
   - Encontram-se no espaço de trabalho local os seguintes documentos de fecho: `Relatorio_Consolidado.md` (versão consolidada final), `Trabalho_CP3/audit_project.py` (script de auditoria de integridade com 29 verificações), `MANIFEST_ENTREGA.md` (manifesto de integridade criptográfica SHA-256) e `AUDITORIA_FINAL_ENTREGA.md` (relatório de auditoria técnica profunda). Estes artefactos encontram-se preparados e validados.
3. **ZIP Destinado à Submissão Académica:**
   - **Ficheiro:** `TVSI_T08_Grupo5_CP03.zip`
   - **Localização:** Raiz do repositório (`./TVSI_T08_Grupo5_CP03.zip`)
   - **Dimensão:** 110.027 bytes (28 ficheiros incluídos, sem diretórios temporários ou ficheiros do Git)
   - **Hash SHA-256:** `8e7527a5d013229c4e52dcb247181af090bad5abba1b491056d5cbcec46bc83c`
   - **Integridade:** Testado com `zipfile.testzip()`, apresentando 0 ficheiros corrompidos. O ficheiro encontra-se ignorado pelo Git (`.gitignore`) para prevenir a inclusão de binários no repositório.
4. **Evidências Efetivamente Verificadas por Execução Direta:**
   - **Sintaxe JSON:** 100% dos ficheiros JSON validados e em conformidade.
   - **Suites de Testes:** Suite humana (`human_cases.json`: 10 PASS / 6 FAIL) e suite final (`final_cases.json`: 13 PASS / 8 FAIL) executadas e validadas.
   - **Paridade Dual-Runtime:** Execução comprovada em Python 3.9.6 e Python 3.12.7, atestando paridade estrita de comportamento.
   - **Regra BR-05:** 4 propriedades de independência e ausência de efeitos secundários demonstradas com sucesso (`PASS`) em Python 3.9 e Python 3.12.
   - **Matriz de Defeitos:** DEF-01 a DEF-04 auditados e mapeados com rigor (H-13 associado exclusivamente a DEF-03, não deteta DEF-04).
   - **Recálculo de Fórmulas do Excel:** Todas as 324 fórmulas da folha `Coverage` foram recalculadas dinamicamente e validadas de forma independente, confirmando 0 discrepâncias e 0 erros `#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`, `#N/A`.
5. **Verificações Ainda Não Realizadas (Pendências Externas/Humanas):**
   - **Preenchimento de Números Mecanográficos:** A indicação dos identificadores numéricos de estudante no formulário eletrónico da plataforma e-Learning da UMinho cabe aos elementos do grupo.
   - **Submissão Formal:** O upload do pacote ZIP e o registo do link do repositório dependem de submissão manual no sistema académico.
   - **Envio Remoto Git (Push):** A sincronização final dos ficheiros locais para o GitHub depende da instrução final do utilizador.

## 11. Declaração Formal de Utilização de IA

Em conformidade com a política académica da Universidade do Minho e a regra BR-08:
- **Geração de Candidatos:** O ficheiro `ai_candidates.json` fornecido no pacote docente foi gerado pelo modelo GPT-6/Codex com curadoria pedagógica.
- **Revisão e Classificação de Candidatos:** Assistida por Claude Sonnet 4.6, aplicando como oráculo estrito as regras BR-01 a BR-08.
- **Construção da Suite e Scripts:** Scripts auxiliares de auditoria e validação de efeitos secundários desenvolvidos com apoio de ferramentas LLM e validados linha a linha pelos engenheiros de teste humanos.
- **Validação Humana:** Todas as asserções, inputs, saídas esperadas e classificações de defeitos foram verificadas e auditadas manualmente pela equipa.

---

## 12. Anexos e Tabelas Consolidadas

### Tabela Consolidada de Defeitos (DEF-01 a DEF-04)

| Defeito | BR | Linha em `shipping.py` | Causa Raiz | Impacto Real | Casos Detetores |
|---|:---:|:---:|---|---|---|
| **DEF-01** | BR-01 | Linha 3 | `weight >= 20000` em vez de `> 20000` | Rejeição indevida do peso máximo legal permitido (20000g) como `INVALID` em vez de aceitar como Tier 3 (12€). | **`H-07`** |
| **DEF-02** | BR-02 | Linha 7 | `weight < 1000` em vez de `<= 1000` | Sobrecobrança indevida a 1000g (taxado a 8€ de Tier 2 em vez de 5€ de Tier 1). | **`H-03`** |
| **DEF-03** | BR-03 | Linha 14 | `fee = 4` em vez de `fee += 4` | Sobrescrita da tarifa base em destinos REMOTE: encomenda cobrada a 4€ (ou 10€ com expresso), perdendo a tarifa base calculada. | **`H-10, H-12, H-13, F-18`** |
| **DEF-04** | BR-04 | Linha 5 | `weight > 10000` em vez de `> 5000` | Falha na rejeição de indisponibilidade de express para REMOTE entre 5001g e 10000g, devolvendo tarifa `OK` em vez de `UNAVAILABLE`. | **`H-14, F-19`** |
