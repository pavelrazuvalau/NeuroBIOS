class StateMachine:
    ALLOWED_STATES = ("IDLE", "WORKING", "END")

    def __init__(self):
        self.state = self.ALLOWED_STATES[0]

    def get_state(self):
        print(f"Current State: {self.state}")

    def set_state(self, state):
        if state in self.ALLOWED_STATES:
            self.state = state
        else:
            print(f"Wrong stage: expected one in the list: {self.ALLOWED_STATES}")