"""CP4 — constrói human_cases.json e final_cases.json e valida os expected contra o oráculo BR.
O oráculo é derivado exclusivamente de BR-01..BR-05 (não importa shipping.py)."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
APP = ROOT / "Trabalho_CP4" / "TVSI_T08_Students_B1.0_CP4" / "app"

def oracle(weight, zone, express):
    if type(weight) is not int or not (1 <= weight <= 20000) or zone not in ("LOCAL", "REMOTE") or type(express) is not bool:
        return {"status": "INVALID", "fee": None}
    if zone == "REMOTE" and express and weight > 5000:
        return {"status": "UNAVAILABLE", "fee": None}
    fee = 5 if weight <= 1000 else 8 if weight <= 5000 else 12
    return {"status": "OK", "fee": fee + (4 if zone == "REMOTE" else 0) + (6 if express else 0)}

starter = json.loads((ROOT / "TVSI_T08_Students_B1.0" / "app" / "human_cases.json").read_text())   # H-ENV (professor)
cp2 = json.loads((ROOT / "Trabalho_CP2" / "human_cases.json").read_text())                          # H-01..H-16 congelados
cp3 = json.loads((ROOT / "Trabalho_CP3" / "final_cases.json").read_text())
ai = json.loads((ROOT / "TVSI_T08_Students_B1.0" / "app" / "ai_candidates.json").read_text())

human = starter + cp2
f_cases = [c for c in cp3 if c["id"].startswith("F-")]          # F-17..F-21 (F-17=AI-11, F-18=AI-12, F-19=AI-09 revisto)
decisions = {"AI-01": "accept", "AI-02": "accept", "AI-03": "accept", "AI-04": "accept",
             "AI-05": "revise", "AI-06": "revise", "AI-07": "accept", "AI-08": "accept",
             "AI-09": "revise", "AI-10": "reject", "AI-11": "accept", "AI-12": "accept"}
already_as_f = {"AI-09": "F-19", "AI-11": "F-17", "AI-12": "F-18"}
ai_new = []
for c in ai:
    d = decisions[c["id"]]
    if d == "reject" or c["id"] in already_as_f:
        continue
    ai_new.append({"id": c["id"], "input": c["input"], "expected": oracle(**c["input"])})
final = human + f_cases + ai_new

errors = [c["id"] for c in final if oracle(**c["input"]) != c["expected"]]
assert not errors, f"expected divergente do oráculo: {errors}"
assert len({c["id"] for c in final}) == len(final), "IDs duplicados"
for c in f_cases:   # F-17..F-19 devem ter os mesmos inputs que os AI correspondentes
    pass
for a, f in already_as_f.items():
    ai_in = next(c["input"] for c in ai if c["id"] == a); f_in = next(c["input"] for c in f_cases if c["id"] == f)
    assert ai_in == f_in, (a, f)

(APP / "human_cases.json").write_text(json.dumps(human, indent=2) + "\n", encoding="utf-8")
(APP / "final_cases.json").write_text(json.dumps(final, indent=2) + "\n", encoding="utf-8")
print(f"human_cases.json: {len(human)} casos | final_cases.json: {len(final)} casos ({len(human)} humanos + {len(f_cases)} F + {len(ai_new)} AI)")
for c in ai:
    exp = oracle(**c["input"]); ok = exp == c["expected"]
    print(f"{c['id']}: IA={c['expected']} oráculo={exp} {'✓' if ok else '✗'} -> {decisions[c['id']]}{' ('+already_as_f[c['id']]+')' if c['id'] in already_as_f else ''}")
