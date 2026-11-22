# Run abortado — sem resultados de teste

Invocação `python3.12 -I run_cases.py <suite>` falhou com `ModuleNotFoundError: No module named 'shipping'`:
o modo isolado (`-I`) retira a pasta do script do `sys.path`. Os exit codes 1 em `exit_codes.txt` são do
ImportError, **não** de comparações. Nenhum `.results.json` foi gerado. Run preservado por regra (não apagar runs);
substituído pelo run seguinte, que usa `-E -s`.
