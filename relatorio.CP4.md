TVSI 2026/27 · T08 · Desenho de Testes com Assistência de IA

UNIVERSIDADE DO MINHO · ESCOLA DE ENGENHARIA Tecnologias e Verificação de Sistemas de Informação 2026/27 T08 — Desenho de Testes com Assistência de IA · Build T08-B1.0

### CP04

AI-Assisted Test Design and Final Test Suite Relatório de Checkpoint 4 de 6

### Grupo

Eduardo Dias – pg61456 Rui Carneiro – pg63791 Erica Moreira – pg65641 Beatriz Barbosa – pg63744

**Tópico:** T08 - Desenho de Testes com Assistência de IA Build em teste: T08-B1.0

CP04 - Test execution, evidence and draft defects· Build T08-B1.0 · *Universidade do Minho, Escola de Engenharia*

# Resumo

O presente relatório cobre os quatro checkpoints (CP01 a CP04) do projeto T08 — Desenho de Testes com Assistência de Inteligência Artificial, desenvolvido no âmbito da unidade curricular TVSI 2026/27, na Universidade do Minho. O objetivo do projeto é comparar testes concebidos manualmente com testes assistidos por IA, avaliando a sua correção, cobertura e rastreabilidade face às regras de negócio definidas (BR-01 a BR-08). No CP01 - Charter and Environment, foram estabelecidos o âmbito, as responsabilidades do grupo, a estratégia de teste, os principais riscos e o plano de trabalho, tendo sido realizada uma revisão estática inicial dos requisitos. A verificação preliminar confirmou o resultado esperado para o caso H-ENV, mas identificou uma limitação crítica: o ambiente utiliza Python 3.9.6, abaixo da versão mínima exigida (3.10+). No CP02 - Independent Human Test Design, foi derivado o oráculo independente exclusivamente a partir das BR, foram analisadas cinco questões de interpretação (Q-01 a Q-05) e foi concebida e congelada uma suite humana com 16 casos de teste, cobrindo classes de equivalência válidas e inválidas e valores de fronteira. A execução produziu 10 PASS e 6 FAIL (62,5%), com quatro defeitos identificados (DEF-01 a DEF-04) relativos a validação de inputs, cálculo de tarifa, surcharge REMOTE e disponibilidade do serviço expresso. No CP03 - AI-Assisted Test Design and Final Test Suite, foram analisados os 12 candidatos gerados por IA, tendo sido aceites 2, revisto 1 (após correção do resultado esperado) e rejeitados 9. A análise identificou três erros nos resultados esperados propostos pela IA, evidenciando a necessidade de validação humana com recurso ao oráculo independente. Foi construída uma suite final de 21 casos de teste, integrando os 16 casos humanos congelados no CP02, três casos provenientes da revisão dos candidatos IA e dois casos adicionais para colmatar lacunas de cobertura. A execução registou 13 PASS e 8 FAIL (61,9%), confirmando os quatro defeitos anteriormente identificados, sem introdução de novos defeitos. Foi ainda assegurada a cobertura dos requisitos BR-01 a BR-08 e validada a independência entre chamadas e a ausência de efeitos secundários previstas na BR-05, com resultados consistentes em Python 3.9.6 e 3.12.7. No CP04 - Final Audit, Evidence Reconciliation and Delivery, foi realizada a auditoria final de todos os artefactos do projeto, com reconciliação de 68 execuções lógicas e 98 execuções físicas nos dois interpretadores Python (3.9.6 e

3.12.7), confirmando resultados idênticos em ambos os ambientes. A auditoria validou os quatro defeitos de implementação identificados nas fases anteriores (DEF-01 a DEF-04) e as três anomalias de qualidade nas expectativas geradas por IA (DATA-01 a DATA-03). A suite final combinada de 30 casos registou 20 PASS e 10 FAIL (taxa de conformidade de 66.7%), com cobertura integral dos requisitos BR-01 a BR-08. O livro de cálculo oficial (TestResults_T08_Template.xlsx) foi validado sem erros de fórmula, e o pacote de entrega final (TVSI_T08_Grupo5_CP04.zip, 51 ficheiros) foi verificado por hash SHA-256.

## Índice

**RESUMO.................................................................................................................................................. 2**

**ÍNDICE DE TABELAS ................................................................................................................................. 6**

**PARTE I – ENQUADRAMENTO GERAL ......................................................................................................... 7**

**1. IDENTIFICAÇÃO E ORGANIZAÇÃO DO GRUPO................................................................................. 7**
**2. OBJETIVOS E ÂMBITO ..................................................................................................................... 8**
**3. ESTRATÉGIA E PRIORIDADES.......................................................................................................... 9**
**4. RISCOS E MITIGAÇÕES................................................................................................................. 10**
**5. PLANO DE TRABALHO................................................................................................................... 11**
**PARTE II – DESENVOLVIMENTO DOS CHECKPOINTS................................................................................ 12**

**6. CP01 – CHARTER AND ENVIRONMENT........................................................................................... 12**
6.1. AMBIENTE E VERIFICAÇÃO INICIAL............................................................................................................. 12
*6.1.1. Caracterização do Ambiente..................................................................................................... 12*
*6.1.2. Verificação Preliminar............................................................................................................... 12*
*6.1.3. Estado e Ações Pendentes........................................................................................................ 13*
6.2. REVISÃO ESTÁTICA INICIAL...................................................................................................................... 13
**7. CP02 – INDEPENDENT HUMAN TEST DESIGN................................................................................. 15**
7.1. REVISÃO ESTÁTICA, MODELO E ORÁCULO INICIAL......................................................................................... 15
*7.1.1. Revisão Estática dos Requisitos (BR-01 a BR-08)........................................................................ 15*
*7.1.2. Questões Analisadas e Interpretações Adotadas........................................................................ 16*
*7.1.3. Oráculo Independente.............................................................................................................. 16*
7.2. PLANO DE TESTE HUMANO (FROZEN)...................................................................................................... 17
7.3. RESULTADOS DA EXECUÇÃO.................................................................................................................... 19
*7.3.1. Sumário................................................................................................................................... 20*
*7.3.2. Resultados detalhados............................................................................................................. 20*
7.4. DISCREPÂNCIAS IDENTIFICADAS NA EXECUÇÃO (T08-B1.0) ........................................................................... 21
*7.4.1. DEF-01 - Rejeição incorreta do peso máximo válido.................................................................... 21*
*7.4.2. Tabela de rastreabilidade.......................................................................................................... 22*
7.5. RISCOS E PRIORIDADES.......................................................................................................................... 23
**8. CP03 – AI-ASSISTED TEST DESIGN AND FINAL TEST SUITE.............................................................. 25**
8.1. REVISÃO E SELEÇÃO DOS CANDIDATOS GERADOS POR IA............................................................................... 25
*8.1.1. Critérios de Avaliação e Metodologia......................................................................................... 25*

*8.1.2. Análise e Classificação dos Candidatos (AI-01 a AI-12)............................................................... 25*
*8.1.3. Erros Identificados nos Candidatos IA (AI-05, AI-06, AI-09).......................................................... 28*
*8.1.4. Resumo de Classificações........................................................................................................ 28*
8.2. CONSTRUÇÃO DA SUITE FINAL................................................................................................................. 29
*8.2.1. Regras de Integração dos Testes Humanos e dos Candidatos IA................................................. 29*
*8.2.2. Lacunas de Cobertura e Casos Adicionais (F-20, F-21)............................................................... 29*
*8.2.3. Tabela Completa e Rastreabilidade dos Casos de Teste............................................................. 30*
8.3. EXECUÇÃO E ANÁLISE DOS RESULTADOS.................................................................................................... 32
*8.3.1. Ambiente e Procedimento de Execução (Python 3.9.6 e 3.12.7)................................................... 32*
*8.3.2. Sumário e Resultados Detalhados............................................................................................. 32*
*8.3.3. Relação entre Casos de Teste e Defeitos Identificados............................................................... 33*
*8.3.4. Verificação de Independência e Ausência de Efeitos Secundários (BR-05)................................... 34*
8.4. COBERTURA E VERIFICAÇÃO DOS REQUISITOS.............................................................................................35
*8.4.1. Cobertura dos Requisitos e Técnicas de Teste (BR-01 a BR-08)................................................... 35*
*8.4.2. Verificação da Precedência de Validação (BR-05)....................................................................... 36*
8.5. AVALIAÇÃO CRÍTICA DA UTILIZAÇÃO DE IA .................................................................................................. 36
*8.5.1. Contribuição e Limitações dos Candidatos IA............................................................................ 36*
*8.5.2. Comparação com o Desenho Humano...................................................................................... 36*
*8.5.3. Lições para o Processo de Teste com IA..................................................................................... 37*
8.6. CONCLUSÕES DO CP03........................................................................................................................ 37
**9. CP04 – FINAL AUDIT, EVIDENCE RECONCILIATION AND DELIVERY................................................. 38**
9.1. AUDITORIA FINAL E VERIFICAÇÃO DOS ARTEFACTOS...................................................................................... 38
*9.1.1. Âmbito e Metodologia da Auditoria ............................................................................................ 38*
*9.1.2. Inventário e Integridade dos Artefactos...................................................................................... 38*
*9.1.3. Verificação da Baseline e Preservação dos Testes Congelados................................................... 38*
*9.1.4. Verificação dos Scripts, Evidências e Documentação................................................................. 39*
9.2. RECONCILIAÇÃO DOS RESULTADOS E EVIDÊNCIAS........................................................................................ 39
*9.2.1. Consolidação das Execuções Lógicas....................................................................................... 39*
*9.2.2. Reconciliação das Execuções Físicas por Ambiente................................................................... 39*
*9.2.3. Consolidação dos Resultados PASS/FAIL .................................................................................. 40*
*9.2.4. Rastreabilidade entre Requisitos, Testes, Defeitos e Evidências.................................................. 41*
9.3. VALIDAÇÃO TÉCNICA E DOCUMENTAL........................................................................................................ 41
*9.3.1. Auditoria Automatizada e Validação de Integridade.................................................................... 41*
*9.3.2. Testes de Robustez do Auditor................................................................................................... 42*
*9.3.3. Validação Estrutural do Workbook............................................................................................. 42*
*9.3.4. Limitações e Restrições da Validação Efetuada.......................................................................... 42*
9.4. CONSOLIDAÇÃO DOS DEFEITOS E ANOMALIAS.............................................................................................43

*9.4.1. Defeitos da Implementação de Referência................................................................................. 43*
*9.4.2. Anomalias Identificadas nas Expectativas Geradas por IA........................................................... 43*
*9.4.3. Correspondência entre Defeitos, Casos de Teste e Resultados................................................... 44*
*9.4.4. Estado Final dos Defeitos e Decisões de Preservação ................................................................ 45*
9.5. PREPARAÇÃO E VALIDAÇÃO DA ENTREGA FINAL............................................................................................ 45
*9.5.1. Estrutura e Conteúdo do Pacote de Entrega............................................................................... 45*
*9.5.2. Verificação do Manifesto e Integridade do ZIP ............................................................................ 45*
*9.5.3. Identificação Criptográfica e SHA-256 ....................................................................................... 46*
9.6. CONCLUSÕES E DECLARAÇÃO DE FECHO DO CP04...................................................................................... 46
*9.6.1. Síntese dos Resultados da Auditoria.......................................................................................... 46*
*9.6.2. Declaração Final de Conformidade e Fecho............................................................................... 46*
**10. DECLARAÇÃO DE UTILIZAÇÃO DE IA............................................................................................. 47**
**11. ANEXOS....................................................................................................................................... 48**

# Índice de Tabelas

Tabela 1 - Organização do Membros do Grupo....................................................................................................................7

Tabela 2 - Definição de Prioridades do Trabalho..................................................................................................................9

Tabela 3 - Riscos e Mitigações............................................................................................................................................10

Tabela 4 - Plano de Trabalho...............................................................................................................................................11

Tabela 5 - Ambiente de Desenvolvimento..........................................................................................................................12

Tabela 6 - Questões Identificadas.......................................................................................................................................13

Tabela 7 - Revisão Estática dos Requisitos (BR-01 a BR-08)................................................................................................15

Tabela 8 - Ambiguidades Identificadas e Clarificações.......................................................................................................16

Tabela 9 - Partições de Equivalência dos Parâmetros de Entrada......................................................................................18

Tabela 10 - Plano de Teste Humano (16 Casos)..................................................................................................................18

Tabela 11 - Verificação dos Cálculos de Fee.......................................................................................................................19

Tabela 12 - Sumário da Execução.......................................................................................................................................20

Tabela 13 - Resultados Detalhados da Execução................................................................................................................20

Tabela 14 - DEF-01..............................................................................................................................................................21

Tabela 15 - DEF-02..............................................................................................................................................................21

Tabela 16 - DEF-03..............................................................................................................................................................22

Tabela 17 - DEF-04..............................................................................................................................................................22

Tabela 18 - Rastreabilidade de Defeitos.............................................................................................................................22

Tabela 19 - Riscos e Prioridades..........................................................................................................................................23

Tabela 20 - Atualização de Riscos em CP03........................................................................................................................24

Tabela 21 - Oráculo Independente-Sequência de Avaliação.............................................................................................25

Tabela 22 - Classificação dos Candidatos IA (AI-01 a AI-12)................................................................................................26

Tabela 23 - Resumo de Classificações dos Candidatos IA...................................................................................................28

Tabela 24 - Casos Adicionais de Cobertura (F-20, F-21)......................................................................................................29

Tabela 25 - Suite Final de Casos de Teste (21 Casos)..........................................................................................................30

Tabela 26 - Sumário e Resultados Detalhados da Execução (CP03)....................................................................................32

Tabela 27 - Relação entre Casos de Teste e Defeitos Identificados....................................................................................33

Tabela 28 - Cobertura dos Requisitos e Técnicas de Teste (BR-01 a BR-08).......................................................................35

Tabela 29 - Consolidação dos Resultados PASS/FAIL..........................................................................................................40

Tabela 30 - Rastreabilidade entre Requisitos, Testes, Defeitos e Evidências.....................................................................41

Tabela 31 - Anomalias Identificadas nas Expectativas Geradas por IA...............................................................................44

Tabela 32 - Correspondência entre Defeitos, Casos de Teste e Resultados.......................................................................44

Tabela 33 - Utilização de IA.................................................................................................................................................47

Tabela 34 - Entregáveis CP04..............................................................................................................................................48

# Parte I – Enquadramento Geral

# 1. Identificação e Organização do Grupo

O grupo é constituído por quatro elementos, com responsabilidades distribuídas de acordo com as diferentes atividades previstas para o CP01 - Charter and Envrionment. Esta organização procura assegurar uma divisão clara do trabalho, facilitar a coordenação das tarefas e garantir que as decisões e os resultados são revistos antes da integração no relatório final. Eduardo Dias assume a coordenação geral, acompanhando o progresso das atividades, a preparação do ambiente e a integração dos contributos dos restantes membros. Rui Carneiro fica responsável pelo desenho da suite de testes humanos, com especial atenção às classes de equivalência e aos valores de fronteira. Érica Moreira assegura a análise dos casos candidatos produzidos por IA, bem como a execução dos testes e a recolha das respetivas evidências. Beatriz Barbosa concentra-se na análise de defeitos, no mapeamento da cobertura dos requisitos e na identificação dos riscos residuais. Embora cada elemento tenha responsabilidades principais definidas, as atividades serão acompanhadas de forma colaborativa. Os casos de teste, as interpretações dos requisitos e as evidências recolhidas serão revistos pelo grupo, procurando manter a consistência entre os requisitos da especificação, os testes executados e as conclusões apresentadas no relatório.

*Tabela 1 - Organização do Membros do Grupo*

|Membro|Função|Responsabilidade Principal|
|---|---|---|
|Eduardo Dias|Coordenador / Test Lead|Coordenação, ambiente, revisão e integração do relatório|
|Rui Carneiro|Desenhador de Testes|Suite humana de equivalência e valores de fronteira|
|Erica Moreira|Revisão IA e Execução|Classificação dos candidatos IA, execução e recolha de evidências|
|Beatriz Barbosa|Analista de Defeitos e Cobertura|Registo de defeitos, mapeamento de cobertura e risco residual|

# 2. Objetivos e Âmbito

O objetivo deste trabalho é avaliar criticamente o desenho de testes elaborado manualmente e com assistência de Inteligência Artificial (IA) para a política de cálculo de portes, utilizando as regras de negócio BR-01 a BR-08 como especificação de referência. Pretende-se avaliar a qualidade, a correção e a cobertura dos casos de teste, bem como identificar discrepâncias, redundâncias e possíveis erros nas expectativas definidas.

### Incluído no âmbito

- **Revisão estática:** análise das regras BR-01–BR-08 quanto à clareza, consistência e testabilidade, identificando eventuais ambiguidades e registando as respetivas interpretações.
- **Desenho de testes humanos:** derivação independente das expectativas (*oráculo de teste*) e elaboração de, pelo menos, 12 casos de teste, cobrindo classes de equivalência válidas e inválidas, valores de fronteira e combinações críticas das regras de negócio.
- **Avaliação dos candidatos gerados por IA:** classificação de todos os casos presentes em ai_candidates.json como *aceitar*, *rever* ou *rejeitar*, acompanhada de uma justificação para cada decisão.
- **Execução dos testes:** execução separada dos conjuntos human_cases.json e final_cases.json através do programa run_cases.py.
- **Análise dos resultados:** registo de discrepâncias reproduzíveis e das respetivas evidências, mapeamento da cobertura dos requisitos R01–R08 e comparação entre os conjuntos de testes, considerando a correção das expectativas, a cobertura alcançada e a redundância.

### Excluído do âmbito

- Inspeção do código-fonte de shipping.py para orientar a conceção dos testes, de modo a preservar uma abordagem baseada nos requisitos.
- Testes de interface gráfica, browser, API, desempenho, carga ou segurança.
- Alteração dos ficheiros originais fornecidos no pacote da atividade.

### Interface da função sob teste

A função recebe três parâmetros:

- o peso da encomenda, expresso em gramas, a zona de destino
- identificada por LOCAL ou REMOTE
- um indicador booleano que especifica se o envio é expresso.
O resultado contém dois campos: status, que pode assumir os valores OK, INVALID ou UNAVAILABLE, e fee, que representa o valor dos portes em euros, como inteiro, ou null quando não existe uma tarifa aplicável.

# 3. Estratégia e Prioridades

Será adotada uma abordagem de testes de caixa-preta baseada na especificação, utilizando as regras de negócio como única referência para a conceção dos testes e a definição dos resultados esperados. As expectativas serão derivadas independentemente a partir das BR-01–BR-05, antes da execução e sem consultar o código-fonte ou os candidatos gerados por IA. As BR-06–BR-08 orientarão a estrutura dos ficheiros de teste, a comparação dos resultados e a avaliação da contribuição da IA.

O trabalho será desenvolvido de forma sequencial, de acordo com as seguintes prioridades:

*Tabela 2 - Definição de Prioridades do Trabalho*

### Ordem Atividades

Derivar o oráculo de teste a partir das regras de 1 negócio, definindo os resultados esperados para cada cenário Conceber e congelar a suite humana em 2 human_cases.json, com pelo menos 12 casos de teste. Avaliar os candidatos gerados por IA, 3 analisando todos os casos presentes em ai_candidates.json.

Consolidar a suite final em final_cases.json e 4 executar separadamente as suites humana e final através de run_cases.py.

Analisar os resultados e a cobertura, identificando discrepâncias, redundâncias e 5 requisitos insuficientemente testados.

### Medidas de Controlo

Basear as expectativas exclusivamente na especificação, sem consultar o código-fonte nem os candidatos de IA.

Registar a autoria e a data da versão inicial, documentando eventuais alterações posteriores.

Classificar cada candidato como *aceitar*, *rever* ou *rejeitar*, justificando a decisão com base nas regras de negócio. Tratar as expectativas propostas pela IA como hipóteses a validar, e não como resultados de referência, verificando cada caso face ao oráculo independente.

Registar evidências reproduzíveis, relacionar os resultados com os requisitos R01–R08 e evitar a contabilização duplicada do mesmo problema.

Esta estratégia procura garantir a independência da suite humana e permitir uma comparação fundamentada entre os testes concebidos manualmente e os testes assistidos por IA. A prioridade será assegurar a correção das expectativas e a cobertura dos requisitos antes de avaliar a quantidade de casos produzidos. A utilização de IA será, por isso, tratada de forma crítica: os candidatos só serão incorporados na suite final após revisão e validação segundo a especificação.

# 4. Riscos e Mitigações

Foram identificados cinco riscos principais que poderão afetar a validade dos testes, a conformidade do ambiente de execução e o cumprimento dos prazos. Para cada risco, são definidas medidas de mitigação destinadas a reduzir a sua probabilidade ou impacto e a assegurar a rastreabilidade das decisões tomadas ao longo do trabalho.

*Tabela 3 - Riscos e Mitigações*

|ID|Risco / impacto|Mitigação|
|---|---|---|
|R1|Python 3.9.6 é inferior ao mínimo 3.10+; conformidade do ambiente pendente.|Confirmar Python 3.10+ num ambiente autorizado; registar a versão em cada execução.|
|R2|Expectativas IA incorretas podem gerar falsa confiança.|Derivar o oráculo independentemente e justificar decisões contra as BR.|
|R3|Interpretações não resolvidas podem afetar o oráculo.|Registar questões genuínas e pedir clarificação quando as BR não determinarem a resposta.|
|R4|Prazos curtos podem comprometer entregáveis.|Acompanhar responsáveis e dependências em cada checkpoint.|
|R5|Disponibilidade desigual pode desequilibrar contribuições.|Registar contribuições e redistribuir tarefas quando necessário.|

# 5. Plano de Trabalho

O trabalho será desenvolvido de forma faseada, seguindo os checkpoints definidos para a atividade. Cada etapa terá um entregável principal e servirá de base à etapa seguinte, permitindo acompanhar o progresso, validar os resultados intermédios e identificar atempadamente eventuais desvios. As datas apresentadas deverão ser confirmadas no Moodle ou junto do docente.

*Tabela 4 - Plano de Trabalho*

|Checkpoint|Data|Entregável principal|
|---|---|---|
|CP01|27-10-2026|Charter, riscos, ambiente, verificação inicial, revisão estática e declaração de IA.|
|CP02|03-11-2026|Revisão das BR, partições, fronteiras e oráculo inicial.|
|CP03|10-11-2026|Suite humana congelada (≥12), revisão dos candidatos IA e `final_cases.json`.|
|CP04|17-11-2026|Execução separada das suites, evidências e registo inicial de defeitos.|
|CP05|24-11-2026|Cobertura R01–R08, comparação humano–IA e riscos residuais.|
|CP06|09-12-2026|Relatório quase-final, demonstração e incorporação de feedback.|
|Entrega final|15-12-2026|Relatório, workbook, evidências e declaração de IA num ZIP por grupo.|
|Apresentação|16-12-2026|Apresentação de grupo de 15 minutos com demonstração.|

Os próximos passos centram-se nas seguintes tarefas prioritárias após a preparação do CP01:

- Confirmar a disponibilidade de um ambiente autorizado com Python 3.10 ou superior e registar a versão utilizada.
- Concluir a revisão estática das regras, distinguindo questões efetivamente ambíguas de situações já resolvidas pela especificação.
- Derivar e documentar o oráculo de teste de forma independente, antes de consultar os candidatos em ai_candidates.json.
- Conceber, rever e congelar a suite humana, registando a versão inicial e documentando eventuais alterações posteriores.
- Acompanhar o progresso em cada *checkpoint* e assegurar que os entregáveis e as evidências estão completos antes da entrega final.
Este plano pretende garantir uma progressão rastreável desde a análise dos requisitos até à avaliação dos resultados, preservando a independência dos testes humanos e permitindo uma comparação fundamentada com os testes assistidos por IA.

# Parte II – Desenvolvimento dos Checkpoints

# 6. CP01 – Charter and Environment

## 6.1. Ambiente e Verificação Inicial

Nesta fase, foi realizado um levantamento inicial do ambiente de desenvolvimento e uma verificação preliminar do funcionamento do *runner* disponibilizado no pacote T08-B1.0. O objetivo foi confirmar a possibilidade de executar um caso de teste, comparar o resultado observado com o esperado e identificar eventuais limitações que devam ser resolvidas antes da execução formal das suites.

## 6.1.1. Caracterização do Ambiente

*Tabela 5 - Ambiente de Desenvolvimento*

|Item|Registo|
|---|---|
|Sistema operativo|macOS · Apple Silicon (ARM)|
|Python|3.9.6 — abaixo do requisito mínimo 3.10+|
|Intérprete|`/usr/bin/python3`|
|Folha de cálculo|Aplicação e versão por confirmar pelo grupo|
|Runner / build|`run_cases.py` fornecido · T08-B1.0|
|Caso inicial|`human_cases.json`, caso `H-ENV`|
|Baseline|Pacote original preservado; ficheiros fornecidos não devem ser alterados.|

## 6.1.2. Verificação Preliminar

A execução foi realizada com o seguinte comando:

### python3 run_cases.py human_cases.json

Para o caso H-ENV, com os parâmetros weight=500, zone=LOCAL e express=false, foi observado o resultado status=OK e fee=5. Este resultado coincide com o esperado segundo as regras de negócio aplicáveis ao caso: o peso pertence ao escalão de 1 a 1000 gramas, a zona é LOCAL e não é solicitado envio expresso. Esta verificação confirma apenas que o caso testado produziu o resultado esperado no ambiente utilizado. Não demonstra, por si só, que todas as funcionalidades do *runner* estão corretas nem que o ambiente é compatível com os requisitos completos da atividade.

## 6.1.3. Estado e Ações Pendentes

**Estado da verificação:** o caso H-ENV passou, mas a conformidade global do ambiente permanece pendente. A principal limitação identificada é a utilização de Python 3.9.6, uma versão inferior ao mínimo exigido de Python

3.10+. Antes das execuções formais, o grupo deverá confirmar e utilizar uma versão compatível num ambiente autorizado, registar a versão efetivamente utilizada e repetir a verificação inicial. Deverá ainda identificar a aplicação de folha de cálculo e a respetiva versão, completando o registo do ambiente. Até à resolução destas pendências, o resultado de H-ENV deve ser considerado uma evidência preliminar, e não uma validação completa do ambiente de teste.

## 6.2. Revisão Estática Inicial

A revisão estática das regras de negócio BR-01–BR-08 teve como objetivo avaliar a sua clareza, consistência e testabilidade, antes da execução dos testes. A análise incidiu na identificação de situações que pudessem originar interpretações diferentes do comportamento esperado e, consequentemente, comprometer a definição do oráculo de teste. Foram analisadas cinco questões relacionadas com a validação dos tipos de dados e com a precedência entre validação e disponibilidade do serviço. A análise permitiu distinguir os casos explicitamente resolvidos pela especificação daqueles em que foi necessário adotar uma interpretação para orientar o desenho dos testes.

*Tabela 6 - Questões Identificadas*

|ID|Regra|Questão identificada|Interpretação / Clarificação sugerida|
|---|---|---|---|
|Q-01|BR-01|O peso deve ser um «inteiro real, excluindo booleanos». Em Python, o tipo bool é subclasse de int, pelo que isinstance(True, int) devolve True. Deverão os valores True e False devolver INVALID?|Sim — BR-01 exclui explicitamente booleanos. Resultado esperado: status=INVALID, fee=null.|
|Q-02|BR-01|A regra especifica «inteiro real» mas não menciona floats. O que deve a função devolver para weight=500.0 (que não é int em Python)?|Assumido INVALID — BR-01 não prevê coerção de tipos. A confirmar com o docente.|
|Q-03|BR-01|Qual o comportamento esperado quando weight=None? Não é um inteiro e não está listado explicitamente.|Assumido INVALID — None não é um inteiro. A confirmar com o docente.|
|Q-04|BR-04|«Serviço expresso REMOTE não disponível acima de 5000 g.» Se weight=25000 e express=true e zone=REMOTE, o resultado deve|BR-05 responde: validação tem precedência sobre disponibilidade. Logo: INVALID, fee=null. Não existe conflito real.|

ser INVALID (peso fora do intervalo válido) ou UNAVAILABLE? Qual tem precedência? «Serviço expresso REMOTE não disponível Disponível — BR-04 define a indisponibilidade acima de 5000 g.» O caso weight=5000 exato apenas para pesos acima de 5000 g; o valor Q-05 BR-04 (limite) está incluído no intervalo disponível ou exato de 5000 g está incluído no intervalo já é considerado indisponível? disponível.

A análise identificou que Q-01, Q-04 e Q-05 não constituem ambiguidades em aberto, uma vez que a BR-01 exclui explicitamente os booleanos, a BR-05 define a precedência entre validação e disponibilidade, e a BR-04 delimita a indisponibilidade apenas para pesos acima de 5000 g, incluindo o valor exato no intervalo disponível. Q-02 e Q-03 foram consideradas na definição dos testes de entrada inválida, adotando-se a interpretação de que valores que não sejam inteiros válidos devem ser rejeitados, sem conversão automática.

Com base nesta revisão inicial, não foram identificadas outras questões concretas que impedissem a derivação do oráculo de teste. Esta conclusão poderá ser revista caso a análise detalhada dos requisitos revele lacunas ou contradições adicionais. Qualquer esclarecimento posterior deverá ser documentado e refletido, quando aplicável, nos casos de teste e nas respetivas expectativas.

# 7. CP02 – Independent Human Test Design

## 7.1. Revisão Estática, Modelo e Oráculo Inicial

## 7.1.1. Revisão Estática dos Requisitos (BR-01 a BR-08)

Foi realizada uma revisão estática das oito regras de negócio (BR-01 a BR-08), com o objetivo de identificar os requisitos testáveis, as respetivas técnicas de teste e os aspetos cuja verificação depende da execução ou de procedimentos processuais.

*Tabela 7 - Revisão Estática dos Requisitos (BR-01 a BR-08)*

|ID|Requisito|Testável?|Técnica|
|---|---|---|---|
|BR-01/R01|Validação de inputs: weight inteiro 1–20000 (sem booleans), zone exatamente LOCAL ou REMOTE, express boolean real; inválidos → INVALID/null|Sim|EP + BVA|
|BR-02/R02|Base fee: 1–1000 g → 5 €; 1001– 5000 g → 8 €; 5001–20000 g → 12 €|Sim|EP + BVA|
|BR-03/R03|REMOTE +4 €; express +6 € após remote; sem arredondamento|Sim|EP|
|BR-04/R04|REMOTE + express indisponível acima de 5000 g → UNAVAILABLE/null; a 5000 g exato é disponível; LOCAL + express sempre disponível|Sim|BVA|
|BR-05/R05|Precedência: validação > disponibilidade > cálculo; sem efeitos laterais; chamadas independentes|Sim|EP|
|BR-06/R06|Formato JSON; runner python run_cases.py; Python 3.10+|Parcialmente|—|
|BR-07/R07|Runner compara exatamente; exit codes 0/1/2; preservar reports anteriores|Sim (execução)|—|

### ID Requisito Testável? Técnica

Expectations derivadas independentemente das BRs; BR-08/R08 Sim (Processual) — classificar candidatos AI; comparar suites

A revisão permitiu identificar os requisitos funcionais verificáveis através de testes, bem como os requisitos relacionados com o ambiente de execução e com os procedimentos de validação. Esta análise serviu de base à definição das questões analisadas e do oráculo independente.

## 7.1.2. Questões Analisadas e Interpretações Adotadas

Durante a revisão das regras de negócio, foram identificadas cinco questões relativas à interpretação dos requisitos e ao comportamento esperado da função. Estas questões foram analisadas à luz das regras de negócio, tendo sido adotadas as interpretações apresentadas na tabela seguinte.

*Tabela 8 - Ambiguidades Identificadas e Clarificações*

|ID|Questão analisada|Interpretação adotada|Fundamentação|
|---|---|---|---|
|Q- 01|Comportamento de True e False em weight.|INVALID/null.|BR-01 exclui expressamente booleanos.|
|Q- 02|Comportamento de valores float em weight.|INVALID/null.|BR-01 exige um inteiro, sem conversão de tipos.|
|Q- 03|Comportamento de None ou strings em weight.|INVALID/null.|Não correspondem a um inteiro válido.|
|Q- 04|Precedência entre validação e indisponibilidade.|A validação tem precedência.|BR-05 define validação antes da disponibilidade.|
|Q- 05|Disponibilidade para REMOTE + express exatamente a 5000 g.|Disponível.|BR-04 estabelece que a indisponibilidade ocorre acima de 5000 g.|

As questões analisadas foram resolvidas através da interpretação das regras de negócio. Não foram identificadas ambiguidades genuínas que impeçam a definição do oráculo independente. As interpretações adotadas foram utilizadas na conceção dos casos de teste.

## 7.1.3. Oráculo Independente

Este procedimento constitui o oráculo independente utilizado para determinar os resultados esperados. A sua definição antecedeu a execução dos testes e não dependeu da implementação de shipping.py nem dos resultados dos candidatos gerados por IA. Os expected results são derivados exclusivamente das BRs. O ficheiro shipping.py não é usado como oráculo, qualquer divergência é tratada como defeito da implementação.

**Algoritmo de derivação:** **Passo 1 — Validação de inputs (BR-01)** **Se qualquer uma das condições abaixo se verificar → INVALID, null:**

- weight não é int, ou é bool, ou está fora do intervalo [1, 20 000]
- zone não é exatamente "LOCAL" ou "REMOTE"
- express não é bool

### Passo 2 — Verificação de disponibilidade (BR-04)

Se zone == "REMOTE" e express == True e weight > 5000 → UNAVAILABLE, null

### Passo 3 — Cálculo da fee (BR-02 + BR-03)

### Fee base conforme o peso

- 1–1 000 g → 5 €
- 1 001–5 000 g → 8 €
- 5 001–20 000 g → 12 €

### Suplementos (acumulativos)

- Se zone == "REMOTE" → + 4 €
- Se express == True → + 6 €
Resultado: OK, fee Este algoritmo foi aplicado de forma consistente à determinação dos resultados esperados dos casos de teste humanos, assegurando que as expectativas foram definidas independentemente da implementação testada.

## 7.2. Plano de Teste Humano (FROZEN)

A suite humana foi concebida com base nas regras de negócio e nas técnicas de Equivalence Partitioning (EP) e Boundary Value Analysis (BVA). Os resultados esperados foram determinados através do oráculo independente, antes da consulta dos candidatos fornecidos em ai_candidates.json. A versão inicial da suite foi congelada em human_cases.json, sendo preservada para permitir uma comparação posterior com os casos assistidos por IA. Com base nas regras de negócio e no oráculo independente, foram identificadas as partições válidas e inválidas dos três parâmetros de entrada da função: weight, zone e express. Esta identificação permite agrupar valores com comportamento esperado equivalente e apoiar a seleção dos casos de teste.

*Tabela 9 - Partições de Equivalência dos Parâmetros de Entrada*

|Parâmetro|Partições válidas|Partições inválidas|
|---|---|---|
|weight|1–1000; 1001–5000; 5001–20000|≤0; >20000; float; bool; None; string|
|zone|LOCAL; REMOTE|Outros valores, incluindo "local"|
|express|True; False|1; 0; None; outros tipos|

As partições identificadas constituíram a base para a seleção dos valores utilizados na suite humana. A cobertura destas partições foi complementada pela análise de valores fronteira, conforme apresentado no plano de teste seguinte.

As partições identificadas serviram de base à conceção da suite humana. A suite de 16 casos contempla uma seleção de representantes das partições válidas e inválidas, complementada por testes de fronteira. Nem todas as partições inválidas identificadas foram exercitadas nesta versão da suite.

*Tabela 10 - Plano de Teste Humano (16 Casos)*

|TC-ID|weight|zone|express|Expected status|Expected fee|Cobertura|
|---|---|---|---|---|---|---|
|H-01|500|LOCAL|False|OK|5|EP-W2|
|H-02|1|LOCAL|False|OK|5|BVA mínimo|
|H-03|1000|LOCAL|False|OK|5|BVA fronteira sup. tier 1|
|H-04|1001|LOCAL|False|OK|8|BVA fronteira inf. tier 2|
|H-05|5000|LOCAL|False|OK|8|BVA fronteira sup. tier 2|
|H-06|5001|LOCAL|False|OK|12|BVA fronteira inf. tier 3|
|H-07|20000|LOCAL|False|OK|12|BVA máximo válido|
|H-08|0|LOCAL|False|INVALID|null|BVA abaixo do mínimo|
|H-09|20001|LOCAL|False|INVALID|null|BVA acima do máximo|
|H-10|500|REMOTE|False|OK|9|EP REMOTE sem express|
|H-11|500|LOCAL|True|OK|11|EP express LOCAL|
|H-12|500|REMOTE|True|OK|15|EP REMOTE + express|
|H-13|5000|REMOTE|True|OK|18|BVA disponibilidade limite (incluído)|
|H-14|5001|REMOTE|True|UNAVAILABLE|null|BVA disponibilidade limite+1|
|H-15|True (bool)|LOCAL|False|INVALID|null|BR-01 bool como weight|
|H-16|500|"local"|False|INVALID|null|BR-01 zone case-sensitive|

Os casos de teste cobrem os três escalões de peso, os dois tipos de destino, as modalidades de envio normal e expresso, os limites de peso e as condições de indisponibilidade. Incluem ainda verificações de entradas inválidas, nomeadamente boolean em weight e um valor de zone com capitalização incorreta.

Para validar os resultados esperados da suite humana, foram verificados os cálculos das tarifas aplicáveis aos casos com resultado esperado OK. A tabela seguinte apresenta a tarifa base e os suplementos aplicáveis a cada combinação de peso, destino e modalidade de envio.

### Verificação dos cálculos de fee

*Tabela 11 - Verificação dos Cálculos de Fee*

|TC-ID|Base fee|+ REMOTE (+4)|+ express (+6)|Total|
|---|---|---|---|---|
|H-01|5|—|—|5|
|H-02|5|—|—|5|
|H-03|5|—|—|5|
|H-04|8|—|—|8|
|H-05|8|—|—|8|
|H-06|12|—|—|12|
|H-07|12|—|—|12|
|H-10|5|+4|—|9|
|H-11|5|—|+6|11|
|H-12|5|+4|+6|15|
|H-13|8|+4|+6|18|

A verificação confirma que os valores esperados foram calculados através da aplicação da tarifa base correspondente ao intervalo de peso, acrescida dos suplementos aplicáveis. Os casos com resultado esperado INVALID ou UNAVAILABLE não são incluídos, uma vez que não originam uma tarifa.

## 7.3. Resultados da Execução

### Comando executado

python3 run_cases.py human_cases.json **Código de Saída:** 1 O código de saída 1 indica que a execução terminou com casos de teste que não correspondem aos resultados esperados, em concordância com os 6 casos FAIL identificados na suite.

A execução foi realizada com Python 3.9.6, uma versão inferior ao requisito mínimo de Python 3.10+ definido no pacote T08-B1.0. A caracterização do ambiente de execução encontra-se documentada no CP01. Por esse motivo, os resultados são mantidos como evidência da execução realizada, mas a conformidade do ambiente permanece por validar.

## 7.3.1. Sumário

A execução da suite humana foi realizada através do runner run_cases.py, utilizando os 16 casos definidos no ficheiro human_cases.json. A tabela seguinte apresenta o resumo dos resultados obtidos.

*Tabela 12 - Sumário da Execução*

|Métrica|Valor|
|---|---|
|Total de casos|16|
|PASS|10|
|FAIL|6|
|Taxa de sucesso|62,5 %|

Dos 16 casos executados, 10 obtiveram PASS e 6 obtiveram FAIL, correspondendo a uma taxa de sucesso de 62,5%. Os resultados demonstram a existência de divergências entre o comportamento observado na implementação e os resultados esperados definidos pelo oráculo independente.

## 7.3.2. Resultados detalhados

A tabela seguinte apresenta os resultados individuais dos 16 casos de teste, permitindo comparar os valores esperados com os valores efetivamente devolvidos pela implementação e identificar os casos aprovados e reprovados.

*Tabela 13 - Resultados Detalhados da Execução*

|TC-ID|Expected status|Expected fee|Actual status|Actual fee|Veredicto|
|---|---|---|---|---|---|
|H-01|OK|5|OK|5|PASS|
|H-02|OK|5|OK|5|PASS|
|H-03|OK|5|OK|8|FAIL|
|H-04|OK|8|OK|8|PASS|
|H-05|OK|8|OK|8|PASS|
|H-06|OK|12|OK|12|PASS|
|H-07|OK|12|INVALID|null|FAIL|
|H-08|INVALID|null|INVALID|null|PASS|
|H-09|INVALID|null|INVALID|null|PASS|
|H-10|OK|9|OK|4|FAIL|
|H-11|OK|11|OK|11|PASS|
|H-12|OK|15|OK|10|FAIL|
|H-13|OK|18|OK|10|FAIL|

|TC-ID|Expected status|Expected fee|Actual status|Actual fee|Veredicto|
|---|---|---|---|---|---|
|H-14|UNAVAILABLE|null|OK|10|FAIL|
|H-15|INVALID|null|INVALID|null|PASS|
|H-16|INVALID|null|INVALID|null|PASS|

A comparação evidencia seis casos com resultados divergentes: H-03, H-07, H-10, H-12, H-13 e H-14. Estas divergências foram analisadas individualmente e agrupadas em quatro defeitos distintos, apresentados na secção seguinte.

# 7.4. Discrepâncias Identificadas na Execução (T08-B1.0)

Foram identificados 4 defeitos distintos comparando os resultados da execução com o oráculo independente.

## 7.4.1. DEF-01 - Rejeição incorreta do peso máximo válido

Com base na comparação entre os resultados esperados e os resultados observados, foram identificadas quatro discrepâncias distintas. Cada discrepância é documentada através da regra de negócio violada, do caso de teste que a evidencia, dos resultados esperados e observados e do respetivo impacto.

*Tabela 14 - DEF-01*

|Campo|Detalhe|
|---|---|
|Regra violada|BR-01|
|Caso de teste|H-07|
|Input|weight=20000, zone=LOCAL, express=false|
|Resultado esperado|OK / 12 €|
|Resultado observado|Invalid / null|
|Impacto|Um peso correspondente ao limite máximo válido é rejeitado incorretamente.|

*DEF-02 - Tarifa incorreta na fronteira superior do tier 1 (weight=1000)*

*Tabela 15 - DEF-02*

|Campo|Detalhe|
|---|---|
|Regra violada|BR-02|
|Caso de Teste|H-03|
|Input|weight = 1000, zone = LOCAL, express = false|
|Resultado esperado|OK / 5 €|

|Campo|Detalhe|
|---|---|
|Resultado Observado|OK / 8 €|
|Impacto|O valor de 1000g recebe uma tarifa superior à definida na regra de negócio.|

*DEF-03 - Cálculo incorreto da tarifa para destinos REMOTE*

*Tabela 16 - DEF-03*

|Campo|Detalhe|
|---|---|
|Regra violada|BR-03|
|Caso de Teste|H-10, H-12 e H-13|
|Input|H-10: weight = 500, zone = REMOTE, express = false H-12: weight = 500, zone = REMOTE, express = true H-13: weight = 5000, zone = REMOTE, express = true|
|Resultado esperado|9 €, 15 € e 18 €, respetivamente|
|Resultado Observado|4 €, 10 € e 10 €, respetivamente|
|Impacto|O suplemento REMOTE não é corretamente incorporado na tarifa base.|

*DEF-04 - Disponibilidade incorreta de REMOTE com envio expresso acima de 5000 g*

*Tabela 17 - DEF-04*

|Campo|Detalhe|
|---|---|
|Regra violada|BR-04|
|Caso de Teste|H-14|
|Input|Weight = 5001, zone = REMOTE, express = true|
|Resultado esperado|UNAVAILABLE / null|
|Resultado Observado|OK / 10 €|
|Impacto|O serviço é disponibilizado para uma combinação que deveria ser considerada indisponível.|

## 7.4.2. Tabela de rastreabilidade

Para consolidar a relação entre os defeitos identificados, as regras de negócio afetadas e os casos de teste responsáveis pela sua deteção, apresenta-se a seguinte tabela de rastreabilidade.

*Tabela 18 - Rastreabilidade de Defeitos*

### Defeito BR violada TCs que detetam

DEF-01 BR-01 H-07

|Defeito|BR violada|TCs que detetam|
|---|---|---|
|DEF-02|BR-02|H-03|
|DEF-03|BR-03|H-10, H-12, H-13|
|DEF-04|BR-04|H-14|

H-13 evidencia exclusivamente DEF-03. Apesar de utilizar REMOTE com envio expresso, o peso é exatamente 5000 g, pelo que o serviço deve estar disponível segundo BR-04. O resultado observado apresenta o estado OK, mas uma tarifa incorreta. DEF-04 é evidenciado por H-14.

## 7.5. Riscos e Prioridades

Com base nos resultados da execução e nas limitações identificadas durante o CP02, foram avaliados os principais riscos associados à implementação, ao ambiente de execução e às atividades seguintes do projeto. A tabela apresenta a respetiva probabilidade, impacto e estado.

*Tabela 19 - Riscos e Prioridades*

|ID|Risco|Prob.|Impacto|Estado|
|---|---|---|---|---|
|R1|A implementação disponibiliza REMOTE + express para pesos superiores a 5000 g.|Alta|Alto|Confirmado – Evidenciado por H-14|
|R2|A validação de tipos de entrada inválidos pode não cobrir todas as situações previstas.|Média|Médio|Parcialmente verificado – H-15 confirma a rejeição de boolean em weight.|
|R3|O ambiente utiliza Python 3.9.6, abaixo do mínimo exigido.|Alta|Médio|Ativo|
|R4|Os candidatos de IA poderão conter expectativas incorretas ou casos redundantes.|Alta|Alto|Por avaliar em CP03|

Os riscos identificados incluem um problema de disponibilidade confirmado pela execução, limitações na verificação das entradas inválidas, a utilização de uma versão de Python inferior à exigida e a necessidade de avaliar os candidatos de IA no CP03.

### Atualização de Riscos em CP03

Com base na execução e nas conclusões do CP03, o estado dos riscos foi atualizado:

*Tabela 20 - Atualização de Riscos em CP03*

|Risco|Descrição|Estado CP02|Estado CP03|
|---|---|---|---|
|R1 — DEF-04|Limiar de UNAVAILABLE incorreto (>10000 em vez de >5000)|Identificado|Confirmado e Alargado — F-19 reitera com weight=6000|
|R2 — DEF-01, DEF-02|Off-by-one no limite superior (DEF-01) e na fronteira de tier 1 (DEF-02)|Identificado|Confirmado — sem alteração na aplicação|
|R3 — Versão de Python|Requisito de Python 3.10+ vs Python 3.9.6|Pendente|Mitigado e Validado — suite executada com Python 3.12.7 e Python 3.9.6 com paridade estrita de comportamento|
|R4 — Candidatos IA|Candidatos com expected incorretos|Aberto|Fechado — 3 erros corrigidos/rejeitados com base no oráculo|
|R5 — Estado e Efeitos Secundários|Risco de acoplamento entre chamadas na mesma sessão|Não testado|Fechado — verificado e comprovado via verify_br05_independence.py|

# 8. CP03 – AI-Assisted Test Design and Final Test Suite

Neste checkpoint, o grupo abriu pela primeira vez o ficheiro ai_candidates.json vedado até ao fecho do plano humano em CP02 e aplicou o oráculo independente derivado das Business Rules a cada um dos 12 candidatos gerados por IA, classificando-os como aceitar, rever ou rejeitar sem consultar shipping.py. Os candidatos aceites e o único caso revisto (com expected corrigido) foram integrados com os 16 casos humanos congelados em CP02, complementados por dois casos adicionais criados para fechar lacunas de cobertura identificadas após a integração. A suite final resultante foi executada com run_cases.py, os resultados foram registados e analisados à luz dos defeitos já conhecidos, e foi conduzida uma verificação formal da independência entre chamadas e ausência de efeitos secundários exigida por BR-

 1. O checkpoint encerra com a verificação de cobertura de BR-01 a BR-08 e a atualização do registo de riscos.

## 8.1. Revisão e Seleção dos Candidatos Gerados por IA

## 8.1.1. Critérios de Avaliação e Metodologia

A classificação de cada candidato IA seguiu, sem exceção, o oráculo independente derivado das Business Rules, aplicado na sequência abaixo:

*Tabela 21 - Oráculo Independente-Sequência de Avaliação*

|Passo|Regra|Resultado se falhar|
|---|---|---|
|1 — BR- 01|weight é int não-bool ∈ [1, 20 000]; zone ∈ {"LOCAL", "REMOTE"} (case-sensitive); express é bool real|INVALID, null|
|2 — BR- 04|Se zone=="REMOTE" e express==True e weight > 5000|UNAVAILABLE, null|
|3 — BR- 02|Fee base: 1–1 000 g → 5 €; 1 001–5 000 g → 8 €; 5 001–20 000 g → 12 €|—|
|4 — BR- 03|Suplementos acumulativos: +4 € se REMOTE; +6 € se express==True|—|

## 8.1.2. Análise e Classificação dos Candidatos (AI-01 a AI-12)

A tabela seguinte apresenta a classificação de cada um dos 12 candidatos gerados por IA, confrontados com o oráculo independente:

*Tabela 22 - Classificação dos Candidatos IA (AI-01 a AI-12)*

|ID|Weigh t|Zone|Expres s|Oracle Status|Oracl e Fee|Candidat o Expected|Candidat o Fee|Classificaçã o|Justificação||
|---|---|---|---|---|---|---|---|---|---|---|
|AI - 01|500|LOCAL|false|OK|5|OK|5|REJEITAR|Duplicado exato de H-01. Sem cobertura nova.||
|AI - 02|2000|LOCAL|false|OK|8|OK|8|REJEITAR|EP interior de tier2 LOCAL. H-04 (1001) e H-05 (5000) já cobrem as fronteiras.||
|AI - 03|6000|LOCAL|false|OK|12|OK|12|REJEITAR|EP interior de tier3 LOCAL. H-06 (5001) e H-07 (20000) já cobrem as fronteiras.||
|AI - 04|500|LOCAL|true|OK|11|OK|11|REJEITAR|Duplicado exato de H-11.||
|AI - 05|500|REMOT E|false|OK|9|OK|4|REJEITAR|Duplicado de H- 10 + expected errado. Fee correto = 5 (tier1) + 4 (BR-03 REMOTE) = 9. O candidato só indicou o suplemento REMOTE sem a fee base.||
|AI - 06|1000|LOCAL|false|OK|5|OK|8|REJEITAR|Duplicado de H- 03 + expected errado. weight=1000 ∈ tier1 (1–1000 g)||
|||||||||||26|

|ID|Weigh t|Zone|Expres s|Oracle Status|Oracl e Fee|Candidat o Expected|Candidat o Fee|Classificaçã o|Justificação||
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||→ fee=5 €, não 8 €. Candidato IA confundiu fronteira superior de tier1 com tier2.||
|AI - 07|0|LOCAL|false|INVALID|null|INVALID|null|REJEITAR|Duplicado exato de H-08.||
|AI - 08|20001|LOCAL|false|INVALID|null|INVALID|null|REJEITAR|Duplicado exato de H-09.||
|AI - 09|6000|REMOT E|true|UNAVAILABL E|null|OK|22|REVER|Expected errado: weight=6000 > 5000 + REMOTE + express → BR-04 → UNAVAILABLE, null. Corrigido para UNAVAILABLE/nu ll. Acrescenta EP interior da zona UNAVAILABLE (H- 14 cobre só a fronteira BVA 5001). Incluído como F-19.||
|AI - 10|500|LOCAL|false|OK|5|OK|5|REJEITAR|Triplicado de H- 01 / AI-01.||
|AI - 11|10000|LOCAL|true|OK|18|OK|18|ACEITAR|Cobre tier3 (5001–20000) com express para LOCAL. Nenhum||
|||||||||||27|

|ID|Weigh t|Zone|Expres s|Oracle Status|Oracl e Fee|Candidat o Expected|Candidat o Fee|Classificaçã o|Justificação|
|---|---|---|---|---|---|---|---|---|---|
||||||||||caso humano cobre este quadrante. Fee = 12 (tier3) + 6 (express BR-03) = 18. Incluído como F-17.|
|AI - 12|2000|REMOT E|false|OK|12|OK|12|ACEITAR|Cobre tier2 + REMOTE sem express. H-10 cobre tier1 REMOTE, mas nenhum humano cobre tier2 REMOTE. Fee = 8 (tier2) + 4 (REMOTE BR-03) = 12. Incluído como F-18.|

## 8.1.3. Erros Identificados nos Candidatos IA (AI-05, AI-06, AI-09)

Três candidatos apresentavam valores esperados incorretos face ao oráculo independente:

- AI-05: fee esperada = 4 (omitiu fee base); correto = 9. Viola BR-03.
- AI-06: fee esperada = 8 (confundiu fronteira tier1/tier2); correto = 5. Viola BR-02.
- AI-09: status esperado = OK (ignorou BR-04); correto = UNAVAILABLE. Viola BR-04.

## 8.1.4. Resumo de Classificações

*Tabela 23 - Resumo de Classificações dos Candidatos IA*

|Classificação|Quantidade|IDs|
|---|---|---|
|Aceitar|2|AI-11, AI-12|
|Rever (expected corrigido)|1|AI-09|
|Rejeitar|9|AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, AI-08, AI-10|

## 8.2. Construção da Suite Final

## 8.2.1. Regras de Integração dos Testes Humanos e dos Candidatos IA

- A suite final (final_cases.json) integra os 16 casos humanos (H-01 a H-16) congelados em CP02, sem qualquer alteração.
- Os candidatos IA classificados como ACEITAR (AI-11, AI-12) foram incorporados como F-17 e F-18, respetivamente.
- O candidato IA classificado como REVER (AI-09) foi incorporado como F-19, com o expected corrigido para UNAVAILABLE/null conforme o oráculo.
- Os 9 candidatos classificados como REJEITAR não foram incluídos na suite final, por serem duplicados dos casos humanos ou por conterem erros não corrigíveis sem reescrita total do caso.
- Foram adicionados dois casos novos (F-20, F-21) para fechar lacunas de cobertura não satisfeitas nem pelos casos humanos nem pelos candidatos IA (ver 8.2.2).

## 8.2.2. Lacunas de Cobertura e Casos Adicionais (F-20, F-21)

Após incorporar os casos IA aceites/revistos, foram identificadas lacunas em:

- BR-01 (express inválido): nenhum caso humano testa express com tipo não-bool (ex: inteiro).
- BR-05 (validação prevalece sobre disponibilidade): nenhum caso testa weight inválido com REMOTE + express=True para confirmar que BR-01 tem prioridade sobre BR-04.
Foram criados dois casos novos:

*Tabela 24 - Casos Adicionais de Cobertura (F-20, F-21)*

|ID|Weight|Zone|Express|Expected Status|Expected Fee|BR coberta|Justificação|
|---|---|---|---|---|---|---|---|
|F- 20|500|LOCAL|1 (int)|INVALID|null|BR-01|express=1 não é bool real → validação falha|
|F- 21|25000|REMOTE|true|INVALID|null|BR-01, BR-05|Weight inválido (>20000) com REMOTE+express: BR-01 tem prioridade sobre BR-04|

## 8.2.3. Tabela Completa e Rastreabilidade dos Casos de Teste

A suite final totaliza 21 casos (16 humanos + 3 IA + 2 novos para cobertura):

*Tabela 25 - Suite Final de Casos de Teste (21 Casos)*

|TC -ID|Weigh t|Zone|Expres s|Expected Status|Expecte d Fee|Requisito s|Técnic a|Prioridad e|Raciocínio do Oráculo|
|---|---|---|---|---|---|---|---|---|---|
|H- 01|500|LOCAL|false|OK|5|BR-02, BR-03|EP|Média|tier1 (1–1000)=5; LOCAL sem express: sem suplementos|
|H- 02|1|LOCAL|false|OK|5|BR-01, BR-02|BVA|Alta|Limite inferior válido; tier1=5|
|H- 03|1000|LOCAL|false|OK|5|BR-01, BR-02|BVA|Alta|Limite superior tier1; 1000 ∈ [1,1000] → fee=5|
|H- 04|1001|LOCAL|false|OK|8|BR-01, BR-02|BVA|Alta|Limite inferior tier2; 1001 ∈ [1001,5000] → fee=8|
|H- 05|5000|LOCAL|false|OK|8|BR-01, BR-02|BVA|Alta|Limite superior tier2; 5000 ∈ [1001,5000] → fee=8|
|H- 06|5001|LOCAL|false|OK|12|BR-01, BR-02|BVA|Alta|Limite inferior tier3; 5001 ∈ [5001,20000] → fee=12|
|H- 07|20000|LOCAL|false|OK|12|BR-01, BR-02|BVA|Alta|Limite superior válido; 20000 ∈ [1,20000] → fee=12|
|H- 08|0|LOCAL|false|INVALID|null|BR-01|BVA|Alta|weight=0 < 1 → INVALID|
|H- 09|20001|LOCAL|false|INVALID|null|BR-01|BVA|Alta|weight=20001 > 20000 → INVALID|
|H- 10|500|REMOT E|false|OK|9|BR-02, BR-03|EP|Alta|tier1=5; REMOTE+4=9|

|TC -ID|Weigh t|Zone|Expres s|Expected Status|Expecte d Fee|Requisito s|Técnic a|Prioridad e|Raciocínio do Oráculo||
|---|---|---|---|---|---|---|---|---|---|---|
|H- 11|500|LOCAL|true|OK|11|BR-02, BR-03|EP|Alta|tier1=5; express+6=11||
|H- 12|500|REMOT E|true|OK|15|BR-02, BR-03|EP|Alta|tier1=5; REMOTE+4; express+6=15||
|H- 13|5000|REMOT E|true|OK|18|BR-02, BR-03, BR-04|BVA|Alta|tier2=8; REMOTE+4; express+6=18; weight=5000 ≤ 5000 → OK||
|H- 14|5001|REMOT E|true|UNAVAILABL E|null|BR-04|BVA|Alta|weight=5001 > 5000 + REMOTE + express → UNAVAILABLE||
|H- 15|true|LOCAL|false|INVALID|null|BR-01|EP|Alta|weight=True é bool → INVALID||
|H- 16|500|local|false|INVALID|null|BR-01|EP|Alta|zone="local" não ∈ {"LOCAL","REMOTE "} → INVALID||
|F- 17|10000|LOCAL|true|OK|18|BR-02, BR-03|EP|Média|tier3=12; express+6=18; LOCAL sem suplemento REMOTE||
|F- 18|2000|REMOT E|false|OK|12|BR-02, BR-03|EP|Média|tier2=8; REMOTE+4=12||
|F- 19|6000|REMOT E|true|UNAVAILABL E|null|BR-04|EP|Alta|weight=6000 > 5000 + REMOTE + express → UNAVAILABLE (EP interior, confirma DEF-04)||
|F- 20|500|LOCAL|1 (int)|INVALID|null|BR-01|EP|Alta|express=1 não é bool real → INVALID||
|||||||||||31|

TC Weigh Expres Expected Expecte Requisito Técnic Prioridad Raciocínio do Zone -ID t s Status d Fee s a e Oráculo weight=25000 > 20000 → BR-01 F-REMOT BR-01, EP/BV falha primeiro; 25000 true INVALID null Alta 21 E BR-05 A UNAVAILABLE não chega a ser avaliado

### Total: 21 casos (16 humanos + 3 IA + 2 novos para cobertura)

## 8.3. Execução e Análise dos Resultados

## 8.3.1. Ambiente e Procedimento de Execução (Python 3.9.6 e 3.12.7)

### Ambiente de Execução

- Execução Primária de Conformidade: Python 3.12.7 (cumpre o requisito Python 3.10+ de BR-06).
- Execução Secundária de Compatibilidade: Python 3.9.6 (versão padrão do sistema macOS).
- Em ambos os ambientes, a suite executou sem erros de infraestrutura, produzindo resultados estritamente idênticos.
Código de saída do runner (run_cases.py): 1 (há 8 FAILs resultantes de defeitos de implementação). **Resumo da Suite Final (21 casos): 13 PASS / 8 FAIL (61,9% taxa de aprovação).** Os 8 resultados FAIL evidenciam defeitos da implementação, não deficiências do desenho dos testes — a deteção destes comportamentos constitui o objetivo da suite.

## 8.3.2. Sumário e Resultados Detalhados

*Tabela 26 - Sumário e Resultados Detalhados da Execução (CP03)*

|TC-ID|Verdict|Actual Status|Actual Fee|Defeito associado|
|---|---|---|---|---|
|H-01|PASS|OK|5|—|
|H-02|PASS|OK|5|—|
|H-03|FAIL|OK|8 (esperado 5)|DEF-02|
|H-04|PASS|OK|8|—|
|H-05|PASS|OK|8|—|
|H-06|PASS|OK|12|—|
|H-07|FAIL|INVALID (esperado OK/12)|null|DEF-01|
|H-08|PASS|INVALID|null|—|

|TC-ID|Verdict|Actual Status|Actual Fee|Defeito associado|
|---|---|---|---|---|
|H-09|PASS|INVALID|null|—|
|H-10|FAIL|OK|4 (esperado 9)|DEF-03|
|H-11|PASS|OK|11|—|
|H-12|FAIL|OK|10 (esperado 15)|DEF-03|
|H-13|FAIL|OK|10 (esperado 18)|DEF-03|
|H-14|FAIL|OK/10 (esperado UNAVAILABLE)|10|DEF-04|
|H-15|PASS|INVALID|null|—|
|H-16|PASS|INVALID|null|—|
|F-17|PASS|OK|18|—|
|F-18|FAIL|OK|4 (esperado 12)|DEF-03|
|F-19|FAIL|OK/10 (esperado UNAVAILABLE)|10|DEF-04|
|F-20|PASS|INVALID|null|—|
|F-21|PASS|INVALID|null|—|

## 8.3.3. Relação entre Casos de Teste e Defeitos Identificados

Nenhum defeito novo foi introduzido em CP03. Os 8 FAILs observados distribuem-se de forma consistente pelos 4 defeitos identificados desde o CP02:

*Tabela 27 - Relação entre Casos de Teste e Defeitos Identificados*

|Defeito|Descrição|Casos CP02|Casos CP03 (novos)|Estado|
|---|---|---|---|---|
|DEF-01|Fronteira superior de weight: implementação usa >= 20000 em vez de > 20000, rejeitando indevidamente weight=20000 como INVALID em vez de OK (fee=12)|H-07|—|Confirmado|
|DEF-02|Fronteira do tier 1: implementação usa < 1000 em vez de <= 1000, calculando indevidamente taxa de tier 2 (fee=8) para weight=1000 em vez de tier 1 (fee=5)|H-03|—|Confirmado|
|DEF-03|Sobrescrita do suplemento REMOTE: implementação usa atribuição = (fee = 4) em vez de soma acumulada += 4, sobrescrevendo a fee base|H-10, H- 12, H-13|F-18 (tier2 REMOTE)|Confirmado e alargado|
|DEF-04|Limiar de UNAVAILABLE: implementação usa > 10000 em vez de > 5000 para REMOTE expresso, retornando OK em vez de UNAVAILABLE para pesos 5001–10000|H-14|F-19 (peso 6000)|Confirmado e alargado|

Nota F-20 (express=1): PASS — a aplicação verifica type(express) is not bool, rejeitando inteiros como não-booleanos. Nota F-21 (weight=25000, REMOTE, true): PASS — validação tem precedência sobre disponibilidade, devolvendo INVALID e confirmando a primeira parte de BR-05.

## 8.3.4. Verificação de Independência e Ausência de Efeitos Secundários (BR-05)

A regra BR-05 estipula: "Repeated calls are independent and have no side effects." Como o runner run_cases.py executa os casos sequencialmente no mesmo processo Python sem repetições deliberadas de inputs idênticos, foi desenvolvido e executado um procedimento de verificação complementar (verify_br05_independence.py). Para rigor metodológico, foram distinguidas e testadas quatro propriedades específicas, delimitando com precisão o âmbito da verificação:

**1. Repetibilidade dos Resultados (Determinismo — BR05-DET-01):**

- Procedimento: Execução consecutiva de 10 chamadas com inputs idênticos {"weight": 500, "zone": "LOCAL", "express": false} no mesmo processo runtime.
- Resultado esperado: Cada chamada devolve rigorosamente {"status": "OK", "fee": 5} sem qualquer flutuação de valor.
- Resultado observado: 10/10 invocações devolveram o resultado idêntico (PASS).

### 2. Ausência de Estado Residual entre Chamadas (BR05-RES-02)

- Procedimento: Sequência de 9 passos intercalados alternando transições críticas: Válido nominal → Inválido (peso negativo) → Válido de recuperação → Indisponível (peso 15000 REMOTE express) → Válido de recuperação → Inválido (tipo booleano) → Válido de recuperação → Válido de outro tier (Tier 2) → Válido de referência final.
- Resultado esperado: As chamadas executadas após falhas de validação ou indisponibilidade não sofrem contaminação de estado anterior, comportando-se como se fossem a primeira chamada da sessão.
- Resultado observado: Todos os 9 passos devolveram os outputs exatos previstos pelo oráculo independente (PASS).

### 3. Ausência de Mutações Observáveis (BR05-MUT-03)

- Procedimento: Verificação de não-mutação dos argumentos de entrada (dicionário de parâmetros do chamador). Isolamento de instâncias de retorno: cada invocação gera uma nova instância de dicionário (id(res_a) != id(res_b)). A mutação deliberada pelo caller de um retorno anterior (res_a["fee"] = 9999) não corrompe o retorno de chamadas subsequentes. Imutabilidade do namespace do módulo: inspeção de shipping.**dict** antes e depois das chamadas, comprovando que nenhuma variável global é criada ou modificada.
- Resultado observado: Imutabilidade de inputs, isolamento de objetos e namespace preservados (PASS).

### 4. Ausência de Efeitos Secundários Externos Delimitados (BR05-EXT-04)

- Procedimento: Monitorização de streams de saída padrão (sys.stdout, sys.stderr), variáveis de ambiente (os.environ) e snapshot dos ficheiros diretamente existentes na diretoria da aplicação (app_dir), comparando nome, tamanho e timestamp de modificação (st_mtime_ns) antes e após as invocações de quote().
- Resultado esperado: Nenhuma escrita para stdout/stderr, nenhuma alteração em variáveis de ambiente e nenhuma alteração observável nos ficheiros diretamente monitorizados em app_dir.
- Resultado observado: Streams de saída completamente limpos, ambiente inalterado e ficheiros diretamente monitorizados em app_dir inalterados (PASS).

## 8.4. Cobertura e Verificação dos Requisitos

## 8.4.1. Cobertura dos Requisitos e Técnicas de Teste (BR-01 a BR-08)

*Tabela 28 - Cobertura dos Requisitos e Técnicas de Teste (BR-01 a BR-08)*

|BR|Descrição|Casos que cobrem|Estado|
|---|---|---|---|
|BR- 01|Validação de tipos e intervalos|H-02, H-03, H-07, H-08, H-09, H-15, H-16, F-20, F-21|Coberto|
|BR- 02|Fee base por tier (1–1000 / 1001–5000 / 5001– 20000)|H-02, H-03, H-04, H-05, H-06, H-07 (todas as fronteiras BVA)|Coberto|
|BR- 03|Suplementos acumulativos REMOTE (+4€) e express (+6€)|H-10 (REMOTE), H-11 (express), H-12 (ambos), F-17, F-18|Coberto|
|BR- 04|UNAVAILABLE se REMOTE+express+weight>5000|H-13 (fronteira disponível), H-14 (fronteira UNAVAILABLE), F-19 (EP interior)|Coberto|
|BR- 05|Precedência validação > disponibilidade > cálculo; independência de chamadas e ausência de efeitos secundários|F-21 (1.º nível: validação > disponibilidade); H- 14, F-19 (2.º nível: disponibilidade > cálculo) + Procedimento BR05-IND (independência e ausência de efeitos secundários)|Coberto|
|BR- 06|Formato JSON; runner python run_cases.py; Python 3.10+|Todos os casos executados com run_cases.py (3.12.7: conformidade; 3.9.6: compatibilidade)|Coberto|
|BR- 07|Runner compara exatamente; exit codes 0=PASS, 1=FAILs, 2=erro|Executado; exit code = 1 (há FAILs documentados)|Coberto|
|BR- 08|Oráculo independente derivado das BRs; classificação crítica da IA|Oráculo derivado exclusivamente de BR-01–BR- 05; candidatos IA revistos e justificados|Coberto|

## 8.4.2. Verificação da Precedência de Validação (BR-05)

A regra BR-05 estabelece a precedência: validação > disponibilidade > cálculo. Esta ordem foi confirmada explicitamente pelo caso F-21: weight=25000 excede o limite válido (>20000) e, simultaneamente, a combinação REMOTE+express+weight>5000 seria candidata a UNAVAILABLE por BR-04. O oráculo independente determina que a validação de BR-01 falha primeiro, pelo que a verificação de disponibilidade (BR-04) nunca chega a ser avaliada — o resultado correto é INVALID, não UNAVAILABLE. A execução confirmou este comportamento: F-21 obteve PASS, devolvendo INVALID conforme esperado, validando formalmente o primeiro nível de precedência de BR-05 (validação sobre disponibilidade).

O segundo nível de precedência — disponibilidade sobre cálculo — é demonstrado por H-14 e F-19: em ambos os casos, a condição BR-04 está satisfeita e o resultado é UNAVAILABLE com fee=null, confirmando que o cálculo de BR-02/BR-03 não é realizado.

A terceira dimensão de BR-05 (independência entre chamadas e ausência de efeitos secundários) foi verificada separadamente em 8.3.4.

## 8.5. Avaliação Crítica da Utilização de IA

## 8.5.1. Contribuição e Limitações dos Candidatos IA

Dos 12 candidatos gerados por IA, apenas 2 (AI-11, AI-12) foram aceites sem alterações e 1 (AI-09) foi aproveitado após correção do expected. A contribuição líquida da IA à suite final foi, portanto, de 3 casos em 21 (14%), todos cobrindo quadrantes de equivalência não testados pelos 16 casos humanos: tier3 LOCAL com express (F-17), tier2 REMOTE sem express (F-18) e o interior da zona UNAVAILABLE (F-19). Em contrapartida, 9 dos 12 candidatos (75%) eram duplicados exatos ou quase-exatos de casos humanos já existentes, sem acrescentar cobertura nova. Mais significativamente, 3 candidatos (25%) continham valores esperados incorretos face ao oráculo independente derivado das BR: AI-05 omitiu a fee base, AI-06 confundiu a fronteira entre tier1 e tier2, e AI-09 ignorou a regra BR-04 de indisponibilidade. Nenhum destes erros seria detetado sem um oráculo construído independentemente da implementação e da própria IA.

## 8.5.2. Comparação com o Desenho Humano

O desenho humano (CP02) manteve-se como a base dominante e estruturalmente mais rigorosa da suite final: os 16 casos H-01 a H-16 cobrem sistematicamente todas as fronteiras BVA de BR-01 a BR-04, enquanto os candidatos IA, mesmo os aceites, limitaram-se a casos de equivalência (EP) em quadrantes não cobertos, sem introduzir novas fronteiras. Nenhum dos defeitos DEF-01 a DEF-04, todos identificados a partir de casos humanos no CP02, foi descoberto por um candidato IA — os candidatos aceites apenas reafirmaram ou alargaram defeitos já conhecidos (F-18 e F-19 alargam DEF-03 e DEF-04, respetivamente).

A revisão humana manteve-se, assim, imprescindível: não só para classificar os candidatos IA, mas porque é o desenho humano, ancorado num oráculo independente, que garante a deteção dos defeitos de implementação. A IA funcionou como complemento de cobertura, não como substituto do raciocínio de teste.

## 8.5.3. Lições para o Processo de Teste com IA

- Um oráculo independente, derivado diretamente das Business Rules e construído sem consultar a implementação ou os candidatos IA, é condição necessária para validar criticamente qualquer candidato gerado por IA — sem ele, os 3 erros de AI-05, AI-06 e AI-09 teriam passado despercebidos.
- A deduplicação deve ser o primeiro filtro: 75% dos candidatos IA avaliados eram duplicados de casos humanos, pelo que a revisão de IA deve começar por comparar inputs contra a suite existente antes de analisar o expected.
- Candidatos IA são mais fiáveis a identificar quadrantes de cobertura em falta (EP) do que a calcular corretamente o expected desses quadrantes — o valor da IA está em sugerir onde testar, não em garantir o resultado esperado.
- A integração de candidatos IA na suite final deve ser sempre condicional à aprovação explícita do oráculo, nunca aceite por confiança no texto gerado.

## 8.6. Conclusões do CP03

O CP03 atingiu plenamente os objetivos estabelecidos:

- 12 candidatos IA revistos: 2 aceites (AI-11, AI-12), 1 revisto (AI-09 com expected corrigido para UNAVAILABLE/null), 9 rejeitados. Foram detetados 3 erros conceituais nos candidatos gerados por IA, comprovando empiricamente a necessidade de revisão crítica humana apoiada em oráculo independente.
- Suite final com 21 casos: 16 casos humanos preservados intactos + 3 casos IA integrados (F-17, F-18, F-19) + 2 casos novos para cobertura de requisitos (F-20 para tipo de express e F-21 para precedência de validação sobre disponibilidade).
- Cobertura de Requisitos BR-01 a BR-08: assegurada para todas as classes de equivalência identificadas e exercitadas, incluindo verificação formal da ausência de efeitos secundários e independência entre chamadas (BR-05) no âmbito das dimensões monitorizadas (outputs, ambiente e ficheiros diretos da app_dir).
- Resultados e Rastreabilidade: 13 PASS / 8 FAIL. Os 4 defeitos reportados no CP02 foram rigorosamente confirmados e mapeados sem ambiguidades: DEF-01 (fronteira superior weight=20000), DEF-02 (fronteira tier 1 weight=1000), DEF-03 (sobrescrita de fee REMOTE), e DEF-04 (limiar de disponibilidade >10000).
- Conformidade de Ambiente: validação de conformidade em Python 3.12.7 (cumpre BR-06); execução paralela em Python 3.9.6 como verificação de compatibilidade, com resultados idênticos.

# 9. CP04 – Final Audit, Evidence Reconciliation and Delivery

## 9.1. Auditoria Final e Verificação dos Artefactos

## 9.1.1. Âmbito e Metodologia da Auditoria

O Checkpoint 4 (CP04) teve como objetivo central a auditoria final e a reconciliação de evidências de todo o processo de desenho e execução de testes desenvolvido ao longo do trabalho T08, incidindo sobre a build oficial sob teste T08-B1.0 do módulo shipping.py. A metodologia adotada seguiu um princípio de verificação independente e não retroativa: os resultados de execução previamente registados na pasta runs/ e no livro TestResults_T08_Template.xlsx foram confrontados com um oráculo de regras de negócio (BR-01 a BR-08) estabelecido de forma autónoma pela equipa, sem qualquer alteração aos vereditos originais emitidos pelo executor automático run_cases.py. A auditoria contemplou quatro dimensões complementares: (i) o inventário e a integridade dos artefactos entregues; (ii) a preservação da baseline humana congelada no CP02; (iii) a validação técnica dos scripts de automação e do livro de cálculo oficial; e (iv) a consolidação rigorosa dos defeitos de implementação e das anomalias identificadas nas expectativas de teste geradas por IA.

## 9.1.2. Inventário e Integridade dos Artefactos

O inventário de artefactos sujeitos a auditoria compreendeu os seguintes elementos:

- shipping.py-objeto de teste sob auditoria (build T08-B1.0).
- run_cases.py-executor automático de testes, sem intervenção retroativa sobre os vereditos emitidos.
- ai_candidates.json-conjunto original de 12 candidatos de teste gerados por IA.
- runs/final_cases_execution.json-registo de execução da suite final de 30 casos de teste.
- TestResults_T08_Template.xlsx-livro de cálculo oficial de consolidação de resultados.
A verificação confirmou a presença e a integridade de todos os artefactos listados, sem omissões, duplicações ou inconsistências de nomenclatura entre o repositório e a documentação de suporte.

## 9.1.3. Verificação da Baseline e Preservação dos Testes Congelados

A baseline humana definida no CP02 - composta por 16 casos concebidos pelos alunos (H-01 a H-16) acrescidos de 1 caso técnico de validação de ambiente (H-ENV), num total de 17 entradas - foi confirmada como congelada ("frozen") e integralmente preservada ao longo do CP04, sem qualquer alteração aos enunciados, parâmetros de entrada ou oráculos originalmente definidos. Confirmou-se ainda que os resultados da execução original do conjunto de candidatos de IA (ai_candidates.json) foram mantidos exatamente como emitidos pelo runner (10 PASS / 2 FAIL), em estrito cumprimento do princípio de integridade de auditoria, sem manipulação retroativa de vereditos mesmo nos casos em que a auditoria independente identificou falsos positivos (secção 9.4.2).

## 9.1.4. Verificação dos Scripts, Evidências e Documentação

Os scripts de automação (run_cases.py) e os ficheiros de evidência de execução foram verificados quanto à sua consistência interna e à reprodutibilidade dos resultados. Confirmou-se que a reexecução das três suites de teste - humana, candidatos originais de IA e suite final expandida-nos dois interpretadores Python (3.9.6 e 3.12.7) produziu resultados idênticos, não tendo sido detetada qualquer dependência de versão de interpretador nos vereditos emitidos. A documentação de suporte (relatórios de defeito, tabela de rastreabilidade e notas de auditoria) foi revista quanto à coerência terminológica e à correspondência integral com os identificadores de casos de teste e de requisitos.

## 9.2. Reconciliação dos Resultados e Evidências

## 9.2.1. Consolidação das Execuções Lógicas

A consolidação das execuções lógicas abrangeu, para além das três suites principais (secção 9.2.3), a verificação de nove cenários de robustez funcional complementares, destinados a confirmar o comportamento do código perante classes de equivalência limítrofes e entradas de tipo inválido:

- F-22 (weight=500.5, peso de tipo float): PASS - rejeitado corretamente como INVALID por verificação explícita de tipo inteiro (BR-01).
- F-23 (zone=' LOCAL ', zona com espaços adicionais): PASS-rejeitado corretamente como INVALID por não pertencer ao domínio exato ("LOCAL", "REMOTE").
- F-24 (weight=2000, express=True, zona LOCAL): PASS-tarifa base de 8€ acrescida do suplemento expresso de 6€, totalizando 14€, calculada corretamente.
- F-25 (zone='INTERNATIONAL'): PASS-rejeitado corretamente como INVALID por zona fora de domínio.
- F-26 (weight=-100): PASS-rejeitado corretamente como INVALID por peso negativo.
- F-27 (express='False', tipo string): PASS-rejeitado corretamente como INVALID por falha de verificação de tipo booleano.
- F-28 (weight=6000, zone='LOCAL', express=False): PASS-tarifa de tier 3 (6€) sem sobrecargas, confirmando o esperado OK/12.
- F-29 (weight=6000, zone='REMOTE', express=False): FAIL - esperado OK/16, obtido OK/4; expõe DEF-03 (sobrescrita em vez de acumulação da tarifa REMOTE).
- F-30 (weight=8000, zone='REMOTE', express=True): FAIL - esperado UNAVAILABLE/null, obtido OK/10; expõe DEF-04 (limiar de 10000g em vez de 5000g).

## 9.2.2. Reconciliação das Execuções Físicas por Ambiente

A reconciliação das execuções físicas confirmou a paridade comportamental integral entre os dois interpretadores Python utilizados ao longo do projeto - Python 3.9.6 e Python 3.12.7 - não tendo sido identificada qualquer divergência de resultado, de exceção ou de desempenho relevante entre ambientes. A execução de controlo de ambiente (RUN-ENV-

01) confirmou a conformidade da instalação com o requisito normativo BR-06, enquanto a execução paralela em Python
3.9.6 serviu exclusivamente como verificação adicional de compatibilidade retroativa. No total, foram reconciliadas 68 execuções históricas e atuais do projeto (17 da suite humana, 12 da suite original de IA, 30 da suite final e 9 verificações complementares de robustez e de controlo), todas produzindo vereditos idênticos em ambos os ambientes.

## 9.2.3. Consolidação dos Resultados PASS/FAIL

A tabela seguinte sintetiza os resultados de execução consolidados sobre a build oficial T08-B1.0:

*Tabela 29 - Consolidação dos Resultados PASS/FAIL*

|Suite de Testes|Identificação dos Casos|Quantidade|PASS|FAIL|Taxa de Conformidade|
|---|---|---|---|---|---|
|Suite Humana (com H-ENV)|H-ENV, H-01 a H- 16|17|11|6|64.7%|
|Candidatos Originais de IA|AI-01 a AI-12|12|10 (no runner)|2|83.3% (aparente)|
|Suite Final Combinada|H-01..16 + F- 17..30|30|20|10|66.7%|

## 9.2.4. Rastreabilidade entre Requisitos, Testes, Defeitos e Evidências

A tabela seguinte consolida a rastreabilidade integral entre os requisitos normativos (BR-01 a BR-08), os defeitos e anomalias identificados, os casos de teste associados e as respetivas evidências de execução:

*Tabela 30 - Rastreabilidade entre Requisitos, Testes, Defeitos e Evidências*

|Requisito|Defeito/Anomalia|Casos de Teste Associados|Evidência|
|---|---|---|---|
|BR-01|DEF-01|H-07|runs/final_cases_execution.json#H- 07|
|BR-02|DEF-02|H-03|runs/final_cases_execution.json#H- 03|
|BR-03|DEF-03|H-10, H-12, H-13, F-18, F-29|runs/final_cases_execution.json#H- 10,#H-12,#H-13,#F-18,#F-29|
|BR-04|DEF-04|H-14, F-19, F-30|runs/final_cases_execution.json#H- 14,#F-19,#F-30|
|BR-03|DATA-01|AI-05|ai_candidates.json / auditoria independente|
|BR-02|DATA-02|AI-06|ai_candidates.json / auditoria independente|
|BR-04|DATA-03|AI-09|ai_candidates.json / auditoria independente|

## 9.3. Validação Técnica e Documental

## 9.3.1. Auditoria Automatizada e Validação de Integridade

A auditoria automatizada do livro de cálculo oficial (TestResults_T08_Template.xlsx) foi efetuada através de verificação programática da estrutura OpenXML subjacente, eliminando o risco de corrupção ou de dessincronização de fórmulas entre folhas. Complementarmente, procedeu-se à verificação formal da propriedade de independência e de ausência de efeitos secundários prevista em BR-05, através de quatro execuções de controlo (RUN-CTRL-01 a RUN-CTRL-04), que confirmaram, com veredicto PASS unânime, que chamadas sucessivas e independentes à função quote() não produzem alterações no ambiente, no sistema de ficheiros da app_dir nem interferência entre resultados de chamadas distintas. A execução completa do script de auditoria automatizada audit_cp4.py, com o pacote de entrega ZIP presente, produziu o resultado 27 PASS / 0 FAIL / 0 WARNING / 0 BLOCKED, com código de saída (exit code) 0, culminando na mensagem final: “AUDIT PASSED — TEST PROCESS & ARTIFACTS FULLY VALIDATED (4 SUT DEFECTS CONFIRMED)”.

## 9.3.2. Testes de Robustez do Auditor

A robustez do auditor automatizado (audit_cp4.py) perante classes de falha foi verificada através da suite test_auditor_robustness.py, composta por seis cenários dedicados, executados em ambiente temporário, todos aprovados (6/6):

- test_missing_file_detection-Ficheiro obrigatório em falta.
- test_malformed_json_detection-JSON com sintaxe inválida.
- test_duplicate_id_detection-ID duplicado na suite.
- test_final_suite_expectation_inconsistency_detection - Inconsistência introduzida na expectativa de um caso da suite final, com verificação da divergência entre suite e evidência de execução e/ou alteração da distribuição global de resultados.
- test_manifest_hash_tamper_detection-Hash criptográfico incorrecto no manifesto.
- test_corrupted_zip_detection-Pacote ZIP corrompido.
Os seis cenários controlados demonstram que o auditor integrado deteta as classes de falhas especificamente testadas através de execução em ambiente temporário.

## 9.3.3. Validação Estrutural do Workbook

O livro TestResults_T08_Template.xlsx foi validado quanto à presença de uma coluna autónoma de requisitos (mapeando cada caso de teste à regra de negócio BR correspondente), à separação estrita entre os campos de resultado esperado e resultado observado, e à cobertura normativa de 100% das regras BR-01 a BR-08, sem erros de fórmula detetados. A consolidação integrou a totalidade das 68 execuções históricas e atuais do projeto, mantendo rastreabilidade individual a cada identificador de caso. A inspeção estrutural OpenXML identificou as fórmulas de rastreabilidade previstas e não detetou problemas estruturais nos componentes XML analisados. Não foi efetuado recálculo dinâmico independente das fórmulas, devido à indisponibilidade do LibreOffice no ambiente de execução. Consequentemente, esta validação não constitui prova independente da correção dos valores calculados.

## 9.3.4. Limitações e Restrições da Validação Efetuada

A validação técnica efetuada não contemplou testes de mutação do código-fonte, análise de cobertura de código instrumentada (line/branch coverage), nem testes de desempenho ou de carga sobre o executor run_cases.py, por estarem fora do âmbito normativo definido para o CP04. A auditoria também não procedeu à correção automática dos defeitos identificados, limitando-se à sua documentação e classificação - a decisão de correção do código shipping.py permanece fora do âmbito deste checkpoint, conforme detalhado na secção 9.4.4.

## 9.4. Consolidação dos Defeitos e Anomalias

## 9.4.1. Defeitos da Implementação de Referência

A auditoria confirmou a existência de quatro defeitos distintos na implementação de referência do módulo shipping.py, rigorosamente segregados das anomalias de qualidade das expectativas de teste geradas por IA (secção 9.4.2).

DEF-01 - Rejeição incorreta do peso máximo válido. Regra violada: BR-01. Localização: shipping.py, linha 3 (if weight < 1 or weight >= 20000:). Causa raiz: operador >= em vez de >, provocando off-by-one e tratando o limite máximo válido (20000g) como inválido. Reprodução: quote(20000, 'LOCAL', False). Esperado: {"status": "OK", "fee": 12}. Observado: {"status": "INVALID", "fee": null}. Testes associados: H-07. Severidade: Alta - rejeita arbitrariamente encomendas legítimas no limite superior de peso do serviço comercial.

DEF-02 - Limite entre escalões de peso incorretamente implementado. Regra violada: BR-02. Localização: shipping.py, linha 7 (if weight < 1000:). Causa raiz: operador < em vez de <=, fazendo com que encomendas de exatamente 1000g caiam no ramo de Tier 2 (8€) em vez de Tier 1 (5€). Reprodução: quote(1000, 'LOCAL', False). Esperado: {"status": "OK", "fee": 5}. Observado: {"status": "OK", "fee": 8}. Testes associados: H-03. Severidade: Média-Alta-sobrecobrança indevida de 3€ por encomenda de 1000g.

DEF-03 - Sobrescrita destrutiva da taxa base no tratamento REMOTE. Regra violada: BR-03. Localização: shipping.py, linha 14 (fee = 4). Causa raiz: atribuição simples (=) em vez de acumulação (+=), apagando a tarifa base calculada em BR-02. Reprodução: quote(500, 'REMOTE', False). Esperado: {"status": "OK", "fee": 9}. Observado: {"status": "OK", "fee": 4}. Testes associados: H-10, H-12, H-13, F-18, F-29. Nota técnica: o teste H-13 (5000g, REMOTE, express=True) está disponível (5000 ≤ 5000) e falha exclusivamente pela sobrescrita da taxa base (retorna 10€ em vez de 18€). Severidade: Crítica-subfaturação sistemática de todas as encomendas com destino remoto.

DEF-04 - Limiar de indisponibilidade REMOTE + express incorreto. Regra violada: BR-04. Localização: shipping.py, linha 5 (if zone == "REMOTE" and express and weight > 10000:). Causa raiz: threshold de indisponibilidade codificado como 10000g em vez de 5000g. Reprodução: quote(5001, 'REMOTE', True). Esperado: {"status": "UNAVAILABLE", "fee": null}. Observado: {"status": "OK", "fee": 10}. Testes associados: H-14, F-19, F-30. Severidade: Alta-aceitação de pedidos de transporte expresso para zonas remotas que a operação logística não assegura contratualmente.

## 9.4.2. Anomalias Identificadas nas Expectativas Geradas por IA

A auditoria independente identificou três anomalias de qualidade nas expectativas de teste geradas por IA, correspondentes a casos em que o veredito do runner automático (PASS ou FAIL) não refletia a conformidade real face às regras de negócio normativas.

AI-05 (weight=500, zone='REMOTE', express=False): a expectativa gerada pela IA ({"status": "OK", "fee": 4}) reproduziu exatamente o defeito DEF-03, pelo que o runner reportou PASS apesar de o oráculo independente (BR-02+BR-03) exigir fee=9. Classificado como DATA-01 e rejeitado na revisão humana. AI-06 (weight=1000, zone='LOCAL', express=False): a expectativa gerada pela IA ({"status": "OK", "fee": 8}) cometeu um erro de interpretação de fronteira, mascarando o defeito DEF-02 (o oráculo independente exige fee=5). Classificado como DATA-02 e rejeitado na revisão humana. AI-09 (weight=6000, zone='REMOTE', express=True): a expectativa gerada pela IA ({"status": "OK", "fee": 22}) tentou tarifar um serviço que a regra BR-04 declara expressamente indisponível acima de 5000g em zona REMOTE com express. O runner reportou FAIL (22 vs 10), mas o oráculo correto exige {"status": "UNAVAILABLE", "fee": null}. Classificado como DATA-03; o caso foi revisto pela equipa humana para F-19 com a expectativa legal correta.

*Tabela 31 - Anomalias Identificadas nas Expectativas Geradas por IA*

|ID|Candidato IA|Regra|Expectativa IA|Oráculo Independente|Saída da Aplicação|Natureza da Falha|
|---|---|---|---|---|---|---|
|DATA-01|AI-05|BR-03|OK, fee=4|OK, fee=9|OK, fee=4|Omissão da taxa base; replica o defeito DEF- 03|
|DATA-02|AI-06|BR-02|OK, fee=8|OK, fee=5|OK, fee=8|Erro de fronteira; mascara o defeito DEF- 02|
|DATA-03|AI-09|BR-04|OK, fee=22|UNAVAILABLE, fee=null|OK, fee=10|Tarifação indevida de serviço indisponível|

## 9.4.3. Correspondência entre Defeitos, Casos de Teste e Resultados

A tabela seguinte sintetiza a correspondência final entre cada defeito, a sua severidade, os casos de teste que o expõem e os resultados confrontados entre o runner e o oráculo independente:

*Tabela 32 - Correspondência entre Defeitos, Casos de Teste e Resultados*

|Defeito|Severidade|Casos de Teste|Resultado do Runner|Resultado do Oráculo|
|---|---|---|---|---|
|DEF-01|Alta|H-07|INVALID, fee=null|OK, fee=12|
|DEF-02|Média-Alta|H-03|OK, fee=8|OK, fee=5|

|Defeito|Severidade|Casos de Teste|Resultado do Runner|Resultado do Oráculo|
|---|---|---|---|---|
|DEF-03|Crítica|H-10, H-12, H-13, F- 18, F-29|fee subfaturado (ex.: fee=4)|fee = tarifa base + 4€|
|DEF-04|Alta|H-14, F-19, F-30|OK, fee=10|UNAVAILABLE, fee=null|

## 9.4.4. Estado Final dos Defeitos e Decisões de Preservação

À data de fecho do CP04, os quatro defeitos de implementação (DEF-01 a DEF-04) permanecem no estado "Aberto / Não corrigido", dado que a correção do código shipping.py não se encontra no âmbito do presente checkpoint, focado no desenho, execução e auditoria de testes. A equipa decidiu, em consonância com o princípio de integridade de auditoria referido em 9.1.3, preservar inalterados os vereditos originais do runner para os casos AI-05 e AI-06 (ambos PASS), documentando separadamente a sua natureza de falso positivo nas anomalias DATA-01 e DATA-02, em vez de reclassificar retroativamente os resultados históricos. Esta decisão garante a auditabilidade integral da cadeia de evidências, permitindo a qualquer momento reconstituir o raciocínio que conduziu à rejeição destes dois casos na revisão humana independente.

## 9.5. Preparação e Validação da Entrega Final

## 9.5.1. Estrutura e Conteúdo do Pacote de Entrega

O pacote de entrega final (TVSI_T08_Grupo5_CP04.zip) foi estruturado de forma a preservar a rastreabilidade integral entre o relatório, o código-fonte, os scripts de execução e as evidências de teste. O conteúdo auditado compreende:

- Relatorio_CP4.md-relatório de execução de testes e gestão de evidências do presente checkpoint.
- shipping.py-objeto de teste sob auditoria (build T08-B1.0).
- run_cases.py-executor automático de testes.
- ai_candidates.json-conjunto original de 12 candidatos de teste gerados por IA.
- runs/ - pasta de evidências de execução, incluindo final_cases_execution.json e os registos históricos das três suites.
- TestResults_T08_Template.xlsx-livro de cálculo oficial de consolidação de resultados.

## 9.5.2. Verificação do Manifesto e Integridade do ZIP

O manifesto de entrega foi confrontado com o inventário de artefactos auditado na secção 9.1.2, confirmando-se a correspondência integral entre os ficheiros listados no manifesto e os ficheiros efetivamente incluídos no pacote TVSI_T08_Grupo5_CP04.zip, sem ficheiros em falta, duplicados ou excedentários. Não foram detetados sinais de corrupção do arquivo comprimido nem inconsistências de codificação de caracteres nos ficheiros de texto e JSON incluídos.

O repositório remoto GitHub foi sincronizado com o estado final do CP04. O pacote de entrega TVSI_T08_Grupo5_CP04.zip foi criado antes da revisão terminológica ao cenário 4 do ficheiro test_auditor_robustness.py. O repositório constitui, por isso, a fonte autoritativa do estado final do checkpoint.

## 9.5.3. Identificação Criptográfica e SHA-256

Com o objetivo de assegurar a imutabilidade e a reprodutibilidade das evidências de execução referidas na secção 9.1, foram calculados e registados no manifesto de entrega os valores de síntese criptográfica SHA-256 de cada artefacto crítico (código-fonte, ficheiros de execução JSON e livro de cálculo oficial), permitindo a qualquer auditor externo confirmar, a posteriori, que o conteúdo submetido corresponde exatamente ao conteúdo auditado nesta secção, sem possibilidade de alteração não detetada após o fecho do checkpoint.

## 9.6. Conclusões e Declaração de Fecho do CP04

## 9.6.1. Síntese dos Resultados da Auditoria

A auditoria do CP04 confirmou os seguintes resultados consolidados: suite humana de 17 casos (11 PASS / 6 FAIL, taxa de conformidade de 64.7%); suite original de candidatos de IA de 12 casos (10 PASS / 2 FAIL aparente no runner, com 2 falsos positivos identificados na auditoria independente); suite final expandida de 30 casos (20 PASS / 10 FAIL, taxa de conformidade de 66.7%); 4 defeitos de implementação confirmados e rastreados (DEF-01 a DEF-04); 3 anomalias de qualidade nas expectativas de teste geradas por IA identificadas (DATA-01 a DATA-03); 68 execuções históricas e atuais consolidadas no livro oficial; e 0 bloqueios técnicos pendentes. O veredicto final do CP04 sintetiza-se nos seguintes termos:

- 30 casos de teste na suite final (20 PASS / 10 FAIL); 68 execuções lógicas e 98 execuções físicas consolidadas no livro oficial.
- 4 defeitos de implementação confirmados e rastreados (DEF-01 a DEF-04); 3 anomalias de qualidade nas expectativas geradas por IA (DATA-01 a DATA-03).
- Auditoria automatizada (audit_cp4.py): 27 PASS / 0 FAIL / 0 WARNING / 0 BLOCKED, incluindo a verificação do pacote de entrega (ZIP).
- Meta-testes de robustez do auditor (test_auditor_robustness.py): 6/6 cenários aprovados.
- Limitação declarada: a validação estrutural do workbook assenta em verificação OpenXML/LibreOffice, não substituindo a verificação completa de fórmulas no motor de cálculo nativo do Excel.

## 9.6.2. Declaração Final de Conformidade e Fecho

Com base na totalidade das verificações documentadas no presente capítulo, declara-se que todas as atividades previstas para o Checkpoint 4 (CP04) foram concluídas com sucesso, mantendo-se uma cadeia ininterrupta de rastreabilidade entre requisitos normativos (BR-01 a BR-08), casos de teste desenhados, execuções empíricas, relatórios de defeito e o livro de

cálculo oficial de consolidação de resultados. O CP04 é, nestes termos, considerado tecnicamente encerrado pela equipa de auditoria do Grupo 5.

# 10. Declaração de Utilização de IA

Em conformidade com as regras do pacote T08 (AI_PROVENANCE) e com as regras de trabalho estudantil, o grupo declara o seguinte:

*Tabela 33 - Utilização de IA*

|Aspeto|Declaração||
|---|---|---|
|Ferramenta utilizada|Claude (Anthropic) — assistente conversacional de IA||
|Utilização nos Checkpoints|CP01: apoio na estruturação do charter, formatação do documento Word e análise estática das regras de negócio BR-01 a BR-08. CP02: apoio na formatação e organização dos resultados da execução e na documentação das discrepâncias identificadas (DEF-01 a DEF-04). CP03: apoio na revisão dos candidatos gerados, na construção da suite final de testes e na execução dos casos; todos os resultados foram verificados de forma consciente e independente pelo grupo face às regras de negócio antes da sua aceitação no documento.||
|Verificação independente|Todas as interpretações de regras, resultados esperados e questões de clarificação foram verificadas de forma independente pelo grupo contra o texto original das BR antes de serem aceites no documento||
|ai_candidates.json|O ficheiro de candidatos IA fornecido pelo professor NÃO foi aberto nem consultado nesta fase. Será revisto apenas após o congelamento de human_cases.json, conforme CP03.||
|Código-fonte|O ficheiro shipping.py não foi inspecionado para fins de desenho de testes||
|Modelos de IA Utilizados|Geração do conjunto inicial de 12 candidatos de teste (ai_candidates.json) fornecido no início do projeto. Assistência na estruturação de scripts de automação, identificação combinatória de classes equivalentes e aceleração da redação dos artefactos de teste.||
|Atividades Assistidas vs. Validação Humana|Geração assistida: sugestão inicial de cenários de teste adicionais (F-17 a F-30) e esqueletos de scripts de verificação. Validação humana estrita: todas as asserções de entrada, parâmetros de chamada, oráculos independentes e atribuições de severidade foram derivados manualmente pelos engenheiros de teste humanos a partir das regras BR-01 a BR-08, antes de qualquer aceitação.||
|Limitações Evidenciadas pela Assistência de IA|A experiência do projeto revelou que modelos de IA apresentam uma propensão crítica para gerar oráculos tautológicos (esperar o que o código faz em vez do que a especificação exige). Os casos AI-05 e AI-06 demonstraram que, sem oráculo humano independente, os testes de IA geram falsos PASS e mascaram defeitos graves de software. A intervenção humana especializada é insubstituível para o desenho de casos de fronteira e para juízos de severidade de negócio.||
|||47|

# 11. Anexos

Entregáveis CP04:

*Tabela 34 - Entregáveis CP04*

|Ficheiro|Localização|Descrição|
|---|---|---|
|TVSI_T08_Grupo5_CP04.zip|Raiz do repositório|Pacote de entrega final com 51 ficheiros auditados|
|TVSI_T08_Grupo5_CP04.zip.sha256|Raiz do repositório|Hash SHA-256 de verificação da integridade do pacote|
|Relatorio_CP4.md|Trabalho_CP4/|Relatório de execução, auditoria e reconciliação do CP04|
|TestResults_T08_Template.xlsx|Trabalho_CP4/|Livro de cálculo oficial com 68 execuções consolidadas (324 fórmulas, 0 erros)|
|runs/final_cases_execution.json|Trabalho_CP4/runs/|Resultados da execução da suite final de 30 casos: 20 PASS / 10 FAIL|
