from .observer_base import Observer

class ConsoleDisplayObserver(Observer):
    def update(self, data):
        print("\n--- Resultado da Avaliação ---")
        if data:
            print(f"  Prompt: {data.get('prompt', 'N/A')}")
            print(f"  Resposta ChatGPT: {data.get('chatgpt_response', 'N/A')}")
            print(f"  Resposta Outro LLM: {data.get('other_llm_response', 'N/A')}")
            print(f"  Estratégia de Avaliação: {data.get('evaluation_strategy', 'N/A')}")
            print(f"  Vencedor: {data.get('winner', 'N/A')}")
            print(f"  Razão: {data.get('reason', 'N/A')}")
            if data.get('details'):
                print(f"  Detalhes da Avaliação: {data.get('details')}")
            print("---------------------------\n")
        else:
            print("  Nenhum resultado de avaliação para exibir.")