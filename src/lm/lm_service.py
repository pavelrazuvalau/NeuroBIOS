import json

from lm.lm_client import ask_model
from lm.system_prompts import analyze_confidence_system_prompt

def predict_metric(context, criteria):
    response = ask_model(analyze_confidence_system_prompt, json.dumps(context), {
        "temperature": 0,
        "reasoning": "off"
    })
    return sanitize_metric_response(response, criteria)

def sanitize_metric_response(response, criteria):
    extracted_word = None
    num_of_occurrences = 0

    print(f"response {response}")
    print(f"criteria {criteria}")

    for word in criteria:
        if word in response:
            extracted_word = word
            num_of_occurrences += 1

    print(f"extracted_word {extracted_word}")
    print(f"num_of_occurrences {num_of_occurrences}")
    
    return extracted_word if num_of_occurrences == 1 else None