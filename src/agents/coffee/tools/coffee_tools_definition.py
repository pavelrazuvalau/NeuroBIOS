from agents.coffee.coffee_constants import CoffeeState
from lm.lm_constants import CONFIDENCE_LEVELS
from lm.lm_service import predict_metric


def grind_coffee(context):
    state = context.get("state", {})

    return {
        "result": "Grinding coffee...",
        "context_update": {
            "messages": [{"role": "assistant", "content": "I grinded coffee"}],
            "state": {
                "coffee_ground": state.get("seeds_available", False),
                "seeds_available": False,
            },
        },
    }


def pour_water(context):
    state = context.get("state", {})
    is_success = state.get("coffee_ground", False)

    return {
        "success": is_success,
        "result": (
            "Pouring water..."
            if is_success
            else "Oops... Looks like we're just pouring water: out of coffee!"
        ),
        "context_update": {
            "messages": [{"role": "assistant", "content": "I poured watter"}],
        },
    }


def pour_milk(context):
    return {
        "result": "Pouring milk...",
        "context_update": {
            "messages": [{"role": "assistant", "content": "I poured milk"}],
        },
    }


def analyze_quality(context):
    confidence_level = predict_metric(context, CONFIDENCE_LEVELS)

    payload = {
        "result": "Analyzing the quality...",
        "context_update": {"state": {"confidence": confidence_level}},
        "success": confidence_level is not None,
        "context_update": {
            "messages": [
                {
                    "role": "assistant",
                    "content": f"I analyzed the quality. The quality is {confidence_level}",
                }
            ],
        },
    }

    next_step_prediction = (
        {"next_state_override": CoffeeState.GRIND_COFFEE}
        if confidence_level == "LOW"
        else {}
    )

    return payload | next_step_prediction


def serve_drink(context):
    return {
        "result": "Enjoy your drink!",
        "context_update": {
            "messages": [
                {
                    "role": "assistant",
                    "content": "I successfully served the beverage to the user",
                }
            ],
        },
    }


def end_flow(context):
    return {"result": "EOF"}


def escalate_flow(context):
    return {
        "result": f"Warning! Flow is interrupted. User attention required: {context}"
    }
