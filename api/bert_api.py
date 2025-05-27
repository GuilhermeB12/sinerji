from transformers import pipeline
from .base import LLMConnector

class BERTAPI(LLMConnector):
    def __init__(self, model_name: str = "bert-base-uncased"):
        try:
            self.generator = pipeline("text-generation", model=model_name) 
        except Exception as e:
            print(f"Erro ao carregar o modelo BERT '{model_name}': {e}")
            self.generator = None

    def ask(self, question: str) -> str:
        if not self.generator:
            return "Modelo BERT não carregado devido a um erro anterior."
        try:
            result = self.generator(
                question,
                max_new_tokens=100,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.01,
                top_k=50,
                top_p=0.95,
                pad_token_id=self.generator.tokenizer.eos_token_id
            )
            generated_text = result[0]['generated_text']
            
            if generated_text.lower().startswith(question.lower()):
                return generated_text[len(question):].strip()
            return generated_text.strip()
        except Exception as e:
            print(f"Erro ao gerar resposta com BERT/GPT2: {e}")
            return "Não foi possível obter uma resposta do BERT no momento."