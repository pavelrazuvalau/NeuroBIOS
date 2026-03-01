class StateMachine:
    IDLE_STATE = "IDLE"

    def __init__(self, state_actions):
        self.state_actions = state_actions
        self.allowed_states = tuple()
        self.state = self.IDLE_STATE

    def set_flow(self, allowed_states):
        if not allowed_states:
            print("Error: flow cannot be empty")
            return

        self.allowed_states = allowed_states
        self.state = self.allowed_states[0]

    def get_state(self):
        print(f"Current State: {self.state}")

    def set_next_state(self):
        if not self.is_running():
            print("StateMachine reached the end of chain")
            return
        
        next_state_index = self.__get_state_index(self.state) + 1
        is_next_step_available = next_state_index < len(self.allowed_states)
        next_state = self.allowed_states[next_state_index] if is_next_step_available else self.IDLE_STATE

        self.set_state(next_state)
    
    def is_running(self):
        return self.state != self.IDLE_STATE
       
    def set_state(self, state):
        if self.__is_transition_permitted(state):
            self.state = state
        else:
            print(f"Failed to set new state {state}: expected one in the tuple after {self.state}: {self.allowed_states}")

    def execute_state(self):
        current_action = self.state_actions.get(self.state)

        if current_action:
            return current_action()
        else:
            print(f"No action found for state {self.state}")
            return None
    
    def __get_state_index(self, state):
        return self.allowed_states.index(state)

    def __is_transition_permitted(self, state):
        if state == self.IDLE_STATE:
            return True
        
        if state not in self.allowed_states:
            return False

        current_index = self.__get_state_index(self.state)
        new_index = self.__get_state_index(state)

        return new_index - current_index == 1