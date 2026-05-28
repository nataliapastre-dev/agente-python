import requests
import datetime

historico = [
    {
        "role": "system",
        "content": "Você é um assistente inteligente, útil e objetivo."
    }
]

def agente():
    print("🤖 Chat iniciado! Digite 'sair' para encerrar.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Encerrando chat... 👋")
            break

        historico.append({"role": "user", "content": user_input})

        try:
            resposta = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": "llama3:latest",
                    "messages": historico,
                    "stream": False
                },
                timeout=120
            )

            data = resposta.json()

            if "message" in data:
                resposta_texto = data["message"]["content"]
            else:
                resposta_texto = str(data)

            historico.append({"role": "assistant", "content": resposta_texto})

            print("\n🤖:", resposta_texto, "\n")

            salvar_log(user_input, resposta_texto)

        except Exception as e:
            print("❌ Erro:", e)


def salvar_log(pergunta, resposta):
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write("\n====================\n")
        f.write(f"Data: {data}\n")
        f.write(f"Você: {pergunta}\n")
        f.write(f"Bot: {resposta}\n")


agente()