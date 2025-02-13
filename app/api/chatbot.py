from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.chat_model import ChatRequest
from app.services.openai_service import get_openai_response

router = APIRouter()

@router.post("/chat")
async def chat_with_gpt(request: ChatRequest):
    try:
        async def response_generator():
            response = get_openai_response(request.message)
            for chunk in response:
                yield chunk

        return StreamingResponse(response_generator(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))