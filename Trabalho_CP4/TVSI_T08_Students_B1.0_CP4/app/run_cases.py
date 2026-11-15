"""Execute JSON cases without third-party dependencies."""
import json, pathlib, sys
from shipping import quote
def main():
    if len(sys.argv)!=2:
        print("Usage: python run_cases.py cases.json");return 2
    try:
        cases=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
        if not isinstance(cases,list): raise ValueError("cases must be a JSON list")
        ids=[c["id"] for c in cases]
        if len(set(ids))!=len(ids): raise ValueError("duplicate case IDs")
        results=[]
        for c in cases:
            actual=quote(**c["input"])
            results.append({"id":c["id"],"input":c["input"],"expected":c["expected"],"actual":actual,"verdict":"PASS" if actual==c["expected"] else "FAIL"})
    except (ValueError,KeyError,TypeError,OSError) as e:
        print("CASE FILE ERROR:",e);return 2
    report={"build":"T08-B1.0","suite":pathlib.Path(sys.argv[1]).name,"python":sys.version,"results":results}
    out=pathlib.Path(sys.argv[1]).with_suffix(".results.json")
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))
    return 1 if any(r["verdict"]=="FAIL" for r in results) else 0
if __name__=="__main__":sys.exit(main())
