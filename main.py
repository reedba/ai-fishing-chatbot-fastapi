from fastapi import FastAPI
from app.api import chatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Include API routes
app.include_router(chatbot.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Chatbot is running!"}