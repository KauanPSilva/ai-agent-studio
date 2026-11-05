import os
from dotenv import load_dotenv

load_dotenv()

ai_provider = os.getenv("AI_PROVIDER")
ai_model = os.getenv("AI_MODEL")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    print("API Key não configurada!")
else:
    print("API Key configurada!")