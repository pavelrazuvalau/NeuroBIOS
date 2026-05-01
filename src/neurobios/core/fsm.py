import inspect
from enum import Enum
from typing import Any, Callable, Generator

from neurobios.core.constants import SystemState


class StateMachine:
    state: SystemState | Enum
    is_flow_running: bool

    _flow_states: tuple[Enum]
    _state_actions: dict[Enum, Callable]
    _next_state: Enum | None

    def __init__(self, state_actions: dict[Enum, Callable]):
        self.state = SystemState.IDLE
        self.is_flow_running = False

        self._flow_states = tuple()
        self._state_actions = state_actions
        self._next_state = None

    def set_flow(self, flow_states: tuple[Enum]) -> None:
        if not flow_states:
            raise ValueError("Error: Flow cannot be empty")

        self.state = flow_states[0]
        self.is_flow_running = True

        self._flow_states = flow_states

    def go_to_next_state(self) -> None:
        if self._next_state:
            self._set_state(self._next_state, True)
            self._next_state = None
            self.is_flow_running = True
            return

        if not self.is_flow_running:
            print(f"The flow is stopped at {self.state} state")
            return

        if self._has_reached_stop_state():
            self.is_flow_running = False
            return

        next_state_index = self._get_state_index(self.state) + 1
        is_next_step_available = next_state_index < len(self._flow_states)
        next_state = (
            self._flow_states[next_state_index]
            if is_next_step_available
            else SystemState.END
        )

        self._set_state(next_state)

    def execute_state(self, state: Any) -> Generator[Any, None, Any]:
        current_action = self._state_actions.get(self.state)

        if current_action:
            response = current_action(state)
            result = (
                (yield from response) if inspect.isgenerator(response) else response
            )

            self._next_state = result.next_state

            return result
        else:
            print(f"No action found for state {self.state}")
            return None

    def _set_state(self, state: Enum, is_override: bool = False) -> None:
        if self._is_transition_permitted(state, is_override):
            self.state = state
        else:
            print(
                f"Failed to set new state {state}: expected one in the tuple after {self.state}: {self._flow_states}"
            )

    def _is_transition_permitted(self, state: Enum, is_override: bool) -> bool:
        if is_override or state == SystemState.END:
            return True

        if state not in self._flow_states:
            return False

        current_index = self._get_state_index(self.state)
        new_index = self._get_state_index(state)

        return new_index - current_index == 1

    def _get_state_index(self, state) -> int:
        return self._flow_states.index(state)

    def _has_reached_stop_state(self) -> bool:
        return self.state == SystemState.END
