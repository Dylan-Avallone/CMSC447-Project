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
    created_at: datetime = datetime.now()
    def __post_init__(self):
        errors = []

        if self.type not in self.TYPES:
            errors.append(ValueError("Invalid type {}".format(self.type)))

        if len(self.content) > Feedback.MAX_LENGTH:
            errors.append(ValueError("Feedback content too long"))

        if errors:
            raise ExceptionGroup("Validation failed: ", errors)