def grind_coffee(context):
    return {
        "result": "Grinding coffee...",
        "context_delta": {
            "messages": [{"role": "assistant", "content": "I grinded coffee"}],
        },
    }


def pour_water(context):
    return {
        "result": "Pouring water...",
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
