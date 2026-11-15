"""Verificação independente: oráculo derivado só das BR (não importa shipping.py)."""
import json, sys, pathlib
def oracle(weight, zone, express):
    if type(weight) is not int or not (1 <= weight <= 20000) or zone not in ("LOCAL","REMOTE") or type(express) is not bool:
        return {"status":"INVALID","fee":None}
    if zone=="REMOTE" and express and weight>5000:
        return {"status":"UNAVAILABLE","fee":None}
    fee = 5 if weight<=1000 else 8 if weight<=5000 else 12
    fee += (4 if zone=="REMOTE" else 0) + (6 if express else 0)
    return {"status":"OK","fee":fee}
root = pathlib.Path(sys.argv[1])
cases = json.loads(pathlib.Path("Trabalho_CP3/final_cases.json").read_text())
human = json.loads(pathlib.Path("Trabalho_CP2/human_cases.json").read_text())
ok = True
for c in cases:
    if oracle(**c["input"]) != c["expected"]:
        ok=False; print("ORÁCULO DIVERGE:", c["id"])
print("expected == oráculo BR:", ok, f"({len(cases)} casos)")
print("H-01..H-16 idênticos a CP2:", cases[:16]==human)
for tag in ("py312","py39"):
    r = json.loads((root/f"final_cases.results.{tag}.json").read_text())
    p = sum(x["verdict"]=="PASS" for x in r["results"])
    fails = [x["id"] for x in r["results"] if x["verdict"]=="FAIL"]
    print(f"{tag}: Python {r['python'].split()[0]} | {p} PASS / {len(fails)} FAIL | FAILs: {', '.join(fails)}")
prev = json.loads(pathlib.Path("Trabalho_CP3/final_cases.results.py312.json").read_text())["results"]
new = json.loads((root/"final_cases.results.py312.json").read_text())["results"]
print("Paridade com execução anterior (py312):", prev==new)
a = json.loads((root/"final_cases.results.py39.json").read_text())["results"]
print("Paridade py312 vs py39:", a==new)
for tag in ("py312","py39"):
    b = json.loads((root/f"br05_independence.{tag}.json").read_text())
    print(f"BR-05 {tag}:", b.get("verdict") or b.get("overall_verdict") or {k:v for k,v in b.items() if 'verdict' in k.lower()})
