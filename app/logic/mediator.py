from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from domain.events.base import BaseEvent
from logic.commands.base import CT, CR, BaseCommand, CommandHandler
from logic.events.base import EventHandler, ER, ET
from logic.exceptions.mediator import EventHandlersNotRegisteredException, CommandHandlersNotRegisteredException


@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]):
        self.events_map[event.__class__].extend(event_handlers)

    def register_commands(self, command: CT, command_handlers: Iterable[EventHandler[CT, CR]]):
        self.commands_map[command.__class__].extend(command_handlers)

    async def handle_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.event_map.get(event_type)

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = event.__class__
        handlers = self.event_map.get(command_type)

        if not handlers:
            raise CommandHandlersNotRegisteredException(event_type)

        return [await handler.handle(command) for handler in handlers]
