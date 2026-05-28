# 🤖 Agente Python com Ollama (ChatGPT Local)

Este projeto é um **assistente de IA local** desenvolvido em Python utilizando o Ollama, permitindo rodar modelos de linguagem (LLMs) diretamente no computador, sem depender da nuvem.

---

## 🚀 Funcionalidades

- Chat estilo ChatGPT no terminal
- Execução de modelos de IA local (Ollama)
- Memória de conversa durante a sessão
- Respostas inteligentes em tempo real
- Salvamento de histórico em arquivo `.txt`

---

## 🧠 Tecnologias utilizadas

- Python
- Ollama
- API HTTP local (`localhost:11434`)
- Modelos LLM (Llama3 / Mistral)

---

## ⚙️ Como executar o projeto

### 1. Instale o Ollama
https://ollama.com

---

### 2. Baixe um modelo
Exemplo:

```bash
ollama pull llama3

Execute o agente
python agent.py

💬 Como usar

Após iniciar o programa:

Você: me ajuda a organizar meu dia
Bot: ...
📁 Estrutura do projeto
agente-python/
│
├── agent.py
├── chat_log.txt
└── README.md
⚡ Exemplo de uso
Você: oi
Bot: Olá! Como posso te ajudar hoje?

Você: cria um plano de estudo
Bot: Aqui está um plano...
📌 Objetivo

Este projeto tem como objetivo demonstrar:

Uso de Inteligência Artificial local
Integração Python + APIs
Criação de assistente conversacional
Base para automações e agentes inteligentes
