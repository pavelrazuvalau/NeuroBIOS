from fsm import StateMachine
from flow_predictor import predict_confidence

# temp functions for coffee machine to set up fsm callbacks
def grind_coffee(context):
    return {
        "result": "Grinding coffee...",
        "context_update": { "coffee_ground": context.get("seeds_available"), "seeds_available": False }
    }

def pour_water(context):
    return {
        "success": context.get("coffee_ground"),
        "result": "Pouring water..." if context.get("coffee_ground") else "Oops... Looks like we're just pouring water: out of coffee!",
    }

def pour_milk(context):
    return {
        "result": "Pouring milk...",
    }

def serve_drink(context):
    confidence_level = predict_confidence(context)

    payload = {
        "result": "Enjoy your drink!",
        "context_update": { "confidence": confidence_level }
    }
    next_step_prediction = { "next_state_override": "GRIND_COFFEE" } if confidence_level == "LOW" else {}

    return payload | next_step_prediction

def end_flow(context):
    return {
        "result": "EOF"
    }

def escalate_flow(context):
    return {
        "result": f"Warning! Flow is interrupted. User attention required: {context}"
    }

def run_fsm(fsm):
    while fsm.is_flow_running:
        step_result = fsm.execute_state()
        print(f"Current step: {fsm.get_state()}")
        print(f"Current result: {step_result}")

        fsm.go_to_next_state()

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

    system_actions = {
        "END": end_flow,
        "ESCALATE": escalate_flow
    }

    coffee_machine = StateMachine(coffee_state_actions, system_actions)

    print("Making Capucino:")

    coffee_machine.set_flow(coffee_machine_menu["capucino"], { "seeds_available": False })
    run_fsm(coffee_machine)

    print("\n")

    print("Making Flat White:")
    coffee_machine.set_flow(coffee_machine_menu["flat_white"], { "seeds_available": True })
    run_fsm(coffee_machine)
 
if __name__ == "__main__":
    main()