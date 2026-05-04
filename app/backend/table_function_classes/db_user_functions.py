from app.backend.db import DB
from app.backend.table_object_classes.user import User

class DBUserFunctions:
    def __init__(self, db:DB):
        self.DB = db

    def add_user(self, user: User):
        """
        Takes a User object and creates an insertion command using values from the attributes of the object.
        """
        command = None
        params = ()
        if user.id == -1:
            command = "INSERT INTO Users (name, email, role) VALUES (?, ?, ?)"
            params = (user.username, user.email, user.role)
        else: # Attempt to add this user which has a non-default ID.
            command = "INSERT INTO Users (id, name, email, role) VALUES (?, ?, ?, ?)"
            params = (user.id, user.username, user.email, user.role)
        self.DB.execute_command(command, params)

    def get_user(self, user: User) -> User:
        command = "SELECT * FROM Users WHERE user_email = ? LIMIT 1"
        params = (email,)
        result = self.DB.get_one(command, params)

        if result:
            return User(id=result[0], username=result[1], email=result[2], role=result[3])
        else:
            return User()

    def get_users_by_role(self, role: str) -> list[User]:
        command = "SELECT user_id, user_name, user_email, user_role FROM Users WHERE user_role = ?"
        params = (role,)
        result = self.DB.get_all(command, params)
        return [User(id=r[0], username=r[1], email=r[2], role=r[3]) for r in result]

    def remove_user(self, user:User):
        command = "DELETE FROM Users WHERE user_id = ?"
        params = (user.id,)
        self.DB.execute_command(command, params)

    def edit_user(self, user:User):
        updates = []
        params = []

        if user.username is not None:
            updates.append("user_name = ?")
            params.append(user.username)
        if user.email is not None:
            updates.append("user_email = ?")
            params.append(user.email)
        if user.role is not None:
            updates.append("user_role = ?")
            params.append(user.role)

        if not updates:
            return

        params.append(user.id)
        command = f"UPDATE Users SET {', '.join(updates)} WHERE user_id = ?"
        self.DB.execute_command(command, params)