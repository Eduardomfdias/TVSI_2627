"""CP4 — atualiza a CÓPIA do workbook (Trabalho_CP4/TVSI_T08_Students_B1.0_CP4) com:
Test Cases (AI-01..AI-08), Executions (run_01..run_03), Defects (evidência CP4 + defeitos de dados),
Technique (revisão IA do CP4) e Coverage (novas ligações). Expected sempre derivado do oráculo BR."""
import copy, json, pathlib, sys
import openpyxl
from openpyxl.formatting.rule import Rule
from openpyxl.worksheet.datavalidation import DataValidation

CP4 = pathlib.Path(__file__).resolve().parents[1]
PKG = CP4 / "TVSI_T08_Students_B1.0_CP4"
EVID = CP4 / "evidence"
WB = PKG / "TestResults_T08_Template.xlsx"
ENV = "2026-11-15 / macOS 27.2.1, Python 3.12.16, T08-B1.0"
TESTER = "Grupo 5 (execução assistida por Claude Code) / run_cases.py"
NEW_LAST = 90  # Executions passa de 80 para 86 linhas úteis (5..90)


def oracle(weight, zone, express):
    if type(weight) is not int or not (1 <= weight <= 20000) or zone not in ("LOCAL", "REMOTE") or type(express) is not bool:
        return {"status": "INVALID", "fee": None}
    if zone == "REMOTE" and express and weight > 5000:
        return {"status": "UNAVAILABLE", "fee": None}
    fee = 5 if weight <= 1000 else 8 if weight <= 5000 else 12
    return {"status": "OK", "fee": fee + (4 if zone == "REMOTE" else 0) + (6 if express else 0)}


def js(d):
    return json.dumps(d, ensure_ascii=False)


def copy_style(src, dst):
    dst.font, dst.fill, dst.border = copy.copy(src.font), copy.copy(src.fill), copy.copy(src.border)
    dst.alignment, dst.number_format, dst.protection = copy.copy(src.alignment), src.number_format, copy.copy(src.protection)


def first_empty(ws, col=1, start=5):
    r = start
    while ws.cell(r, col).value not in (None, ""):
        r += 1
    return r


wb = openpyxl.load_workbook(WB)

# ---------------------------------------------------------------- Test Cases
tc = wb["Test Cases"]
existing = {tc.cell(r, 1).value for r in range(5, 85)}
ai = {c["id"]: c for c in json.loads((PKG / "app" / "ai_candidates.json").read_text())}
tc_rows = {
    "AI-01": ("EP", "BR-02, BR-03: Tier 1 LOCAL standard (candidato IA aceite; mesmos inputs que H-01)", "Medium"),
    "AI-02": ("EP", "BR-02: Ponto interior do Tier 2 (2000g) LOCAL standard (candidato IA aceite)", "Medium"),
    "AI-03": ("EP", "BR-02: Ponto interior do Tier 3 (6000g) LOCAL standard (candidato IA aceite)", "Medium"),
    "AI-04": ("EP", "BR-03: Express LOCAL Tier 1 (5+6=11€) (candidato IA aceite; mesmos inputs que H-11)", "Medium"),
    "AI-05": ("EP", "BR-03: REMOTE standard Tier 1 (5+4=9€) — candidato IA REVISTO (IA esperava fee=4)", "High"),
    "AI-06": ("BVA", "BR-02: Fronteira superior Tier 1 (1000g → 5€) — candidato IA REVISTO (IA esperava fee=8)", "High"),
    "AI-07": ("BVA", "BR-01: weight=0 abaixo do mínimo → INVALID (candidato IA aceite; mesmos inputs que H-08)", "Medium"),
    "AI-08": ("BVA", "BR-01: weight=20001 acima do máximo → INVALID (candidato IA aceite; mesmos inputs que H-09)", "Medium"),
}
r = first_empty(tc)
for tid, (tech, obj, prio) in tc_rows.items():
    if tid in existing:
        continue
    inp = ai[tid]["input"]
    args = f"{inp['weight']}, '{inp['zone']}', {inp['express']}"
    vals = [tid, tech, obj, "Build T08-B1.0, Python 3.10+, terminal na pasta app", js(inp),
            f"Executar quote({args}) via run_cases.py final_cases.json", js(oracle(**inp)), "Nenhum (função pura)", prio]
    for c, v in enumerate(vals, 1):
        tc.cell(r, c, v)
        copy_style(tc.cell(r - 1, c), tc.cell(r, c))
    r += 1
expected_by_id = {tc.cell(r, 1).value: tc.cell(r, 7).value for r in range(5, 85) if tc.cell(r, 1).value}

# ---------------------------------------------------------------- Executions (estender tabela para 90)
ex = wb["Executions"]
ex.tables["ExecutionsTable"].ref = f"A4:I{NEW_LAST}"
for row in range(85, NEW_LAST + 1):
    for c in range(1, 10):
        copy_style(ex.cell(84, c), ex.cell(row, c))
ex.data_validations.dataValidation = []
dv = DataValidation(type="list", formula1='"NOT RUN,PASS,FAIL,BLOCKED"', allow_blank=True)
dv.add(f"G5:G{NEW_LAST}")
ex.add_data_validation(dv)
old_cf = ex.conditional_formatting
rules = [rule for cf in old_cf for rule in cf.rules]
ex.conditional_formatting = type(old_cf)()
for rule in rules:
    ex.conditional_formatting.add(f"G5:G{NEW_LAST}", rule)

defect_for = {  # mapeamento observado→defeito (DEF-01..04 já registados no CP2/CP3)
    "H-03": "DEF-02", "AI-06": "DEF-02", "H-07": "DEF-01",
    "H-10": "DEF-03", "H-12": "DEF-03", "H-13": "DEF-03", "F-18": "DEF-03", "AI-05": "DEF-03", "AI-12": "DEF-03",
    "H-14": "DEF-04", "F-19": "DEF-04", "AI-09": "DEF-04",
}
data_defect = {"AI-05": "DEF-05", "AI-06": "DEF-06", "AI-09": "DEF-07"}
last_run = max(int(ex.cell(r, 1).value.split("-")[1]) for r in range(5, 85) if ex.cell(r, 1).value)
r = first_empty(ex)
runs = [("run_01_human_20261115.results.json", "human_cases.json"),
        ("run_02_ai_20261115.results.json", "ai_candidates.json"),
        ("run_03_final_20261115.results.json", "final_cases.json")]
summary = {}
for fname, suite in runs:
    rep = json.loads((EVID / fname).read_text())
    assert rep["python"].startswith("3.12.16"), rep["python"]
    p = f = 0
    for res in rep["results"]:
        last_run += 1
        tid, actual = res["id"], res["actual"]
        oracle_exp = oracle(**res["input"])
        verdict = "PASS" if actual == oracle_exp else "FAIL"
        p += verdict == "PASS"; f += verdict == "FAIL"
        note = f"{TESTER} / suite {suite}"
        if suite == "ai_candidates.json":
            note += f" / veredicto do runner: {res['verdict']} (contra expected da IA {js(res['expected'])})"
            if res["verdict"] != verdict:
                note += " — divergente do oráculo BR: um match com expected errado não é evidência (BR-07)"
            if tid == "AI-10":
                note += " / candidato rejeitado (duplicado de AI-01/H-01)"
        defects = defect_for.get(tid, "") if verdict == "FAIL" else ""
        if suite == "ai_candidates.json" and tid in data_defect:
            defects = ", ".join(x for x in (defects, data_defect[tid]) if x)
        vals = [f"RUN-{last_run:02d}", tid, ENV, js(actual), "Nenhum observado", note, verdict,
                f"Trabalho_CP4/evidence/{fname}#{tid}", defects or None]
        for c, v in enumerate(vals, 1):
            ex.cell(r, c, v)
        r += 1
    summary[suite] = (p, f)
assert r - 1 <= NEW_LAST, f"Executions excede a capacidade ({r-1})"

# ---------------------------------------------------------------- Coverage (fórmulas → novo intervalo)
cv = wb["Coverage"]
for row in cv.iter_rows():
    for c in row:
        if isinstance(c.value, str) and c.value.startswith("="):
            c.value = c.value.replace("Executions!$B$5:$B$84", f"Executions!$B$5:$B${NEW_LAST}") \
                             .replace("Executions!$G$5:$G$84", f"Executions!$G$5:$G${NEW_LAST}")
links = {(cv.cell(r, 1).value, cv.cell(r, 2).value) for r in range(21, 121)}
new_links = [("R01", "AI-06"), ("R01", "AI-07"), ("R01", "AI-08"),
             ("R02", "AI-01"), ("R02", "AI-02"), ("R02", "AI-03"), ("R02", "AI-06"),
             ("R03", "AI-04"), ("R03", "AI-05"),
             ("R07", "AI-05"), ("R07", "AI-06")] + [("R08", f"AI-0{i}") for i in range(1, 9)]
r = first_empty(cv, start=21)
for a, b in new_links:
    if (a, b) in links:
        continue
    cv.cell(r, 1, a); cv.cell(r, 2, b)
    r += 1
assert r - 1 <= 120

# ---------------------------------------------------------------- Technique (revisão IA do CP4)
te = wb["Technique"]
tech = {
    "AI-01": ("Accept", "Expected correto (BR-02). Mesmos inputs que H-01; aceite no CP4 para comparação de suites de igual tamanho (redundância assinalada).", "AI-01"),
    "AI-02": ("Accept", "Expected correto (8€, BR-02). Ponto interior do Tier 2, complementa as fronteiras H-04/H-05.", "AI-02"),
    "AI-03": ("Accept", "Expected correto (12€, BR-02). Ponto interior do Tier 3, complementa as fronteiras H-06/H-07.", "AI-03"),
    "AI-04": ("Accept", "Expected correto (5+6=11€, BR-03). Mesmos inputs que H-11 (redundância assinalada).", "AI-04"),
    "AI-05": ("Revise", "Expected errado: IA indicou 4€ (só o suplemento REMOTE). Oráculo BR-02+BR-03: 5+4=9€. Incluído com expected corrigido.", "AI-05"),
    "AI-06": ("Revise", "Expected errado: IA tratou 1000g como Tier 2 (8€). BR-02: 1–1000g inclusive → 5€. Incluído com expected corrigido.", "AI-06"),
    "AI-07": ("Accept", "Expected correto (BR-01, weight=0 → INVALID). Mesmos inputs que H-08.", "AI-07"),
    "AI-08": ("Accept", "Expected correto (BR-01, weight=20001 → INVALID). Mesmos inputs que H-09.", "AI-08"),
    "AI-09": ("Revise", "Expected errado: IA ignorou BR-04 (OK/22). REMOTE+express+6000g>5000 → UNAVAILABLE/null. Mantido como F-19 (ID do CP3).", "F-19"),
    "AI-10": ("Reject", "Duplicado exato de AI-01 (e de H-01) dentro do próprio conjunto IA; sem valor adicional.", "-"),
    "AI-11": ("Accept", "Expected correto (12+6=18€). Lacuna da suite humana (Tier 3 LOCAL express). Mantido como F-17 (ID do CP3).", "F-17"),
    "AI-12": ("Accept", "Expected correto (8+4=12€). Lacuna da suite humana (Tier 2 REMOTE). Mantido como F-18 (ID do CP3).", "F-18"),
}
for r in range(5, 45):
    cid = te.cell(r, 1).value
    if cid in tech:
        dec, why, final_id = tech[cid]
        te.cell(r, 4, f"{oracle(**ai[cid]['input'])['status']}, fee={oracle(**ai[cid]['input'])['fee'] if oracle(**ai[cid]['input'])['fee'] is not None else 'null'}")
        te.cell(r, 5, dec); te.cell(r, 6, why); te.cell(r, 7, final_id)
        te.cell(r, 8, f"ai_candidates.json#{cid}; execução: Trabalho_CP4/evidence/run_02_ai_20261115.results.json#{cid}")

# ---------------------------------------------------------------- Defects
de = wb["Defects"]
setup = "Build T08-B1.0 / macOS 27.2.1 / Python 3.12.16 (BR-06 3.10+)"
cmd = "cd app && python run_cases.py final_cases.json"
impl = {
    "DEF-01": ("[Implementação] weight=20000 (máximo válido) devolvido como INVALID — H-07", "BR-01",
               '{"weight": 20000, "zone": "LOCAL", "express": false}', "run_01#H-07; run_03#H-07",
               "Alta / Rejeita o peso máximo permitido pela regra; perda de serviço numa fronteira válida"),
    "DEF-02": ("[Implementação] weight=1000 cobrado como Tier 2 (8€ em vez de 5€) — H-03, AI-06", "BR-02",
               '{"weight": 1000, "zone": "LOCAL", "express": false}', "run_01#H-03; run_03#H-03,#AI-06",
               "Média / Sobrecobrança de 3€ numa única fronteira; restante Tier 1 correto"),
    "DEF-03": ("[Implementação] Zona REMOTE devolve fee=4 (+6 se express) em vez de base+4 — H-10, H-12, H-13, F-18, AI-05", "BR-03",
               '{"weight": 500, "zone": "REMOTE", "express": false}', "run_01#H-10,#H-12,#H-13; run_03#F-18,#AI-05; run_02#AI-12",
               "Alta / Fee errada em todos os pedidos REMOTE OK observados (5 casos, 3 tiers)"),
    "DEF-04": ("[Implementação] REMOTE express acima de 5000g devolve OK em vez de UNAVAILABLE — H-14, F-19", "BR-04",
               '{"weight": 5001, "zone": "REMOTE", "express": true}', "run_01#H-14; run_03#F-19; run_02#AI-09",
               "Alta / Serviço indisponível é vendido e cobrado; viola regra de disponibilidade"),
}
for r in range(5, 45):
    did = de.cell(r, 1).value
    if did in impl:
        title, rule, inp, ev, sev = impl[did]
        de.cell(r, 2, title)
        de.cell(r, 3, f"{rule} / {setup}")
        de.cell(r, 4, f"1) {cmd}  2) caso com input {inp}  (equivalente: quote(**input))")
        de.cell(r, 5, js(oracle(**json.loads(inp))))
        de.cell(r, 7, f"Trabalho_CP4/evidence/{ev}")
        de.cell(r, 8, sev)
        de.cell(r, 9, "Confirmado em CP4 (reproduzido) / Aberto")
data = [
    ("DEF-05", "[Dados — ai_candidates.json] AI-05 com expected incorreto (fee=4)", "AI-05",
     "O runner dá PASS ao AI-05 porque o expected errado coincide com o output defeituoso: o DEF-03 fica mascarado nessa suite.",
     "Média / Expectativa errada produz falso PASS e esconde um defeito de implementação"),
    ("DEF-06", "[Dados — ai_candidates.json] AI-06 com expected incorreto (fee=8 a 1000g)", "AI-06",
     "O runner dá PASS ao AI-06 porque o expected errado coincide com o output defeituoso: o DEF-02 fica mascarado nessa suite.",
     "Média / Expectativa errada produz falso PASS e esconde um defeito de fronteira"),
    ("DEF-07", "[Dados — ai_candidates.json] AI-09 com expected incorreto (OK/22 em vez de UNAVAILABLE)", "AI-09",
     "O runner dá FAIL ao AI-09 (actual OK/10 ≠ OK/22), mas a falha resulta de uma expectativa errada; só com o oráculo BR-04 se identifica o DEF-04.",
     "Baixa / Expectativa errada; o FAIL é verdadeiro por acaso, mas o diagnóstico seria enganador"),
]
r = first_empty(de)
have = {de.cell(x, 1).value for x in range(5, 45)}
for did, title, cid, obs, sev in data:
    if did in have:
        continue
    inp = ai[cid]["input"]
    vals = [did, title, f"BR-08 (e {('BR-03' if cid=='AI-05' else 'BR-02' if cid=='AI-06' else 'BR-04')}) / {setup}",
            f"1) cd app && python run_cases.py ai_candidates.json  2) ler {cid}: input {js(inp)}, expected {js(ai[cid]['expected'])}",
            f"expected derivado das BR: {js(oracle(**inp))}", f"expected no ficheiro IA: {js(ai[cid]['expected'])}. {obs}",
            f"Trabalho_CP4/evidence/run_02_ai_20261115.results.json#{cid}", sev,
            "Confirmado / Corrigido na suite final (revise)" if cid != "AI-09" else "Confirmado / Corrigido na suite final como F-19 (revise)"]
    for c, v in enumerate(vals, 1):
        de.cell(r, c, v)
        copy_style(de.cell(r - 1, c), de.cell(r, c))
    r += 1

wb.save(WB)
print("Workbook atualizado:", WB)
for s, (p, f) in summary.items():
    print(f"  {s}: {p} PASS / {f} FAIL (veredicto manual contra o oráculo BR)")
