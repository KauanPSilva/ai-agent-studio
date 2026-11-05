messages = [
    {
        "role": "system",
        "content": "Você é um especialista em python que vai tirar dúvidas sobre código indentação entre outros tópicos sobre python você irá receber e responder mensagens em português."
    },
    {
        "role": "user",
        "content": "Qual a diferênça entre uma lista e uma tupla em python?"
    }
]

user_messages = []
for message in messages:
    if message["role"] == "user":
        user_messages.append(message["content"])

print(user_messages[0])
