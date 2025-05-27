import os
from openai import OpenAI
from .base import LLMConnector

class ChatGPTAPI(LLMConnector):
    def __init__(self):
        self.client = OpenAI()
    
    def ask(self, question: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=250,
            )
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Erro ao chamar a API do OpenAI (ChatGPT): {e}")
            return "Não foi possível obter uma resposta do ChatGPT no momento."