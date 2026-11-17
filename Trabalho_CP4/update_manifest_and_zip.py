#!/usr/bin/env python3
"""Script to package TVSI_T08_Grupo5_CP04.zip, validate extracted contents,
and generate clean SHA-256 manifests without circular dependencies."""

import os
import zipfile
import hashlib
import pathlib
import tempfile
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
zip_path = ROOT / "TVSI_T08_Grupo5_CP04.zip"
zip_sha_path = ROOT / "TVSI_T08_Grupo5_CP04.zip.sha256"

# Exactly the 51 files that constitute the CP04 submission package
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

def generate_manifest_and_zip():
    print(f"=== Starting Package & Manifest Generation ({len(files)} files) ===")
    
    # 1. Check that all files exist on disk
    for f in files:
        if not (ROOT / f).is_file():
            raise FileNotFoundError(f"Required deliverable missing on disk: {f}")
    
    # 2. Compute SHA-256 and byte sizes of all 50 files (excluding MANIFEST_ENTREGA.md itself)
    manifest_entries = {}
    for f in files:
        if f != "MANIFEST_ENTREGA.md":
            p = ROOT / f
            manifest_entries[f] = {
                "size": p.stat().st_size,
                "sha256": sha256_file(p)
            }
    
    # 3. Write clean, non-circular MANIFEST_ENTREGA.md
    manifest_header = f"""# MANIFESTO DE ENTREGA — CP04
## Projeto TVSI 2026/27 — T08 — Grupo 5

**Data de Emissão:** 17 de Novembro de 2026  
**Build sob Teste:** T08-B1.0  
**Grupo:** Grupo 5 (Eduardo Dias, Rui Carneiro, Érica Moreira, Beatriz Barbosa)  
**Arquivo Consolidado de Submissão:** `TVSI_T08_Grupo5_CP04.zip`  
**Total de Ficheiros Integrados no Pacote:** {len(files)}

---

## 1. REGISTO CRIPTOGRÁFICO DE INTEGRIDADE DOS FICHEIROS (SHA-256)

A tabela seguinte regista a dimensão em bytes e o hash criptográfico SHA-256 de cada ficheiro constituinte do projeto de entrega.

| Ficheiro | Dimensão (Bytes) | SHA-256 |
|---|:---:|---|
"""
    table_rows = []
    for f in sorted(manifest_entries.keys()):
        sz = manifest_entries[f]["size"]
        hsh = manifest_entries[f]["sha256"]
        table_rows.append(f"| `{f}` | {sz:,} | `{hsh}` |")
    
    manifest_footer = """

---

## 2. ARQUIVO DE SUBMISSÃO CONSOLIDADO (ZIP)

O pacote de submissão para o Moodle (`TVSI_T08_Grupo5_CP04.zip`) agrega exatamente os ficheiros acima listados.
Para evitar dependências circulares de cálculo e autorreferência no manifesto contido dentro do próprio arquivo, o hash de integridade SHA-256 do arquivo ZIP final é mantido no ficheiro externo de verificação:
- `TVSI_T08_Grupo5_CP04.zip.sha256`

Este manifesto atesta com exatidão matemática a proveniência e a conformidade integral de todos os artefactos entregues.
"""
    manifest_text = manifest_header + "\n".join(table_rows) + manifest_footer
    (ROOT / "MANIFEST_ENTREGA.md").write_text(manifest_text, encoding="utf-8")
    
    # 4. Create ZIP package
    if zip_path.exists():
        zip_path.unlink()
        
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(files):
            zf.write(ROOT / f, arcname=f)
            
    # 5. Validate ZIP structure
    with zipfile.ZipFile(zip_path, "r") as zf:
        corrupt = zf.testzip()
        if corrupt is not None:
            raise RuntimeError(f"Corrupted file detected inside generated ZIP: {corrupt}")
        
        namelist = zf.namelist()
        if len(namelist) != len(files):
            raise ValueError(f"ZIP file count mismatch: expected {len(files)}, got {len(namelist)}")
            
        # Ensure no forbidden files
        forbidden = [f for f in namelist if ".git/" in f or "__pycache__" in f or ".DS_Store" in f]
        if forbidden:
            raise RuntimeError(f"Forbidden files present in ZIP: {forbidden}")
            
    # 6. Deep extraction test to verify bit-by-bit integrity
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = pathlib.Path(tmpdir)
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(tmp_path)
            
        for f in files:
            orig = ROOT / f
            extr = tmp_path / f
            if not extr.is_file():
                raise FileNotFoundError(f"Extracted file missing: {f}")
            if orig.stat().st_size != extr.stat().st_size:
                raise ValueError(f"Size mismatch on extraction: {f}")
            if sha256_file(orig) != sha256_file(extr):
                raise ValueError(f"SHA-256 hash mismatch on extraction: {f}")
                
    print("  [SUCCESS] ZIP extraction test: 100% bit-by-bit identical to source files!")
    
    # 7. Compute final ZIP properties and write external verification file
    z_size = zip_path.stat().st_size
    z_hash = sha256_file(zip_path)
    
    # Standard format: "<hash>  <filename>"
    zip_sha_path.write_text(f"{z_hash}  {zip_path.name}\n", encoding="utf-8")
    
    # 8. Update Relatorio_Consolidado.md if needed
    rel_cons = ROOT / "Relatorio_Consolidado.md"
    if rel_cons.is_file():
        r_text = rel_cons.read_text(encoding="utf-8")
        # Replace SHA-256 of zip in table
        new_r_text = re.sub(
            r"\| `TVSI_T08_Grupo5_CP04\.zip` \| [^|]+ \| `[a-f0-9]+` \|",
            f"| `TVSI_T08_Grupo5_CP04.zip` | {z_size:,} | `{z_hash}` |",
            r_text
        )
        if new_r_text != r_text:
            rel_cons.write_text(new_r_text, encoding="utf-8")
            
    print(f"Package created: {zip_path.name}")
    print(f"Total files: {len(files)}")
    print(f"ZIP Size: {z_size:,} bytes")
    print(f"ZIP SHA-256: {z_hash}")
    print(f"External SHA-256 verification file written: {zip_sha_path.name}")

if __name__ == "__main__":
    generate_manifest_and_zip()
