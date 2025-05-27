from abc import ABC, abstractmethod

class LLMConnector(ABC):
    @abstractmethod
    def ask(self, question: str) -> str:
        pass