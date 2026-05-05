from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

@dataclass
class Feedback:
    MAX_LENGTH: ClassVar[int] = 1000
    TYPES: ClassVar[list] = ['bug report', 'feature request', 'compliment']
    type: str
    content: str
    id: int = -1
    user_id: int = -1
    submission_time: datetime = datetime.now()

    def __post_init__(self):
        errors = []

        if self.type not in self.TYPES:
            errors.append(ValueError("Invalid type {}".format(self.type)))

        if len(self.content) > Feedback.MAX_LENGTH:
            errors.append(ValueError("Feedback content too long"))

        if errors:
            raise ExceptionGroup("Validation failed: ", errors)

    @classmethod
    def from_row(cls, row):
        try:
            return cls(row["type"],
                   row["content"],
                   row["id"],
                   row["user_id"],
                   row["submission_time"])
        except (KeyError, IndexError) as e:
            raise AttributeError(f"Database Mapping Error: Column {e} not found in row passed to from_row") from e

    def to_row(self):
        return {"type": self.type, "content": self.content, "id": self.id, "user_id": self.user_id, "submission_time": self.submission_time}