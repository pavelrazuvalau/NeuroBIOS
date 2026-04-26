import inspect

from neurobios.core.context_manager import ContextManager
from neurobios.core.controller.base_controller import BaseController


class BaseLMController(BaseController):
    def __init__(self, dependencies, tools_contract=None):
        super().__init__(dependencies)
        self._tools_contract = tools_contract
        self._lm_service = self._dependencies.get("lm_service")

    def _build_system_prompt(self, state, context):
        pass

    def _execute(self, state, context):
        system_prompt = self._build_system_prompt(state, context)

        context_manager = ContextManager(context)
        context_to_send = (
            context_manager.get_history_with_system_prompt(system_prompt)
            if system_prompt
            else context_manager.get_messages_history()
        )

        response = self._lm_service.send_messages(
            context_to_send, tools=self._tools_contract
        )
        return (yield from response) if inspect.isgenerator(response) else response
