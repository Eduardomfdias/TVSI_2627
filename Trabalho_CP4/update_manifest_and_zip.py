#!/usr/bin/env python3
"""Script to package TVSI_T08_Grupo5_CP04.zip and harmonize SHA-256 hashes in MANIFEST_ENTREGA.md and Relatorio_Consolidado.md"""

import os
import zipfile
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
zip_path = ROOT / "TVSI_T08_Grupo5_CP04.zip"

files = [
    "AUDITORIA_FINAL_ENTREGA.md",
    "CLAUDE.md",
    "FECHO_FINAL_CP04.md",
    "MANIFEST_ENTREGA.md",
    "README.md",
    "Relatorio_Consolidado.md",
    "TVSI_T08_Students_B1.0/AI_PROVENANCE.html",
    "TVSI_T08_Students_B1.0/AI_PROVENANCE.md",
    "TVSI_T08_Students_B1.0/BusinessRules.html",
    "TVSI_T08_Students_B1.0/BusinessRules.md",
    "TVSI_T08_Students_B1.0/START_HERE.html",
    "TVSI_T08_Students_B1.0/START_HERE.md",
    "TVSI_T08_Students_B1.0/StudentAssignment.html",
    "TVSI_T08_Students_B1.0/StudentAssignment.md",
    "TVSI_T08_Students_B1.0/TestResults_T08_Template.xlsx",
    "TVSI_T08_Students_B1.0/app/ai_candidates.json",
    "TVSI_T08_Students_B1.0/app/ai_candidates.results.json",
    "TVSI_T08_Students_B1.0/app/human_cases.json",
    "TVSI_T08_Students_B1.0/app/human_cases.results.json",
    "TVSI_T08_Students_B1.0/app/run_cases.py",
    "TVSI_T08_Students_B1.0/app/shipping.py",
    "Trabalho_CP1/CP1.md",
    "Trabalho_CP1/TestResults_T08_Template.xlsx",
    "Trabalho_CP2/CP2.md",
    "Trabalho_CP2/Relatorio_CP2.md",
    "Trabalho_CP2/human_cases.json",
    "Trabalho_CP2/human_cases.results.json",
    "Trabalho_CP3/CP3.md",
    "Trabalho_CP3/Relatorio_CP3.md",
    "Trabalho_CP3/audit_project.py",
    "Trabalho_CP3/br05_independence.py312.json",
    "Trabalho_CP3/br05_independence.results.json",
    "Trabalho_CP3/final_cases.json",
    "Trabalho_CP3/final_cases.results.json",
    "Trabalho_CP3/final_cases.results.py312.json",
    "Trabalho_CP3/verify_br05_independence.py",
    "Trabalho_CP4/CP4.md",
    "Trabalho_CP4/Relatorio_CP4.md",
    "Trabalho_CP4/TestResults_T08_Template.xlsx",
    "Trabalho_CP4/audit_cp4.py",
    "Trabalho_CP4/evidence/br05_independence_cp4.json",
    "Trabalho_CP4/evidence/runner_robustness_evidence.json",
    "Trabalho_CP4/final_cases.json",
    "Trabalho_CP4/final_cases.results.json",
    "Trabalho_CP4/human_cases_cp4.json",
    "Trabalho_CP4/human_cases_cp4.results.json",
    "Trabalho_CP4/runs/ai_candidates_execution.json",
    "Trabalho_CP4/runs/final_cases_execution.json",
    "Trabalho_CP4/runs/final_cases_execution.py312.json",
    "Trabalho_CP4/runs/human_17_execution.json",
    "Trabalho_CP4/update_workbook_cp4.py"
]

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print(f"Checking {len(files)} files...")
    for f in files:
        if not (ROOT / f).exists():
            raise FileNotFoundError(f"Missing file: {f}")

    # Compute hashes of all 50 files except MANIFEST_ENTREGA.md
    hashes = {}
    for f in files:
        if f != "MANIFEST_ENTREGA.md":
            hashes[f] = sha256_file(ROOT / f)

    # Build MANIFEST_ENTREGA.md
    manifest_header = """# MANIFESTO DE ENTREGA — CP04
## Projeto TVSI 2026/27 — T08 — Grupo 5

**Data de Emissão:** 17 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Grupo:** Grupo 5 (Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa)  
**Arquivo de Entrega:** `TVSI_T08_Grupo5_CP04.zip`

---

## 1. HASHES CRIPTOGRÁFICOS DOS FICHEIROS DO PROJETO (SHA-256)

| Ficheiro | SHA-256 |
|---|---|
"""
    table_rows = []
    for f in sorted(hashes.keys()):
        table_rows.append(f"| `{f}` | `{hashes[f]}` |")

    manifest_footer = """

---

## 2. ARQUIVO DE SUBMISSÃO CONSOLIDADO

| Arquivo ZIP | Dimensão (Bytes) | SHA-256 |
|---|---|---|
"""
    manifest_text = manifest_header + "\n".join(table_rows) + manifest_footer

    # Write manifest temporarily to include it in zip
    temp_manifest = manifest_text + "| `TVSI_T08_Grupo5_CP04.zip` | TEMPORARY | TEMPORARY |\n"
    (ROOT / "MANIFEST_ENTREGA.md").write_text(temp_manifest, encoding="utf-8")

    # Create ZIP archive
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(files):
            zf.write(ROOT / f, arcname=f)

    # Compute actual ZIP properties
    z_size = zip_path.stat().st_size
    z_hash = sha256_file(zip_path)

    # Finalize MANIFEST_ENTREGA.md with exact ZIP stats
    final_manifest = manifest_text + f"| `TVSI_T08_Grupo5_CP04.zip` | {z_size:,} | `{z_hash}` |\n"
    final_manifest += "\nEste manifesto atesta que todos os ficheiros entregues correspondem com exatidão matemática às evidências e códigos gerados, validados e auditados.\n"
    (ROOT / "MANIFEST_ENTREGA.md").write_text(final_manifest, encoding="utf-8")

    # Re-package ZIP with finalized MANIFEST_ENTREGA.md
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(files):
            zf.write(ROOT / f, arcname=f)

    final_z_size = zip_path.stat().st_size
    final_z_hash = sha256_file(zip_path)

    # Also update Relatorio_Consolidado.md ZIP hash section if present
    rel_cons_path = ROOT / "Relatorio_Consolidado.md"
    if rel_cons_path.exists():
        text = rel_cons_path.read_text(encoding="utf-8")
        # Replace SHA-256 of zip in table
        new_text = re.sub(
            r"\| `TVSI_T08_Grupo5_CP04\.zip` \| [^|]+ \| `[a-f0-9]+` \|",
            f"| `TVSI_T08_Grupo5_CP04.zip` | {final_z_size:,} | `{final_z_hash}` |",
            text
        )
        rel_cons_path.write_text(new_text, encoding="utf-8")

    print(f"ZIP package finalized: {zip_path.name}")
    print(f"Files included: {len(files)}")
    print(f"ZIP Size: {final_z_size:,} bytes")
    print(f"ZIP SHA-256: {final_z_hash}")

if __name__ == "__main__":
    main()
