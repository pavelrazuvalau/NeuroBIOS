from fsm import StateMachine

# temp functions for coffee machine to set up fsm callbacks
def grind_coffee(context):
    return {
        "result": "Grinding coffee...",
        "context_update": { "coffee_ground": context.get("seeds_available"), "seeds_available": False }
    }

def pour_water(context):
    return {
        "result": "Pouring water..." if context.get("coffee_ground") else "Oops... Looks like we're just pouring water: out of coffee!",
    }

def pour_milk(context):
    return {
        "result": "Pouring milk...",
    }

def serve_drink(context):
    return {
        "result": "Enjoy your drink",
    }

def run_fsm(fsm):
    while fsm.is_running():
        step_result = fsm.execute_state()
        print(f"Current step: {fsm.get_state()}")
        print(f"Current result: {step_result}")

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

    coffee_machine.set_flow(coffee_machine_menu["capucino"], { "seeds_available": True })
    run_fsm(coffee_machine)

    print("\n")

    print("Testing edge case:")
    coffee_machine.set_flow(())
    run_fsm(coffee_machine)

    print("\n")

    print("Making Flat White:")
    coffee_machine.set_flow(coffee_machine_menu["flat_white"], { "seeds_available": False })
    run_fsm(coffee_machine)
 
if __name__ == "__main__":
    main()