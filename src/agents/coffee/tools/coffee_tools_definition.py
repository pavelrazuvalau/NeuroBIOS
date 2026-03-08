from agents.coffee.coffee_constants import CoffeeState
from lm.lm_constants import CONFIDENCE_LEVELS
from lm.lm_service import predict_metric


def grind_coffee(context):
    return {
        "result": "Grinding coffee...",
        "context_update": {
            "coffee_ground": context.get("seeds_available"),
            "seeds_available": False,
        },
    }


def pour_water(context):
    return {
        "success": context.get("coffee_ground"),
        "result": (
            "Pouring water..."
            if context.get("coffee_ground")
            else "Oops... Looks like we're just pouring water: out of coffee!"
        ),
    }


def pour_milk(context):
    return {
        "result": "Pouring milk...",
    }


def analyze_quality(context):
    confidence_level = predict_metric(context, CONFIDENCE_LEVELS)

    payload = {
        "result": "Analyzing the quality...",
        "context_update": {"confidence": confidence_level},
        "success": confidence_level is not None,
    }

    next_step_prediction = (
        {"next_state_override": CoffeeState.GRIND_COFFEE}
        if confidence_level == "LOW"
        else {}
    )

    return payload | next_step_prediction


def serve_drink(context):
    return {"result": "Enjoy your drink!"}


def end_flow(context):
    return {"result": "EOF"}


def escalate_flow(context):
    return {
        "result": f"Warning! Flow is interrupted. User attention required: {context}"
    }
