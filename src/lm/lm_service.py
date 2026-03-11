import json

from lm.lm_client import prompt_model
from lm.system_prompts import analyze_confidence_system_prompt


def send_messages(system_prompt, messages_history):
    messages_to_send = [
        {"role": "system", "content": system_prompt},
        *messages_history,
    ]
    return prompt_model(messages_to_send)


def predict_metric(context, criteria):
    response = send_messages(
        analyze_confidence_system_prompt,
        [{"role": "user", "content": json.dumps(context)}],
    )
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
