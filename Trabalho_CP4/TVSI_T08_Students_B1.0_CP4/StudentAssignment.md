# T08 — AI-Assisted Test Design
TVSI 2026/27 · Student assignment v1.0 · For teacher review

## Your challenge
Apply **Critical comparison of human and AI test designs** to the supplied test object. You are testing supplied software, not developing an application. Python 3.10+ must be available. Open a terminal in the extracted app folder. Check `python --version` (Windows: `py -3 --version`). Use the commands in BusinessRules. No pip install, account, server or IDE is needed. If Python is unavailable, report the environment as BLOCKED and ask the teacher for a lab machine; do not invent execution results.

## 1. Plan and review
Produce a one-page charter: group members and roles, scope, risks, priorities, environment and approach. Review BR-01–BR-08 for clarity/testability. Record genuine ambiguities with suggested clarifications; do not invent issues to fill the template. Rules are the oracle, not application output.

## 2. Design before execution
Before opening ai_candidates.json, independently design at least 12 tests and freeze them in human_cases.json. Then review the supplied AI candidate set: classify every candidate as accept, revise or reject, justify against business rules, identify gaps, and build at least 16 final tests. Compare equal-sized suites where possible using rule/boundary coverage, invalid expectations, redundancy and confirmed defects. Execute both suites; candidate expectations are claims to review, not an oracle.

Put exact inputs, preconditions, expected outputs and side effects in Test Cases BEFORE executing. Link to R01–R08 and state the technique and priority. Include positive, negative and boundary cases. Separate setup from the action being tested. Record topic-specific design in Technique and attach diagrams or additional tables where useful.

## 3. Execute and report
Record build T08-B1.0, OS, browser or Python version, date, tester, exact observed output and evidence filename for every execution. Preserve earlier runs. A PASS requires every expected outcome to match. A blocked run is not a pass. Reproduce unexpected behaviour from the same initial conditions.

Log one defect per distinct reproducible issue, with exact setup/steps, rule, expected/actual, evidence and severity with rationale. Several failing cases may support one defect. Separate specification questions, data defects and implementation defects. Do not guess root causes from symptoms.

## 4. Evaluate coverage
Map requirements to tests and executions. Explain technique-specific coverage, gaps, residual risks and limitations. A high percentage or many tests does not establish correctness. Finding all planted defects is not the assessment objective.

## Submission
Submit a 4–6-page report excluding appendices, completed workbook, charter, topic-specific design records, evidence folder and a 15-minute group presentation. Include individual contributions and AI disclosure (tool, purpose, material used, independent verification). Every member must explain and reproduce selected tests. Do not claim supplied software as your development.

Suggested report: scope/risks; static review; design/oracle; executions/findings; coverage/limitations; contributions. Assessment weights, group rules and deadlines are those confirmed by the teacher.

## Proposed checkpoints

| Proposed date (2026) | Evidence checkpoint |
|---|---|
| 27 October | Charter, roles, scope, risks, environment check |
| 3 November | Static review, model/partitions, initial oracle |
| 10 November | Designed tests and expected results before execution |
| 17 November | Executions, reproducible evidence and draft defects |
| 24 November | Consolidated findings, coverage and remaining risks |
| 9 December | Near-final report and demonstration for feedback |
| 15 December, 23:59 (Portugal local time) | Final submission |
| 16 December | Final presentation |

Dates and submission times require teacher confirmation in Moodle. Do not infer a weekly class day from this table.
