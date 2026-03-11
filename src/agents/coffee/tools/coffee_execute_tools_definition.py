def grind_coffee(context):
    state = context.get("state", {})

    return {
        "result": "Grinding coffee...",
        "context_delta": {
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
        "context_delta": {
            "messages": [{"role": "assistant", "content": "I poured watter"}],
        },
    }


def pour_milk(context):
    return {
        "result": "Pouring milk...",
        "context_delta": {
            "messages": [{"role": "assistant", "content": "I poured milk"}],
        },
    }


def serve_drink(context):
    return {
        "result": "Enjoy your drink!",
        "context_delta": {
            "messages": [
                {
                    "role": "assistant",
                    "content": "I successfully served the beverage to the user",
                }
            ],
        },
    }
