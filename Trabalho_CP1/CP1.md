# CP01 — Charter e Ambiente

**T08 · Desenho de Testes com Assistência de IA · Build T08-B1.0**
Data: 2026-10-22

---

## 1. Membros do Grupo e Funções

| Nome | Função | Responsabilidades |
| --- | --- | --- |
| Eduardo Dias | Coordenador / Test Lead | Charter, configuração do ambiente, revisão estática, coordenação do relatório final |
| [Nome 2] | Desenhador de Testes | Desenho humano de casos de teste, partições de equivalência, análise de fronteiras |
| [Nome 3] | Revisão IA e Execução | Classificação de candidatos IA, execução das suites de testes, recolha de evidências |
| [Nome 4] | Analista de Defeitos e Cobertura | Registo de defeitos, mapeamento de cobertura, análise de risco residual |

> Ajustar as linhas ao tamanho real do grupo. As funções podem sobrepor-se em grupos mais pequenos.

Divisão de trabalho para o CP01: Eduardo Dias — configuração do ambiente, charter, revisão estática.

---

## 2. Seleção de Tópico

**T08 — Desenho de Testes com Assistência de IA**

Objeto de teste: função `quote(weight, zone, express)` em `shipping.py`, build T08-B1.0.
A função calcula uma taxa de envio com base no peso, na zona de entrega e na opção expresso.

---

## 3. Objetivos e Âmbito

**Incluído no âmbito:**

- Revisão estática de BR-01 a BR-08 para clareza e testabilidade
- Desenho independente de casos de teste humanos (mínimo 12) usando partições de equivalência e análise de valores de fronteira
- Revisão crítica da suite candidata fornecida pela IA (`ai_candidates.json`)
- Execução das suites humana e final usando o runner fornecido
- Registo de defeitos face a resultados esperados derivados de forma independente
- Mapeamento de cobertura de requisitos (R01–R08)
- Comparação crítica da qualidade do desenho humano vs. IA

**Excluído do âmbito:**

- Inspeção do código-fonte (`shipping.py`) — T08 não o exige
- Testes de browser ou interface gráfica
- Testes de desempenho ou carga

---

## 4. Prioridades e Abordagem

1. Derivar resultados esperados de forma independente a partir de BR-01–BR-05 antes de qualquer execução
2. Congelar `human_cases.json` antes de abrir `ai_candidates.json`
3. Classificar cada candidato IA (aceitar / rever / rejeitar) com justificação
4. Executar as duas suites em separado; tratar as expectativas dos candidatos como alegações, não como oráculo
5. Registar apenas defeitos reproduzíveis; separar questões de especificação de defeitos de implementação

---

## 5. Riscos e Restrições

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Python 3.9.6 instalado (requisito: 3.10+) | O runner pode comportar-se de forma diferente do especificado; funcionalidades de sintaxe em falta | Documentar todos os resultados com a versão Python; atualizar se surgirem problemas |
| As expectativas dos candidatos IA podem conter erros | Falsa confiança em resultados errados | Todos os resultados esperados derivados de forma independente das BR antes de rever a suite IA |
| Regras de negócio com fronteiras ambíguas | Oráculo incorreto | Levantar questões de clarificação (ver Revisão Estática abaixo) |
| Restrição de tempo — CP01 com entrega a 2026-10-27 | Submissão incompleta | Charter e ambiente concluídos no CP01; desenho congelado no CP02 |

---

## 6. Plano até à Apresentação Final

| Checkpoint | Data | Entregável planeado |
| --- | --- | --- |
| CP01 | 2026-10-27 | Charter, funções, âmbito, riscos, verificação de ambiente ✅ |
| CP02 | 2026-11-03 | Revisão estática, partições de equivalência, oráculo inicial |
| CP03 | 2026-11-10 | `human_cases.json` congelado (≥12 testes), revisão dos candidatos IA, `final_cases.json` |
| CP04 | 2026-11-17 | Execuções, evidências, rascunho de defeitos |
| CP05 | 2026-11-24 | Análise de cobertura, conclusões consolidadas, riscos residuais |
| CP06 | 2026-12-09 | Relatório quase-final e demonstração |
| Entrega final | 2026-12-15 23:59 | Relatório, workbook, pasta de evidências, declaração de IA |
| Apresentação | 2026-12-16 | Apresentação de grupo de 15 minutos |

---

## 7. Registo de Ambiente

| Item | Valor |
| --- | --- |
| Sistema Operativo | macOS (Apple Silicon) |
| Versão Python | 3.9.6 (Clang 21.0.0) — abaixo do requisito declarado de 3.10+ |
| Aplicação de folha de cálculo | [ex.: Microsoft Excel / LibreOffice Calc — preencher] |
| Build em teste | T08-B1.0 |
| Runner | `run_cases.py` (fornecido, não modificado) |
| Baseline preservado | Sim — pacote original mantido sem alterações |

**Resultado da verificação de ambiente:**

```
python3 run_cases.py human_cases.json
```

```json
{
  "build": "T08-B1.0",
  "suite": "human_cases.json",
  "python": "3.9.6 (default, Aug 25 2026, 21:26:21) [Clang 21.0.0]",
  "results": [
    {
      "id": "H-ENV",
      "input": { "weight": 500, "zone": "LOCAL", "express": false },
      "expected": { "status": "OK", "fee": 5 },
      "actual":   { "status": "OK", "fee": 5 },
      "verdict": "PASS"
    }
  ]
}
```

**Veredicto: PASS.** O ambiente está funcional. A restrição de versão de Python foi registada como risco.

---

## 8. Revisão Estática — BR-01 a BR-08

Questões levantadas após leitura das regras de negócio. Não foram inventados problemas; apenas registadas ambiguidades genuínas.

| ID | Regra | Questão | Clarificação sugerida |
| --- | --- | --- | --- |
| Q-01 | BR-01 | O peso deve ser um "inteiro real, excluindo booleanos." Em Python, `bool` é uma subclasse de `int`. `True` e `False` devem devolver INVALID? | Sim — BR-01 exclui explicitamente booleanos. Esperado: INVALID, null. |
| Q-02 | BR-01 | Qual o comportamento esperado para um float como `500.0`? A regra diz "inteiro real" mas não menciona floats explicitamente. | Assumido INVALID — sem coerção conforme BR-01. A confirmar. |
| Q-03 | BR-01 | Qual o comportamento esperado para `None` como peso? | Assumido INVALID — não é um inteiro. A confirmar. |
| Q-04 | BR-04 | "O serviço expresso REMOTE não está disponível acima de 5000 g." A validação ocorre antes? Ex.: weight=25000, REMOTE, express=true → INVALID (e não UNAVAILABLE)? | Sim — BR-05 indica que a validação tem precedência sobre a disponibilidade. |

Não foram encontradas ambiguidades em BR-02, BR-03, BR-06, BR-07, BR-08.

---

## 9. Declaração de Assistência por IA

Este charter foi redigido com assistência de IA (Claude, Anthropic) para estrutura e análise estática das regras de negócio. Todos os resultados esperados e interpretações de regras foram verificados de forma independente pelo grupo face a BR-01–BR-08 antes de serem aceites. O ficheiro `ai_candidates.json` fornecido ainda não foi revisto nesta fase.
