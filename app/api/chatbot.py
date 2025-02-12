from fastapi import APIRouter, HTTPException
from app.models.chat_model import ChatRequest
from app.services.openai_service import get_openai_response

router = APIRouter()

@router.post("/chat")
async def chat_with_gpt(request: ChatRequest):
    try:
        response = get_openai_response(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
