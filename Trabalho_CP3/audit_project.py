#!/usr/bin/env python3
"""Automated Project Audit and Integrity Verification Script for TVSI_2627.

Usage:
    python3 Trabalho_CP3/audit_project.py

Validates:
1. Existence of all mandatory project deliverables.
2. Syntax and structure of all JSON files.
3. Frozen status of CP02 human test suite (16 cases).
4. Final test suite composition (21 cases: 13 PASS / 8 FAIL).
5. Dual-Python execution evidence parity (Python 3.9.6 vs Python 3.12.7).
6. Defect traceability matrix (DEF-01 to DEF-04) and absence of H-13/DEF-04 confusion.
7. BR-05 multi-property independence evidence (4 properties, both Py 3.9 and Py 3.12).
8. Excel workbook integrity (6 sheets, 22 cases, 0 formula errors).
9. Submission ZIP package completeness and archive integrity.
"""

import sys, os, json, pathlib, subprocess, zipfile, xml.etree.ElementTree as ET

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

def run_audit():
    print("=" * 80)
    print("  TVSI_2627 — AUTOMATED PROJECT AUDIT AND INTEGRITY VERIFICATION")
    print("  T08: AI-Assisted Test Design | Grupo 5")
    print("=" * 80)

    checks_passed = 0
    checks_total = 0
    failures = []

    def check(name, condition, error_msg=""):
        nonlocal checks_passed, checks_total
        checks_total += 1
        if condition:
            checks_passed += 1
            print(f"  [PASS] {name}")
            return True
        else:
            failures.append(f"{name}: {error_msg}")
            print(f"  [FAIL] {name} — {error_msg}")
            return False

    # -------------------------------------------------------------------------
    # 1. Existence of Mandatory Deliverables
    # -------------------------------------------------------------------------
    print("\n[1/9] Verifying Mandatory Deliverables...")
    required_files = [
        "Relatorio_Consolidado.md",
        "README.md",
        "CLAUDE.md",
        "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx",
        "TVSI_T08_Students_B1.0/BusinessRules.md",
        "TVSI_T08_Students_B1.0/StudentAssignment.md",
        "TVSI_T08_Students_B1.0/AI_PROVENANCE.md",
        "TVSI_T08_Students_B1.0/app/shipping.py",
        "TVSI_T08_Students_B1.0/app/run_cases.py",
        "TVSI_T08_Students_B1.0/app/ai_candidates.json",
        "Trabalho_CP1/CP1.md",
        "Trabalho_CP2/CP2.md",
        "Trabalho_CP2/Relatorio_CP2.md",
        "Trabalho_CP2/human_cases.json",
        "Trabalho_CP2/human_cases.results.json",
        "Trabalho_CP3/CP3.md",
        "Trabalho_CP3/Relatorio_CP3.md",
        "Trabalho_CP3/final_cases.json",
        "Trabalho_CP3/final_cases.results.json",
        "Trabalho_CP3/final_cases.results.py312.json",
        "Trabalho_CP3/verify_br05_independence.py",
        "Trabalho_CP3/br05_independence.results.json",
        "Trabalho_CP3/br05_independence.py312.json"
    ]
    missing = [f for f in required_files if not (ROOT_DIR / f).is_file()]
    check("All required repository files exist", len(missing) == 0, f"Missing: {missing}")

    # -------------------------------------------------------------------------
    # 2. JSON Syntax Validation
    # -------------------------------------------------------------------------
    print("\n[2/9] Validating JSON Files Syntax...")
    json_files = list(ROOT_DIR.glob("**/*.json"))
    json_errors = []
    for jf in json_files:
        if ".git" in str(jf):
            continue
        try:
            with open(jf, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            json_errors.append(f"{jf.name}: {e}")
    check("All JSON files are valid syntax", len(json_errors) == 0, f"Errors: {json_errors}")

    # -------------------------------------------------------------------------
    # 3. Frozen Human Suite Integrity
    # -------------------------------------------------------------------------
    print("\n[3/9] Checking Frozen Human Suite Integrity (CP02)...")
    human_json = ROOT_DIR / "Trabalho_CP2" / "human_cases.json"
    with open(human_json, "r", encoding="utf-8") as f:
        human_cases = json.load(f)
    check("Human suite has exactly 16 cases", len(human_cases) == 16, f"Count: {len(human_cases)}")
    check("Human suite IDs are H-01 to H-16", [c["id"] for c in human_cases] == [f"H-{i:02d}" for i in range(1, 17)])

    # Check git diff against freeze commit 54ec4d3 if git available
    try:
        git_diff = subprocess.run(["git", "diff", "54ec4d3", "--", str(human_json)], capture_output=True, text=True, cwd=ROOT_DIR)
        check("Human cases identical to freeze commit 54ec4d3", git_diff.stdout.strip() == "", "File was modified since freeze commit")
    except Exception as e:
        print(f"  [WARN] Could not run git diff: {e}")

    # -------------------------------------------------------------------------
    # 4. Final Suite Composition and Results
    # -------------------------------------------------------------------------
    print("\n[4/9] Checking Final Test Suite Composition and Results (CP03)...")
    final_json = ROOT_DIR / "Trabalho_CP3" / "final_cases.json"
    with open(final_json, "r", encoding="utf-8") as f:
        final_cases = json.load(f)
    check("Final suite has exactly 21 cases", len(final_cases) == 21, f"Count: {len(final_cases)}")
    expected_ids = [f"H-{i:02d}" for i in range(1, 17)] + [f"F-{i:02d}" for i in range(17, 22)]
    check("Final suite IDs are H-01..H-16 + F-17..F-21", [c["id"] for c in final_cases] == expected_ids)

    # -------------------------------------------------------------------------
    # 5. Dual-Python Execution Evidence Parity
    # -------------------------------------------------------------------------
    print("\n[5/9] Validating Dual-Python Execution Results...")
    res_py39 = json.load(open(ROOT_DIR / "Trabalho_CP3" / "final_cases.results.json"))
    res_py312 = json.load(open(ROOT_DIR / "Trabalho_CP3" / "final_cases.results.py312.json"))

    check("Python 3.9 results record Python 3.9 runtime", "3.9" in res_py39["python"])
    check("Python 3.12 results record Python 3.12 runtime", "3.12" in res_py312["python"])

    pass_39 = sum(1 for r in res_py39["results"] if r["verdict"] == "PASS")
    fail_39 = sum(1 for r in res_py39["results"] if r["verdict"] == "FAIL")
    pass_312 = sum(1 for r in res_py312["results"] if r["verdict"] == "PASS")
    fail_312 = sum(1 for r in res_py312["results"] if r["verdict"] == "FAIL")

    check("Python 3.9 results: 13 PASS / 8 FAIL", pass_39 == 13 and fail_39 == 8, f"Got {pass_39} PASS / {fail_39} FAIL")
    check("Python 3.12 results: 13 PASS / 8 FAIL", pass_312 == 13 and fail_312 == 8, f"Got {pass_312} PASS / {fail_312} FAIL")
    check("Strict parity of all 21 outputs between Py 3.9 and Py 3.12", res_py39["results"] == res_py312["results"])

    # -------------------------------------------------------------------------
    # 6. Defect Traceability Matrix and H-13/DEF-04 Verification
    # -------------------------------------------------------------------------
    print("\n[6/9] Auditing Defect Traceability (DEF-01 to DEF-04)...")
    fail_dict = {r["id"]: r for r in res_py39["results"] if r["verdict"] == "FAIL"}
    check("Exact 8 failing tests in final suite", set(fail_dict.keys()) == {"H-03", "H-07", "H-10", "H-12", "H-13", "H-14", "F-18", "F-19"})

    # Check that H-13 uses weight=5000 and expects OK/18, getting OK/10 (DEF-03)
    h13_case = next(c for c in final_cases if c["id"] == "H-13")
    check("H-13 has weight=5000, express=True, zone=REMOTE", h13_case["input"] == {"weight": 5000, "zone": "REMOTE", "express": True})
    check("H-13 expected is OK, fee=18 (available under BR-04)", h13_case["expected"] == {"status": "OK", "fee": 18})

    # Verify no erroneous H-13 -> DEF-04 links in deliverables
    # H-13 must strictly NOT be listed as detecting DEF-04 (only DEF-03)
    target_docs = [
        ROOT_DIR / "Relatorio_Consolidado.md",
        ROOT_DIR / "README.md",
        ROOT_DIR / "Trabalho_CP2" / "CP2.md",
        ROOT_DIR / "Trabalho_CP2" / "Relatorio_CP2.md",
        ROOT_DIR / "Trabalho_CP3" / "Relatorio_CP3.md"
    ]
    bad_associations = []
    for mf in target_docs:
        if not mf.exists():
            continue
        text = mf.read_text(encoding="utf-8")
        lines = text.splitlines()
        for idx, line in enumerate(lines, 1):
            # Check if line lists H-13 under DEF-04 or maps H-13 to DEF-04 as a detector
            if "DEF-04" in line and "H-13" in line:
                lower = line.lower()
                if not any(neg in lower for neg in ["não deteta", "não viola", "exclusiv", "situa-se", "apenas", "único", "estrit", "demarca"]):
                    bad_associations.append(f"{mf.name}:{idx}: {line.strip()}")
    check("Zero erroneous H-13 / DEF-04 associations in deliverable documents", len(bad_associations) == 0, f"Found: {bad_associations}")

    # -------------------------------------------------------------------------
    # 7. BR-05 Multi-Property Independence Verification
    # -------------------------------------------------------------------------
    print("\n[7/9] Verifying BR-05 Multi-Property Evidences...")
    br_39 = json.load(open(ROOT_DIR / "Trabalho_CP3" / "br05_independence.results.json"))
    br_312 = json.load(open(ROOT_DIR / "Trabalho_CP3" / "br05_independence.py312.json"))

    check("BR-05 Py 3.9 overall verdict is PASS", br_39["overall_verdict"] == "PASS")
    check("BR-05 Py 3.12 overall verdict is PASS", br_312["overall_verdict"] == "PASS")
    check("BR-05 Py 3.9 tests all 4 properties (PASS)", len(br_39["tests"]) == 4 and all(t["verdict"] == "PASS" for t in br_39["tests"]))
    check("BR-05 Py 3.12 tests all 4 properties (PASS)", len(br_312["tests"]) == 4 and all(t["verdict"] == "PASS" for t in br_312["tests"]))
    check("BR-05 correctly delimits app_dir filesystem scope", "direct files in app_dir" in br_39["verification_scope"].get("filesystem_scope_delimitation", ""))

    # -------------------------------------------------------------------------
    # 8. Excel Workbook Integrity
    # -------------------------------------------------------------------------
    print("\n[8/9] Auditing Official Excel Workbook...")
    wb_path = ROOT_DIR / "TVSI_T08_Students_B1.0" / "TestResults_T08_Template.xlsx"
    with zipfile.ZipFile(wb_path, "r") as z:
        wb_xml = ET.fromstring(z.read("xl/workbook.xml"))
        ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
        sheets = [s.attrib["name"] for s in wb_xml.findall(f".//{ns}sheet")]
        expected_sheets = ["Test Cases", "Executions", "Defects", "Static Review", "Coverage", "Technique"]
        check("Workbook contains exactly the 6 official sheets", sheets == expected_sheets, f"Got: {sheets}")

        # Check for formula errors across all sheets
        errors_found = []
        for i, sname in enumerate(sheets, 1):
            s_xml = ET.fromstring(z.read(f"xl/worksheets/sheet{i}.xml"))
            for c in s_xml.findall(f".//{ns}c"):
                v = c.find(f"{ns}v")
                if v is not None and v.text and any(err in v.text for err in ["#REF!", "#VALUE!", "#NAME?", "#DIV/0!", "#N/A"]):
                    errors_found.append(f"{sname}:{c.attrib.get('r')} = {v.text}")
        check("Zero formula errors (#REF!, #VALUE!, etc.) in workbook", len(errors_found) == 0, f"Errors: {errors_found}")

        # Check H-13 defect in Executions sheet (cell I18)
        s2_xml = ET.fromstring(z.read("xl/worksheets/sheet2.xml"))
        i18_cell = next((c for c in s2_xml.findall(f".//{ns}c") if c.attrib.get("r") == "I18"), None)
        i18_val = i18_cell.find(f"{ns}v").text if i18_cell is not None and i18_cell.find(f"{ns}v") is not None else ""
        check("Cell I18 (RUN-14 for H-13) defect is strictly DEF-03", i18_val == "DEF-03", f"Got: '{i18_val}'")

    # -------------------------------------------------------------------------
    # 9. Submission ZIP Integrity
    # -------------------------------------------------------------------------
    print("\n[9/9] Checking Submission ZIP Package...")
    zip_path = ROOT_DIR / "TVSI_T08_Grupo5_CP03.zip"
    if check("TVSI_T08_Grupo5_CP03.zip exists", zip_path.is_file()):
        with zipfile.ZipFile(zip_path, "r") as zf:
            corrupt = zf.testzip()
            check("ZIP archive passes crc32/read test without corruption", corrupt is None, f"Corrupt file: {corrupt}")
            check("ZIP contains Relatorio_Consolidado.md", "Relatorio_Consolidado.md" in zf.namelist())
            check("ZIP contains TestResults_T08_Template.xlsx", "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx" in zf.namelist())
            check("ZIP contains dual Python result files", "Trabalho_CP3/final_cases.results.py312.json" in zf.namelist() and "Trabalho_CP3/final_cases.results.json" in zf.namelist())

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print(f"AUDIT SUMMARY: {checks_passed} / {checks_total} CHECKS PASSED")
    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"  - {f}")
        print("=" * 80)
        return 1
    else:
        print("STATUS: ALL CHECKS PASSED — REPOSITORY 100% COMPLIANT")
        print("=" * 80)
        return 0

if __name__ == "__main__":
    sys.exit(run_audit())
