from punq import Container

from fastapi import Depends
from fastapi.websockets import WebSocket
from fastapi import Depends, WebSocketDisconnect
from fastapi.routing import APIRouter
from infra.websockets.managers import BaseConectionManager

from infra.websockets.managers import BaseConectionManager
from logic.init import init_container

router = APIRouter(tags=['chats'])


@router.websocket('/{chat_oid}/')
async def websocket_endpoint(
    chat_oid: str,
    websocket: WebSocket,
    container: Container = Depends(init_container)
    ):
    connection_manager: BaseConectionManager = container.resolve(BaseConectionManager)
    await connection_manager.accept_connection(websocket=websocket, key=str(chat_oid))

    await websocket.send_text("You are now connected!")


    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:

        await connection_manager.remove_connection(websocket=websocket, key=chat_oid)