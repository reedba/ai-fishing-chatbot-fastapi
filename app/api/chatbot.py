from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.responses import StreamingResponse
from app.models.chat_model import ChatRequest
from app.services.openai_service import get_openai_response

router = APIRouter()

@router.post("/chat")
async def chat_with_gpt(request: ChatRequest):
    try:
        async def response_generator():
            async for chunk in get_openai_response(request.message):
                yield chunk

        return StreamingResponse(response_generator(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app = FastAPI()
app.include_router(router)