from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self):
        pass