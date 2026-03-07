from core.constants import SYSTEM_STOP_STATES, SystemState


class StateMachine:
    def __init__(self, flow_actions, system_actions = None):
        self.state = SystemState.IDLE
        self.context = {}
        self.is_flow_running = False

        self._flow_states = tuple()

        self._system_actions = system_actions or {}
        self._flow_actions = flow_actions
        self._actions = self._system_actions | self._flow_actions

        self._is_unhandled_failure_occurred = False
        self._next_state_override = None

    def set_flow(self, flow_states, context = None):
        if not flow_states:
            raise ValueError("Error: Flow cannot be empty")

        self.state = flow_states[0]
        self.context = context if context else {}
        self.is_flow_running = True

        self._flow_states = flow_states

    def get_state(self):
        return {"state": self.state.name, "context": self.context}

    def go_to_next_state(self):
        if self._next_state_override:
            self._set_state(self._next_state_override, True)
            self._next_state_override = None
            self.is_flow_running = True
            return

        if not self.is_flow_running:
            print(f"The flow is stopped at {self.state} state")
            return
        
        if self._is_unhandled_failure_occurred:
            self._set_state(SystemState.ESCALATE)
            self._is_unhandled_failure_occurred = False
            return
        
        if self._has_reached_stop_state():
            self.is_flow_running = False
            return
        
        next_state_index = self._get_state_index(self.state) + 1
        is_next_step_available = next_state_index < len(self._flow_states)
        next_state = self._flow_states[next_state_index] if is_next_step_available else SystemState.END

        self._set_state(next_state)

    def execute_state(self):
        current_action = self._actions.get(self.state)

        if current_action:
            response = current_action(self.context) or {}

            context_update = response.get("context_update", {})
            self.context |= context_update

            self._next_state_override = response.get("next_state_override", None)

            is_success = response.get("success", True)
            self._is_unhandled_failure_occurred = not is_success

            return response.get("result")
        else:
            print(f"No action found for state {self.state}")
            return None
        
    def _set_state(self, state, is_override = False):
        if self._is_transition_permitted(state, is_override):
            self.state = state
        else:
            print(f"Failed to set new state {state}: expected one in the tuple after {self.state}: {self._flow_states}")

    def _is_transition_permitted(self, state, is_override):
        if is_override or state in SYSTEM_STOP_STATES:
            return True
        
        if state not in self._flow_states:
            return False

        current_index = self._get_state_index(self.state)
        new_index = self._get_state_index(state)

        return new_index - current_index == 1
    
    def _get_state_index(self, state):
        return self._flow_states.index(state)
        
    def _has_reached_stop_state(self):
        return self.state in SYSTEM_STOP_STATES