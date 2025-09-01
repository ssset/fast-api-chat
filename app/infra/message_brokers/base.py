from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncIterator


@dataclass
class BaseMessageBroker(ABC):

    @abstractmethod
    async def start(self):
        ...
    
    @abstractmethod
    async def close(self):
        ...


    @abstractmethod
    async def send_message(self, topic: str, key: str, value: bytes, headers: list[tuple]):
        ...

    @abstractmethod
    async def start_consuming(self, topic: str) -> AsyncIterator[dict]:
        ...

    @abstractmethod
    async def stop_consuming(self):
        ...
    