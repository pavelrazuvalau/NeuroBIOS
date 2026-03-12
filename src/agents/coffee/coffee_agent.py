from agents.coffee.coffee_config import (
    COFFEE_FLOW,
    COFFEE_FLOW_ACTIONS,
    COFFEE_SYSTEM_STATE_ACTIONS,
)
from core.fsm import StateMachine
from core.utils import deep_merge


class CoffeeAgent:
    def __init__(self):
        self._fsm = StateMachine(COFFEE_FLOW_ACTIONS, COFFEE_SYSTEM_STATE_ACTIONS)
        self._context_history = {}

    def run(self, user_prompt):
        self._set_user_prompt(user_prompt)

        self._fsm.set_flow(COFFEE_FLOW)
        self._run_fsm()

    def _run_fsm(self):
        while self._fsm.is_flow_running:
            print(f"\n[Current step]: {self._fsm.state.name}")
            step_response = self._fsm.execute_state(self._context_history)
            # print(f"[Current step response]: {step_response}")

            # step_result = step_response.get("result", None)
            step_context_delta = step_response.get("context_delta", {})
            self._update_context_history(step_context_delta)

            self._fsm.go_to_next_state()

    def _set_user_prompt(self, user_prompt):
        # TODO: move context management to a new entity (e.g. ContextManager)
        user_message_delta = {"messages": [{"role": "user", "content": user_prompt}]}
        self._update_context_history(user_message_delta)

    def _update_context_history(self, delta):
        deep_merge(self._context_history, delta)
