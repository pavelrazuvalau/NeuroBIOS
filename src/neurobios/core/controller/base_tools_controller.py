from neurobios.core.controller.base_controller import BaseController
from neurobios.core.constants import StreamingEvent


class BaseToolsController(BaseController):
    def __init__(self, dependencies, tools_registry=None):
        super().__init__(dependencies)
        self._tools_registry = tools_registry or {}

    def _execute(self, state, context):
        last_message = context[-1] if context else {}
        tool_calls = last_message.get("tool_calls", None)
        tool_responses = []

        if tool_calls:
            for tool_call in tool_calls:
                tool_call_id = tool_call.get("id")
                function_to_call = tool_call.get("function", {})
                function_name = function_to_call.get("name", None)
                function_arguments = function_to_call.get("arguments", None)

                action_function = self._tools_registry.get(function_name, None)

                if action_function:
                    function_result = action_function(function_arguments)
                    current_tool_response = {
                        "role": "tool",
                        "tool_call_id": tool_call_id,
                        "name": function_name,
                        "content": function_result,
                    }

                    tool_responses.append(current_tool_response)

                    yield {
                        "event": StreamingEvent.TOOL_CALL,
                        "payload": current_tool_response,
                    }

        return tool_responses
