# Comparador de Modelos de Linguagem (LLMs)

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em Python que permite comparar respostas de diferentes Large Language Models (LLMs), como ChatGPT e BERT (utilizando um modelo generativo como GPT-2 ou similar), para uma mesma pergunta. A aplicação utiliza diversos padrões de projeto (Factory, Command, Strategy, Observer) para garantir uma arquitetura modular e extensível.

## Funcionalidades

* **Conexão com Múltiplos LLMs:** Suporte para ChatGPT (via API da OpenAI) e outro LLM baseado em Transformers (como GPT-2) da Hugging Face.
* **Padrão Factory:** Criação flexível e desacoplada de conectores para LLMs.
* **Padrão Command:** Encapsulamento das operações de "fazer pergunta" como comandos, permitindo sua execução e extensão de forma organizada.
* **Padrão Strategy:** Definição de diferentes algoritmos para comparar as respostas dos LLMs (atualmente por comprimento e palavras-chave), permitindo que o usuário escolha a estratégia em tempo de execução.
* **Padrão Observer:** Notificação e exibição dos resultados da avaliação de forma desacoplada, permitindo adicionar novos observadores facilmente (ex: para salvar em um arquivo).
* **Interface CLI:** Interação simples e direta via linha de comando para inserir perguntas e escolher estratégias.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python 3.8+ instalado e as seguintes dependências:

* `openai`
* `transformers`
* `torch` (ou `tensorflow`, dependendo da sua preferência e da biblioteca Transformers)

Além disso, para usar o ChatGPT, você precisará de uma chave de API da OpenAI.

## Configuração

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/sinerji.git](https://github.com/seu-usuario/sinerji.git)
    cd sinerji
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    É altamente recomendável usar um ambiente virtual para gerenciar as dependências.
    ```bash
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a Chave de API da OpenAI:**
    A chave de API do ChatGPT deve ser definida como uma variável de ambiente. Crie um arquivo `.env` na raiz do projeto (se o `python-dotenv` for usado implicitamente ou explicitamente pelo `openai` library) ou exporte-a diretamente no seu terminal:
    ```bash
    export OPENAI_API_KEY="sua_chave_openai_aqui"
    # No Windows (Command Prompt)
    set OPENAI_API_KEY="sua_chave_openai_aqui"
    # No Windows (PowerShell)
    $env:OPENAI_API_KEY="sua_chave_openai_aqui"
    ```
    Substitua `"sua_chave_openai_aqui"` pela sua chave real da OpenAI.

## Execução

Após a configuração, você pode iniciar a aplicação a partir da raiz do projeto:

```bash
python main.py