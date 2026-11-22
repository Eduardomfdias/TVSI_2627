"""T6 — comparação humano vs IA (suites de igual dimensão) e classificação black-box de sintomas.

Uso: python analise_t6.py <pasta results do run CP5>
Os defeitos são atribuídos por padrão de input/output observado face ao oráculo das BR, nunca pelo código.
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from oracle import oracle  # noqa: E402

BOUNDS = [0, 1, 1000, 1001, 5000, 5001, 20000, 20001]


def weight_class(w):
    if type(w) is bool:
        return "bool"
    if w is None or isinstance(w, str):
        return "null/str"
    if isinstance(w, float):
        return "float"
    if w <= 0:
        return "<=0"
    if w <= 1000:
        return "T1"
    if w <= 5000:
        return "T2"
    if w <= 20000:
        return "T3"
    return ">20000"


def zone_class(z):
    return z if z in ("LOCAL", "REMOTE") and type(z) is str else "inválida"


def express_class(e):
    return str(e) if type(e) is bool else "inválido"


def partitions(inp):
    w, z, e = inp["weight"], inp["zone"], inp["express"]
    p = {"W:" + weight_class(w), "Z:" + zone_class(z), "E:" + express_class(e)}
    valid = oracle(w, z, e)["status"] != "INVALID"
    if valid and e is True:
        p.add("AV:REMOTE<=5000" if z == "REMOTE" and w <= 5000 else
              "AV:REMOTE>5000" if z == "REMOTE" else "AV:LOCAL-express")
    return p


def requirements(inp):
    w, z, e = inp["weight"], inp["zone"], inp["express"]
    o = oracle(w, z, e)
    r = {"R01"}
    if o["status"] == "OK":
        r.add("R02")
        if z == "REMOTE" or e is True:
            r.add("R03")
    if o["status"] != "INVALID" and e is True:
        r.add("R04")
    if o["status"] == "INVALID" and z == "REMOTE" and e is True:
        r.add("R05")
    if o["status"] == "UNAVAILABLE":
        r.add("R05")
    return r


def boundaries(inp):
    w, z, e = inp["weight"], inp["zone"], inp["express"]
    b = {f"W={w}" for x in BOUNDS if type(w) is int and w == x}
    if z == "REMOTE" and e is True and w in (5000, 5001):
        b.add(f"REMOTE-express={w}")
    return b


def symptom(inp, actual):
    """Defeito exposto pelo input sob o oráculo corrigido (classificação por sintoma observado)."""
    w, z, e = inp["weight"], inp["zone"], inp["express"]
    o = oracle(w, z, e)
    if actual == o:
        return None
    if w == 20000 and actual["status"] == "INVALID":
        return "DEF-01"
    if z == "REMOTE" and o["status"] == "UNAVAILABLE" and actual["status"] == "OK":
        return "DEF-04"
    if z == "REMOTE" and o["status"] == "OK" and actual["status"] == "OK":
        return "DEF-03"
    if w == 1000 and z == "LOCAL" and actual["status"] == "OK":
        return "DEF-02"
    return "NOVO-SINTOMA"


def summarize(name, rows):
    reqs, parts, bnds, inputs = set(), set(), set(), []
    invalid_exp, sig = 0, []
    det_orig, det_corr = set(), set()
    for r in rows:
        inp = r["input"]
        reqs |= requirements(inp)
        parts |= partitions(inp)
        bnds |= boundaries(inp)
        inputs.append(json.dumps(inp, sort_keys=True))
        o = oracle(**inp)
        if r["expected"] != o:
            invalid_exp += 1
        s = symptom(inp, r["actual"])
        if s:
            det_corr.add(s)
            if r["expected"] == o:  # FAIL legítimo com a expectativa original
                det_orig.add(s)
        w = inp["weight"]
        wsig = f"W={w}" if type(w) is int and w in BOUNDS else weight_class(w)
        sig.append((wsig, json.dumps(inp["zone"]), json.dumps(inp["express"])))
    dup_exact = len(inputs) - len(set(inputs))
    dup_part = len(sig) - len(set(sig))
    return {
        "suite": name, "n": len(rows),
        "req": sorted(reqs & {"R01", "R02", "R03", "R04", "R05"}),
        "partitions": len(parts), "partitions_list": sorted(parts),
        "boundaries": sorted(bnds), "invalid_expectations": invalid_exp,
        "dup_exact": dup_exact, "dup_same_partition": dup_part,
        "defects_original": sorted(det_orig), "defects_corrected": sorted(det_corr),
    }


def load(results_dir, prefix):
    f = glob.glob(os.path.join(results_dir, prefix + ".*.results.json"))[0]
    return json.load(open(f))["results"]


if __name__ == "__main__":
    rd = sys.argv[1]
    human = {r["id"]: r for r in load(rd, "human_cases_cp4")}
    ai = load(rd, "ai_candidates")
    h12 = [human[f"H-{i:02d}"] for i in range(1, 13)]
    h16 = [human[f"H-{i:02d}"] for i in range(1, 17)]
    out = [summarize("Humano H-01..H-12", h12), summarize("IA AI-01..AI-12", ai),
           summarize("Humano completo H-01..H-16", h16)]
    allb = set(f"W={b}" for b in BOUNDS) | {"REMOTE-express=5000", "REMOTE-express=5001"}
    print("| Suite | n | Requisitos R01–R05 | Partições | Fronteiras (de 10) | Fronteiras em falta | Expectativas inválidas | Duplicados exatos | Mesma partição | Defeitos (expectativas originais) | Defeitos (oráculo corrigido) |")
    print("|---|---:|---|---:|---:|---|---:|---:|---:|---|---|")
    for s in out:
        miss = sorted(allb - set(s["boundaries"]))
        print(f"| {s['suite']} | {s['n']} | {', '.join(s['req'])} | {s['partitions']} | {len(s['boundaries'])} | {', '.join(miss) or '—'} | {s['invalid_expectations']} | {s['dup_exact']} | {s['dup_same_partition']} | {', '.join(s['defects_original']) or '—'} | {', '.join(s['defects_corrected']) or '—'} |")
    json.dump(out, open(os.path.join(os.path.dirname(rd.rstrip('/')), "t6_comparacao.json"), "w"), indent=2, ensure_ascii=False)
    print("\nSintoma por caso (oráculo corrigido):")
    for r in ai + h16:
        s = symptom(r["input"], r["actual"])
        if s:
            print(f"  {r['id']}: {s}  input={json.dumps(r['input'])} actual={json.dumps(r['actual'])}")
