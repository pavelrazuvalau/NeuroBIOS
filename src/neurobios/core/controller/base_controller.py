import inspect
from abc import ABC, abstractmethod
from typing import Any, Generator

from neurobios.core.models import (
    ControllerState,
    AgentStepResult,
    AgentStreamingEvent,
)


class BaseController(ABC):
    def run(
        self, state: ControllerState
    ) -> Generator[AgentStreamingEvent, None, AgentStepResult] | AgentStepResult:
        response = self._execute(state)
        result = (yield from response) if inspect.isgenerator(response) else response
        return self._build_response(result)

    @abstractmethod
    def _execute(
        self, state: ControllerState
    ) -> Generator[AgentStreamingEvent, None, Any] | Any: ...

    @abstractmethod
    def _build_response(self, result: Any) -> AgentStepResult: ...
