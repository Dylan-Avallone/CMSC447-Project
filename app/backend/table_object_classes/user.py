from dataclasses import dataclass
from typing import ClassVar
from app.backend.table_object_classes.table_object import TableObject

@dataclass
class User(TableObject):
    ROLES: ClassVar[list] = ["admin", "user", "developer"]
    id: int = -1
    username: str = "Anonymous/Unknown"
    email: str = None
    role: str = None

    def __post_init__(self):
        if self.role not in self.ROLES:
            raise ValueError("Invalid role {}".format(self.role))

    @classmethod
    def from_row(cls, row):
        try:
            return cls(row["id"], row["username"], row["email"], row["role"])
        except (KeyError, IndexError) as e:
            raise AttributeError(f"Database Mapping Error: Column {e} not found in row passed to from_row") from e

    @classmethod
    def has_higher_privilege(self, other: User) -> bool:
        """
        Returns true if the passed User has lower or equal privilege level
        """
        privilege_level_dict = {"developer": 3, "admin": 2, "user": 1}
        return privilege_level_dict[self.role] >= privilege_level_dict[other.role]