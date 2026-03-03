import random

def predict_confidence(context):
    # call LLM
    return random.choice(["HIGH", "MEDIUM", "LOW"])