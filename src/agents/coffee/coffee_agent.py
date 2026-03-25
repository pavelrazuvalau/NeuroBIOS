from agents.coffee.coffee_config import (
    COFFEE_FLOW,
    COFFEE_FLOW_ACTIONS,
    COFFEE_SYSTEM_STATE_ACTIONS,
)
from core.constants import MessageRole
from core.fsm import StateMachine
from core.utils import deep_merge
from core.context_manager import ContextManager


class CoffeeAgent:
    def __init__(self):
        self._fsm = StateMachine(COFFEE_FLOW_ACTIONS, COFFEE_SYSTEM_STATE_ACTIONS)
        self._context_manager = ContextManager()
        self._agent_state = {}

    def run(self, user_prompt):
        self._context_manager.append_message(MessageRole.USER, user_prompt)

        self._fsm.set_flow(COFFEE_FLOW)
        self._run_fsm()

    def _run_fsm(self):
        while self._fsm.is_flow_running:
            current_context = self._context_manager.get_messages_history()

            step_response = (
                self._fsm.execute_state(
                    context=current_context, state=self._agent_state
                )
                or {}
            )

            step_messages_delta = step_response.get("context_delta", {})
            step_state_delta = step_response.get("state_delta", {})

            self._context_manager.append_messages_list(step_messages_delta)
            self._update_agent_state(step_state_delta)

            self._fsm.go_to_next_state()

    def _update_agent_state(self, delta):
        deep_merge(self._agent_state, delta)
