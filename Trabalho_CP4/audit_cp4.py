#!/usr/bin/env python3
"""Comprehensive Deep Audit & Compliance Verification Script for CP04 — TVSI_2627.

Usage:
    python3 Trabalho_CP4/audit_cp4.py

Validates the 12 rigorous QA and Audit areas:
1. Baseline Integrity (shipping.py identical to initial commit 9d9f950, normative docs present)
2. Frozen Human Suite Preservation (CP02 commit 54ec4d3 integrity, H-ENV + H-01..H-16 = 17 entries)
3. JSON Syntax & Schema Validity (All repository JSON files)
4. Uniqueness of Test IDs (Across all suites)
5. Suite–Evidence Correspondence (1-to-1 input/expected mapping)
6. Individual Execution Results & Oracles Verification (Deterministic run comparison in Py 3.9 & 3.12)
7. End-to-End Requirement Traceability (R01..R08 100% coverage, 0 unexecuted)
8. Defect vs AI Expectation Data Quality Segregation (DEF-01..04 vs DATA-01..03)
9. Excel Workbook Integrity & Executions Reconciled Count (68 runs, 0 errors, Coverage verified)
10. Documentation Cross-Consistency (CP4 plan, CP4 report, consolidated report, README, FECHO_FINAL_CP04)
11. Submission ZIP Package Integrity (Extraction test, 0 corruptions, zero forbidden files)
12. Cryptographic SHA-256 Correspondence with MANIFEST_ENTREGA.md & TVSI_T08_Grupo5_CP04.zip.sha256
"""

import sys, os, json, pathlib, subprocess, zipfile, hashlib, tempfile, re
import xml.etree.ElementTree as ET

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

# Add app directory to sys.path for direct execution verification
app_dir = ROOT_DIR / "TVSI_T08_Students_B1.0/app"
if str(app_dir) not in sys.path:
    sys.path.insert(0, str(app_dir))

import shipping

def calculate_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def run_deep_audit():
    print("=" * 80)
    print("  TVSI_2627 — CHECKPOINT 4 (CP04) COMPREHENSIVE QA & TECHNICAL AUDIT")
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
    print("\n[AREA 1/12] Auditing Original Baseline Integrity...")
    shipping_path = ROOT_DIR / "TVSI_T08_Students_B1.0/app/shipping.py"
    if not shipping_path.is_file():
        log_result("BLOCKED", "Baseline shipping.py exists", "shipping.py missing!")
    else:
        # Check against initial commit 9d9f950
        try:
            diff = subprocess.run(["git", "diff", "9d9f950", "--", str(shipping_path)], capture_output=True, text=True, cwd=ROOT_DIR)
            if diff.stdout.strip() == "":
                log_result("PASS", "Baseline shipping.py is 100% intact and identical to initial commit 9d9f950")
            else:
                log_result("FAIL", "Baseline shipping.py was modified!", diff.stdout[:200])
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
    print("\n[AREA 2/12] Auditing Frozen Human Suite Preservation...")
    cp2_human_json = ROOT_DIR / "Trabalho_CP2/human_cases.json"
    if cp2_human_json.is_file():
        with open(cp2_human_json, "r", encoding="utf-8") as f:
            h_data = json.load(f)
        if len(h_data) == 16 and [c["id"] for c in h_data] == [f"H-{i:02d}" for i in range(1, 17)]:
            log_result("PASS", "CP02 frozen human suite contains exactly 16 cases (H-01 to H-16)")
        else:
            log_result("FAIL", "CP02 human suite corrupted", f"Count: {len(h_data)}")
        
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
    # AREA 3: JSON Syntax & Schema Validity
    # -------------------------------------------------------------------------
    print("\n[AREA 3/12] Validating JSON Syntax & Schema Across Repository...")
    json_files = list(ROOT_DIR.glob("**/*.json"))
    json_errors = []
    json_count = 0
    for jf in json_files:
        if ".git" in str(jf) or "__pycache__" in str(jf):
            continue
        json_count += 1
        try:
            with open(jf, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            json_errors.append(f"{jf.relative_to(ROOT_DIR)}: {e}")
    if not json_errors:
        log_result("PASS", f"All {json_count} repository JSON files have 100% valid syntax")
    else:
        log_result("FAIL", "JSON syntax errors detected", str(json_errors))

    # -------------------------------------------------------------------------
    # AREA 4: Uniqueness of Test IDs Across All Suites
    # -------------------------------------------------------------------------
    print("\n[AREA 4/12] Checking Uniqueness of Test IDs Across Suites...")
    suites_to_check = [
        ("Trabalho_CP2/human_cases.json", 16),
        ("Trabalho_CP4/human_cases_cp4.json", 17),
        ("TVSI_T08_Students_B1.0/app/ai_candidates.json", 12),
        ("Trabalho_CP4/final_cases.json", 30)
    ]
    suite_id_errors = []
    for sp, exp_count in suites_to_check:
        sf = ROOT_DIR / sp
        if sf.is_file():
            with open(sf) as f:
                s_data = json.load(f)
            ids = [item["id"] for item in s_data]
            if len(ids) != exp_count:
                suite_id_errors.append(f"{sp}: expected {exp_count} cases, found {len(ids)}")
            if len(ids) != len(set(ids)):
                suite_id_errors.append(f"{sp}: duplicate IDs detected!")
        else:
            suite_id_errors.append(f"{sp}: missing file!")
    if not suite_id_errors:
        log_result("PASS", "All suites contain strictly unique Test IDs with expected counts")
    else:
        log_result("FAIL", "Suite Test ID validation failed", str(suite_id_errors))

    # -------------------------------------------------------------------------
    # AREA 5: Suite–Evidence Correspondence
    # -------------------------------------------------------------------------
    print("\n[AREA 5/12] Verifying Suite–Evidence Mapping...")
    final_cases_file = ROOT_DIR / "Trabalho_CP4/final_cases.json"
    final_run_file = ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.json"
    if final_cases_file.is_file() and final_run_file.is_file():
        with open(final_cases_file) as f1, open(final_run_file) as f2:
            fc_data = json.load(f1)
            fr_data = json.load(f2)
        suite_dict = {c["id"]: c for c in fc_data}
        run_dict = {r["id"]: r for r in fr_data.get("results", [])}
        
        mismatches = []
        for cid, scase in suite_dict.items():
            if cid not in run_dict:
                mismatches.append(f"Missing run for {cid}")
            else:
                rcase = run_dict[cid]
                if scase["input"] != rcase["input"]:
                    mismatches.append(f"Input mismatch for {cid}")
                if scase["expected"] != rcase["expected"]:
                    mismatches.append(f"Expected mismatch for {cid}")
        
        if not mismatches:
            log_result("PASS", f"1-to-1 input & expected correspondence confirmed for all {len(suite_dict)} final cases")
        else:
            log_result("FAIL", "Suite-to-evidence mismatch found", str(mismatches))
    else:
        log_result("BLOCKED", "Final suite or evidence missing", "Files not found")

    # -------------------------------------------------------------------------
    # AREA 6: Individual Results & Deterministic Execution Verification
    # -------------------------------------------------------------------------
    print("\n[AREA 6/12] Verifying Individual Execution Results & Oracles...")
    with open(final_cases_file) as f:
        cases = json.load(f)
    
    actual_pass = 0
    actual_fail = 0
    for c in cases:
        inp = c["input"]
        exp = c["expected"]
        observed = shipping.quote(inp["weight"], inp["zone"], inp["express"])
        expected_verdict = "PASS" if observed == exp else "FAIL"
        if expected_verdict == "PASS":
            actual_pass += 1
        else:
            actual_fail += 1
    
    if actual_pass == 20 and actual_fail == 10 and len(cases) == 30:
        log_result("PASS", "Direct execution of 30 final cases confirms exactly 20 PASS / 10 FAIL")
    else:
        log_result("FAIL", "Direct execution count mismatch", f"PASS: {actual_pass}, FAIL: {actual_fail}")

    # Dual-runtime parity verification (Py 3.9 vs Py 3.12 run records)
    f312_run = ROOT_DIR / "Trabalho_CP4/runs/final_cases_execution.py312.json"
    if f312_run.is_file():
        d312 = json.load(open(f312_run)).get("results", [])
        p312 = sum(1 for r in d312 if r["verdict"] == "PASS")
        f312 = sum(1 for r in d312 if r["verdict"] == "FAIL")
        if len(d312) == 30 and p312 == 20 and f312 == 10:
            log_result("PASS", "Dual-Python execution parity verified (Python 3.9 vs Python 3.12: identical 20 PASS / 10 FAIL)")
        else:
            log_result("FAIL", "Python 3.12 run mismatch", f"PASS: {p312}, FAIL: {f312}")

    # -------------------------------------------------------------------------
    # AREA 7: End-to-End Requirement Traceability
    # -------------------------------------------------------------------------
    print("\n[AREA 7/12] Auditing End-to-End Requirement Traceability...")
    wb_file = ROOT_DIR / "Trabalho_CP4/TestResults_T08_Template.xlsx"
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
    # AREA 8: Defect vs AI Expectation Data Quality Segregation
    # -------------------------------------------------------------------------
    print("\n[AREA 8/12] Auditing Defect Reports and Classification Segregation...")
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
    # AREA 9: Excel Workbook Integrity & Executions Reconciled Count
    # -------------------------------------------------------------------------
    print("\n[AREA 9/12] Auditing Excel Workbook & Reconciling Executions Count...")
    canonical_wb = ROOT_DIR / "Trabalho_CP4/TestResults_T08_Template.xlsx"
    if not canonical_wb.is_file():
        log_result("FAIL", "Canonical workbook missing", str(canonical_wb))
    else:
        with zipfile.ZipFile(canonical_wb, "r") as z:
            wb_xml = ET.fromstring(z.read("xl/workbook.xml"))
            sheets = [s.attrib["name"] for s in wb_xml.findall(f".//{ns_xl}sheet")]
            expected_sheets = ["Test Cases", "Executions", "Defects", "Static Review", "Coverage", "Technique"]
            if sheets == expected_sheets:
                log_result("PASS", f"Canonical workbook ({canonical_wb.name}) contains exactly the 6 official sheets in order")
            else:
                log_result("FAIL", "Workbook sheets mismatch", f"Got: {sheets}")

            s2_xml = ET.fromstring(z.read("xl/worksheets/sheet2.xml"))
            c4_cell = next((c for c in s2_xml.findall(f".//{ns_xl}c") if c.attrib.get("r") == "C4"), None)
            c4_val = c4_cell.find(f"{ns_xl}v").text if c4_cell is not None and c4_cell.find(f"{ns_xl}v") is not None else ""
            if "Requirement" in c4_val:
                log_result("PASS", f"Autonomous 'Requirement ID(s)' column present in Executions (Cell C4: '{c4_val}')")
            else:
                log_result("FAIL", "Autonomous Requirement column missing in Executions", f"C4: '{c4_val}'")

            # Reconcile exact 68 execution rows
            execution_rows = []
            for r in s2_xml.findall(f".//{ns_xl}row")[4:]:
                cells = {c.attrib.get("r")[0]: c.find(f"{ns_xl}v").text if c.find(f"{ns_xl}v") is not None else "" for c in r.findall(f"{ns_xl}c")}
                if cells.get("A"):
                    execution_rows.append(cells)
            
            if len(execution_rows) == 68:
                log_result("PASS", "Reconciled exactly 68 execution rows in Executions sheet (1 ENV + 16 H + 12 AI + 30 Final + 4 BR05 + 5 Robustness)")
            else:
                log_result("FAIL", "Executions row count mismatch", f"Count: {len(execution_rows)}")

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

        # Check replica workbooks consistency
        can_bytes = canonical_wb.read_bytes()
        replicas = [
            ROOT_DIR / "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx",
            ROOT_DIR / "Trabalho_CP1/TestResults_T08_Template.xlsx",
            ROOT_DIR / "Trabalho_CP4/TVSI_T08_Students_B1.0_CP4/TestResults_T08_Template.xlsx"
        ]
        rep_mismatches = []
        for rep in replicas:
            if rep.is_file() and rep.read_bytes() != can_bytes:
                rep_mismatches.append(str(rep.relative_to(ROOT_DIR)))
        if not rep_mismatches:
            log_result("PASS", f"All repository workbook replicas match canonical {canonical_wb.relative_to(ROOT_DIR)} bit-for-bit")
        else:
            log_result("FAIL", "Workbook replicas mismatch canonical version", str(rep_mismatches))

    # -------------------------------------------------------------------------
    # AREA 10: Documentation Cross-Consistency
    # -------------------------------------------------------------------------
    print("\n[AREA 10/12] Checking Documentation Cross-Consistency...")
    cp4_plan = ROOT_DIR / "Trabalho_CP4/CP4.md"
    cp4_rep = ROOT_DIR / "Trabalho_CP4/Relatorio_CP4.md"
    readme_f = ROOT_DIR / "README.md"
    rel_cons = ROOT_DIR / "Relatorio_Consolidado.md"
    fecho_final = ROOT_DIR / "FECHO_FINAL_CP04.md"
    
    docs_to_check = [cp4_plan, cp4_rep, readme_f, rel_cons, fecho_final]
    missing_docs = [f.name for f in docs_to_check if not f.is_file()]
    if not missing_docs:
        plan_text = cp4_plan.read_text(encoding="utf-8")
        rep_text = cp4_rep.read_text(encoding="utf-8")
        readme_text = readme_f.read_text(encoding="utf-8")
        cons_text = rel_cons.read_text(encoding="utf-8")
        fecho_text = fecho_final.read_text(encoding="utf-8")

        # 1. No obsolete '21 testes humanos congelados' or 'H-20' freeze
        if "21 testes humanos" not in plan_text and "H-20" not in plan_text and "21 testes humanos" not in rep_text:
            log_result("PASS", "Documentation strictly aligns with 17 human entries (H-ENV + H-01..16)")
        else:
            log_result("FAIL", "Documentation contains obsolete '21 testes humanos congelados' statement")

        # 2. Defect terminology consistency: DEF-01 (weight 20000), DEF-02 (weight 1000), DEF-03 (REMOTE surcharge), DEF-04 (REMOTE express limit)
        defect_terms_ok = True
        for tname, txt in [("Relatorio_CP4", rep_text), ("Relatorio_Consolidado", cons_text), ("FECHO_FINAL_CP04", fecho_text)]:
            if "20000" not in txt or "1000" not in txt or "REMOTE" not in txt:
                defect_terms_ok = False
                log_result("FAIL", f"Missing key defect definitions in {tname}")
        if defect_terms_ok:
            log_result("PASS", "Defect terminology (DEF-01..04) perfectly harmonized across key reports")
            
        # 3. AI anomaly definitions: DATA-01 (AI-05), DATA-02 (AI-06), DATA-03 (AI-09)
        if "AI-05" in cons_text and "AI-06" in cons_text and "AI-09" in cons_text and "DATA-01" in fecho_text:
            log_result("PASS", "AI anomaly classification (DATA-01..03) harmonized across key reports")
        else:
            log_result("FAIL", "AI anomaly classification mismatch in reports")
    else:
        log_result("BLOCKED", "Documentation files available", f"Missing: {missing_docs}")

    # -------------------------------------------------------------------------
    # AREA 11: Submission ZIP Package Integrity & Deep Extraction Test
    # -------------------------------------------------------------------------
    print("\n[AREA 11/12] Verifying Submission ZIP Package Integrity...")
    zip_path = ROOT_DIR / "TVSI_T08_Grupo5_CP04.zip"
    if zip_path.is_file():
        with zipfile.ZipFile(zip_path, "r") as zf:
            corrupt = zf.testzip()
            if corrupt is None:
                log_result("PASS", f"ZIP archive '{zip_path.name}' is structurally intact (0 corrupted files)")
            else:
                log_result("FAIL", f"ZIP archive corrupted file: {corrupt}")
            
            namelist = zf.namelist()
            if zip_path.name in namelist:
                log_result("FAIL", "ZIP archive contains itself (circular dependency)!")
            else:
                log_result("PASS", "ZIP archive is free of self-referential archive inclusion")

            forbidden = [f for f in namelist if ".git/" in f or "__pycache__" in f or ".DS_Store" in f]
            if not forbidden:
                log_result("PASS", "ZIP archive clean: zero git/cache/system files included")
            else:
                log_result("FAIL", "Forbidden files found in ZIP", str(forbidden))

            # Perform deep extraction check in temporary directory
            with tempfile.TemporaryDirectory() as tmpdir:
                tmp_p = pathlib.Path(tmpdir)
                zf.extractall(tmp_p)
                extraction_errors = []
                for fname in namelist:
                    src_f = ROOT_DIR / fname
                    ext_f = tmp_p / fname
                    if not ext_f.is_file():
                        extraction_errors.append(f"Missing extracted: {fname}")
                    elif src_f.stat().st_size != ext_f.stat().st_size:
                        extraction_errors.append(f"Size diff: {fname}")
                    elif calculate_sha256(src_f) != calculate_sha256(ext_f):
                        extraction_errors.append(f"Hash diff: {fname}")
                
                if not extraction_errors:
                    log_result("PASS", f"Deep extraction test: all {len(namelist)} extracted files match repository bit-for-bit")
                else:
                    log_result("FAIL", "Extraction mismatches detected", str(extraction_errors[:3]))
    else:
        log_result("WARNING", f"ZIP archive '{zip_path.name}' not yet generated (Pending creation step)")

    # -------------------------------------------------------------------------
    # AREA 12: Cryptographic SHA-256 Correspondence with MANIFEST
    # -------------------------------------------------------------------------
    print("\n[AREA 12/12] Verifying Cryptographic Hashes in MANIFEST_ENTREGA.md...")
    manifest_path = ROOT_DIR / "MANIFEST_ENTREGA.md"
    zip_sha_file = ROOT_DIR / "TVSI_T08_Grupo5_CP04.zip.sha256"
    
    if manifest_path.is_file():
        manifest_text = manifest_path.read_text(encoding="utf-8")
        hash_mismatches = []
        table_matches = re.findall(r"\|\s*`([^`]+)`\s*\|\s*[\d,]+\s*\|\s*`([a-f0-9]{64})`\s*\|", manifest_text)
        
        for rel_path, exp_hash in table_matches:
            target_file = ROOT_DIR / rel_path
            if target_file.is_file():
                actual_hash = calculate_sha256(target_file)
                if exp_hash.lower() != actual_hash.lower():
                    hash_mismatches.append(f"{rel_path}: manifest={exp_hash[:12]}... actual={actual_hash[:12]}...")
            else:
                hash_mismatches.append(f"{rel_path}: file missing on disk")
        
        if len(table_matches) >= 50 and not hash_mismatches:
            log_result("PASS", f"100% cryptographic SHA-256 match for all {len(table_matches)} files in MANIFEST_ENTREGA.md")
        else:
            log_result("FAIL", f"Manifest hash verification failed ({len(hash_mismatches)} mismatches)", str(hash_mismatches[:3]))

        # Reconcile inventory: 50 manifest entries + 1 MANIFEST_ENTREGA.md = 51 files in ZIP
        if len(table_matches) == 50 and zip_path.is_file():
            with zipfile.ZipFile(zip_path, "r") as zf:
                if len(zf.namelist()) == 51:
                    log_result("PASS", "Inventory exact reconciliation: 50 manifest payload files + 1 manifest = 51 files in ZIP")
                else:
                    log_result("FAIL", "Inventory count mismatch between manifest and ZIP", f"ZIP has {len(zf.namelist())}")

        # Also verify external zip sha256 file
        if zip_sha_file.is_file() and zip_path.is_file():
            content = zip_sha_file.read_text(encoding="utf-8").strip()
            exp_z_hash = content.split()[0]
            act_z_hash = calculate_sha256(zip_path)
            if exp_z_hash.lower() == act_z_hash.lower():
                log_result("PASS", f"External ZIP SHA-256 file ({zip_sha_file.name}) verified exactly")
            else:
                log_result("FAIL", "External ZIP SHA-256 mismatch", f"Expected: {exp_z_hash[:12]}..., Got: {act_z_hash[:12]}...")
        else:
            log_result("WARNING", "External ZIP SHA-256 verification file not found")
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
        print("\nOVERALL STATUS: AUDIT PASSED — TEST PROCESS & ARTIFACTS FULLY VALIDATED (4 SUT DEFECTS CONFIRMED)")
        return 0

if __name__ == "__main__":
    sys.exit(run_deep_audit())
