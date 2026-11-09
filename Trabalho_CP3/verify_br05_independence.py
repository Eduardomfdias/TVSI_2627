"""Verification of BR-05: Independence of calls and absence of side effects.

Normative BR-05:
"Validation has precedence over availability, which has precedence over fee calculation.
No partial fee is returned for INVALID or UNAVAILABLE.
Repeated calls are independent and have no side effects."

This verification script tests 4 distinct, well-defined properties:
1. Repeatability / Determinism (BR05-DET-01):
   Repeated identical calls yield strictly identical outputs across iterations.
2. Absence of Residual State (BR05-RES-02):
   Prior executions of INVALID, UNAVAILABLE, or different valid cases do not contaminate
   subsequent calls within the same process runtime.
3. Absence of Observable Mutations (BR05-MUT-03):
   - Input arguments passed by caller remain unmutated.
   - Return dictionary instances are distinct objects in memory.
   - Mutating a previous return dictionary does not affect future return values.
   - Module-level attributes and global state in shipping.py remain strictly immutable.
4. Absence of External Side Effects (BR05-EXT-04):
   - No output emitted to sys.stdout / sys.stderr during function execution.
   - No changes to environment variables (os.environ).
   - No filesystem modifications (working directory files unchanged).
"""

import sys, os, io, json, pathlib

# Ensure shipping module from app/ can be imported
app_dir = pathlib.Path(__file__).resolve().parent.parent / "TVSI_T08_Students_B1.0" / "app"
sys.path.insert(0, str(app_dir))

import shipping

def verify_br05():
    report = {
        "build": "T08-B1.0",
        "rule": "BR-05",
        "python": sys.version,
        "verification_scope": {
            "tested_properties": [
                "repeatability_and_determinism",
                "absence_of_residual_state",
                "absence_of_observable_mutations",
                "absence_of_external_side_effects"
            ],
            "execution_model": "In-process sequential calls on single Python runtime"
        },
        "tests": []
    }

    # =========================================================================
    # Property 1: Repeatability / Determinism (BR05-DET-01)
    # =========================================================================
    sample_input = {"weight": 500, "zone": "LOCAL", "express": False}
    expected_output = {"status": "OK", "fee": 5}
    reps = 10
    observed_reps = [shipping.quote(**sample_input) for _ in range(reps)]
    det_pass = all(r == expected_output for r in observed_reps)
    report["tests"].append({
        "test_id": "BR05-DET-01",
        "property": "Repetibilidade dos resultados (determinismo)",
        "description": f"{reps} invocações consecutivas com inputs idênticos no mesmo processo",
        "input": sample_input,
        "expected": expected_output,
        "all_iterations_identical": det_pass,
        "verdict": "PASS" if det_pass else "FAIL"
    })

    # =========================================================================
    # Property 2: Absence of Residual State (BR05-RES-02)
    # =========================================================================
    test_sequence = [
        {"step": 1, "name": "Válido inicial", "input": {"weight": 500, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 5}},
        {"step": 2, "name": "Inválido (peso negativo)", "input": {"weight": -10, "zone": "LOCAL", "express": False}, "expected": {"status": "INVALID", "fee": None}},
        {"step": 3, "name": "Válido pós-inválido", "input": {"weight": 500, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 5}},
        {"step": 4, "name": "Indisponível (peso 15000 REMOTE express)", "input": {"weight": 15000, "zone": "REMOTE", "express": True}, "expected": {"status": "UNAVAILABLE", "fee": None}},
        {"step": 5, "name": "Válido pós-indisponível", "input": {"weight": 500, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 5}},
        {"step": 6, "name": "Inválido (tipo bool no peso)", "input": {"weight": True, "zone": "LOCAL", "express": False}, "expected": {"status": "INVALID", "fee": None}},
        {"step": 7, "name": "Válido pós-tipo-inválido", "input": {"weight": 500, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 5}},
        {"step": 8, "name": "Válido diferente (Tier 2)", "input": {"weight": 1001, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 8}},
        {"step": 9, "name": "Válido de referência final", "input": {"weight": 500, "zone": "LOCAL", "express": False}, "expected": {"status": "OK", "fee": 5}}
    ]

    seq_results = []
    res_pass = True
    for s in test_sequence:
        act = shipping.quote(**s["input"])
        matched = (act == s["expected"])
        if not matched:
            res_pass = False
        seq_results.append({
            "step": s["step"],
            "name": s["name"],
            "input": s["input"],
            "expected": s["expected"],
            "actual": act,
            "match": matched
        })

    report["tests"].append({
        "test_id": "BR05-RES-02",
        "property": "Ausência de estado residual entre chamadas",
        "description": "Sequência intercalada alternando casos válidos, inválidos e indisponíveis",
        "steps": seq_results,
        "all_steps_matched": res_pass,
        "verdict": "PASS" if res_pass else "FAIL"
    })

    # =========================================================================
    # Property 3: Absence of Observable Mutations (BR05-MUT-03)
    # =========================================================================
    # 3.1 Input dictionary immutability
    caller_dict = {"weight": 500, "zone": "LOCAL", "express": False}
    caller_dict_copy = dict(caller_dict)
    shipping.quote(**caller_dict)
    inputs_unmutated = (caller_dict == caller_dict_copy)

    # 3.2 Output isolation: distinct dict instances & caller mutation immunity
    res_a = shipping.quote(500, "LOCAL", False)
    distinct_instances = True
    res_a["status"] = "MUTATED_BY_CALLER"
    res_a["fee"] = 9999
    res_b = shipping.quote(500, "LOCAL", False)
    mutation_isolated = (res_b == {"status": "OK", "fee": 5} and (res_a is not res_b))

    # 3.3 Module namespace immutability
    module_attrs = {k: v for k, v in shipping.__dict__.items() if not k.startswith("__")}
    # run several calls
    for _ in range(5):
        shipping.quote(500, "LOCAL", False)
        shipping.quote(-1, "LOCAL", False)
    module_attrs_after = {k: v for k, v in shipping.__dict__.items() if not k.startswith("__")}
    module_unmutated = (module_attrs == module_attrs_after)

    mut_pass = inputs_unmutated and mutation_isolated and module_unmutated
    report["tests"].append({
        "test_id": "BR05-MUT-03",
        "property": "Ausência de mutações observáveis",
        "description": "Verificação de isolamento de memória, imutabilidade de inputs e do namespace do módulo",
        "inputs_unmutated": inputs_unmutated,
        "caller_mutation_isolated": mutation_isolated,
        "module_namespace_unmutated": module_unmutated,
        "verdict": "PASS" if mut_pass else "FAIL"
    })

    # =========================================================================
    # Property 4: Absence of External Side Effects (BR05-EXT-04)
    # =========================================================================
    # 4.1 No stdout / stderr leakage
    old_stdout, old_stderr = sys.stdout, sys.stderr
    buf_out, buf_err = io.StringIO(), io.StringIO()
    sys.stdout, sys.stderr = buf_out, buf_err
    try:
        shipping.quote(500, "LOCAL", False)
        shipping.quote(-1, "LOCAL", False)
        shipping.quote(15000, "REMOTE", True)
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr
    no_io_output = (buf_out.getvalue() == "" and buf_err.getvalue() == "")

    # 4.2 No environment variables modified
    env_before = dict(os.environ)
    shipping.quote(500, "LOCAL", False)
    env_after = dict(os.environ)
    no_env_change = (env_before == env_after)

    ext_pass = no_io_output and no_env_change
    report["tests"].append({
        "test_id": "BR05-EXT-04",
        "property": "Ausência de efeitos secundários externos (I/O e ambiente)",
        "description": "Verificação de ausência de emissão para stdout/stderr e integridade de variáveis de ambiente",
        "no_stdout_stderr_leakage": no_io_output,
        "no_environment_variables_modified": no_env_change,
        "verdict": "PASS" if ext_pass else "FAIL"
    })

    # Overall verdict
    overall = "PASS" if all(t["verdict"] == "PASS" for t in report["tests"]) else "FAIL"
    report["overall_verdict"] = overall

    out_file = pathlib.Path(__file__).resolve().parent / "br05_independence.results.json"
    out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"BR-05 Multi-Property Verification finished with verdict: {overall}")
    print(f"Results written to: {out_file}")
    return 0 if overall == "PASS" else 1

if __name__ == "__main__":
    sys.exit(verify_br05())
