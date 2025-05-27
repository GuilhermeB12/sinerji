import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if project_root not in sys.path:
    sys.path.append(project_root)

from api.factory import LLMFactory
from command.ask_question import AskQuestionCommand
from command.invoker import CLIInvoker
from strategy.evaluator import ResponseEvaluator
from strategy.length_score import LengthEvaluationStrategy
from strategy.keyword_match import KeywordMatchEvaluationStrategy
from observer.console_observer import ConsoleDisplayObserver
from observer.subject import LLMResponsePublisher

def main():
    print("Iniciando a aplicação...")

    factory = LLMFactory()
    
    chatgpt_connector = None
    bert_connector = None

    try:
        chatgpt_connector = factory.create("chatgpt")
        print("Conector ChatGPT criado com sucesso.")
    except Exception as e:
        print(f"Falha ao criar o conector ChatGPT. Verifique a chave de API e a quota: {e}")

    try:
        bert_connector = factory.create("bert", llm_model_name="bert-base-uncased")
        print("Conector BERT criado com sucesso. (Pode demorar para baixar o modelo na primeira vez)")
    except Exception as e:
        print(f"Falha ao criar o conector BERT: {e}")

    if not chatgpt_connector and not bert_connector:
        print("Nenhum conector de LLM pôde ser inicializado. Encerrando aplicação.")
        return

    publisher = LLMResponsePublisher()
    console_observer = ConsoleDisplayObserver()
    publisher.attach(console_observer)

    print("\nBem-vindo ao comparador de LLMs!")
    print("Digite 'sair' para encerrar a aplicação.")

    while True:
        user_prompt = input("\nSua pergunta (ou 'sair'): ")
        if user_prompt.lower() == 'sair':
            print("Encerrando a aplicação.")
            break
        
        chatgpt_response = "N/A (Conector não disponível)"
        bert_response = "N/A (Conector não disponível)"

        if chatgpt_connector:
            try:
                chatgpt_command = AskQuestionCommand(chatgpt_connector, user_prompt)
                chatgpt_response = chatgpt_command.execute()
            except Exception as e:
                chatgpt_response = f"Erro ao obter resposta do ChatGPT: {e}"
                print(f"DEBUG: Erro ao executar comando ChatGPT: {e}")
        
        if bert_connector:
            try:
                bert_command = AskQuestionCommand(bert_connector, user_prompt)
                bert_response = bert_command.execute()
            except Exception as e:
                bert_response = f"Erro ao obter resposta do BERT: {e}"
                print(f"DEBUG: Erro ao executar comando BERT: {e}")

        print("\n--- Respostas Coletadas dos LLMs ---")
        print(f"ChatGPT: {chatgpt_response}")
        print(f"BERT: {bert_response}")

        if ("Erro ao" in chatgpt_response or "Não foi possível" in chatgpt_response) or \
           ("Erro ao" in bert_response or "Não foi possível" in bert_response):
            print("\nNão foi possível avaliar as respostas devido a erros na obtenção de uma ou ambas.")
            publisher.chosen_response_info = {
                "prompt": user_prompt,
                "chatgpt_response": chatgpt_response,
                "other_llm_response": bert_response,
                "evaluation_strategy": "Não avaliado (erros de LLM)",
                "winner": "N/A",
                "reason": "Erro em um ou ambos os LLMs. Verifique logs/console para detalhes.",
                "details": {}
            }
            continue

        evaluator = ResponseEvaluator()
        
        print("\nEscolha uma estratégia de avaliação:")
        print("1. Avaliar por comprimento (maior resposta)")
        print("2. Avaliar por palavras-chave (digite as palavras-chave)")
        print("3. Pular avaliação")

        choice = input("Sua escolha (1, 2 ou 3): ")

        evaluation_results = None
        current_strategy_name = "N/A"

        if choice == '1':
            evaluator.strategy = LengthEvaluationStrategy()
            current_strategy_name = "Comprimento da Resposta"
            evaluation_results = evaluator.evaluate_responses(chatgpt_response, bert_response)
        elif choice == '2':
            keywords_input = input("Digite as palavras-chave separadas por vírgula (ex: neymar, brasil, futebol): ")
            keywords_list = [k.strip() for k in keywords_input.split(',') if k.strip()]
            if keywords_list:
                evaluator.strategy = KeywordMatchEvaluationStrategy(keywords_list)
                current_strategy_name = f"Correspondência de Palavras-chave ({', '.join(keywords_list)})"
                evaluation_results = evaluator.evaluate_responses(chatgpt_response, bert_response)
            else:
                print("Nenhuma palavra-chave informada para avaliação por palavras-chave.")
                evaluation_results = None 
        elif choice == '3':
            print("Avaliação pulada.")
        else:
            print("Escolha inválida. Nenhuma avaliação será feita.")

        full_results_data = {
            "prompt": user_prompt,
            "chatgpt_response": chatgpt_response,
            "other_llm_response": bert_response,
            "evaluation_strategy": current_strategy_name,
            "winner": evaluation_results.get("winner") if evaluation_results else "N/A",
            "reason": evaluation_results.get("reason") if evaluation_results else "N/A",
            "details": evaluation_results.get("details") if evaluation_results else {}
        }
        publisher.chosen_response_info = full_results_data

if __name__ == "__main__":
    main()