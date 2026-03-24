from core.constants import MessageRole


class ContextManager:
    def __init__(self, history: list | None = None):
        self._history = history or []

    def get_history_with_system_prompt(self, system_prompt: str):
        formatted_system_message = self._format_message(MessageRole.SYSTEM, system_prompt)
        return [formatted_system_message, *self._history]

    def get_messages_history(self):
        return list(self._history)

    def append_message(self, role: MessageRole, content: str, **kwargs):
        formatted_message = self._format_message(role, content, **kwargs)
        self._history.append(formatted_message)

    def append_messages_list(self, message):
        self._history.extend(message)

    def _format_message(self, role: MessageRole, content: str, **kwargs):
        return {"role": role.value, "content": content, **kwargs}
