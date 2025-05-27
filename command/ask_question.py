from .base import Command
from api.base import LLMConnector

class AskQuestionCommand(Command):
    def __init__(self, model: LLMConnector, question: str):
        self.model = model
        self.question = question
        self.response = None

    def execute(self) -> str:
        self.response = self.model.ask(self.question)
        return self.response