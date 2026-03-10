from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


def prompt_model(messages):
    completion = client.chat.completions.create(
        model="qwen/qwen3.5-9b", messages=messages
    )

    return completion.choices[0].message.content
