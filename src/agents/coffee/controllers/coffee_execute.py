from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.tools.coffee_execute_tools_definition import (
    grind_coffee,
    pour_chocolate,
    pour_milk,
    pour_water,
)
from core.constants import StreamingEvent

COFFEE_TOOLS_REGISTRY = {
    "grind_coffee": grind_coffee,
    "pour_water": pour_water,
    "pour_milk": pour_milk,
    "pour_chocolate": pour_chocolate,
}


def execute(**kwargs):
    context = kwargs.get("context", [])
    last_message = context[-1]
    tool_calls = last_message.get("tool_calls", None)

    tool_responses = []

    if tool_calls:
        for tool_call in tool_calls:
            tool_call_id = tool_call.get("id")
            function_to_call = tool_call.get("function", {})
            function_name = function_to_call.get("name", None)
            function_arguments = function_to_call.get("arguments", None)

            action_function = COFFEE_TOOLS_REGISTRY.get(function_name, None)

            if action_function:
                function_result = action_function(function_arguments)

                yield {
                    "event": StreamingEvent.TOOL_CALL,
                    "payload": {"name": function_name, "arguments": function_arguments},
                }

                tool_responses.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call_id,
                        "name": function_name,
                        "content": function_result,
                    }
                )

    return {
        "result": "Execute complete",
        "context_delta": tool_responses,
        "next_state": CoffeeFlowState.NEXT_STEP_PLAN if tool_responses else None,
    }
