class AccessControl:
    def __init__(self):
        self.permissions = {}

    def assign_role(self, user, role):
        self.permissions[user] = role

    def has_access(self, user, resource):
        return self.permissions.get(user, None) == resource
