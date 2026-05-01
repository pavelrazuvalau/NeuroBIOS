from typing import Generator
from openai import OpenAI

from neurobios.core.constants import StreamingEvent, MessageRole
from neurobios.core.models import AgentStreamingEvent
from neurobios.lm.models import Message, LMRequestConfig, ToolCall, ToolCallFunction


class LMClient:
    def __init__(self, *, base_url: str, api_key: str, model: str):
        self._client = OpenAI(base_url=base_url, api_key=api_key)
        self._model = model

    def prompt_model(
        self, messages: list[Message], config: LMRequestConfig
    ) -> Message | Generator[AgentStreamingEvent, None, Message]:
        request_payload = {
            "model": self._model,
            "messages": [message.model_dump(exclude_none=True) for message in messages],
            **config.model_dump(exclude_none=True),
        }

        response = self._client.chat.completions.create(**request_payload)

        return (
            self._handle_streamed_response(response)
            if request_payload.get("stream")
            else self._handle_static_response(response)
        )

    def _handle_streamed_response(
        self, response
    ) -> Generator[AgentStreamingEvent, None, Message]:
        accumulated_content = ""
        accumulated_tool_calls: list[ToolCall] = []

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
                yield AgentStreamingEvent(
                    event=StreamingEvent.REASONING_STREAM,
                    payload={"content": reasoning_token},
                )

            if content_token:
                yield AgentStreamingEvent(
                    event=StreamingEvent.CONTENT_STREAM,
                    payload={"content": content_token},
                )
                accumulated_content += content_token

            if tool_calls_delta:
                for tool_call_chunk in tool_calls_delta:
                    index = tool_call_chunk.index
                    is_new_tool_call = not (0 <= index < len(accumulated_tool_calls))

                    if is_new_tool_call:
                        accumulated_tool_calls.append(
                            ToolCall(
                                id=tool_call_chunk.id,
                                function=ToolCallFunction(
                                    name=tool_call_chunk.function.name,
                                    arguments="",
                                ),
                            )
                        )

                    if tool_call_chunk.function.arguments:
                        accumulated_tool_calls[
                            index
                        ].function.arguments += tool_call_chunk.function.arguments

        return Message(
            role=MessageRole.ASSISTANT.value,
            content=accumulated_content or None,
            tool_calls=accumulated_tool_calls or None,
        )

    def _handle_static_response(self, response) -> Message:
        message = response.choices[0].message

        tool_calls = None
        if message.tool_calls:
            tool_calls = [
                ToolCall(
                    id=tool_call.id,
                    function=ToolCallFunction(
                        name=tool_call.function.name,
                        arguments=tool_call.function.arguments,
                    ),
                )
                for tool_call in message.tool_calls
            ]

        return Message(
            role=MessageRole.ASSISTANT.value,
            content=message.content,
            tool_calls=tool_calls,
        )
