from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from logic.commands.base import BaseCommand


@dataclass(frozen=True)
class BaseQuery(ABC):
    ...


QT = TypeVar('CT', bound=BaseCommand)
QR = TypeVar('CR', bound=Any)


@dataclass(frozen=True)
class BaseQueryHandler(ABC, Generic[QT, QR]):
    @abstractmethod
    async def handle(self, query: QT) -> QR:
        ...