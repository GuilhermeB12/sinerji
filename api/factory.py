from .base import LLMConnector
from .chatgpt_api import ChatGPTAPI
from .bert_api import BERTAPI

class LLMFactory:
    @staticmethod
    def create(llm_type: str, llm_model_name: str = None, **kwargs) -> LLMConnector:
        llm_type_lower = llm_type.lower()

        if llm_type_lower == "chatgpt":
            return ChatGPTAPI()
        elif llm_type_lower == "bert":
            actual_bert_model = llm_model_name if llm_model_name else "bert-base-uncased"
            return BERTAPI(actual_bert_model)
        else:
            raise ValueError(f"Modelo desconhecido: '{llm_type}'. Tipos suportados: 'chatgpt', 'bert'.")