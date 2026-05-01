import inspect
from abc import abstractmethod
from typing import Generator

from neurobios.core.context_manager import ContextManager
from neurobios.core.controller.base_controller import BaseController
from neurobios.core.models import (
    AgentStepResult,
    ControllerState,
    AgentStreamingEvent,
)
from neurobios.lm.models import Message, LMRequestConfig, ToolSchema
from neurobios.core.deps import CoreDependencies
from neurobios.lm.lm_service import LMService


class BaseLMController(BaseController):
    _tools_contract: list[ToolSchema] | None
    _lm_service: LMService

    def __init__(
        self,
        dependencies: CoreDependencies,
        tools_contract: list[ToolSchema] | None = None,
    ):
        super().__init__()
        self._tools_contract = tools_contract
        self._lm_service = dependencies.lm_service

    def _build_system_prompt(self, state: ControllerState) -> str:
        return ""

    def _execute(
        self, state: ControllerState
    ) -> Generator[AgentStreamingEvent, None, Message] | Message:
        system_prompt = self._build_system_prompt(state)

        context_manager = ContextManager(state.context)
        context_to_send = (
            context_manager.get_history_with_system_prompt(system_prompt)
            if system_prompt
            else context_manager.get_messages_history()
        )

        request_config = LMRequestConfig(tools=self._tools_contract)
        response = self._lm_service.send_messages(context_to_send, request_config)

        return (yield from response) if inspect.isgenerator(response) else response

    @abstractmethod
    def _build_response(self, model_response: Message) -> AgentStepResult:
        ...
