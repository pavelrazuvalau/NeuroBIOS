from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


# TODO: replace print with returning and handling the stream outside
def prompt_model(messages, params):
    request_payload = {
        "model": "qwen/qwen3.5-9b",
        "messages": messages,
        "stream": True,
        "extra_body": {"reasoning": {"enabled": False}},
    }
    hide_output = params.pop("hide_output", False)

    request_payload.update(params)
    response = client.chat.completions.create(**request_payload)

    return (
        _handle_streamed_response(response, hide_output)
        if request_payload.get("stream")
        else _handle_static_response(response)
    )


def _handle_streamed_response(response, hide_output=False):
    accumulated_content = ""

    for chunk in response:
        # ignore service chunks
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta
        # print(f"chunk: {delta}")
        token = delta.content

        if token:
            # TODO: remove condition
            if not hide_output:
                print(token, end="", flush=True)

            accumulated_content += token

    return _format_final_response(accumulated_content)


def _handle_static_response(response):
    message = response.choices[0].message
    content = message.content
    tool_calls = message.tool_calls

    print("\n", content or "")

    accumulated_tool_calls = []

    if message.tool_calls:
        for tool_called in tool_calls:
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

    return _format_final_response(content, accumulated_tool_calls)


def _format_final_response(content, tool_calls=None):
    return {
        "role": "assistant",
        "content": content,
        "tool_calls": tool_calls,
    }
