import inspect
from enum import Enum
from typing import Any, Callable, Generator

from neurobios.core.constants import MessageRole, StreamingEvent
from neurobios.core.fsm import StateMachine
from neurobios.core.utils import deep_merge
from neurobios.core.context_manager import ContextManager
from neurobios.core.controller.base_controller import BaseController
from neurobios.core.deps import CoreConfig, CoreDependencies
from neurobios.core.models import (
    ControllerState,
    AgentStepResult,
    AgentStreamingEvent,
)
from neurobios.lm.models import Message


class AgentCore:
    _fsm: StateMachine
    _context_manager: ContextManager
    _agent_state: dict[str, Any]

    def __init__(
        self,
        *,
        states_config: dict[Enum, BaseController],
        core_config: CoreConfig,
        dependencies: CoreDependencies | None = None,
    ):
        if dependencies is None:
            dependencies = CoreDependencies()

        if not isinstance(dependencies, CoreDependencies):
            raise TypeError("Dependencies must inherit from CoreDependencies")

        dependencies._init_core_dependencies(core_config)

        self._fsm = StateMachine(
            self._init_fsm_state_actions(states_config, dependencies)
        )
        self._context_manager = ContextManager()
        self._agent_state = {}

    def run(
        self, flow: tuple, user_prompt: str
    ) -> Generator[AgentStreamingEvent, None, None]:
        self._context_manager.append_message(
            Message(role=MessageRole.USER.value, content=user_prompt)
        )

        self._fsm.set_flow(flow)
        yield from self._run_fsm()

    def _init_fsm_state_actions(
        self,
        states_config: dict[Enum, BaseController],
        dependencies: CoreDependencies,
    ) -> dict[Enum, Callable]:
        fsm_state_actions = {}

        for fsm_state, controller in states_config.items():
            controller_instance = controller(dependencies)
            fsm_state_actions[fsm_state] = controller_instance.run

        return fsm_state_actions

    def _run_fsm(self) -> Generator[AgentStreamingEvent, None, None]:
        while self._fsm.is_flow_running:
            current_context = self._context_manager.get_messages_history()

            yield AgentStreamingEvent(
                event=StreamingEvent.EXECUTING_NEXT_STEP, payload={}
            )

            controller_state = ControllerState(
                context=current_context, agent_state=self._agent_state
            )
            step_response = self._fsm.execute_state(controller_state)

            step_result: AgentStepResult = (
                (yield from step_response)
                if inspect.isgenerator(step_response)
                else step_response
            )

            if step_result:
                step_messages_delta = step_result.context_delta or []
                self._context_manager.append_messages_list(step_messages_delta)

                step_state_delta = step_result.state_delta or {}
                self._update_agent_state(step_state_delta)

            self._fsm.go_to_next_state()

        yield AgentStreamingEvent(event=StreamingEvent.RESPONSE_END, payload={})

    def _update_agent_state(self, delta: dict[str, Any]) -> None:
        deep_merge(self._agent_state, delta)
