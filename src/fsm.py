class StateMachine:

    def __init__(self, allowed_states):
        self.allowed_states = allowed_states
        self.state = self.allowed_states[0]

    def get_state(self):
        print(f"Current State: {self.state}")

    def set_state(self, new_state):
        if self.__is_transition_permitted(new_state):
            self.state = new_state
        else:
            print(f"Failed to set new state {new_state}: expected one in the list after {self.state}: {self.allowed_states}")

    def __is_transition_permitted(self, new_state):
        if new_state not in self.allowed_states:
            return False

        current_index = self.allowed_states.index(self.state)
        new_index = self.allowed_states.index(new_state)

        return new_index - current_index == 1