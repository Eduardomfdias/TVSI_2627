#!/usr/bin/env python3
"""Script to update and audit TestResults_T08_Template.xlsx for CP04.

Ensures:
1. 'Test Cases' has all 31 cases (H-ENV, H-01..H-16, F-17..F-30).
2. 'Executions' has autonomous 'Requirement ID(s)' column, separated Expected and Observed results,
   full execution history (CP01 smoke, CP02 human, CP03 AI original, CP04 final 30 cases, BR-05 control, runner robustness),
   and tester roles (Executante / Supervisão / Validação).
3. 'Defects' clearly separates 4 software defects (DEF-01..DEF-04) from 3 AI expectation quality issues (DATA-01..DATA-03).
4. 'Coverage' formulas and links remain 100% valid with 0 errors (#REF!, #VALUE!, etc.).
"""

import sys, os, zipfile, io, json
import xml.etree.ElementTree as ET

def build_workbook():
    template_path = 'TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx'
    
    # Read existing template zip entries
    with zipfile.ZipFile(template_path, 'r') as z:
        entries = {name: z.read(name) for name in z.namelist()}

    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

    # -------------------------------------------------------------------------
    # Helper to construct cell XML
    # -------------------------------------------------------------------------
    def make_cell(coord, val, t='str', style='0'):
        if val is None or val == '':
            return f'<c r="{coord}" s="{style}"/>'
        if t == 'str':
            val_escaped = str(val).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
            return f'<c r="{coord}" t="str" s="{style}"><v>{val_escaped}</v></c>'
        elif t == 'n':
            return f'<c r="{coord}" s="{style}"><v>{val}</v></c>'
        return f'<c r="{coord}" s="{style}"/>'

    # -------------------------------------------------------------------------
    # 1. Update Sheet 1: Test Cases (84 rows total)
    # -------------------------------------------------------------------------
    test_cases_data = [
        # (ID, Tech, Rule/Obj, Setup, Exact Inputs, Action, Expected Outputs, Side Effects, Priority)
        ("H-ENV", "Smoke / Environment", "Ambiente: weight=500, zone=LOCAL, express=false -> OK, fee=5", "Build T08-B1.0, Python 3.10+, terminal na pasta app", '{"weight": 500, "zone": "LOCAL", "express": false}', "Executar quote(500, 'LOCAL', False) via runner", '{"status": "OK", "fee": 5}', "Nenhum (função pura)", "Alta"),
        ("H-01", "EP", "BR-02, BR-03: Caso nominal Tier 1 (1–1000g), zona LOCAL sem express", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "LOCAL", "express": false}', "Executar quote(500, 'LOCAL', False)", '{"status": "OK", "fee": 5}', "Nenhum", "Alta"),
        ("H-02", "BVA", "BR-01, BR-02: Limite inferior mínimo válido de peso (weight=1g), Tier 1", "Build T08-B1.0, Python 3.10+", '{"weight": 1, "zone": "LOCAL", "express": false}', "Executar quote(1, 'LOCAL', False)", '{"status": "OK", "fee": 5}', "Nenhum", "Alta"),
        ("H-03", "BVA", "BR-01, BR-02: Limite superior da fronteira do Tier 1 (weight=1000g)", "Build T08-B1.0, Python 3.10+", '{"weight": 1000, "zone": "LOCAL", "express": false}', "Executar quote(1000, 'LOCAL', False)", '{"status": "OK", "fee": 5}', "Nenhum", "Alta"),
        ("H-04", "BVA", "BR-01, BR-02: Limite inferior da fronteira do Tier 2 (weight=1001g)", "Build T08-B1.0, Python 3.10+", '{"weight": 1001, "zone": "LOCAL", "express": false}', "Executar quote(1001, 'LOCAL', False)", '{"status": "OK", "fee": 8}', "Nenhum", "Alta"),
        ("H-05", "BVA", "BR-01, BR-02: Limite superior da fronteira do Tier 2 (weight=5000g)", "Build T08-B1.0, Python 3.10+", '{"weight": 5000, "zone": "LOCAL", "express": false}', "Executar quote(5000, 'LOCAL', False)", '{"status": "OK", "fee": 8}', "Nenhum", "Alta"),
        ("H-06", "BVA", "BR-01, BR-02: Limite inferior da fronteira do Tier 3 (weight=5001g)", "Build T08-B1.0, Python 3.10+", '{"weight": 5001, "zone": "LOCAL", "express": false}', "Executar quote(5001, 'LOCAL', False)", '{"status": "OK", "fee": 12}', "Nenhum", "Alta"),
        ("H-07", "BVA", "BR-01, BR-02: Limite superior máximo válido de peso (weight=20000g), Tier 3", "Build T08-B1.0, Python 3.10+", '{"weight": 20000, "zone": "LOCAL", "express": false}', "Executar quote(20000, 'LOCAL', False)", '{"status": "OK", "fee": 12}', "Nenhum", "Alta"),
        ("H-08", "BVA", "BR-01: Limite inferior inválido abaixo do mínimo (weight=0)", "Build T08-B1.0, Python 3.10+", '{"weight": 0, "zone": "LOCAL", "express": false}', "Executar quote(0, 'LOCAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Alta"),
        ("H-09", "BVA", "BR-01: Limite superior inválido acima do máximo (weight=20001)", "Build T08-B1.0, Python 3.10+", '{"weight": 20001, "zone": "LOCAL", "express": false}', "Executar quote(20001, 'LOCAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Alta"),
        ("H-10", "EP", "BR-02, BR-03: Suplemento de zona REMOTE (+4€) em Tier 1 sem express", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "REMOTE", "express": false}', "Executar quote(500, 'REMOTE', False)", '{"status": "OK", "fee": 9}', "Nenhum", "Alta"),
        ("H-11", "EP", "BR-02, BR-03: Suplemento de envio express (+6€) para zona LOCAL em Tier 1", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "LOCAL", "express": true}', "Executar quote(500, 'LOCAL', True)", '{"status": "OK", "fee": 11}', "Nenhum", "Alta"),
        ("H-12", "EP", "BR-02, BR-03: Suplementos acumulativos REMOTE (+4€) e express (+6€) em Tier 1", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "REMOTE", "express": true}', "Executar quote(500, 'REMOTE', True)", '{"status": "OK", "fee": 15}', "Nenhum", "Alta"),
        ("H-13", "BVA", "BR-02, BR-03, BR-04: Limite exato de disponibilidade express REMOTE (5000g disponível)", "Build T08-B1.0, Python 3.10+", '{"weight": 5000, "zone": "REMOTE", "express": true}', "Executar quote(5000, 'REMOTE', True)", '{"status": "OK", "fee": 18}', "Nenhum", "Crítica"),
        ("H-14", "BVA", "BR-04: Limite imediato de indisponibilidade express REMOTE (5001g indisponível)", "Build T08-B1.0, Python 3.10+", '{"weight": 5001, "zone": "REMOTE", "express": true}', "Executar quote(5001, 'REMOTE', True)", '{"status": "UNAVAILABLE", "fee": null}', "Nenhum", "Crítica"),
        ("H-15", "EP", "BR-01: Rejeição de tipo booleano no peso (weight=True excluído de int)", "Build T08-B1.0, Python 3.10+", '{"weight": true, "zone": "LOCAL", "express": false}', "Executar quote(True, 'LOCAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("H-16", "EP", "BR-01: Validação estrita case-sensitive da zona (zone='local' inválido)", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "local", "express": false}', "Executar quote(500, 'local', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-17", "EP", "BR-02, BR-03: Tier 3 (10000g) com express para zona LOCAL (12+6=18€)", "Build T08-B1.0, Python 3.10+", '{"weight": 10000, "zone": "LOCAL", "express": true}', "Executar quote(10000, 'LOCAL', True)", '{"status": "OK", "fee": 18}', "Nenhum", "Média"),
        ("F-18", "EP", "BR-02, BR-03: Tier 2 (2000g) para zona REMOTE sem express (8+4=12€)", "Build T08-B1.0, Python 3.10+", '{"weight": 2000, "zone": "REMOTE", "express": false}', "Executar quote(2000, 'REMOTE', False)", '{"status": "OK", "fee": 12}', "Nenhum", "Alta"),
        ("F-19", "EP", "BR-04: Ponto interior da classe de indisponibilidade REMOTE express (weight=6000g)", "Build T08-B1.0, Python 3.10+", '{"weight": 6000, "zone": "REMOTE", "express": true}', "Executar quote(6000, 'REMOTE', True)", '{"status": "UNAVAILABLE", "fee": null}', "Nenhum", "Alta"),
        ("F-20", "EP", "BR-01: Rejeição de tipo inteiro no parâmetro express (express=1 não é bool real)", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "LOCAL", "express": 1}', "Executar quote(500, 'LOCAL', 1)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-21", "EP/BVA", "BR-01, BR-04, BR-05: Precedência de validação (weight=25000 > 20000) sobre disponibilidade", "Build T08-B1.0, Python 3.10+", '{"weight": 25000, "zone": "REMOTE", "express": true}', "Executar quote(25000, 'REMOTE', True)", '{"status": "INVALID", "fee": null}', "Nenhum", "Alta"),
        ("F-22", "EP", "BR-01: Robustez de tipo numérico — rejeição de float no peso (weight=500.5)", "Build T08-B1.0, Python 3.10+", '{"weight": 500.5, "zone": "LOCAL", "express": false}', "Executar quote(500.5, 'LOCAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-23", "EP", "BR-01: Robustez de zona com espaços — rejeição de whitespace em zone (' LOCAL ')", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": " LOCAL ", "express": false}', "Executar quote(500, ' LOCAL ', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-24", "EP", "BR-02, BR-03: Combinação nominal de Tier 2 com serviço express LOCAL (8+6=14€)", "Build T08-B1.0, Python 3.10+", '{"weight": 2000, "zone": "LOCAL", "express": true}', "Executar quote(2000, 'LOCAL', True)", '{"status": "OK", "fee": 14}', "Nenhum", "Média"),
        ("F-25", "EP", "BR-01: Rejeição de zona inválida fora do domínio permitido ('INTERNATIONAL')", "Build T08-B1.0, Python 3.10+", '{"weight": 1000, "zone": "INTERNATIONAL", "express": false}', "Executar quote(1000, 'INTERNATIONAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-26", "BVA", "BR-01: Limite inferior negativo de peso (weight=-100) fora do intervalo", "Build T08-B1.0, Python 3.10+", '{"weight": -100, "zone": "LOCAL", "express": false}', "Executar quote(-100, 'LOCAL', False)", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-27", "EP", "BR-01: Rejeição de express como string em vez de booleano real ('False')", "Build T08-B1.0, Python 3.10+", '{"weight": 500, "zone": "LOCAL", "express": \"False\"}', "Executar quote(500, 'LOCAL', 'False')", '{"status": "INVALID", "fee": null}', "Nenhum", "Média"),
        ("F-28", "EP", "BR-02, BR-03: Ponto interior Tier 3 nominal para zona LOCAL sem express (12€)", "Build T08-B1.0, Python 3.10+", '{"weight": 6000, "zone": "LOCAL", "express": false}', "Executar quote(6000, 'LOCAL', False)", '{"status": "OK", "fee": 12}', "Nenhum", "Média"),
        ("F-29", "EP", "BR-02, BR-03: Tier 3 para zona REMOTE sem express (12+4=16€) expondo DEF-03", "Build T08-B1.0, Python 3.10+", '{"weight": 6000, "zone": "REMOTE", "express": false}', "Executar quote(6000, 'REMOTE', False)", '{"status": "OK", "fee": 16}', "Nenhum", "Alta"),
        ("F-30", "EP", "BR-04: Limiar interior de indisponibilidade express REMOTE (weight=8000g) expondo DEF-04", "Build T08-B1.0, Python 3.10+", '{"weight": 8000, "zone": "REMOTE", "express": true}', "Executar quote(8000, 'REMOTE', True)", '{"status": "UNAVAILABLE", "fee": null}', "Nenhum", "Alta")
    ]

    # Generate Sheet 1 XML
    s1_rows = []
    # Row 1-3: Headers
    s1_rows.append('<row r="1" spans="1:9"><c r="A1" t="str"><v>Test Cases — T08</v></c><c r="B1"/><c r="C1"/><c r="D1"/><c r="E1"/><c r="F1"/><c r="G1"/><c r="H1"/><c r="I1"/></row>')
    s1_rows.append('<row r="2" spans="1:9"><c r="A2" t="str"><v>Derive expected results from BusinessRules BEFORE execution. One scenario per row.</v></c><c r="B2"/><c r="C2"/><c r="D2"/><c r="E2"/><c r="F2"/><c r="G2"/><c r="H2"/><c r="I2"/></row>')
    s1_rows.append('<row r="3" spans="1:9"><c r="A3"/><c r="B3"/><c r="C3"/><c r="D3"/><c r="E3"/><c r="F3"/><c r="G3"/><c r="H3"/><c r="I3"/></row>')
    s1_rows.append('<row r="4" spans="1:9"><c r="A4" t="str"><v>Test ID</v></c><c r="B4" t="str"><v>Technique</v></c><c r="C4" t="str"><v>Rules / objective</v></c><c r="D4" t="str"><v>Setup / preconditions</v></c><c r="E4" t="str"><v>Exact inputs</v></c><c r="F4" t="str"><v>Action steps</v></c><c r="G4" t="str"><v>Expected outputs</v></c><c r="H4" t="str"><v>Expected side effects</v></c><c r="I4" t="str"><v>Priority</v></c></row>')

    for idx, tc in enumerate(test_cases_data, 5):
        cells = [
            make_cell(f'A{idx}', tc[0]),
            make_cell(f'B{idx}', tc[1]),
            make_cell(f'C{idx}', tc[2]),
            make_cell(f'D{idx}', tc[3]),
            make_cell(f'E{idx}', tc[4]),
            make_cell(f'F{idx}', tc[5]),
            make_cell(f'G{idx}', tc[6]),
            make_cell(f'H{idx}', tc[7]),
            make_cell(f'I{idx}', tc[8]),
        ]
        s1_rows.append(f'<row r="{idx}" spans="1:9">{"".join(cells)}</row>')

    # Empty rows up to 84 to preserve worksheet range
    for idx in range(len(test_cases_data) + 5, 85):
        s1_rows.append(f'<row r="{idx}" spans="1:9"><c r="A{idx}"/><c r="B{idx}"/><c r="C{idx}"/><c r="D{idx}"/><c r="E{idx}"/><c r="F{idx}"/><c r="G{idx}"/><c r="H{idx}"/><c r="I{idx}"/></row>')

    sheet1_xml = f'<?xml version="1.0" encoding="utf-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheetViews><sheetView tabSelected="0" workbookViewId="0"/></sheetViews><sheetFormatPr defaultRowHeight="15"/><sheetData>{"".join(s1_rows)}</sheetData><tableParts count="1"><tablePart r:id="rId1"/></tableParts></worksheet>'
    entries['xl/worksheets/sheet1.xml'] = sheet1_xml.encode('utf-8')


    # -------------------------------------------------------------------------
    # 2. Update Sheet 2: Executions (Preserving full history, autonomous Requirement ID(s))
    # -------------------------------------------------------------------------
    # Columns in Sheet 2:
    # A: Run ID
    # B: Test ID
    # C: Requirement ID(s)
    # D: Date / environment
    # E: Expected outputs (independently derived)
    # F: Actual outputs
    # G: Verdict (PASS / FAIL) -> Stays on col G so Coverage formula works!
    # H: Evidence
    # I: Defect IDs
    # J: Tester (Executante / Supervisão / Validação)
    # K: Actual side effects / Notes

    executions_data = [
        # Block 1: Smoke / Environment (CP01)
        ("RUN-ENV-01", "H-ENV", "R01, R02, R06, R07", "2026-10-27 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "app/human_cases.results.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Grupo 5)", "Nenhum (função pura sem efeitos secundários)"),

        # Block 2: Frozen Human Suite (CP02, 2026-10-30) - 10 PASS, 6 FAIL
        ("RUN-H02-01", "H-01", "R02, R03", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-02", "H-02", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-03", "H-03", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 8}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-02", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (violou BR-02: 1000g cobrado como tier 2)"),
        ("RUN-H02-04", "H-04", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-05", "H-05", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-06", "H-06", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 12}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-07", "H-07", "R01, R02", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "INVALID", "fee": null}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-01", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (violou BR-01: 20000g rejeitado como INVALID)"),
        ("RUN-H02-08", "H-08", "R01", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-09", "H-09", "R01", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-10", "H-10", "R02, R03", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 9}', '{"status": "OK", "fee": 4}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-03", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (violou BR-03: taxa base sobrescrita por fee=4)"),
        ("RUN-H02-11", "H-11", "R02, R03", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 11}', '{"status": "OK", "fee": 11}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-12", "H-12", "R02, R03", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 15}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-03", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (violou BR-03: taxa base sobrescrita por fee=4)"),
        ("RUN-H02-13", "H-13", "R02, R03, R04", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 18}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-03", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (disponível a 5000g; violou estritamente DEF-03)"),
        ("RUN-H02-14", "H-14", "R04", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP2/human_cases.results.json", "DEF-04", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum (violou BR-04: aceitou 5001g REMOTE express)"),
        ("RUN-H02-15", "H-15", "R01", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),
        ("RUN-H02-16", "H-16", "R01", "2026-10-30 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP2/human_cases.results.json", "-", "Grupo 5 (Exec: Eduardo Dias; Sup: Rui Carneiro; Val: Grupo 5)", "Nenhum"),

        # Block 3: AI Candidates Original Execution in Runner (CP03, 2026-11-08) - 10 PASS, 2 FAIL
        ("RUN-AI-01", "AI-01", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-02", "AI-02", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-03", "AI-03", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 12}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-04", "AI-04", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 11}', '{"status": "OK", "fee": 11}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-05", "AI-05", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 4}', '{"status": "OK", "fee": 4}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "DATA-01", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS (Nota: expectativa da IA incorreta omite base 5€, replicando bug DEF-03)"),
        ("RUN-AI-06", "AI-06", "R02", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "DATA-02", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS (Nota: expectativa da IA incorreta assume 8€ a 1000g, mascarando DEF-02)"),
        ("RUN-AI-07", "AI-07", "R01", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-08", "AI-08", "R01", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-09", "AI-09", "R04", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 22}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/ai_candidates_execution.json", "DATA-03", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: FAIL (Nota: IA tentou tarifar 6000g REMOTE express que é UNAVAILABLE; revisto para F-19)"),
        ("RUN-AI-10", "AI-10", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS"),
        ("RUN-AI-11", "AI-11", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 18}', '{"status": "OK", "fee": 18}', "PASS", "Trabalho_CP4/runs/ai_candidates_execution.json", "-", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: PASS (Aceite para suite final como F-17)"),
        ("RUN-AI-12", "AI-12", "R02, R03", "2026-11-08 / macOS, Python 3.9.6, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 4}', "FAIL", "Trabalho_CP4/runs/ai_candidates_execution.json", "DEF-03", "Grupo 5 (Exec: Claude Code assistido; Sup: Érica Moreira; Val: Beatriz Barbosa)", "Runner original: FAIL (Aceite com oráculo independente como F-18)"),

        # Block 4: Official Final Suite Execution for CP04 (30 cases, 2026-11-16) - 20 PASS, 10 FAIL
        ("RUN-CP4-01", "H-01", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-02", "H-02", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 5}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-03", "H-03", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 8}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-02", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Violou BR-02: 1000g cobrado como Tier 2"),
        ("RUN-CP4-04", "H-04", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-05", "H-05", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 8}', '{"status": "OK", "fee": 8}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-06", "H-06", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 12}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-07", "H-07", "R01, R02", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "INVALID", "fee": null}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-01", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Violou BR-01: limite 20000g rejeitado como INVALID"),
        ("RUN-CP4-08", "H-08", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-09", "H-09", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-10", "H-10", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 9}', '{"status": "OK", "fee": 4}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-03", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Violou BR-03: taxa base sobrescrita por fee=4"),
        ("RUN-CP4-11", "H-11", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 11}', '{"status": "OK", "fee": 11}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-12", "H-12", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 15}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-03", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Violou BR-03: taxa base sobrescrita por fee=4 (+ express 6 = 10)"),
        ("RUN-CP4-13", "H-13", "R02, R03, R04", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 18}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-03", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Disponível a 5000g; falha estritamente por DEF-03"),
        ("RUN-CP4-14", "H-14", "R04", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-04", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Violou BR-04: aceitou 5001g REMOTE express"),
        ("RUN-CP4-15", "H-15", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-16", "H-16", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Érica Moreira)", "Nenhum"),
        ("RUN-CP4-17", "F-17", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 18}', '{"status": "OK", "fee": 18}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum"),
        ("RUN-CP4-18", "F-18", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 4}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-03", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Violou BR-03: taxa base sobrescrita por fee=4"),
        ("RUN-CP4-19", "F-19", "R04", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-04", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Violou BR-04: aceitou 6000g REMOTE express"),
        ("RUN-CP4-20", "F-20", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum"),
        ("RUN-CP4-21", "F-21", "R01, R04, R05", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum"),
        ("RUN-CP4-22", "F-22", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (robustez peso float)"),
        ("RUN-CP4-23", "F-23", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (robustez zona com espaços)"),
        ("RUN-CP4-24", "F-24", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 14}', '{"status": "OK", "fee": 14}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (combinação LOCAL express)"),
        ("RUN-CP4-25", "F-25", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (zona inválida 'INTERNATIONAL')"),
        ("RUN-CP4-26", "F-26", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (peso negativo -100)"),
        ("RUN-CP4-27", "F-27", "R01", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "INVALID", "fee": null}', '{"status": "INVALID", "fee": null}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (express como string)"),
        ("RUN-CP4-28", "F-28", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 12}', '{"status": "OK", "fee": 12}', "PASS", "Trabalho_CP4/runs/final_cases_execution.json", "-", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Nenhum (Tier 3 nominal)"),
        ("RUN-CP4-29", "F-29", "R02, R03", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "OK", "fee": 16}', '{"status": "OK", "fee": 4}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-03", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Violou BR-03: taxa base sobrescrita por fee=4"),
        ("RUN-CP4-30", "F-30", "R04", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "FAIL", "Trabalho_CP4/runs/final_cases_execution.json", "DEF-04", "Grupo 5 (Exec: Rui Carneiro; Sup: Eduardo Dias; Val: Beatriz Barbosa)", "Violou BR-04: aceitou 8000g REMOTE express"),

        # Block 5: BR-05 Independence & Side Effect Controls
        ("RUN-CTRL-01", "BR05-DET-01", "R05", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", "Determinismo estrito em 100 chamadas idênticas", "Determinismo estrito em 100 chamadas idênticas", "PASS", "Trabalho_CP4/evidence/br05_independence_cp4.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Nenhum (determinismo comprovado)"),
        ("RUN-CTRL-02", "BR05-RES-02", "R05", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", "Ausência de estado residual inter-chamadas", "Ausência de estado residual inter-chamadas", "PASS", "Trabalho_CP4/evidence/br05_independence_cp4.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Nenhum (ordem não afeta saídas)"),
        ("RUN-CTRL-03", "BR05-MUT-03", "R05", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", "Imutabilidade de módulos e memória global", "Imutabilidade de módulos e memória global", "PASS", "Trabalho_CP4/evidence/br05_independence_cp4.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Nenhum (memória inalterada)"),
        ("RUN-CTRL-04", "BR05-EXT-04", "R05", "2026-11-16 / macOS, Python 3.9.6 & 3.12.7, T08-B1.0", "Isolamento de I/O, stdout/stderr, ambiente e filesystem", "Isolamento de I/O, stdout/stderr, ambiente e filesystem", "PASS", "Trabalho_CP4/evidence/br05_independence_cp4.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Nenhum (sistema de ficheiros intocado)"),

        # Block 6: Runner Robustness Controls (Exit code 2)
        ("RUN-ROB-01", "ROB-CLI-01", "R06, R07", "2026-11-16 / macOS, Python 3.9.6, T08-B1.0", "Exit code 2 e mensagem de uso sem argumentos", "Exit code 2 e mensagem de uso sem argumentos", "PASS", "Trabalho_CP4/evidence/runner_robustness_evidence.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Runner robusto sem argumentos"),
        ("RUN-ROB-02", "ROB-CLI-02", "R06, R07", "2026-11-16 / macOS, Python 3.9.6, T08-B1.0", "Exit code 2 e CASE FILE ERROR para ficheiro inexistente", "Exit code 2 e CASE FILE ERROR para ficheiro inexistente", "PASS", "Trabalho_CP4/evidence/runner_robustness_evidence.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Runner robusto ficheiro inexistente"),
        ("RUN-ROB-03", "ROB-CLI-03", "R06, R07", "2026-11-16 / macOS, Python 3.9.6, T08-B1.0", "Exit code 2 e CASE FILE ERROR para JSON malformado", "Exit code 2 e CASE FILE ERROR para JSON malformado", "PASS", "Trabalho_CP4/evidence/runner_robustness_evidence.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Runner robusto sintaxe JSON inválida"),
        ("RUN-ROB-04", "ROB-CLI-04", "R06, R07", "2026-11-16 / macOS, Python 3.9.6, T08-B1.0", "Exit code 2 e CASE FILE ERROR para case IDs duplicados", "Exit code 2 e CASE FILE ERROR para case IDs duplicados", "PASS", "Trabalho_CP4/evidence/runner_robustness_evidence.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Runner robusto IDs duplicados"),
        ("RUN-ROB-05", "ROB-CLI-05", "R06, R07", "2026-11-16 / macOS, Python 3.9.6, T08-B1.0", "Exit code 2 e CASE FILE ERROR para raiz não-lista", "Exit code 2 e CASE FILE ERROR para raiz não-lista", "PASS", "Trabalho_CP4/evidence/runner_robustness_evidence.json", "-", "Grupo 5 (Exec: Rui Carneiro; Val: Grupo 5)", "Runner robusto raiz JSON inválida")
    ]

    s2_rows = []
    # Header lines
    s2_rows.append('<row r="1" spans="1:11"><c r="A1" t="str"><v>Executions — T08</v></c><c r="B1"/><c r="C1"/><c r="D1"/><c r="E1"/><c r="F1"/><c r="G1"/><c r="H1"/><c r="I1"/><c r="J1"/><c r="K1"/></row>')
    s2_rows.append('<row r="2" spans="1:11"><c r="A2" t="str"><v>Manual verdict: compare ALL expected outcomes. Preserve prior runs; BLOCKED is not PASS.</v></c><c r="B2"/><c r="C2"/><c r="D2"/><c r="E2"/><c r="F2"/><c r="G2"/><c r="H2"/><c r="I2"/><c r="J2"/><c r="K2"/></row>')
    s2_rows.append('<row r="3" spans="1:11"><c r="A3"/><c r="B3"/><c r="C3"/><c r="D3"/><c r="E3"/><c r="F3"/><c r="G3"/><c r="H3"/><c r="I3"/><c r="J3"/><c r="K3"/></row>')
    s2_rows.append('<row r="4" spans="1:11"><c r="A4" t="str"><v>Run ID</v></c><c r="B4" t="str"><v>Test ID</v></c><c r="C4" t="str"><v>Requirement ID(s)</v></c><c r="D4" t="str"><v>Date / environment</v></c><c r="E4" t="str"><v>Expected outputs (independently derived)</v></c><c r="F4" t="str"><v>Actual outputs</v></c><c r="G4" t="str"><v>Verdict</v></c><c r="H4" t="str"><v>Evidence</v></c><c r="I4" t="str"><v>Defect IDs</v></c><c r="J4" t="str"><v>Tester (Role: Exec / Sup / Val)</v></c><c r="K4" t="str"><v>Actual side effects / Notes</v></c></row>')

    for idx, ex in enumerate(executions_data, 5):
        cells = [
            make_cell(f'A{idx}', ex[0]),
            make_cell(f'B{idx}', ex[1]),
            make_cell(f'C{idx}', ex[2]),
            make_cell(f'D{idx}', ex[3]),
            make_cell(f'E{idx}', ex[4]),
            make_cell(f'F{idx}', ex[5]),
            make_cell(f'G{idx}', ex[6]),
            make_cell(f'H{idx}', ex[7]),
            make_cell(f'I{idx}', ex[8]),
            make_cell(f'J{idx}', ex[9]),
            make_cell(f'K{idx}', ex[10])
        ]
        s2_rows.append(f'<row r="{idx}" spans="1:11">{"".join(cells)}</row>')

    # Empty rows up to 84
    for idx in range(len(executions_data) + 5, 85):
        s2_rows.append(f'<row r="{idx}" spans="1:11"><c r="A{idx}"/><c r="B{idx}"/><c r="C{idx}"/><c r="D{idx}"/><c r="E{idx}"/><c r="F{idx}"/><c r="G{idx}"/><c r="H{idx}"/><c r="I{idx}"/><c r="J{idx}"/><c r="K{idx}"/></row>')

    sheet2_xml = f'<?xml version="1.0" encoding="utf-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheetViews><sheetView tabSelected="0" workbookViewId="0"/></sheetViews><sheetFormatPr defaultRowHeight="15"/><sheetData>{"".join(s2_rows)}</sheetData><tableParts count="1"><tablePart r:id="rId1"/></tableParts></worksheet>'
    entries['xl/worksheets/sheet2.xml'] = sheet2_xml.encode('utf-8')

    # Update table2.xml to reflect the 11 columns in ExecutionsTable
    table2_xml = f'<?xml version="1.0" encoding="utf-8"?><x:table id="2" name="ExecutionsTable" displayName="ExecutionsTable" ref="A4:K84" headerRowCount="1" totalsRowCount="0" totalsRowShown="0" xmlns:x="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><x:tableColumns count="11"><x:tableColumn id="1" name="Run ID" /><x:tableColumn id="2" name="Test ID" /><x:tableColumn id="3" name="Requirement ID(s)" /><x:tableColumn id="4" name="Date / environment" /><x:tableColumn id="5" name="Expected outputs (independently derived)" /><x:tableColumn id="6" name="Actual outputs" /><x:tableColumn id="7" name="Verdict" /><x:tableColumn id="8" name="Evidence" /><x:tableColumn id="9" name="Defect IDs" /><x:tableColumn id="10" name="Tester (Role: Exec / Sup / Val)" /><x:tableColumn id="11" name="Actual side effects / Notes" /></x:tableColumns><x:tableStyleInfo name="TableStyleMedium2" showFirstColumn="0" showLastColumn="0" showRowStripes="1" showColumnStripes="0" /></x:table>'
    entries['xl/tables/table2.xml'] = table2_xml.encode('utf-8')


    # -------------------------------------------------------------------------
    # 3. Update Sheet 3: Defects (4 Software Defects + 3 AI Expectation Quality Issues)
    # -------------------------------------------------------------------------
    defects_data = [
        # (ID, Title/Tests, Rule/Build/Env, Exact Repro, Expected, Actual, Evidence, Severity/Rationale, Status)
        ("DEF-01", "Off-by-one limite superior de peso: weight=20000 tratado como INVALID (H-07)", "BR-01 / Build T08-B1.0 / Python 3.12 & 3.9", "quote(20000, 'LOCAL', False) -> linha 3 usa 'weight >= 20000'", '{"status": "OK", "fee": 12}', '{"status": "INVALID", "fee": null}', "final_cases_execution.json#H-07", "Alta / Rejeição indevida do limite máximo legal permitido em BR-01", "Open"),
        ("DEF-02", "Off-by-one na transição entre Tier 1 e Tier 2: weight=1000 cobrado a 8€ (H-03)", "BR-02 / Build T08-B1.0 / Python 3.12 & 3.9", "quote(1000, 'LOCAL', False) -> linha 7 usa 'weight < 1000'", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 8}', "final_cases_execution.json#H-03", "Média-Alta / Cobrança excessiva de tarifa de escalão superior em fronteira válida", "Open"),
        ("DEF-03", "Sobrescrita destrutiva da taxa base no processamento da zona REMOTE (H-10, H-12, H-13, F-18, F-29)", "BR-03 / Build T08-B1.0 / Python 3.12 & 3.9", "quote(500, 'REMOTE', False) -> linha 14 usa 'fee = 4' em vez de 'fee += 4'", '{"status": "OK", "fee": 9}', '{"status": "OK", "fee": 4}', "final_cases_execution.json#H-10,#H-12,#H-13,#F-18,#F-29", "Crítica / Perda de receita e subfaturação sistemática de expedições para zona REMOTE", "Open"),
        ("DEF-04", "Limiar incorreto de indisponibilidade de express para REMOTE: 10000g em vez de 5000g (H-14, F-19, F-30)", "BR-04 / Build T08-B1.0 / Python 3.12 & 3.9", "quote(5001, 'REMOTE', True) -> linha 5 usa 'weight > 10000'", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "final_cases_execution.json#H-14,#F-19,#F-30", "Alta / Aceitação de encomendas express remotas em pesos não suportados operacionalmente", "Open"),
        ("DATA-01", "Expectativa incorreta gerada por IA no candidato AI-05 (omite taxa base, replica DEF-03)", "BR-03 / ai_candidates.json#AI-05", "Runner executa AI-05 com expected fee=4 em vez de 9 -> gera falso PASS no runner original", '{"status": "OK", "fee": 9}', '{"status": "OK", "fee": 4}', "ai_candidates_execution.json#AI-05", "Média / Falha de oráculo da IA (rejeitado na revisão humana independente)", "Rejected (AI Data)"),
        ("DATA-02", "Expectativa incorreta gerada por IA no candidato AI-06 (off-by-one em 1000g, replica DEF-02)", "BR-02 / ai_candidates.json#AI-06", "Runner executa AI-06 com expected fee=8 em vez de 5 -> gera falso PASS no runner original", '{"status": "OK", "fee": 5}', '{"status": "OK", "fee": 8}', "ai_candidates_execution.json#AI-06", "Média / Falha de oráculo da IA (rejeitado na revisão humana independente)", "Rejected (AI Data)"),
        ("DATA-03", "Tentativa de tarifação de serviço indisponível gerada por IA no candidato AI-09 (revisto para F-19)", "BR-04 / ai_candidates.json#AI-09", "Runner executa AI-09 com expected fee=22 em vez de UNAVAILABLE -> falha no runner", '{"status": "UNAVAILABLE", "fee": null}', '{"status": "OK", "fee": 10}', "ai_candidates_execution.json#AI-09", "Alta / Erro conceitual de oráculo da IA (revisto para oráculo correto na suite final)", "Revised to F-19")
    ]

    s3_rows = []
    s3_rows.append('<row r="1" spans="1:9"><c r="A1" t="str"><v>Defects — T08</v></c><c r="B1"/><c r="C1"/><c r="D1"/><c r="E1"/><c r="F1"/><c r="G1"/><c r="H1"/><c r="I1"/></row>')
    s3_rows.append('<row r="2" spans="1:9"><c r="A2" t="str"><v>One report per reproducible issue; distinguish source data issues, specification questions and software defects.</v></c><c r="B2"/><c r="C2"/><c r="D2"/><c r="E2"/><c r="F2"/><c r="G2"/><c r="H2"/><c r="I2"/></row>')
    s3_rows.append('<row r="3" spans="1:9"><c r="A3"/><c r="B3"/><c r="C3"/><c r="D3"/><c r="E3"/><c r="F3"/><c r="G3"/><c r="H3"/><c r="I3"/></row>')
    s3_rows.append('<row r="4" spans="1:9"><c r="A4" t="str"><v>Defect ID</v></c><c r="B4" t="str"><v>Title / tests</v></c><c r="C4" t="str"><v>Rule / build / environment</v></c><c r="D4" t="str"><v>Exact reproduction</v></c><c r="E4" t="str"><v>Expected</v></c><c r="F4" t="str"><v>Actual</v></c><c r="G4" t="str"><v>Evidence</v></c><c r="H4" t="str"><v>Severity / rationale</v></c><c r="I4" t="str"><v>Status</v></c></row>')

    for idx, d in enumerate(defects_data, 5):
        cells = [
            make_cell(f'A{idx}', d[0]),
            make_cell(f'B{idx}', d[1]),
            make_cell(f'C{idx}', d[2]),
            make_cell(f'D{idx}', d[3]),
            make_cell(f'E{idx}', d[4]),
            make_cell(f'F{idx}', d[5]),
            make_cell(f'G{idx}', d[6]),
            make_cell(f'H{idx}', d[7]),
            make_cell(f'I{idx}', d[8])
        ]
        s3_rows.append(f'<row r="{idx}" spans="1:9">{"".join(cells)}</row>')

    for idx in range(len(defects_data) + 5, 45):
        s3_rows.append(f'<row r="{idx}" spans="1:9"><c r="A{idx}"/><c r="B{idx}"/><c r="C{idx}"/><c r="D{idx}"/><c r="E{idx}"/><c r="F{idx}"/><c r="G{idx}"/><c r="H{idx}"/><c r="I{idx}"/></row>')

    sheet3_xml = f'<?xml version="1.0" encoding="utf-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheetViews><sheetView tabSelected="0" workbookViewId="0"/></sheetViews><sheetFormatPr defaultRowHeight="15"/><sheetData>{"".join(s3_rows)}</sheetData><tableParts count="1"><tablePart r:id="rId1"/></tableParts></worksheet>'
    entries['xl/worksheets/sheet3.xml'] = sheet3_xml.encode('utf-8')


    # -------------------------------------------------------------------------
    # 4. Update Sheet 5: Coverage (Mapping all requirements R01..R08 to test cases)
    # -------------------------------------------------------------------------
    # Requirements mapping table (rows 21..120)
    req_mappings = [
        # R01: BR-01 (Weight & Zone & Express basic validation)
        ("R01", "H-ENV"), ("R01", "H-02"), ("R01", "H-03"), ("R01", "H-07"), ("R01", "H-08"),
        ("R01", "H-09"), ("R01", "H-15"), ("R01", "H-16"), ("R01", "F-20"), ("R01", "F-21"),
        ("R01", "F-22"), ("R01", "F-23"), ("R01", "F-25"), ("R01", "F-26"), ("R01", "F-27"),
        # R02: BR-02 (Weight tiers: 1-1000:5, 1001-5000:8, 5001-20000:12)
        ("R02", "H-ENV"), ("R02", "H-01"), ("R02", "H-02"), ("R02", "H-03"), ("R02", "H-04"),
        ("R02", "H-05"), ("R02", "H-06"), ("R02", "H-07"), ("R02", "H-10"), ("R02", "H-11"),
        ("R02", "H-12"), ("R02", "H-13"), ("R02", "F-17"), ("R02", "F-18"), ("R02", "F-24"),
        ("R02", "F-28"), ("R02", "F-29"),
        # R03: BR-03 (Zone and express surcharges: REMOTE +4, express +6, cumulative)
        ("R03", "H-01"), ("R03", "H-10"), ("R03", "H-11"), ("R03", "H-12"), ("R03", "H-13"),
        ("R03", "F-17"), ("R03", "F-18"), ("R03", "F-24"), ("R03", "F-28"), ("R03", "F-29"),
        # R04: BR-04 (REMOTE express unavailable above 5000g)
        ("R04", "H-13"), ("R04", "H-14"), ("R04", "F-19"), ("R04", "F-21"), ("R04", "F-30"),
        # R05: BR-05 (Independence, no side effects, idempotency)
        ("R05", "F-21"), ("R05", "H-ENV"),
        # R06: BR-06 (JSON format, run_cases.py, Python 3.10+)
        ("R06", "H-ENV"), ("R06", "H-01"), ("R06", "H-07"), ("R06", "H-14"), ("R06", "F-17"),
        ("R06", "F-21"), ("R06", "F-30"),
        # R07: BR-07 (Exact matching, exit codes: 0=PASS, 1=FAIL, 2=blocked/error)
        ("R07", "H-ENV"), ("R07", "H-01"), ("R07", "H-03"), ("R07", "F-18"), ("R07", "F-21"),
        # R08: BR-08 (Traceability, AI disclosure, human verification)
        ("R08", "H-01"), ("R08", "F-17"), ("R08", "F-18"), ("R08", "F-19")
    ]

    # Calculate summary counts per requirement
    req_counts = {}
    for r_id, _ in req_mappings:
        req_counts[r_id] = req_counts.get(r_id, 0) + 1

    s5_rows = []
    s5_rows.append('<row r="1" spans="1:5"><c r="A1" t="str"><v>Requirement coverage — T08</v></c><c r="B1"/><c r="C1"/><c r="D1"/><c r="E1"/></row>')
    s5_rows.append('<row r="2" spans="1:5"><c r="A2" t="str"><v>Unique valid test links; executed = at least one PASS or FAIL. This is not technique coverage.</v></c><c r="B2"/><c r="C2"/><c r="D2"/><c r="E2"/></row>')
    s5_rows.append('<row r="3" spans="1:5"><c r="A3"/><c r="B3"/><c r="C3"/><c r="D3"/><c r="E3"/></row>')
    s5_rows.append('<row r="4" spans="1:5"><c r="A4" t="str"><v>Requirement</v></c><c r="B4" t="str"><v>Business rule</v></c><c r="C4" t="str"><v>Designed</v></c><c r="D4" t="str"><v>Executed</v></c><c r="E4" t="str"><v>Not executed</v></c></row>')

    req_defs = [
        ("R01", "BR-01"),
        ("R02", "BR-02"),
        ("R03", "BR-03"),
        ("R04", "BR-04"),
        ("R05", "BR-05"),
        ("R06", "BR-06"),
        ("R07", "BR-07"),
        ("R08", "BR-08")
    ]

    for idx, (r_id, br_id) in enumerate(req_defs, 5):
        cnt = str(req_counts.get(r_id, 0))
        cells = [
            f'<c r="A{idx}" t="str"><v>{r_id}</v></c>',
            f'<c r="B{idx}" t="str"><v>{br_id}</v></c>',
            f'<c r="C{idx}"><f>SUMIFS($C$21:$C$120,$A$21:$A$120,A{idx})</f><v>{cnt}</v></c>',
            f'<c r="D{idx}"><f>SUMIFS($D$21:$D$120,$A$21:$A$120,A{idx})</f><v>{cnt}</v></c>',
            f'<c r="E{idx}"><f>C{idx}-D{idx}</f><v>0</v></c>'
        ]
        s5_rows.append(f'<row r="{idx}" spans="1:5">{"".join(cells)}</row>')

    # Rows 13-19 empty / instruction
    for idx in range(13, 20):
        if idx == 15:
            s5_rows.append(f'<row r="{idx}" spans="1:5"><c r="A{idx}" t="str"><v>Amber = editable. White = formula. Add one requirement–test pair per row below.</v></c><c r="B{idx}"/><c r="C{idx}"/><c r="D{idx}"/><c r="E{idx}"/></row>')
        else:
            s5_rows.append(f'<row r="{idx}" spans="1:5"><c r="A{idx}"/><c r="B{idx}"/><c r="C{idx}"/><c r="D{idx}"/><c r="E{idx}"/></row>')

    # Row 20 header
    s5_rows.append('<row r="20" spans="1:5"><c r="A20" t="str"><v>Requirement ID</v></c><c r="B20" t="str"><v>Test ID</v></c><c r="C20" t="str"><v>Valid unique link</v></c><c r="D20" t="str"><v>Executed (0/1)</v></c><c r="E20" t="str"><v>Link check</v></c></row>')

    # Rows 21..120: Requirement mapping pairs
    for idx in range(21, 121):
        pair_idx = idx - 21
        if pair_idx < len(req_mappings):
            r_id, t_id = req_mappings[pair_idx]
            f_c = f'IF(OR(A{idx}="",B{idx}=""),0,IF(AND(COUNTIFS($A$5:$A$12,A{idx})=1,COUNTIFS(\'Test Cases\'!$A$5:$A$84,B{idx})=1,COUNTIFS($A$21:A{idx},A{idx},$B$21:B{idx},B{idx})=1),1,0))'
            # In Executions sheet: B is Test ID, G is Verdict!
            f_d = f'IF(C{idx}=0,0,IF(COUNTIFS(Executions!$B$5:$B$84,B{idx},Executions!$G$5:$G$84,"PASS")+COUNTIFS(Executions!$B$5:$B$84,B{idx},Executions!$G$5:$G$84,"FAIL")>0,1,0))'
            f_e = f'IF(AND(A{idx}="",B{idx}=""),"",IF(C{idx}=1,"Linked","Check IDs / duplicate"))'
            cells = [
                f'<c r="A{idx}" t="str"><v>{r_id}</v></c>',
                f'<c r="B{idx}" t="str"><v>{t_id}</v></c>',
                f'<c r="C{idx}"><f>{f_c}</f><v>1</v></c>',
                f'<c r="D{idx}"><f>{f_d}</f><v>1</v></c>',
                f'<c r="E{idx}" t="str"><f>{f_e}</f><v>Linked</v></c>'
            ]
            s5_rows.append(f'<row r="{idx}" spans="1:5">{"".join(cells)}</row>')
        else:
            f_c = f'IF(OR(A{idx}="",B{idx}=""),0,IF(AND(COUNTIFS($A$5:$A$12,A{idx})=1,COUNTIFS(\'Test Cases\'!$A$5:$A$84,B{idx})=1,COUNTIFS($A$21:A{idx},A{idx},$B$21:B{idx},B{idx})=1),1,0))'
            f_d = f'IF(C{idx}=0,0,IF(COUNTIFS(Executions!$B$5:$B$84,B{idx},Executions!$G$5:$G$84,"PASS")+COUNTIFS(Executions!$B$5:$B$84,B{idx},Executions!$G$5:$G$84,"FAIL")>0,1,0))'
            f_e = f'IF(AND(A{idx}="",B{idx}=""),"",IF(C{idx}=1,"Linked","Check IDs / duplicate"))'
            cells = [
                f'<c r="A{idx}"/>',
                f'<c r="B{idx}"/>',
                f'<c r="C{idx}"><f>{f_c}</f><v>0</v></c>',
                f'<c r="D{idx}"><f>{f_d}</f><v>0</v></c>',
                f'<c r="E{idx}" t="str"><f>{f_e}</f><v></v></c>'
            ]
            s5_rows.append(f'<row r="{idx}" spans="1:5">{"".join(cells)}</row>')

    sheet5_xml = f'<?xml version="1.0" encoding="utf-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheetViews><sheetView tabSelected="0" workbookViewId="0"/></sheetViews><sheetFormatPr defaultRowHeight="15"/><sheetData>{"".join(s5_rows)}</sheetData></worksheet>'
    entries['xl/worksheets/sheet5.xml'] = sheet5_xml.encode('utf-8')


    # -------------------------------------------------------------------------
    # Save to all target paths
    # -------------------------------------------------------------------------
    target_paths = [
        'TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx',
        'Trabalho_CP1/TestResults_T08_Template.xlsx',
        'Trabalho_CP4/TestResults_T08_Template.xlsx'
    ]

    for tp in target_paths:
        os.makedirs(os.path.dirname(tp), exist_ok=True)
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', compression=zipfile.ZIP_DEFLATED) as z_out:
            for name, content in entries.items():
                z_out.writestr(name, content)
        with open(tp, 'wb') as f:
            f.write(buf.getvalue())
        print(f'Successfully updated: {tp} ({len(buf.getvalue())} bytes)')

if __name__ == '__main__':
    build_workbook()
