from lm.lm_constants import MessageRole


class ContextStore:
    def __init__(self):
        self._history = []

    def get_history(self):
        return list(self._history)
    
    def clear_history(self):
        system_message = self.get_system_message()
        self._history = [system_message] if system_message else []

    def get_system_message(self):
        return (
            self._history[0]
            if self._history
            and self._is_message_role_equal(self._history[0], MessageRole.SYSTEM)
            else None
        )

    def get_last_message(self):
        return self._history[-1] if self._history else None

    def set_system_prompt(self, system_prompt: str):
        formatted_message = self._format_message(MessageRole.SYSTEM, system_prompt)
        first_history_message = self._history[0] if self._history else {}

        if self._is_message_role_equal(first_history_message, MessageRole.SYSTEM):
            self._history[0] = formatted_message
        else:
            self._history.insert(0, formatted_message)

    def append_message(self, role: MessageRole, content: str, **kwargs):
        formatted_message = self._format_message(role, content, **kwargs)
        self._history.append(formatted_message)

    def _format_message(self, role: MessageRole, content: str, **kwargs):
        return {"role": role.value, "content": content, **kwargs}

    def _is_message_role_equal(self, message: dict, role: MessageRole):
        return message.get("role") == role.value
