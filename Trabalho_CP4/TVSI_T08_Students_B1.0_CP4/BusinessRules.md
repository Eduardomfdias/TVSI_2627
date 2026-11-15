# T08 — AI-Assisted Test Design
Normative rules v1.0 · Build T08-B1.0 · 20 October 2026

These rules are the independent test oracle. The supplied implementation may disagree. Use only fictitious data.

## BR-01 / R01
quote(weight,zone,express) returns status and fee (integer EUR or null/None). weight is an actual integer in grams, 1–20000 inclusive, excluding booleans. zone exactly LOCAL or REMOTE. express an actual boolean. Invalid inputs return INVALID and fee null; no trimming/coercion.

## BR-02 / R02
For LOCAL and REMOTE alike, base fee is EUR 5 for 1–1000 g inclusive; EUR 8 for 1001–5000 inclusive; EUR 12 for 5001–20000 inclusive.

## BR-03 / R03
REMOTE adds EUR 4 to the base fee. LOCAL adds nothing. Express, when available, adds EUR 6 after the remote surcharge. There is no tax or rounding.

## BR-04 / R04
REMOTE express service is unavailable above 5000 g, returning UNAVAILABLE and fee null. At exactly 5000 it is available. LOCAL express is available for every valid weight.

## BR-05 / R05
Validation has precedence over availability, which has precedence over fee calculation. No partial fee is returned for INVALID or UNAVAILABLE. Repeated calls are independent and have no side effects.

## BR-06 / R06
JSON test file is a list of objects with unique id, input containing weight/zone/express, and expected containing status/fee. JSON uses true/false/null, Python uses True/False/None. Run from app: python run_cases.py human_cases.json (Windows: py -3 may replace python). No pip packages; Python 3.10+ required.

## BR-07 / R07
The runner compares expected and actual exactly and writes <suite>.results.json. Exit code 0 means all comparisons match, 1 means at least one mismatch, 2 means the case file could not be processed. A match to a WRONG expected value is not evidence of correctness. Preserve earlier reports before overwriting.

## BR-08 / R08
Use AI_PROVENANCE for the provenance and limits of the curated candidate suite. Derive final expectations independently from BR-01–BR-05, document every accepted/revised/rejected candidate, and use the supplied offline comparison even without access to an AI service.

## Environment check
weight=500, zone=LOCAL, express=false → OK, fee=5. The single starter human case must pass.

## Comparison method
Freeze human_cases.json, review ai_candidates.json, then save final_cases.json. Run each separately. Report rule/partition/boundary coverage, incorrect expectations, duplicates, and confirmed defects under the independently corrected oracle. Report suite size and avoid counting a defect twice. The supplied material cannot establish general AI capability.
