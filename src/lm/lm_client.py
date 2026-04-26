from openai import OpenAI

from core.constants import StreamingEvent


class LMClient:
    def __init__(self, *, base_url, api_key, model):
        self._client = OpenAI(base_url=base_url, api_key=api_key)
        self._model = model

    def prompt_model(self, messages, params):
        request_payload = {
            "model": self._model,
            "messages": messages,
            "stream": True,
        }

        request_payload.update(params)
        response = self._client.chat.completions.create(**request_payload)

        return (
            self._handle_streamed_response(response)
            if request_payload.get("stream")
            else self._handle_static_response(response)
        )

    def _handle_streamed_response(self, response):
        accumulated_content = ""
        accumulated_tool_calls = []

        for chunk in response:
            # ignore service chunks
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta
            content_token = delta.content
            tool_calls_delta = delta.tool_calls
            reasoning_token = None

            # There's inconsistency among providers related to streaming of reasoning tokens
            # llama.cpp
            if hasattr(delta, "reasoning_content"):
                reasoning_token = delta.reasoning_content
            # OpenRouter
            elif hasattr(delta, "reasoning"):
                reasoning_token = delta.reasoning

            if reasoning_token:
                yield {
                    "event": StreamingEvent.REASONING_STREAM,
                    "payload": {"content": reasoning_token},
                }

            if content_token:
                yield {
                    "event": StreamingEvent.CONTENT_STREAM,
                    "payload": {"content": content_token},
                }
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

        return self._format_final_response(accumulated_content, accumulated_tool_calls)

    def _handle_static_response(self, response):
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

        return self._format_final_response(content, accumulated_tool_calls)

    def _format_final_response(self, content, tool_calls=None):
        return {
            "role": "assistant",
            "content": content,
            "tool_calls": tool_calls,
        }
