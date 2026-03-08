from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


def prompt_model(system_prompt, user_prompt):
    completion = client.chat.completions.create(
        model="qwen/qwen3.5-9b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return completion.choices[0].message.content
