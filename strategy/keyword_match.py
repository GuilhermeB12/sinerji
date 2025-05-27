from .base import EvaluationStrategy

class KeywordMatchEvaluationStrategy(EvaluationStrategy):
    def __init__(self, keywords: list[str]):
        self.keywords = [k.lower() for k in keywords]

    def evaluate(self, response1: str, response2: str) -> dict:
        score1 = sum(1 for keyword in self.keywords if keyword in response1.lower())
        score2 = sum(1 for keyword in self.keywords if keyword in response2.lower())

        winner_name = ""
        reason_text = ""

        if score1 > score2:
            winner_name = "Resposta 1 (ChatGPT)"
            reason_text = f"Resposta 1 tem mais palavras-chave correspondentes ({score1}) que Resposta 2 ({score2})."
        elif score2 > score1:
            winner_name = "Resposta 2 (Outro LLM)"
            reason_text = f"Resposta 2 tem mais palavras-chave correspondentes ({score2}) que Resposta 1 ({score1})."
        else:
            winner_name = "Empate"
            reason_text = f"Ambas as respostas têm o mesmo número de palavras-chave correspondentes ({score1})."
        
        return {
            "winner": winner_name,
            "reason": reason_text,
            "details": {"score_r1": score1, "score_r2": score2, "keywords_used": self.keywords}
        }