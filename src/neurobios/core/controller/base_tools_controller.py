from abc import abstractmethod
from typing import Callable, Generator

from neurobios.core.controller.base_controller import BaseController
from neurobios.core.constants import StreamingEvent, MessageRole
from neurobios.core.models import (
    AgentStepResult,
    ControllerState,
    AgentStreamingEvent,
)
from neurobios.lm.models import Message
from neurobios.core.deps import CoreDependencies


class BaseToolsController(BaseController):
    _tools_registry: dict[str, Callable[[str], str]]

    def __init__(
        self,
        tools_registry: dict[str, Callable[[str], str]] | None = None,
    ):
        super().__init__()
        self._tools_registry = tools_registry or {}

    def _execute(
        self, state: ControllerState
    ) -> Generator[AgentStreamingEvent, None, list[Message]]:
        last_message = state.context[-1] if state.context else None
        tool_responses: list[Message] = []

        if last_message and last_message.tool_calls:
            for tool_call in last_message.tool_calls:
                tool_call_id = tool_call.id
                function_name = tool_call.function.name
                function_arguments = tool_call.function.arguments

                action_function = self._tools_registry.get(function_name, None)

                if action_function:
                    function_result = action_function(function_arguments)
                    current_tool_response = Message(
                        role=MessageRole.TOOL.value,
                        tool_call_id=tool_call_id,
                        name=function_name,
                        content=str(function_result),
                    )

                    tool_responses.append(current_tool_response)

                    yield AgentStreamingEvent(
                        event=StreamingEvent.TOOL_CALL,
                        payload=current_tool_response.model_dump(),
                    )

        return tool_responses

    @abstractmethod
    def _build_response(self, tool_responses: list[Message]) -> AgentStepResult:
        ...
