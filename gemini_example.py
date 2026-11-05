import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
ai_model = os.getenv("AI_MODEL")

if not gemini_api_key:
    print("API Key não configurada!")
    sys.exit(1)

client = genai.Client(api_key=gemini_api_key)
print("Cliente Gemini criado com sucesso!")

response = client.models.generate_content(model=ai_model,
                                        contents="Explique o que é FastAPI.")

print(response.text)
