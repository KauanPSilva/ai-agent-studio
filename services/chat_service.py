import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_response(prompt: str) -> str:
    ai_model = os.getenv("AI_MODEL")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("API Key não está configurada!")

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(model=ai_model, contents=prompt)

    return response.text