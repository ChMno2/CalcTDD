"""Wait for the GitHub Actions run of a commit and print its job steps and annotations."""
import json
import sys
import time
import urllib.request

REPO = "ChMno2/CalcTDD"
sha = sys.argv[1]


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


run = None
for _ in range(40):
    runs = get(f"https://api.github.com/repos/{REPO}/actions/runs?head_sha={sha}")["workflow_runs"]
    if runs and runs[0]["status"] == "completed":
        run = runs[0]
        break
    time.sleep(15)
if run is None:
    sys.exit(f"timed out waiting for run of {sha}")

print(f"run {run['id']} sha {sha[:7]} conclusion={run['conclusion']} {run['html_url']}")
for job in get(run["jobs_url"])["jobs"]:
    for step in job["steps"]:
        print(f"  step: {step['name']:<28} {step['conclusion']}")
    for a in get(f"https://api.github.com/repos/{REPO}/check-runs/{job['id']}/annotations"):
        print(f"  annotation: {a['annotation_level']}: {a['message']}")
