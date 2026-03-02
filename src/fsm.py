class StateMachine:
    IDLE_STATE = "IDLE"
    END_STATE = "END"
    ESCALATE_STATE = "ESCALATE"
    STOP_STATES = (END_STATE, ESCALATE_STATE)

    def __init__(self, flow_actions, system_actions = None):
        self.state = self.IDLE_STATE
        self.is_flow_running = False

        self.__flow_states = tuple()
        self.__system_actions = system_actions or {}
        self.__flow_actions = flow_actions
        self.__actions = self.__system_actions | self.__flow_actions
        self.__is_unhandled_failure_occured = False

    def set_flow(self, flow_states, context = None):
        if not flow_states:
            print("Error: flow cannot be empty")
            return

        self.context = context if context is not None else {}
        self.state = flow_states[0]
        self.is_flow_running = True

        self.__flow_states = flow_states

    def get_state(self):
        return { "state": self.state, "context": self.context }

    def go_to_next_state(self):
        if not self.is_flow_running:
            print(f"The flow is stopped at {self.state} state")
            return
        
        if self.__is_unhandled_failure_occured:
            self.__is_unhandled_failure_occured = False
            self.__set_state(self.ESCALATE_STATE)
            return
        
        if self.__has_reached_stop_state():
            self.is_flow_running = False
            return
        
        next_state_index = self.__get_state_index(self.state) + 1
        is_next_step_available = next_state_index < len(self.__flow_states)
        next_state = self.__flow_states[next_state_index] if is_next_step_available else self.END_STATE

        self.__set_state(next_state)

    def execute_state(self):
        current_action = self.__actions.get(self.state)

        if current_action:
            response = current_action(self.context)
            context_update = response.get("context_update", {})
            self.context |= context_update

            is_success = response.get("success", True)
            self.__is_unhandled_failure_occured = not is_success

            return response.get("result")
        else:
            print(f"No action found for state {self.state}")
            return None
        
    def __set_state(self, state):
        if self.__is_transition_permitted(state):
            self.state = state
        else:
            print(f"Failed to set new state {state}: expected one in the tuple after {self.state}: {self.__flow_states}")

    def __is_transition_permitted(self, state):
        if state in self.STOP_STATES:
            return True
        
        if state not in self.__flow_states:
            return False

        current_index = self.__get_state_index(self.state)
        new_index = self.__get_state_index(state)

        return new_index - current_index == 1
    
    def __get_state_index(self, state):
        return self.__flow_states.index(state)
        
    def __has_reached_stop_state(self):
        return self.state in self.STOP_STATES