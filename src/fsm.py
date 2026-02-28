class StateMachine:
    def __init__(self): # IDLE, WORKING, ...,  END
        self.state = "IDLE"

    def get_state(self):
        print(f"Current State: {self.state}")

    def set_state(self, state):
        self.state = state