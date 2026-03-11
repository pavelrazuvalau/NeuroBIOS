from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


def prompt_model(messages):
    completion_stream = client.chat.completions.create(
        model="qwen/qwen3.5-9b", messages=messages, stream=True
    )

    final_response = ""

    for chunk in completion_stream:
        token = chunk.choices[0].delta.content

        if token:
            print(token, end="", flush=True)
            final_response += token

    print()

    return final_response
