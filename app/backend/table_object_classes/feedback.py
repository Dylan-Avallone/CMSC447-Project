from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Feedback:
    MAX_LENGTH: ClassVar[int] = 1000
    TYPES: ClassVar[list] = ['bug report', 'feature request', 'compliment']
    id: int
    type: str
    content: str
    def __post_init__(self):
        errors = []

        if self.type not in self.TYPES:
            errors.append(ValueError("Invalid type {}".format(self.type)))

        if len(self.content) > Feedback.MAX_LENGTH:
            errors.append(ValueError("Feedback content too long"))

        if errors:
            raise ExceptionGroup(errors)