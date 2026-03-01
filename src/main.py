from fsm import StateMachine


def main():
    fsm = StateMachine(("IDLE", "WORKING", "VERIFYING", "END"))
    fsm.get_state()
    fsm.set_state("WORKING")
    fsm.get_state()
    fsm.set_state("FLYING_PIG")
    fsm.get_state()
    fsm.set_state("END")
    fsm.get_state()
 
if __name__ == "__main__":
    main()