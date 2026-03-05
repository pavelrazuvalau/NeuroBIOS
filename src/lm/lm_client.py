import random


def prompt_model(context):
    responses = [
        "HIGH", 
        "I am absolutely sure, it's HIGH.", 
        "  LOW \n", 
        "The HIGH metric is MEDIUM.",
        "BANANA"
    ]

    return random.choice(responses)