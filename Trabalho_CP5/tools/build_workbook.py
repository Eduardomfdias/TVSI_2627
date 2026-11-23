"""Constrói Trabalho_CP5/TestResults_T08_CP05.xlsx a partir do workbook do CP04 (só leitura).

1. Corrige numa cópia em memória os <tablePart r:id="rId1"/> para o Id real dos .rels (causa do KeyError no openpyxl).
2. Acrescenta Test Cases F-31+, execuções RUN-CP5, Defects revistos, ligações de Coverage e a comparação T6.
3. Alarga tabelas e intervalos das fórmulas para MAXR linhas.
Uso: python build_workbook.py  (a partir de qualquer pasta)
"""
import glob
import io
import json
import os
import re
import sys
import zipfile

import openpyxl
from openpyxl.styles import Font

HERE = os.path.dirname(os.path.abspath(__file__))
CP5 = os.path.dirname(HERE)
ROOT = os.path.dirname(CP5)
sys.path.insert(0, HERE)
from analise_t6 import symptom  # noqa: E402
from oracle import oracle  # noqa: E402

SRC = os.path.join(ROOT, "Trabalho_CP4", "TestResults_T08_Template.xlsx")
DST = os.path.join(CP5, "TestResults_T08_CP05.xlsx")
MAXR = 300
NOTA_39 = "CP05: ambiente Python 3.9.6 não conforme com BR-06 (3.10+); execução preservada, não conta como execução conforme."


def repaired_bytes(src):
    zin = zipfile.ZipFile(src)
    rels = {}
    for n in zin.namelist():
        if "worksheets/_rels/" in n:
            rels[n.split("/")[-1][:-5]] = re.findall(r'Id="([^"]+)"', zin.read(n).decode())
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in zin.namelist():
            d = zin.read(n)
            base = n.split("/")[-1]
            if n.startswith("xl/worksheets/sheet") and base in rels and rels[base]:
                d = d.decode().replace('tablePart r:id="rId1"', f'tablePart r:id="{rels[base][0]}"').encode()
            zout.writestr(zin.getinfo(n), d)
    buf.seek(0)
    return buf


def last_row(ws, col=1, start=5):
    r = start - 1
    for i in range(start, ws.max_row + 1):
        if ws.cell(i, col).value not in (None, ""):
            r = i
    return r


def j(x):
    return json.dumps(x, ensure_ascii=False)


def extend_table(ws, name, last_col):
    t = ws.tables[name]
    t.ref = f"A4:{last_col}{MAXR}"
    if t.autoFilter is not None:
        t.autoFilter.ref = t.ref


def run_dirs():
    out = []
    for d in sorted(glob.glob(os.path.join(CP5, "runs", "RUN-CP5-*"))):
        if not os.path.exists(os.path.join(d, "ABORTED.md")):
            out.append(d)
    return out


def main():
    wb = openpyxl.load_workbook(repaired_bytes(SRC))
    tc, ex, de, sr, cov, te = (wb[n] for n in ["Test Cases", "Executions", "Defects", "Static Review", "Coverage", "Technique"])

    # ---------- Test Cases: F-31+ (desenho; expected frozen) ----------
    gap = json.load(open(os.path.join(CP5, "gap_cases.json"), encoding="utf-8"))
    design = {d["id"]: d for d in json.load(open(os.path.join(CP5, "gap_cases.design.json"), encoding="utf-8"))}
    existing = {tc.cell(i, 1).value for i in range(5, tc.max_row + 1)}
    r = last_row(tc) + 1
    for c in gap:
        if c["id"] in existing:
            continue
        d = design[c["id"]]
        i = c["input"]
        vals = [c["id"], d["technique"], f"{d['requirements'].replace(',', ', ')}: {d['oracle_note']} (CP05, lacuna de cobertura)",
                d["setup"], j(i), f"Executar quote({j(i['weight'])}, {j(i['zone'])}, {j(i['express'])}) via runner (gap_cases.json)",
                j(c["expected"]), d["side_effects_expected"], d["priority"]]
        for k, v in enumerate(vals, 1):
            tc.cell(r, k, v)
        r += 1
    extend_table(tc, "TestCasesTable", "I")

    # ---------- Executions ----------
    req_by_test = {}
    for i in range(5, ex.max_row + 1):
        tid, req = ex.cell(i, 2).value, ex.cell(i, 3).value
        if tid and req:
            req_by_test.setdefault(tid, req)
        env = str(ex.cell(i, 4).value or "")
        note = str(ex.cell(i, 11).value or "")
        if "3.9.6" in env and "CP05:" not in note:
            ex.cell(i, 11, (note + " | " if note else "") + NOTA_39)
    for c in gap:
        req_by_test.setdefault(c["id"], design[c["id"]]["requirements"].replace(",", ", "))

    done = {ex.cell(i, 1).value for i in range(5, ex.max_row + 1)}
    r = last_row(ex) + 1
    support = {}  # defeito -> lista de (test, run)
    for d in run_dirs():
        rid = open(os.path.join(d, "RUN_ID")).read().strip()
        env = open(os.path.join(d, "ENVIRONMENT.txt"), encoding="utf-8").read()
        date = re.search(r"Data: (\S+)", env).group(1)[:10]
        so = re.search(r"SO: (.+)", env).group(1)
        py = re.search(r"Python: (.+)", env).group(1)
        for f in sorted(glob.glob(os.path.join(d, "results", "*.results.json"))):
            rep = json.load(open(f, encoding="utf-8"))
            suite = os.path.basename(f).split(".")[0]
            for k, res in enumerate(rep["results"], 1):
                run_id = f"{rid}/{suite}/{k:02d}"
                if run_id in done:
                    continue
                inp, exp, act = res["input"], res["expected"], res["actual"]
                corr = oracle(**inp)
                sym = symptom(inp, act)
                if res["verdict"] == "FAIL" and exp != corr:
                    defect = "DATA (expectativa da IA errada)" + (f"; input expõe {sym} sob oráculo corrigido" if sym else "")
                elif res["verdict"] == "FAIL":
                    defect = sym
                elif exp != corr:
                    defect = "DATA (falso PASS: expectativa da IA errada)" + (f"; input expõe {sym}" if sym else "")
                else:
                    defect = "-"
                if sym:
                    support.setdefault(sym, []).append((res["id"], rid, exp == corr))
                notes = "Nenhum efeito lateral observado pelo runner"
                if exp != corr:
                    notes = f"Oráculo independente (BR): {j(corr)}. Veredicto do runner preservado tal como emitido."
                vals = [run_id, res["id"], req_by_test.get(res["id"], "a confirmar"),
                        f"{date} / {so}, {py}, T08-B1.0", j(exp), j(act), res["verdict"],
                        os.path.relpath(f, ROOT) + "#" + res["id"], defect,
                        "A confirmar (Exec: sessão Claude Code a pedido do grupo; Val: a confirmar)", notes]
                for col, v in enumerate(vals, 1):
                    ex.cell(r, col, v)
                r += 1
    extend_table(ex, "ExecutionsTable", "K")

    # ---------- Defects (T2 revisto: black-box, sem linhas de código) ----------
    rid_main = os.path.basename(run_dirs()[0]) if run_dirs() else "—"

    def tests_for(dfx):
        seen = []
        for t, _rid, ok in support.get(dfx, []):
            lbl = t if ok else f"{t} (oráculo corrigido)"
            if lbl not in seen:
                seen.append(lbl)
        return ", ".join(seen)

    setup = "Setup: cópia limpa de app/ (T08-B1.0, SHA-256 = 9d9f950), Python 3.12, cwd = app/. Comando: python -E -s -c \"from shipping import quote; print(quote(%s))\". Input JSON: %s. Observado: %s"
    status = f"Confirmed · Reproduced 2026-11-22, {rid_main}, 3/3 processos novos (tester: a confirmar)"
    rows = [
        ["DEF-01", "weight=20000 (limite superior válido) devolvido como INVALID", "BR-01, BR-02 / T08-B1.0 / Python 3.12",
         setup % ("20000, 'LOCAL', False", '{"weight": 20000, "zone": "LOCAL", "express": false}', "{'status': 'INVALID', 'fee': None}"),
         '{"status": "OK", "fee": 12}', '{"status": "INVALID", "fee": null}', "reproducoes_isoladas.txt#DEF-01",
         "Alta / rejeita encomendas válidas no limite máximo do serviço", status],
        ["DEF-02", "weight=1000 (limite superior do escalão 1) cobrado com base de 8 € em vez de 5 €", "BR-02 / T08-B1.0 / Python 3.12",
         setup % ("1000, 'LOCAL', False", '{"weight": 1000, "zone": "LOCAL", "express": false}', "{'status': 'OK', 'fee': 8}"),
         '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 8}', "reproducoes_isoladas.txt#DEF-02",
         "Média-Alta / sobrecobrança de 3 € numa fronteira válida da tabela de preços", status],
        ["DEF-03", "Zona REMOTE devolve fee sem a tarifa base (ex.: 4 em vez de 9)", "BR-03 / T08-B1.0 / Python 3.12",
         setup % ("500, 'REMOTE', False", '{"weight": 500, "zone": "REMOTE", "express": false}', "{'status': 'OK', 'fee': 4}"),
         '{"status": "OK", "fee": 9}', '{"status": "OK", "fee": 4}', "reproducoes_isoladas.txt#DEF-03",
         "Crítica / subfaturação em todas as encomendas REMOTE com status OK", status],
        ["DEF-04", "REMOTE + express acima de 5000 g devolve OK em vez de UNAVAILABLE", "BR-04, BR-05 / T08-B1.0 / Python 3.12",
         setup % ("5001, 'REMOTE', True", '{"weight": 5001, "zone": "REMOTE", "express": true}', "{'status': 'OK', 'fee': 10}"),
         '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "reproducoes_isoladas.txt#DEF-04",
         "Alta / aceita um serviço que a regra declara indisponível e cobra uma fee parcial", status],
    ]
    for row in rows:
        t = tests_for(row[0])
        if t:
            row[1] += f" — testes de suporte: {t}"
    data = [
        ["DATA-01", "Fixture IA: AI-05 espera fee=4 (omite a base); falso PASS no runner", "BR-02, BR-03 / ai_candidates.json#AI-05",
         "Executar ai_candidates.json original; comparar expected de AI-05 com o oráculo das BR",
         '{"status": "OK", "fee": 9}', 'expected da IA: {"status": "OK", "fee": 4}', "ai_candidates.%s.results.json#AI-05" % rid_main,
         "Média / expectativa coincide com o output defeituoso e esconde DEF-03", "Data defect (fixture IA) — rejeitado"],
        ["DATA-02", "Fixture IA: AI-06 espera fee=8 para 1000 g; falso PASS no runner", "BR-02 / ai_candidates.json#AI-06",
         "Executar ai_candidates.json original; comparar expected de AI-06 com o oráculo das BR",
         '{"status": "OK", "fee": 5}', 'expected da IA: {"status": "OK", "fee": 8}', "ai_candidates.%s.results.json#AI-06" % rid_main,
         "Média / expectativa coincide com o output defeituoso e esconde DEF-02", "Data defect (fixture IA) — rejeitado"],
        ["DATA-03", "Fixture IA: AI-09 espera OK/22 para serviço indisponível", "BR-04 / ai_candidates.json#AI-09",
         "Executar ai_candidates.json original; comparar expected de AI-09 com o oráculo das BR",
         '{"status": "UNAVAILABLE", "fee": null}', 'expected da IA: {"status": "OK", "fee": 22}', "ai_candidates.%s.results.json#AI-09" % rid_main,
         "Alta / FAIL do runner por expectativa errada, não por deteção; revisto para F-19", "Data defect (fixture IA) — revisto (F-19)"],
        ["NOTA-01", "AI-10 é duplicado exato de AI-01 (redundância, não defeito)", "BR-08 / ai_candidates.json#AI-10",
         "Comparação de inputs dentro da suite IA", "-", "-", "t6_comparacao.json", "n/a / redundância", "Não é defeito"],
        ["NOTA-02", "Observação de inspeção de código (CP02), NÃO usada como oráculo nem como causa-raiz nos relatórios acima",
         "-", "O grupo leu shipping.py no CP02; essa leitura contraria o âmbito black-box do charter (CP01). Registado como limitação.",
         "-", "-", "Trabalho_CP2/CP2.md §9", "n/a", "Limitação de processo"],
    ]
    for i in range(5, de.max_row + 1):
        for col in range(1, 10):
            de.cell(i, col, None)
    for k, row in enumerate(rows + data, 5):
        for col, v in enumerate(row, 1):
            de.cell(k, col, v)

    # ---------- Static Review: reavaliação CP05 ----------
    reav = {
        "REV-01": "CP05: resolvido pelo texto de BR-01 ('excluding booleans'); o desfecho não deve citar a implementação.",
        "REV-02": "CP05: resolvido pelo texto de BR-01 ('actual boolean'; 'no trimming/coercion'); o desfecho não deve citar a implementação.",
        "REV-03": "CP05: não é ambiguidade genuína — BR-04 diz 'At exactly 5000 it is available'. Mantido como registo histórico.",
        "REV-04": "CP05: não é ambiguidade genuína — BR-05 define a precedência validação > disponibilidade. Mantido como registo histórico.",
    }
    for i in range(5, sr.max_row + 1):
        rid_ = sr.cell(i, 1).value
        if rid_ in reav and "CP05:" not in str(sr.cell(i, 6).value):
            sr.cell(i, 6, f"{sr.cell(i, 6).value} || {reav[rid_]}")
    nr = last_row(sr) + 1
    sr.cell(nr, 1, "REV-CP05")
    sr.cell(nr, 2, "BR-01..BR-08")
    sr.cell(nr, 3, "Questões de especificação em aberto após reavaliação: nenhuma.")
    sr.cell(nr, 4, "As BR fixam tipos, fronteiras, precedência e formato; todos os casos têm expectativa derivável sem consultar a implementação.")
    sr.cell(nr, 5, "-")
    sr.cell(nr, 6, "Testabilidade confirmada pelo oráculo tools/oracle.py (só BR) / a confirmar pelo grupo")

    # ---------- Coverage: ligações revistas e limpas (sem H-ENV em R05, sem quote() em R06-R08) ----------
    # Limpa linhas 21..MAXR na folha Coverage para garantir que não sobram ligações espúrias herdadas
    for i in range(21, max(cov.max_row + 1, MAXR + 1)):
        for col in range(1, 6):
            cov.cell(i, col, None)

    # Ligações funcionais genuínas de CP04 (R01..R05)
    # R05-H-ENV removido por não exercitar precedência/independência funcional
    # Casos quote() removidos de R06-R08 por serem requisitos de processo/runner
    valid_cp4_links = [
        # R01 / BR-01 (Validação)
        ("R01", "H-ENV"), ("R01", "H-02"), ("R01", "H-03"), ("R01", "H-07"), ("R01", "H-08"),
        ("R01", "H-09"), ("R01", "H-15"), ("R01", "H-16"), ("R01", "F-20"), ("R01", "F-21"),
        ("R01", "F-22"), ("R01", "F-23"), ("R01", "F-25"), ("R01", "F-26"), ("R01", "F-27"),
        # R02 / BR-02 (Fee base)
        ("R02", "H-ENV"), ("R02", "H-01"), ("R02", "H-02"), ("R02", "H-03"), ("R02", "H-04"),
        ("R02", "H-05"), ("R02", "H-06"), ("R02", "H-07"), ("R02", "H-10"), ("R02", "H-11"),
        ("R02", "H-12"), ("R02", "H-13"), ("R02", "F-17"), ("R02", "F-18"), ("R02", "F-24"),
        ("R02", "F-28"), ("R02", "F-29"),
        # R03 / BR-03 (Suplementos)
        ("R03", "H-01"), ("R03", "H-10"), ("R03", "H-11"), ("R03", "H-12"), ("R03", "H-13"),
        ("R03", "F-17"), ("R03", "F-18"), ("R03", "F-24"), ("R03", "F-28"), ("R03", "F-29"),
        # R04 / BR-04 (Disponibilidade)
        ("R04", "H-13"), ("R04", "H-14"), ("R04", "F-19"), ("R04", "F-21"), ("R04", "F-30"),
        # R05 / BR-05 (Precedência funcional: validação > disponibilidade)
        ("R05", "F-21"),
    ]

    links = set()
    r = 21
    for req, cid in valid_cp4_links:
        cov.cell(r, 1, req)
        cov.cell(r, 2, cid)
        links.add((req, cid))
        r += 1

    # Ligações dos casos de lacuna F-31..F-47 (desenhados, por executar)
    for c in gap:
        for req in design[c["id"]]["requirements"].split(","):
            req = req.strip()
            if (req, c["id"]) not in links:
                cov.cell(r, 1, req)
                cov.cell(r, 2, c["id"])
                links.add((req, c["id"]))
                r += 1

    for i in range(5, 13):
        cov.cell(i, 3, f"=SUMIFS($C$21:$C${MAXR},$A$21:$A${MAXR},A{i})")
        cov.cell(i, 4, f"=SUMIFS($D$21:$D${MAXR},$A$21:$A${MAXR},A{i})")
        cov.cell(i, 5, f"=C{i}-D{i}")
    for i in range(21, MAXR + 1):
        cov.cell(i, 3, f"=IF(OR(A{i}=\"\",B{i}=\"\"),0,IF(AND(COUNTIFS($A$5:$A$12,A{i})=1,COUNTIFS('Test Cases'!$A$5:$A${MAXR},B{i})=1,COUNTIFS($A$21:A{i},A{i},$B$21:B{i},B{i})=1),1,0))")
        cov.cell(i, 4, f"=IF(C{i}=0,0,IF(COUNTIFS(Executions!$B$5:$B${MAXR},B{i},Executions!$G$5:$G${MAXR},\"PASS\")+COUNTIFS(Executions!$B$5:$B${MAXR},B{i},Executions!$G$5:$G${MAXR},\"FAIL\")>0,1,0))")
        cov.cell(i, 5, f"=IF(AND(A{i}=\"\",B{i}=\"\"),\"\",IF(C{i}=1,\"Linked\",\"Check IDs / duplicate\"))")
    cov.cell(14, 1, f"CP05: intervalos das fórmulas alargados para $5:${MAXR}/$21:${MAXR}. R01–R05 cobrem os requisitos funcionais da função quote(). R05–H-ENV retirado por falta de fundamento funcional (H-ENV não testa precedência). R06–R08 são requisitos de processo e framework (formato JSON, runner CLI em Python 3.10+, exit codes 0/1/2 e auditoria de IA), verificados ao nível do processo/runner e documentalmente, sem associações espúrias a testes quote().")

    # ---------- Technique: T6 + redundância da suite final ----------
    t6p = os.path.join(run_dirs()[0], "t6_comparacao.json")
    base = 48
    te.cell(base, 1, "T6 — Comparação humano vs IA (CP05). Suite humana de 12 = H-01..H-12 por ordem de ID, fixada antes do cálculo.").font = Font(bold=True)
    hdr = ["Suite", "n", "Requisitos R01–R05", "Partições", "Fronteiras (de 10)", "Expectativas inválidas", "Duplicados exatos / mesma partição", "Defeitos: expectativas originais | oráculo corrigido"]
    for col, v in enumerate(hdr, 1):
        te.cell(base + 1, col, v).font = Font(bold=True)
    if os.path.exists(t6p):
        for k, s in enumerate(json.load(open(t6p, encoding="utf-8")), base + 2):
            vals = [s["suite"], s["n"], ", ".join(s["req"]), s["partitions"], len(s["boundaries"]), s["invalid_expectations"],
                    f"{s['dup_exact']} / {s['dup_same_partition']}",
                    f"{', '.join(s['defects_original']) or '—'} | {', '.join(s['defects_corrected']) or '—'}"]
            for col, v in enumerate(vals, 1):
                te.cell(k, col, v)
    te.cell(base + 6, 1, "Limite: o fixture IA é curado pelo docente (AI_PROVENANCE); não permite afirmar superioridade de humanos ou de IA.")
    red = base + 8
    te.cell(red, 1, "Redundância na suite final (CP05; nenhum caso apagado)").font = Font(bold=True)
    for k, row in enumerate([
        ["F-19 (6000, REMOTE, express)", "BR-04", "-", "-", "Redundante para DEF-04", "Mesma partição de H-14 (>5000 REMOTE express); acrescenta só um ponto interior", "H-14", "t6_comparacao.json"],
        ["F-30 (8000, REMOTE, express)", "BR-04", "-", "-", "Redundante para DEF-04", "Mesma partição de H-14 e F-19", "H-14", "-"],
        ["F-28 (6000, LOCAL, false)", "BR-02", "-", "-", "Redundante", "Inputs idênticos a AI-03 (rejeitado no CP03)", "AI-03", "-"],
        ["F-46 / F-47 (10000 / 10001, REMOTE, express)", "BR-04", "-", "-", "Acrescenta (caracterização)", "Delimitam o sintoma de DEF-04; valores escolhidos com conhecimento prévio do código (CP02) — declarado como limitação", "-", "gap_cases.json"],
    ], red + 1):
        for col, v in enumerate(row, 1):
            te.cell(k, col, v)

    wb.save(DST)
    openpyxl.load_workbook(DST)  # verificação de abertura sem read_only
    print("Gravado e reaberto sem erro:", DST)
    print("Execuções:", last_row(ex) - 4, "· Test Cases:", last_row(tc) - 4, "· Ligações Coverage:", len(links))


if __name__ == "__main__":
    main()
