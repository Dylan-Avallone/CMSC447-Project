from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    ROLES: ClassVar[list]= ["admin", "user", "developer"]
    id: int
    username: str
    email: str
    role: str

    def __post_init__(self):
        if self.role not in self.ROLES:
            raise ValueError("Invalid role {}".format(self.role))