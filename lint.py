import subprocess
import json
import sys
import os

files = sys.argv[1].split()
severity = sys.argv[2]

results = {}

for file in files:

    process = subprocess.run(
        ["verilator", "--lint-only", file],
        capture_output=True,
        text=True
    )

    if process.returncode == 0:
        results[file] = {
            "status": "PASS",
            "severity": severity
        }

    else:
        results[file] = {
            "status": "FAIL",
            "severity": severity,
            "errors": process.stderr
        }

json_result = json.dumps(results)

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"result={json_result}\n")

print(json_result)

