#!/usr/bin/env python3
"""Integrated Mutation Meta-Test Suite for audit_cp4.py.

Executes audit_cp4.py against isolated temporary sandboxes with controlled mutations
to demonstrate that the integrated auditor actively detects the 6 required failure classes:
1. Missing mandatory deliverable file
2. Malformed JSON syntax
3. Duplicate test ID in a suite
4. Mismatched execution result / oracle divergence
5. Incorrect cryptographic hash in manifest
6. Corrupted ZIP package

Formulação metodológica:
Os seis cenários controlados demonstram que o auditor integrado deteta as
classes de falhas especificamente testadas através de execução em ambiente temporário.
"""

import sys
import os
import json
import pathlib
import tempfile
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent

def create_isolated_sandbox():
    """Creates a temporary isolated copy of the repository for safe mutation testing."""
    tmp = tempfile.TemporaryDirectory()
    sandbox = pathlib.Path(tmp.name)
    for item in ROOT.iterdir():
        if item.name in (".git", ".DS_Store", "brain"):
            continue
        dest = sandbox / item.name
        if item.is_dir():
            shutil.copytree(item, dest, symlinks=True)
        else:
            shutil.copy2(item, dest)
    return tmp, sandbox

def run_auditor_in_sandbox(sandbox_path):
    """Executes audit_cp4.py as a subprocess inside the given isolated sandbox."""
    script_path = sandbox_path / "Trabalho_CP4/audit_cp4.py"
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=sandbox_path,
        capture_output=True,
        text=True
    )
    return proc

def test_missing_file_detection():
    print("[TEST 1/6] Testing integrated detection of missing mandatory deliverable...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        # Remove a mandatory normative file
        target = sandbox / "TVSI_T08_Students_B1.0/BusinessRules.md"
        target.unlink()
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on missing file, got {proc.returncode}"
        assert "Missing normative documents" in proc.stdout, "Auditor should explicitly flag missing normative document"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped missing file with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def test_malformed_json_detection():
    print("[TEST 2/6] Testing integrated detection of malformed JSON syntax...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        target = sandbox / "Trabalho_CP4/final_cases.json"
        target.write_text("{ malformed: json, missing quotes, }", encoding="utf-8")
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on malformed JSON, got {proc.returncode}"
        assert "JSON syntax errors detected" in proc.stdout, "Auditor should report JSON syntax error"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped malformed JSON syntax with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def test_duplicate_id_detection():
    print("[TEST 3/6] Testing integrated detection of duplicate test IDs...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        target = sandbox / "Trabalho_CP4/final_cases.json"
        data = json.loads(target.read_text(encoding="utf-8"))
        data[1]["id"] = data[0]["id"]
        target.write_text(json.dumps(data, indent=2), encoding="utf-8")
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on duplicate ID, got {proc.returncode}"
        assert "duplicate IDs detected" in proc.stdout, "Auditor should flag duplicate ID"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped duplicate test IDs with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def test_oracle_divergence_detection():
    print("[TEST 4/6] Inconsistência introduzida na expectativa de um caso da suite final, com verificação da deteção da divergência entre a suite e a evidência de execução e/ou da alteração da distribuição global de resultados...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        target = sandbox / "Trabalho_CP4/final_cases.json"
        data = json.loads(target.read_text(encoding="utf-8"))
        # Mutate expected fee of case 0 from 5 to 9999
        data[0]["expected"]["fee"] = 9999
        target.write_text(json.dumps(data, indent=2), encoding="utf-8")
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on oracle divergence, got {proc.returncode}"
        assert ("Direct execution count mismatch" in proc.stdout or "Suite-to-evidence mismatch" in proc.stdout), "Auditor should detect divergence in final cases"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped expected fee mutation divergence with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def test_manifest_hash_tamper_detection():
    print("[TEST 5/6] Testing integrated detection of hash tampering in manifest...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        manifest_p = sandbox / "MANIFEST_ENTREGA.md"
        content = manifest_p.read_text(encoding="utf-8")
        # Tamper hash of CLAUDE.md
        assert "24468175d9c2" in content, "Known SHA prefix of CLAUDE.md must exist in manifest"
        content = content.replace("24468175d9c2", "000000000000")
        manifest_p.write_text(content, encoding="utf-8")
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on tampered manifest, got {proc.returncode}"
        assert "Manifest hash verification failed" in proc.stdout, "Auditor should report manifest hash mismatch"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped manifest hash tampering with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def test_corrupted_zip_detection():
    print("[TEST 6/6] Testing integrated detection of corrupted ZIP package...")
    tmp, sandbox = create_isolated_sandbox()
    try:
        zip_p = sandbox / "TVSI_T08_Grupo5_CP04.zip"
        zip_p.write_bytes(b"PK\x03\x04corrupted_payload_data_not_valid_deflate")
        proc = run_auditor_in_sandbox(sandbox)
        assert proc.returncode != 0, f"Auditor should exit with non-zero code on corrupted ZIP, got {proc.returncode}"
        assert ("ZIP archive invalid or corrupted" in proc.stdout or "ZIP archive corrupted" in proc.stdout or "Extraction mismatches detected" in proc.stdout), "Auditor should report corrupted ZIP"
        assert "FAIL" in proc.stdout, "Auditor output should flag FAIL"
        print("  -> PASSED: Integrated auditor trapped corrupted ZIP archive with exit code", proc.returncode)
    finally:
        tmp.cleanup()

def main():
    print("=" * 70)
    print("  AUDITOR ROBUSTNESS & INTEGRATED MUTATION VERIFICATION")
    print("=" * 70)
    
    test_missing_file_detection()
    test_malformed_json_detection()
    test_duplicate_id_detection()
    test_oracle_divergence_detection()
    test_manifest_hash_tamper_detection()
    test_corrupted_zip_detection()
    
    print("=" * 70)
    print("  Os seis cenários controlados demonstram que o auditor integrado")
    print("  deteta as seis classes de falhas especificamente introduzidas")
    print("  nos ambientes temporários de teste. A cobertura não deve ser")
    print("  interpretada como demonstração exaustiva da deteção de todas as")
    print("  possíveis divergências entre a SUT e os oráculos independentes.")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
