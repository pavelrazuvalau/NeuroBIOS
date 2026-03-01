from fsm import StateMachine

# temp functions for coffee machine to set up fsm callbacks
def grind_coffee():
    return "Grinding coffee..."

def pour_water():
    return "Pouring water..."

def pour_milk():
    return "Pouring milk..."

def serve_drink():
    return "Enjoy your drink"

def run_fsm(fsm):
    while fsm.is_running():
        step_result = fsm.execute_state()
        print(step_result)

        fsm.set_next_state()

def main():
    coffee_machine_menu = {
        "black_coffee": ("GRIND_COFFEE", "POUR_WATER", "SERVE"),
        "capucino": ("POUR_MILK", "GRIND_COFFEE", "POUR_WATER", "SERVE"),
        "flat_white": ("GRIND_COFFEE", "POUR_WATER", "POUR_MILK", "SERVE")
    }

    coffee_state_actions = {
        "GRIND_COFFEE": grind_coffee,
        "POUR_WATER": pour_water,
        "POUR_MILK": pour_milk,
        "SERVE": serve_drink
    }

    coffee_machine = StateMachine(coffee_state_actions)

    print("Making Capucino:")

    coffee_machine.set_flow(coffee_machine_menu["capucino"])
    run_fsm(coffee_machine)

    print("\n")

    print("Testing edge case:")
    coffee_machine.set_flow(())
    run_fsm(coffee_machine)

    print("\n")

    print("Making Flat White:")
    coffee_machine.set_flow(coffee_machine_menu["flat_white"])
    run_fsm(coffee_machine)
 
if __name__ == "__main__":
    main()