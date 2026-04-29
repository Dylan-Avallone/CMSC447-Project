from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    ROLES: ClassVar[list] = ["admin", "user", "developer"]
    id: int
    username: str = None
    email: str = None
    role: str = None

    def __post_init__(self):
        if self.role not in self.ROLES:
            raise ValueError("Invalid role {}".format(self.role))