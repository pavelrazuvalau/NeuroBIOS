import requests


def ask_model(system_prompt, user_prompt, params = None):
    payload = {
        "model": "qwen/qwen3.5-9b",
        "system_prompt": system_prompt,
        "input": user_prompt,
    } | (params if params else {})

    response = requests.post("http://localhost:1234/api/v1/chat", json=payload).json()
    output = next(response_entity for response_entity in response["output"] if response_entity["type"] == "message")

    return output["content"]
