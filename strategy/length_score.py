from .base import EvaluationStrategy

class LengthEvaluationStrategy(EvaluationStrategy):
    def evaluate(self, response1: str, response2: str) -> dict:
        len1 = len(response1)
        len2 = len(response2)
        
        winner_name = ""
        reason_text = ""

        if len1 > len2:
            winner_name = "Resposta 1 (ChatGPT)"
            reason_text = f"Resposta 1 é mais longa ({len1} caracteres) que Resposta 2 ({len2} caracteres)."
        elif len2 > len1:
            winner_name = "Resposta 2 (Outro LLM)"
            reason_text = f"Resposta 2 é mais longa ({len2} caracteres) que Resposta 1 ({len1} caracteres)."
        else:
            winner_name = "Empate"
            reason_text = f"Ambas as respostas têm o mesmo comprimento ({len1} caracteres)."
        
        return {
            "winner": winner_name,
            "reason": reason_text,
            "details": {"len_r1": len1, "len_r2": len2}
        }