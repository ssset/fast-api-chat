from dataclasses import dataclass, field
from domain.values.messages import Text, Title
from domain.entities.base import BaseEntity


@dataclass
class Message(BaseEntity):
    text: Text
    __hash__ = BaseEntity.__hash__


@dataclass
class Chat(BaseEntity):
    title: Title
    __hash__ = BaseEntity.__hash__
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True
    )

    def add_message(self, message: Message):
        self.messages.add(message)
