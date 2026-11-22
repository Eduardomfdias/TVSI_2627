"""Oráculo independente derivado só de BR-01..BR-05 (não importa nem lê shipping.py)."""
import json
import sys


def oracle(weight, zone, express):
    # BR-01: tipos exatos, sem coerção; bool excluído de weight
    if type(weight) is not int or not 1 <= weight <= 20000:
        return {"status": "INVALID", "fee": None}
    if type(zone) is not str or zone not in ("LOCAL", "REMOTE"):
        return {"status": "INVALID", "fee": None}
    if type(express) is not bool:
        return {"status": "INVALID", "fee": None}
    # BR-04 (precedência BR-05: validação > disponibilidade > fee)
    if zone == "REMOTE" and express and weight > 5000:
        return {"status": "UNAVAILABLE", "fee": None}
    # BR-02
    fee = 5 if weight <= 1000 else 8 if weight <= 5000 else 12
    # BR-03
    if zone == "REMOTE":
        fee += 4
    if express:
        fee += 6
    return {"status": "OK", "fee": fee}


def check(path):
    rows = []
    for c in json.load(open(path, encoding="utf-8")):
        o = oracle(**c["input"])
        rows.append((c["id"], c["input"], c["expected"], o, c["expected"] == o))
    return rows


if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        print(f"## {p}")
        for cid, inp, exp, o, ok in check(p):
            mark = "OK " if ok else "ERR"
            bad += not ok
            print(f"{mark} {cid:6} {json.dumps(inp):55} esperado={json.dumps(exp):34} oraculo={json.dumps(o)}")
    print(f"\nExpectativas divergentes do oráculo: {bad}")
