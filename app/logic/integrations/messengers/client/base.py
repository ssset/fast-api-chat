from abc import ABC, abstractmethod
from dataclasses import dataclass

from logic.integrations.messengers.dots import Notification


@dataclass
class BaseNotificationClient(ABC):

    @abstractmethod
    async def _format_notification(self, notification: Notification) -> str:
        ...

    @abstractmethod
    async def send(self, notifications: Notification):
        ...