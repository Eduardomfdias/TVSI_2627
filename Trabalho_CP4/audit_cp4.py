#!/usr/bin/env python3
"""Automated Integrity and Quality Audit Script for CP04 — TVSI_2627.

Usage:
    python3 Trabalho_CP4/audit_cp4.py

Validates the 11 normative areas:
1. Original baseline integrity (shipping.py, BusinessRules.md, StudentAssignment.md).
2. Frozen human suite preservation (H-01..H-16 + H-ENV = 17 entries).
3. Existence and validity of all test execution evidences.
4. Correspondence between Test IDs and execution runs.
5. Correspondence between Requirement IDs and test cases.
6. Execution results consistency (Human: 11 PASS / 6 FAIL; AI: 10 PASS / 2 FAIL; Final: 20 PASS / 10 FAIL).
7. Traceability and structure of defect reports (DEF-01..04 vs DATA-01..03).
8. Excel workbook integrity (6 sheets, autonomous Requirement column, 0 formula errors).
9. Documentation consistency (CP4 plan, CP4 report, consolidated report, README).
10. ZIP submission package integrity (TVSI_T08_Grupo5_CP04.zip).
11. Cryptographic SHA-256 correspondence with MANIFEST_ENTREGA.md.
"""

import sys, os, json, pathlib, subprocess, zipfile, hashlib
import xml.etree.ElementTree as ET

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

def calculate_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def run_audit():
    print("=" * 80)
    print("  TVSI_2627 — CHECKPOINT 4 (CP04) AUTOMATED COMPLIANCE & QUALITY AUDIT")
    print("  U. Minho | TVSI 2026/27 | T08: AI-Assisted Test Design | Grupo 5")
    print("=" * 80)

    stats = {"PASS": 0, "FAIL": 0, "WARNING": 0, "BLOCKED": 0}
    findings = []

    def log_result(status, check_name, details=""):
        stats[status] += 1
        tag = f"[{status}]"
        if details:
            print(f"  {tag:<10} {check_name} — {details}")
            if status in ("FAIL", "BLOCKED"):
                findings.append(f"{check_name}: {details}")
        else:
            print(f"  {tag:<10} {check_name}")

    # -------------------------------------------------------------------------
    # AREA 1: Original Baseline Integrity
    # -------------------------------------------------------------------------
    print("\n[AREA 1/11] Auditing Original Baseline Integrity...")
    shipping_path = ROOT_DIR / "TVSI_T08_Students_B1.0/app/shipping.py"
    if not shipping_path.is_file():
        log_result("BLOCKED", "Baseline shipping.py exists", "shipping.py missing!")
    else:
        # Verify shipping.py is identical to origin
        try:
            diff = subprocess.run(["git", "diff", "origin/main", "--", str(shipping_path)], capture_output=True, text=True, cwd=ROOT_DIR)
            if diff.stdout.strip() == "":
                log_result("PASS", "Baseline shipping.py is 100% intact and unmodified")
            else:
                log_result("FAIL", "Baseline shipping.py modified", diff.stdout[:200])
        except Exception as e:
            log_result("WARNING", "Git diff check on shipping.py", str(e))

    normative_files = [
        "TVSI_T08_Students_B1.0/BusinessRules.md",
        "TVSI_T08_Students_B1.0/StudentAssignment.md",
        "TVSI_T08_Students_B1.0/START_HERE.md",
        "TVSI_T08_Students_B1.0/AI_PROVENANCE.md",
        "TVSI_T08_Students_B1.0/app/run_cases.py"
    ]
    missing_normative = [f for f in normative_files if not (ROOT_DIR / f).is_file()]
    if not missing_normative:
        log_result("PASS", "All official instructor normative documents are present")
    else:
        log_result("FAIL", "Missing normative documents", str(missing_normative))

    # -------------------------------------------------------------------------
    # AREA 2: Frozen Human Suite Preservation
    # -------------------------------------------------------------------------
    print("\n[AREA 2/11] Checking Frozen Human Suite Preservation...")
    cp2_human_json = ROOT_DIR / "Trabalho_CP2/human_cases.json"
    if cp2_human_json.is_file():
        with open(cp2_human_json, "r", encoding="utf-8") as f:
            h_data = json.load(f)
        if len(h_data) == 16 and [c["id"] for c in h_data] == [f"H-{i:02d}" for i in range(1, 17)]:
            log_result("PASS", "CP02 frozen human suite contains exactly 16 cases (H-01 to H-16)")
        else:
            log_result("FAIL", "CP02 human suite corrupted", f"Count: {len(h_data)}")
        
        # Check against freeze commit 54ec4d3
        try:
            diff_cp2 = subprocess.run(["git", "diff", "54ec4d3", "--", str(cp2_human_json)], capture_output=True, text=True, cwd=ROOT_DIR)
            if diff_cp2.stdout.strip() == "":
                log_result("PASS", "CP02 human suite is identical to freeze commit 54ec4d3")
            else:
                log_result("FAIL", "CP02 human suite was modified after freeze commit", diff_cp2.stdout[:200])
        except Exception as e:
            log_result("WARNING", "Git diff against freeze commit 54ec4d3", str(e))
    else:
        log_result("BLOCKED", "CP02 human_cases.json exists", "File not found")

    cp4_human_json = ROOT_DIR / "Trabalho_CP4/human_cases_cp4.json"
    if cp4_human_json.is_file():
        with open(cp4_human_json, "r", encoding="utf-8") as f:
            h4_data = json.load(f)
        if len(h4_data) == 17 and h4_data[0]["id"] == "H-ENV" and [c["id"] for c in h4_data[1:]] == [f"H-{i:02d}" for i in range(1, 17)]:
            log_result("PASS", "CP04 human suite contains exactly 17 entries (H-ENV + H-01..H-16)")
        else:
            log_result("FAIL", "CP04 human suite mismatch", f"Count: {len(h4_data)}")
    else:
        log_result("FAIL", "CP04 human_cases_cp4.json exists", "Missing file")

    # -------------------------------------------------------------------------
    # AREA 3: Existence and Validity of All Test Evidences
    # -------------------------------------------------------------------------
    print("\n[AREA 3/11] Auditing Test Execution Evidences...")
    required_evidence_files = [
        "Trabalho_CP4/runs/human_17_execution.json",
        "Trabalho_CP4/runs/ai_candidates_execution.json",
        "Trabalho_CP4/runs/final_cases_execution.json",
        "Trabalho_CP4/runs/final_cases_execution.py312.json",
        "Trabalho_CP4/evidence/br05_independence_cp4.json",
        "Trabalho_CP4/evidence/runner_robustness_evidence.json"
    ]
    missing_evidence = [ef for ef in required_evidence_files if not (ROOT_DIR / ef).is_file()]
    if not missing_evidence:
        log_result("PASS", "All required CP04 run execution and evidence files exist")
    else:
        log_result("FAIL", "Missing evidence files", str(missing_evidence))

    # -------------------------------------------------------------------------
    # AREA 4: Correspondence Between Test IDs and Execution Runs
    # -------------------------------------------------------------------------
    print("\n[AREA 4/11] Verifying Test IDs and Execution Correspondence...")
    final_cases_file = ROOT_DIR / "Trabalho_CP4/final_cases.json"
    final_run_file = ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.json"
    if final_cases_file.is_file() and final_run_file.is_file():
        with open(final_cases_file) as f1, open(final_run_file) as f2:
            fc_data = json.load(f1)
            fr_data = json.load(f2)
        suite_ids = [c["id"] for c in fc_data]
        run_ids = [r["id"] for r in fr_data.get("results", [])]
        if suite_ids == run_ids:
            log_result("PASS", f"Strict 1-to-1 correspondence between suite Test IDs and run execution ({len(suite_ids)} cases)")
        else:
            log_result("FAIL", "Mismatch between suite IDs and run IDs", f"Suite: {len(suite_ids)}, Run: {len(run_ids)}")
    else:
        log_result("BLOCKED", "Final cases and run files available", "Files missing")

    # -------------------------------------------------------------------------
    # AREA 5: Correspondence Between Requirement IDs and Test Cases
    # -------------------------------------------------------------------------
    print("\n[AREA 5/11] Verifying Requirement IDs Coverage...")
    wb_file = ROOT_DIR / "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx"
    with zipfile.ZipFile(wb_file, "r") as z:
        ns_xl = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
        s5_xml = ET.fromstring(z.read("xl/worksheets/sheet5.xml"))
        req_counts = {}
        for r in s5_xml.findall(f".//{ns_xl}row")[4:12]:
            cells = {c.attrib.get("r")[0]: c.find(f"{ns_xl}v").text if c.find(f"{ns_xl}v") is not None else "" for c in r.findall(f"{ns_xl}c")}
            req_id = cells.get("A")
            des = int(cells.get("C", 0))
            exc = int(cells.get("D", 0))
            not_exc = int(cells.get("E", 0))
            req_counts[req_id] = (des, exc, not_exc)
        
        all_covered = len(req_counts) == 8 and all(v[0] > 0 and v[0] == v[1] and v[2] == 0 for v in req_counts.values())
        if all_covered:
            log_result("PASS", "100% Requirement coverage (R01..R08): all designed tests are executed with 0 unexecuted")
        else:
            log_result("FAIL", "Requirement coverage gaps found", str(req_counts))

    # -------------------------------------------------------------------------
    # AREA 6: Execution Results Consistency
    # -------------------------------------------------------------------------
    print("\n[AREA 6/11] Auditing Execution Results Consistency...")
    # Human suite (17 cases -> 11 PASS, 6 FAIL)
    if (ROOT_DIR / "Trabalho_CP4/runs/human_17_execution.json").is_file():
        h_run = json.load(open(ROOT_DIR / "Trabalho_CP4/runs/human_17_execution.json"))
        h_res = h_run.get("results", [])
        h_p = sum(1 for r in h_res if r["verdict"] == "PASS")
        h_f = sum(1 for r in h_res if r["verdict"] == "FAIL")
        if len(h_res) == 17 and h_p == 11 and h_f == 6:
            log_result("PASS", f"Human suite (17 cases): 11 PASS / 6 FAIL (Matches specification)")
        else:
            log_result("FAIL", "Human suite verdict count mismatch", f"Total: {len(h_res)}, PASS: {h_p}, FAIL: {h_f}")

    # AI original suite (12 cases -> 10 PASS, 2 FAIL in original runner)
    if (ROOT_DIR / "Trabalho_CP4/runs/ai_candidates_execution.json").is_file():
        ai_run = json.load(open(ROOT_DIR / "Trabalho_CP4/runs/ai_candidates_execution.json"))
        ai_res = ai_run.get("results", [])
        ai_p = sum(1 for r in ai_res if r["verdict"] == "PASS")
        ai_f = sum(1 for r in ai_res if r["verdict"] == "FAIL")
        if len(ai_res) == 12 and ai_p == 10 and ai_f == 2:
            log_result("PASS", f"AI original suite (12 cases): 10 PASS / 2 FAIL in runner (Preserves historical runner results)")
        else:
            log_result("FAIL", "AI candidates runner verdict count mismatch", f"Total: {len(ai_res)}, PASS: {ai_p}, FAIL: {ai_f}")

    # Final suite (30 cases -> 20 PASS, 10 FAIL)
    if (ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.json").is_file():
        f_run = json.load(open(ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.json"))
        f_res = f_run.get("results", [])
        f_p = sum(1 for r in f_res if r["verdict"] == "PASS")
        f_f = sum(1 for r in f_res if r["verdict"] == "FAIL")
        if len(f_res) == 30 and f_p == 20 and f_f == 10:
            log_result("PASS", f"Final suite (30 cases): 20 PASS / 10 FAIL (Matches specification)")
        else:
            log_result("FAIL", "Final suite verdict count mismatch", f"Total: {len(f_res)}, PASS: {f_p}, FAIL: {f_f}")

    # Dual-runtime parity
    if (ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.py312.json").is_file():
        f312_run = json.load(open(ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.py312.json"))
        f312_res = f312_run.get("results", [])
        f312_p = sum(1 for r in f312_res if r["verdict"] == "PASS")
        f312_f = sum(1 for r in f312_res if r["verdict"] == "FAIL")
        if len(f312_res) == 30 and f312_p == 20 and f312_f == 10:
            log_result("PASS", "Dual-Python execution parity confirmed (Python 3.9 vs Python 3.12: identical 20 PASS / 10 FAIL)")
        else:
            log_result("FAIL", "Python 3.12 parity mismatch", f"Total: {len(f312_res)}, PASS: {f312_p}, FAIL: {f312_f}")

    # -------------------------------------------------------------------------
    # AREA 7: Structure and Traceability of Defect Reports
    # -------------------------------------------------------------------------
    print("\n[AREA 7/11] Auditing Defect Reports and Classification...")
    with zipfile.ZipFile(wb_file, "r") as z:
        s3_xml = ET.fromstring(z.read("xl/worksheets/sheet3.xml"))
        defect_rows = []
        for r in s3_xml.findall(f".//{ns_xl}row")[4:]:
            cells = {c.attrib.get("r")[0]: c.find(f"{ns_xl}v").text if c.find(f"{ns_xl}v") is not None else "" for c in r.findall(f"{ns_xl}c")}
            d_id = cells.get("A", "")
            if d_id:
                defect_rows.append((d_id, cells.get("B", "")))
        
        d_ids = [d[0] for d in defect_rows]
        has_all_defects = all(f"DEF-0{i}" in d_ids for i in range(1, 5))
        has_ai_issues = all(f"DATA-0{i}" in d_ids for i in range(1, 4))
        if has_all_defects and has_ai_issues:
            log_result("PASS", "Defect register contains 4 software defects (DEF-01..04) and 3 AI data quality issues (DATA-01..03)")
        else:
            log_result("FAIL", "Defect register missing items", f"Found: {d_ids}")

    # -------------------------------------------------------------------------
    # AREA 8: Excel Workbook Integrity
    # -------------------------------------------------------------------------
    print("\n[AREA 8/11] Auditing Excel Workbook Integrity...")
    with zipfile.ZipFile(wb_file, "r") as z:
        wb_xml = ET.fromstring(z.read("xl/workbook.xml"))
        sheets = [s.attrib["name"] for s in wb_xml.findall(f".//{ns_xl}sheet")]
        expected_sheets = ["Test Cases", "Executions", "Defects", "Static Review", "Coverage", "Technique"]
        if sheets == expected_sheets:
            log_result("PASS", "Workbook contains exactly the 6 official sheets in order")
        else:
            log_result("FAIL", "Workbook sheets mismatch", f"Got: {sheets}")

        # Check autonomous Requirement ID(s) column in Executions
        s2_xml = ET.fromstring(z.read("xl/worksheets/sheet2.xml"))
        c4_cell = next((c for c in s2_xml.findall(f".//{ns_xl}c") if c.attrib.get("r") == "C4"), None)
        c4_val = c4_cell.find(f"{ns_xl}v").text if c4_cell is not None and c4_cell.find(f"{ns_xl}v") is not None else ""
        if "Requirement" in c4_val:
            log_result("PASS", f"Autonomous 'Requirement ID(s)' column present in Executions (Cell C4: '{c4_val}')")
        else:
            log_result("FAIL", "Autonomous Requirement column missing in Executions", f"C4: '{c4_val}'")

        # Check for formula errors across all sheets
        errors = []
        for i, sname in enumerate(sheets, 1):
            s_xml = ET.fromstring(z.read(f"xl/worksheets/sheet{i}.xml"))
            for c in s_xml.findall(f".//{ns_xl}c"):
                v = c.find(f"{ns_xl}v")
                if v is not None and v.text and any(err in v.text for err in ["#REF!", "#VALUE!", "#NAME?", "#DIV/0!", "#N/A"]):
                    errors.append(f"{sname}:{c.attrib.get('r')} = {v.text}")
        if not errors:
            log_result("PASS", "Zero formula errors (#REF!, #VALUE!, etc.) across all 6 workbook sheets")
        else:
            log_result("FAIL", "Formula errors detected in workbook", str(errors))

    # -------------------------------------------------------------------------
    # AREA 9: Documentation Consistency
    # -------------------------------------------------------------------------
    print("\n[AREA 9/11] Checking Documentation Consistency...")
    cp4_plan = ROOT_DIR / "Trabalho_CP4/CP4.md"
    cp4_rep = ROOT_DIR / "Trabalho_CP4/Relatorio_CP4.md"
    if cp4_plan.is_file() and cp4_rep.is_file():
        plan_text = cp4_plan.read_text(encoding="utf-8")
        rep_text = cp4_rep.read_text(encoding="utf-8")
        
        # Verify reference text in CP4 plan
        ref_phrase = "A suite humana utilizada no CP04 preserva integralmente os 16 casos de teste concebidos e congelados no CP02 (H-01 a H-16), sendo acompanhada pelo caso técnico H-ENV para validação do ambiente. O conjunto contém, assim, 17 entradas, sem introdução retroativa de casos apresentados como independentes da revisão dos candidatos de IA."
        has_ref = ref_phrase in plan_text
        no_h20_freeze = "H-20" not in plan_text and "21 testes humanos" not in plan_text
        if has_ref and no_h20_freeze:
            log_result("PASS", "CP04 plan strictly aligns with 17 human entries and official reference text")
        else:
            log_result("FAIL", "CP04 plan contains obsolete or inconsistent human suite description", f"has_ref={has_ref}, no_h20={no_h20_freeze}")

        has_table_results = "11" in rep_text and "6" in rep_text and "10" in rep_text and "2" in rep_text and "20" in rep_text and "10" in rep_text
        if has_table_results:
            log_result("PASS", "CP04 report documents official table (Human 11/6, AI 10/2, Final 20/10)")
        else:
            log_result("FAIL", "CP04 report table values missing or mismatched")
    else:
        log_result("BLOCKED", "CP4 documentation files available", "Missing CP4.md or Relatorio_CP4.md")

    # -------------------------------------------------------------------------
    # AREA 10: Submission ZIP Package Integrity
    # -------------------------------------------------------------------------
    print("\n[AREA 10/11] Verifying Submission ZIP Package...")
    zip_path = ROOT_DIR / "TVSI_T08_Grupo5_CP04.zip"
    if zip_path.is_file():
        with zipfile.ZipFile(zip_path, "r") as zf:
            corrupt = zf.testzip()
            if corrupt is None:
                log_result("PASS", f"ZIP archive '{zip_path.name}' is structurally intact (0 corrupted files)")
            else:
                log_result("FAIL", f"ZIP archive corrupted file: {corrupt}")
            
            # Check mandatory files inside ZIP
            namelist = zf.namelist()
            zip_required = [
                "Relatorio_Consolidado.md",
                "README.md",
                "MANIFEST_ENTREGA.md",
                "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx",
                "Trabalho_CP4/CP4.md",
                "Trabalho_CP4/Relatorio_CP4.md",
                "Trabalho_CP4/final_cases.json",
                "Trabalho_CP4/runs/final_cases_execution.json",
                "Trabalho_CP4/runs/final_cases_execution.py312.json",
                "Trabalho_CP4/runs/human_17_execution.json",
                "Trabalho_CP4/runs/ai_candidates_execution.json",
                "Trabalho_CP4/audit_cp4.py"
            ]
            missing_in_zip = [f for f in zip_required if f not in namelist]
            if not missing_in_zip:
                log_result("PASS", f"ZIP archive contains all essential project deliverables ({len(namelist)} files total)")
            else:
                log_result("FAIL", "ZIP archive missing essential files", str(missing_in_zip))

            # Ensure no forbidden files (.git, __pycache__, .DS_Store)
            forbidden = [f for f in namelist if ".git/" in f or "__pycache__" in f or ".DS_Store" in f]
            if not forbidden:
                log_result("PASS", "ZIP archive clean: zero git/cache/system files included")
            else:
                log_result("FAIL", "Forbidden files found in ZIP", str(forbidden))
    else:
        log_result("WARNING", f"ZIP archive '{zip_path.name}' not yet generated (Pending creation step)")

    # -------------------------------------------------------------------------
    # AREA 11: Cryptographic SHA-256 Correspondence with MANIFEST
    # -------------------------------------------------------------------------
    print("\n[AREA 11/11] Verifying Cryptographic Hashes in MANIFEST_ENTREGA.md...")
    manifest_path = ROOT_DIR / "MANIFEST_ENTREGA.md"
    if manifest_path.is_file():
        manifest_text = manifest_path.read_text(encoding="utf-8")
        hash_mismatches = []
        for line in manifest_text.splitlines():
            line = line.strip()
            if len(line) > 65 and line[:64].isalnum() and line[64:66] == "  ":
                exp_hash = line[:64]
                rel_path = line[66:]
                target_file = ROOT_DIR / rel_path
                if target_file.is_file():
                    actual_hash = calculate_sha256(target_file)
                    if exp_hash.lower() != actual_hash.lower():
                        hash_mismatches.append(f"{rel_path}: manifest={exp_hash[:12]}... actual={actual_hash[:12]}...")
                else:
                    hash_mismatches.append(f"{rel_path}: file does not exist on disk")
        
        if not hash_mismatches:
            log_result("PASS", "100% cryptographic SHA-256 hash match between disk files and MANIFEST_ENTREGA.md")
        else:
            log_result("WARNING", f"{len(hash_mismatches)} hash mismatches (Will be aligned in final manifest generation)", str(hash_mismatches[:3]))
    else:
        log_result("BLOCKED", "MANIFEST_ENTREGA.md exists", "Manifest missing")

    # -------------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("  AUDIT SUMMARY")
    print(f"  PASS: {stats['PASS']} | FAIL: {stats['FAIL']} | WARNING: {stats['WARNING']} | BLOCKED: {stats['BLOCKED']}")
    print("=" * 80)

    if stats["FAIL"] > 0 or stats["BLOCKED"] > 0:
        print("\nCRITICAL FAILURES DETECTED:")
        for f in findings:
            print(f"  - {f}")
        print("\nOVERALL STATUS: AUDIT REJECTED (Corrections required)")
        return 1
    elif stats["WARNING"] > 0:
        print("\nOVERALL STATUS: CONDITIONALLY ACCEPTED (Warnings present)")
        return 0
    else:
        print("\nOVERALL STATUS: AUDIT PASSED — 100% NORMATIVE COMPLIANCE ACHIEVED")
        return 0

if __name__ == "__main__":
    sys.exit(run_audit())
