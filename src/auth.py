class AuthError(Exception):
    pass

class IAMGate:
    """Minimal IAM-style role guard for demo."""

    role_permissions = {
        "analyst": ["run_loyalty_gap_analysis"],
        "manager": ["run_loyalty_gap_analysis", "export_report"],
        "guest": [],
    }

    def __init__(self, user_role: str):
        self.user_role = user_role

    def can(self, permission: str) -> bool:
        return permission in self.role_permissions.get(self.user_role, [])

    def check(self, permission: str):
        if not self.can(permission):
            raise AuthError(f"Role '{self.user_role}' lacks permission '{permission}'")
