from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from domain.events.base import BaseEvent
from infra.message_brokers.base import BaseMessageBroker
from infra.websockets.managers import BaseConectionManager

ET = TypeVar('ET', bound=BaseEvent)
ER = TypeVar('ER', bound=Any)


@dataclass
class IntegrationEvent(BaseEvent, ABC):
    ...    


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    message_broker: BaseMessageBroker
    connection_manager: BaseConectionManager
    broker_topic: str | None = None

    @abstractmethod
    def handle(self, event: ET) -> ER:
        ...