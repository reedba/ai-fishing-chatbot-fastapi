import logging
from fastapi import FastAPI
from app.api import chatbot
from dotenv import load_dotenv
from app.middleware.cors_middleware import add_cors_middleware

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

# Include API routes
app.include_router(chatbot.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Chatbot is running!"}

# Add logging
logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {response.status_code}")
    return response