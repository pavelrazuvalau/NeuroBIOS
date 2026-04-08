from openai import OpenAI


client = OpenAI(base_url="http://localhost:8080", api_key="llama.cpp")


def prompt_model(messages, params):
    request_payload = {
        "model": "qwen/qwen3.5-9b",
        "messages": messages,
        "stream": True,
        "extra_body": {"reasoning": {"enabled": False}},
    }

    request_payload.update(params)
    response = client.chat.completions.create(**request_payload)

    return (
        _handle_streamed_response(response)
        if request_payload.get("stream")
        else _handle_static_response(response)
    )


def _handle_streamed_response(response):
    accumulated_content = ""
    accumulated_tool_calls = []

    for chunk in response:
        # ignore service chunks
        if not chunk.choices:
            continue

        delta = chunk.choices[0].delta
        # print(f"chunk: {delta}")
        content_token = delta.content
        tool_calls_delta = delta.tool_calls

        if content_token:
            yield content_token
            accumulated_content += content_token

        if tool_calls_delta:
            for tool_call_chunk in tool_calls_delta:
                current_tool_call_index = tool_call_chunk.index
                is_accumulated_tool_call_index_exist = (
                    0 <= current_tool_call_index < len(accumulated_tool_calls)
                )

                if not is_accumulated_tool_call_index_exist:
                    accumulated_tool_calls.append(
                        {
                            "id": tool_call_chunk.id,
                            "type": "function",
                            "function": {
                                "name": tool_call_chunk.function.name,
                                "arguments": "",
                            },
                        }
                    )

                if tool_call_chunk.function.arguments:
                    accumulated_tool_calls[current_tool_call_index]["function"][
                        "arguments"
                    ] += tool_call_chunk.function.arguments

    return _format_final_response(accumulated_content, accumulated_tool_calls)


def _handle_static_response(response):
    message = response.choices[0].message
    content = message.content
    tool_calls = message.tool_calls

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
