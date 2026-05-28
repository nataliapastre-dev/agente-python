# 🤖 Agente Python com Ollama (ChatGPT Local)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-orange.svg)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen.svg)

Este projeto é um **assistente de IA local** desenvolvido em Python utilizando o Ollama, permitindo rodar modelos de linguagem (LLMs) diretamente no seu computador, com total privacidade e sem depender da nuvem.

---

## 🚀 Funcionalidades

* 💬 **Chat no terminal:** Interface amigável e interativa direto pela linha de comando.
* 🧠 **IA Local:** Execução de modelos de forma 100% offline via Ollama.
* 💾 **Memória de sessão:** O assistente gerencia o estado da conversa, lembrando do contexto atual.
* ⏱️ **Respostas em tempo real:** Integração otimizada para respostas rápidas e inteligentes.
* 📝 **Histórico automático:** Persistência de dados das conversas salvas automaticamente em arquivo `.txt`.

---

## 🎯 Destaques para Recrutadores (Skills Aplicadas)

Este projeto demonstra competências práticas essenciais para o desenvolvimento de software moderno e integração com Inteligência Artificial:

* **Consumo de APIs REST:** Comunicação direta com o serviço local do Ollama via requisições HTTP (`requests`).
* **Manipulação de Arquivos (I/O):** Persistência de dados em tempo de execução para salvamento de logs de conversação de forma assíncrona/estruturada.
* **Gerenciamento de Estado:** Lógica implementada em Python para manter a memória de contexto entre os inputs do usuário (histórico da sessão).
* **Clean Code & Arquitetura Simples:** Código modular, de fácil leitura, focado em reaproveitamento e boas práticas de desenvolvimento.

---

## 🛠️ Tecnologias Utilizadas

* **Python** (Linguagem base para lógica e estruturação)
* **Ollama** (Gerenciador e orquestrador de LLMs locais)
* **API HTTP Local** (`http://localhost:11434` como endpoint de comunicação)
* **Modelos suportados:** Llama3, Mistral, Phi-3, entre outros.

---

## 📁 Estrutura do Projeto

```text
agente-python/
│
├── agent.py          # Código-fonte principal com a lógica do assistente
├── chat_log.txt      # Arquivo de persistência do histórico (gerado dinamicamente)
└── README.md         # Documentação técnica do projeto

