import openai
from app.core.config import settings

def get_openai_response(message: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
        temperature=0.7,
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]
