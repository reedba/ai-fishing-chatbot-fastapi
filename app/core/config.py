
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    def configure_openai(self):
        import openai
        openai.api_key = self.OPENAI_API_KEY  # Explicitly set OpenAI API key

settings = Settings()
settings.configure_openai()  # Ensure OpenAI is configured
