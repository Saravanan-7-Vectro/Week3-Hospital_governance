import json
import sys
from governance_rules import check_governance

print("\n=== Hospital Governance Access Check ===\n")

with open("access_request.json") as f:
    request = json.load(f)

status, message = check_governance(request)

if status:
    print("[✔] GOVERNANCE PASSED")
    print("Access granted to patient records")
    sys.exit(0)
else:
    print("[✘] GOVERNANCE FAILED")
    print("Access denied")
    print("Reason:", message)
    sys.exit(1)
