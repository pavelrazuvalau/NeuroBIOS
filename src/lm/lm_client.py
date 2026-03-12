from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


# TODO: replace print with returning and handling the stream outside
def prompt_model(messages, params):
    request_payload = {"model": "qwen/qwen3.5-9b", "messages": messages, "stream": True}
    hide_output = params.pop("hide_output", False)

    request_payload.update(params)
    completion_response = client.chat.completions.create(**request_payload)

    final_response = {"role": "assistant"}
    accumulated_content = ""
    accumulated_tool_calls = []

    for chunk in completion_response:
        delta = chunk.choices[0].delta
        # print(f"chunk: {delta}")
        token = delta.content

        if token:
            # TODO: remove condition
            if not hide_output:
                print(token, end="", flush=True)

            accumulated_content += token

        if delta.tool_calls:
            for tool_called in delta.tool_calls:
                accumulated_tool_calls.append(
                    {
                        "id": tool_called.id,
                        "type": "function",
                        "function": {
                            "name": tool_called.function.name,
                            "arguments": tool_called.function.arguments,
                        },
                    }
                )

    final_response.update({
        "content": accumulated_content,
        "tool_calls": accumulated_tool_calls or None
    })

    return final_response
