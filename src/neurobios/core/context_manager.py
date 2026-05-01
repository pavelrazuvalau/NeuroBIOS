from neurobios.core.constants import MessageRole
from neurobios.lm.models import Message


class ContextManager:
    def __init__(self, history: list[Message] | None = None):
        self._history: list[Message] = history or []

    def get_history_with_system_prompt(self, system_prompt: str) -> list[Message]:
        system_message = Message(role=MessageRole.SYSTEM.value, content=system_prompt)
        return [system_message, *self._history]

    def get_messages_history(self) -> list[Message]:
        return list(self._history)

    def append_message(self, message: Message) -> None:
        self._history.append(message)

    def append_messages_list(self, messages: list[Message]) -> None:
        self._history.extend(messages)
