from agents.coffee.coffee_config import (
    COFFEE_FLOW_ACTIONS,
    COFFEE_SYSTEM_STATE_ACTIONS,
)
from core.fsm import StateMachine


class CoffeeAgent:
    def __init__(self):
        self._fsm = StateMachine(COFFEE_FLOW_ACTIONS, COFFEE_SYSTEM_STATE_ACTIONS)

    def run(self, flow, context):
        self._fsm.set_flow(flow, context)
        self._run_fsm()

    def _run_fsm(self):
        while self._fsm.is_flow_running:
            print(f"\nCurrent step: {self._fsm.get_state()["state"]}")
            step_result = self._fsm.execute_state()
            print(f"Current result: {step_result}")

            self._fsm.go_to_next_state()
