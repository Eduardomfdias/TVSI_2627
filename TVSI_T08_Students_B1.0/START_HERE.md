# T08 — AI-Assisted Test Design
TVSI 2026/27 · T08-B1.0 · Student package

1. Download the ZIP and extract ALL files to a normal local folder. Do not run inside ZIP or Google Drive preview.
2. Read [Student assignment](StudentAssignment.html) and [Business rules](BusinessRules.html).
3. Python 3.10+ must be available. Open a terminal in the extracted app folder. Check `python --version` (Windows: `py -3 --version`). Use the commands in BusinessRules. No pip install, account, server or IDE is needed. If Python is unavailable, report the environment as BLOCKED and ask the teacher for a lab machine; do not invent execution results.
4. Run the environment check in BusinessRules before designing tests.
5. Save a working copy of [Test results template](TestResults_T08_Template.xlsx). Use any compatible desktop spreadsheet application; record its name/version.
6. Keep evidence with unique test/run IDs. Never overwrite a prior execution silently.

Open the app folder in your file manager; this Python topic has no browser application.

## Recording work
Test Cases holds preconditions, exact inputs, steps and independently derived expectations. Executions holds actual results, environment, evidence and a manual verdict (PASS/FAIL/BLOCKED/NOT RUN). Defects holds reproducible findings. Static Review records rule questions. Coverage maps R01–R08 to Test IDs and counts unique designed/executed tests. Technique holds the topic-specific design record.

Use one requirement–test pair per Coverage row. PASS/FAIL count as executed; BLOCKED does not. This is requirement coverage only, not decision, branch, boundary or exploration coverage. The template supports 80 cases, 80 runs and 100 mappings. Extend both tables and bounded formulas if needed.

All datasets are fictitious. The HTML/Markdown handouts work offline and can be printed from the browser. Keep the supplied test object unchanged. The source code is part of the executable package, but only T07 asks you to inspect it for test design.
