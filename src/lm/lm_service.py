from lm.lm_client import prompt_model


def send_messages(messages, **params):
    return prompt_model(messages, params)


def predict_metric(messages, criteria):
    response = send_messages(
        messages,
        hide_output=True
    )

    content = response.get("content", "")
    return sanitize_metric_response(content, criteria)


def sanitize_metric_response(content, criteria):
    extracted_word = None
    num_of_occurrences = 0

    # print(f"content {content}")
    # print(f"criteria {criteria}")

    for word in criteria:
        if word in content:
            extracted_word = word
            num_of_occurrences += 1

    # print(f"extracted_word {extracted_word}")
    # print(f"num_of_occurrences {num_of_occurrences}")

    return extracted_word if num_of_occurrences == 1 else None
