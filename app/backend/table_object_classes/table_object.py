from abc import ABC, abstractmethod

class TableObject(ABC):
    @classmethod
    @abstractmethod
    def from_row(cls, row):
        pass