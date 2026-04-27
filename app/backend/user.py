class User:
    roles = ["admin", "user"]
    def __init__(self, id, username = None, email = None, role = None):
        self.ID = id
        self.Username = username
        self.Email = email

        if role not in self.roles:
            raise ValueError("Invalid role {}".format(role))
        else:
            self.Role = role