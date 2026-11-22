| Suite | n | Requisitos R01–R05 | Partições | Fronteiras (de 10) | Fronteiras em falta | Expectativas inválidas | Duplicados exatos | Mesma partição | Defeitos (expectativas originais) | Defeitos (oráculo corrigido) |
|---|---:|---|---:|---:|---|---:|---:|---:|---|---|
| Humano H-01..H-12 | 12 | R01, R02, R03, R04 | 11 | 8 | REMOTE-express=5000, REMOTE-express=5001 | 0 | 0 | 0 | DEF-01, DEF-02, DEF-03 | DEF-01, DEF-02, DEF-03 |
| IA AI-01..AI-12 | 12 | R01, R02, R03, R04, R05 | 11 | 3 | REMOTE-express=5000, REMOTE-express=5001, W=1, W=1001, W=20000, W=5000, W=5001 | 3 | 1 | 1 | DEF-03 | DEF-02, DEF-03, DEF-04 |
| Humano completo H-01..H-16 | 16 | R01, R02, R03, R04, R05 | 14 | 10 | — | 0 | 0 | 0 | DEF-01, DEF-02, DEF-03, DEF-04 | DEF-01, DEF-02, DEF-03, DEF-04 |

Sintoma por caso (oráculo corrigido):
  AI-05: DEF-03  input={"weight": 500, "zone": "REMOTE", "express": false} actual={"status": "OK", "fee": 4}
  AI-06: DEF-02  input={"weight": 1000, "zone": "LOCAL", "express": false} actual={"status": "OK", "fee": 8}
  AI-09: DEF-04  input={"weight": 6000, "zone": "REMOTE", "express": true} actual={"status": "OK", "fee": 10}
  AI-12: DEF-03  input={"weight": 2000, "zone": "REMOTE", "express": false} actual={"status": "OK", "fee": 4}
  H-03: DEF-02  input={"weight": 1000, "zone": "LOCAL", "express": false} actual={"status": "OK", "fee": 8}
  H-07: DEF-01  input={"weight": 20000, "zone": "LOCAL", "express": false} actual={"status": "INVALID", "fee": null}
  H-10: DEF-03  input={"weight": 500, "zone": "REMOTE", "express": false} actual={"status": "OK", "fee": 4}
  H-12: DEF-03  input={"weight": 500, "zone": "REMOTE", "express": true} actual={"status": "OK", "fee": 10}
  H-13: DEF-03  input={"weight": 5000, "zone": "REMOTE", "express": true} actual={"status": "OK", "fee": 10}
  H-14: DEF-04  input={"weight": 5001, "zone": "REMOTE", "express": true} actual={"status": "OK", "fee": 10}
