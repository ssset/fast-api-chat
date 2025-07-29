from fastapi.websockets import WebSocket
from fastapi.routing import APIRoute

router = APIRoute(tags=['chats'])


@router.websocket('{chat_oid}')
async def messages_handlers(chat_oid: str, websocket: WebSocket):
    await websocket.accept()

    