from .base import EvaluationStrategy

class ResponseEvaluator:
    def __init__(self, strategy: EvaluationStrategy = None):
        self._strategy = strategy

    @property
    def strategy(self) -> EvaluationStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: EvaluationStrategy):
        self._strategy = strategy

    def evaluate_responses(self, response1: str, response2: str) -> dict:
        if not self._strategy:
            raise ValueError("Nenhuma estratégia de avaliação definida.")
        return self._strategy.evaluate(response1, response2)