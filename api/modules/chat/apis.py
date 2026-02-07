"""
chat module APIs
"""
import json
from collections.abc import AsyncGenerator
from typing import Any
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from chatbot_ai import intelligence
from .schema import UserOut, UserQuery

router = APIRouter(prefix="/chat")

@router.get("/list/", response_model=list[UserOut])
def list_chats():
    """List all chats
    Returns:
        list[UserOut]: A list of user chat summaries
    """
    return [{"id": 1, "message": "Hi"}]

@router.post(path="/")
async def ask_ai(payload: UserQuery) -> StreamingResponse:
    """API to ask AI any query

    Args:
        payload (UserQuery): a dict that contains query

    Returns:
        StreamingResponse: Streaming response utiltiy from FastAPI
    """
    async def generate() -> AsyncGenerator[str, Any]:
        """
        async generate method
        """
        message: str = """"""
        async for chunk in intelligence.astream(query=payload.query):
            message += chunk
            yield f"data: {json.dumps({'id': 1, 'message': message})}\n\n"

    return StreamingResponse(content=generate(), media_type="text/event-stream")
