from openai import OpenAI
from app.core.config import settings
import pdb

client = OpenAI()

async def get_openai_response(message: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
            stream=True,
                )

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                yield content
    except Exception as e:
        raise