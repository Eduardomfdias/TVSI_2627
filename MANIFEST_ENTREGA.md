# Manifesto Oficial de Entregáveis — TVSI_2627 (CP01, CP02 e CP03)

**Unidade Curricular:** Tecnologias e Verificação de Sistemas de Informação 2026/27  
**Instituição:** Universidade do Minho — Mestrado em Engenharia Informática  
**Trabalho:** T08 — Desenho de Testes com Assistência de IA  
**Grupo:** Grupo 5 (*Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa*)  
**Arquivo de Entrega:** `TVSI_T08_Grupo5_CP03.zip`  
**Hash SHA-256 do Arquivo ZIP:** `8e7527a5d013229c4e52dcb247181af090bad5abba1b491056d5cbcec46bc83c`  
**Dimensão do Arquivo ZIP:** 111.231 bytes  
**Data:** 09 de Novembro de 2026  
**Total de Entregáveis:** 28 ficheiros  

---

## 1. Inventário Detalhado dos Ficheiros do Pacote de Submissão

| # | Ficheiro | Tamanho | Categoria | Finalidade / Descrição | Ambiente / Versão | Estado |
|---|---|---:|---|---|---|:---:|
| 01 | `Relatorio_Consolidado.md` | 24,402 B | Documentação Académica | Relatório Consolidado Principal | Todos | **Validado** |
| 02 | `README.md` | 11,533 B | Documentação Técnica | Instruções Gerais e Mapa do Repositório | Geral | **Validado** |
| 03 | `CLAUDE.md` | 2,179 B | Documentação de Suporte | Diretrizes e Convenções de Engenharia | Geral | **Validado** |
| 04 | `TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx` | 30,709 B | Folha de Cálculo | Workbook Oficial Preenchido (6 folhas) | Excel / OpenXML | **Auditado e Validado** |
| 05 | `TVSI_T08_Students_B1.0/BusinessRules.md` | 2,693 B | Especificação Normativa | Especificação das Regras de Negócio BR-01 a BR-08 | Oficial Docente | **Preservado** |
| 06 | `TVSI_T08_Students_B1.0/StudentAssignment.md` | 4,044 B | Enunciado | Enunciado e Requisitos de Avaliação | Oficial Docente | **Preservado** |
| 07 | `TVSI_T08_Students_B1.0/START_HERE.md` | 2,034 B | Guia Docente | Instruções de Inicialização da Baseline | Oficial Docente | **Preservado** |
| 08 | `TVSI_T08_Students_B1.0/AI_PROVENANCE.md` | 4,714 B | Declaração de IA | Declaração de Proveniência de IA e Cronologia | Geral | **Auditado e Validado** |
| 09 | `TVSI_T08_Students_B1.0/app/shipping.py` | 628 B | Código Fonte em Teste | Implementação sob Teste (função quote) | Python 3.10+ | **Preservado (não alterado)** |
| 10 | `TVSI_T08_Students_B1.0/app/run_cases.py` | 1,251 B | Ferramenta de Teste | Runner Oficial de Testes JSON | Python 3 | **Preservado** |
| 11 | `TVSI_T08_Students_B1.0/app/human_cases.json` | 195 B | Suite Técnica | Caso Técnico Starter de Ambiente (H-ENV) | CP01 | **Validado** |
| 12 | `TVSI_T08_Students_B1.0/app/human_cases.results.json` | 461 B | Evidência Técnica | Evidência de Execução de H-ENV | Python 3.9.6 | **Validado** |
| 13 | `TVSI_T08_Students_B1.0/app/ai_candidates.json` | 2,313 B | Fixture de IA | Conjunto de 12 Candidatos Gerados por IA | Oficial Docente | **Auditado** |
| 14 | `Trabalho_CP1/CP1.md` | 6,892 B | Documentação CP01 | Relatório de Checkpoint 1 (Charter e Ambiente) | CP01 | **Validado** |
| 15 | `Trabalho_CP1/TestResults_T08_Template.xlsx` | 30,709 B | Folha de Cálculo | Cópia de Trabalho do Workbook | Excel / OpenXML | **Auditado e Validado** |
| 16 | `Trabalho_CP2/CP2.md` | 13,756 B | Documentação CP02 | Especificação do Oráculo e Modelo de Teste | CP02 | **Validado** |
| 17 | `Trabalho_CP2/Relatorio_CP2.md` | 12,676 B | Documentação CP02 | Relatório de Checkpoint 2 (Suite Humana Congelada) | CP02 | **Validado** |
| 18 | `Trabalho_CP2/human_cases.json` | 2,219 B | Suite de Teste | Suite Humana Congelada (16 casos: H-01 a H-16) | CP02 (Frozen) | **Intacto (Commit 54ec4d3)** |
| 19 | `Trabalho_CP2/human_cases.results.json` | 4,971 B | Evidência CP02 | Evidência de Execução da Suite Humana | Python 3.9.6 | **Validado (10 PASS / 6 FAIL)** |
| 20 | `Trabalho_CP3/CP3.md` | 6,787 B | Documentação CP03 | Planeamento de Revisão dos Candidatos IA | CP03 | **Validado** |
| 21 | `Trabalho_CP3/Relatorio_CP3.md` | 22,345 B | Documentação CP03 | Relatório de Checkpoint 3 (Revisão e Suite Final) | CP03 | **Validado** |
| 22 | `Trabalho_CP3/final_cases.json` | 2,926 B | Suite de Teste | Suite Final Combinada (21 casos: H-01..16 + F-17..21) | CP03 Final | **Validado (21 casos)** |
| 23 | `Trabalho_CP3/final_cases.results.json` | 6,491 B | Evidência CP03 | Evidência da Suite Final sob Python 3.9.6 (Baseline) | Python 3.9.6 | **Validado (13 PASS / 8 FAIL)** |
| 24 | `Trabalho_CP3/final_cases.results.py312.json` | 6,503 B | Evidência CP03 | Evidência da Suite Final sob Python 3.12.7 (Conformidade) | Python 3.12.7 | **Validado (13 PASS / 8 FAIL)** |
| 25 | `Trabalho_CP3/verify_br05_independence.py` | 10,347 B | Automação QA | Script de Verificação das 4 Propriedades BR-05 | Python 3 | **Auditado e Validado** |
| 26 | `Trabalho_CP3/br05_independence.results.json` | 6,159 B | Evidência BR-05 | Evidência de Validação BR-05 sob Python 3.9.6 | Python 3.9.6 | **Validado (PASS 4/4)** |
| 27 | `Trabalho_CP3/br05_independence.py312.json` | 6,171 B | Evidência BR-05 | Evidência de Validação BR-05 sob Python 3.12.7 | Python 3.12.7 | **Validado (PASS 4/4)** |
| 28 | `Trabalho_CP3/audit_project.py` | 13,014 B | Automação QA | Script de Auditoria Automatizada do Projeto | Python 3 | **Validado (29/29 PASS)** |

---

## 2. Tabela de Verificação de Integridade Criptográfica (SHA-256)

Para garantia estrita de integridade académica e não-adulteração, apresentam-se os hashes SHA-256 de todos os artefactos incluídos no pacote de entrega:

```text
a3bfb62da5843cd91b8fa2175918541fc181c32c81d09dfd3ddd86eb5b697bb3  Relatorio_Consolidado.md
0ebf95c420bf1f38a3ad4dce11216cfc1f34fd806e42b45a2def9989a79ad420  README.md
24468175d9c2783d8735cad09ea0c8ba39dc5b7bdaea1a3c462c5e7e7a76b2eb  CLAUDE.md
b541a1e993f23c3df1a653201035a3f6c166cf68b0acd3e2f35ec45464e9f88e  TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx
a0afab852b1623104ec7a964d95f1e197d45337e1a8b4d336aa09078c707e6d8  TVSI_T08_Students_B1.0/BusinessRules.md
871ab128db61a2297e65df6bbe9b60d1e45e1ec1704d49f070d6145903ef79af  TVSI_T08_Students_B1.0/StudentAssignment.md
f211b901987a97f44591e2312caf5c58a5063ef9da699168524051c93056cddf  TVSI_T08_Students_B1.0/START_HERE.md
f365eef25a652acb4f8ec6d33d97dc73324b5dbcebaa85119ab2e86c1070d309  TVSI_T08_Students_B1.0/AI_PROVENANCE.md
693d5db56573f0458c99d8ab00073cb99400133c40d3f3eb5294033aa8029077  TVSI_T08_Students_B1.0/app/shipping.py
36e1f23173dbf7c4e187910e65e1e02c7bcdea963c8f1b4b68425f60eb36c293  TVSI_T08_Students_B1.0/app/run_cases.py
ffe07ffc79ef6d516abea5dc63c63c77f1bdd7904d36ed2e599fafc9b2486120  TVSI_T08_Students_B1.0/app/human_cases.json
7a80d2519815908be981d945946c74af4c0cb61a31954d934bf257aa8a80fe5a  TVSI_T08_Students_B1.0/app/human_cases.results.json
d526115a176803dca2d3c547072b46af615b4a6b4f2927b6cd11d710e02e2f81  TVSI_T08_Students_B1.0/app/ai_candidates.json
75750f810997fb1537dcde6fa2f96b8f49cd0c8b2f99dbd9dfed9de9597d3879  Trabalho_CP1/CP1.md
b541a1e993f23c3df1a653201035a3f6c166cf68b0acd3e2f35ec45464e9f88e  Trabalho_CP1/TestResults_T08_Template.xlsx
09bd75c968114813b0ca2d800214ea9653888c357c7c230430eac7908f8e645d  Trabalho_CP2/CP2.md
cb00ceb0a319a7d3d40be5679674a75c8c755c32a237388ab2feacd92824fd83  Trabalho_CP2/Relatorio_CP2.md
18d6d52445c09afaef1e8fd8d3509f0bb040d3d32d6e44359aa843ff707d7fca  Trabalho_CP2/human_cases.json
985641b54ebd741786b91c7e85300d35e8a07cbefc9e445ca52cef74b88e38d8  Trabalho_CP2/human_cases.results.json
eab977f06306025ef2f1a75db75eeced4895f71ae03762eb1b38e0652b281d27  Trabalho_CP3/CP3.md
352a8b572daaa69eefec27cc7a575eb17c6516c27d76b34fcf829338a652d926  Trabalho_CP3/Relatorio_CP3.md
1c281acc25633f164ae9c1683c452809a2d333a7ca860efe50fcffe42c23fd26  Trabalho_CP3/final_cases.json
2e45f0f76f78bc5c448d216138eb591d886215f3fe8d3141b391d9546e848eaa  Trabalho_CP3/final_cases.results.json
11947899754c2672cc3cd11922c50d60079dbb162b85d5263bf1cd5f6d2ab343  Trabalho_CP3/final_cases.results.py312.json
61e53b7e18449b64f7d3542cdc761d40b1699257bf13a6f5ee1a456d43a8ad6a  Trabalho_CP3/verify_br05_independence.py
45765b7ac95f31aee29c338d98cdf6a667b6f1db0e7f4d2a59fc490df0919f25  Trabalho_CP3/br05_independence.results.json
c0b4c114d85bd29050bb536fba5a9bb965b648af66df43d09eab6295f42ebe74  Trabalho_CP3/br05_independence.py312.json
75d6ded567dea1271f8ac6e927dea53416dde156a327a99244c85edbfd61b977  Trabalho_CP3/audit_project.py
```

---

## 3. Conformidade das Regras de Entrega
1. **Preservação da Suite Congelada:** `Trabalho_CP2/human_cases.json` é rigorosamente idêntico ao commit de congelamento `54ec4d3`.
2. **Preservação do Objeto sob Teste:** `TVSI_T08_Students_B1.0/app/shipping.py` foi preservado sem alterações à baseline original.
3. **Paridade de Ambientes:** As evidências de execução da suite final (`final_cases.results.json` e `final_cases.results.py312.json`) comprovam paridade de resultados (13 PASS / 8 FAIL) entre Python 3.9.6 e Python 3.12.7.
4. **Independência BR-05:** Comprovada em 4 dimensões com veredicto global PASS (`br05_independence.results.json` e `br05_independence.py312.json`).
5. **Rastreabilidade de Defeitos:** DEF-01 a DEF-04 mapeados com rigor sem contradições (H-13 associado exclusivamente a DEF-03).
