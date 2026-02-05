def check_governance(data):
    allowed_roles = ["doctor", "family"]

    if data["role"] not in allowed_roles:
        return False, "Unauthorized role"

    if not data["privacy_policy_accepted"]:
        return False, "Privacy policy not accepted"

    if not data["approved_by_admin"]:
        return False, "Admin approval missing"

    return True, "Governance approved"
