import inspect

from core.context_manager import ContextManager
from lm.lm_service import send_messages
from core.controller.base_controller import BaseController


class BaseLMController(BaseController):
    def __init__(self, **config):
        super().__init__(**config)
        self._system_prompt = self._config.get("system_prompt", None)
        self._tools_contract = self._config.get("tools_contract", None)
        self._are_tools_enabled = True

    def _build_system_prompt(self, state, context):
        return self._system_prompt

    def _execute(self, state, context):
        system_prompt = self._build_system_prompt(state, context)
        tools_contract = self._tools_contract if self._are_tools_enabled else None

        context_manager = ContextManager(context)
        context_to_send = (
            context_manager.get_history_with_system_prompt(system_prompt)
            if system_prompt
            else context_manager.get_messages_history()
        )

        response = send_messages(context_to_send, tools=tools_contract)
        return (yield from response) if inspect.isgenerator(response) else response
