from agents.coffee.prompts.system.coffee_maker_system_prompt import coffee_maker_system_prompt
from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from lm.lm_service import send_messages
from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_prompt,
)


def plan_next_step(context):
    messages_history = context.get("messages", [])
    response = send_messages(
        f"{coffee_maker_system_prompt.strip()}\n\n{plan_step_prompt.strip()}",
        messages_history,
        tools=COFFEE_TOOLS_LIST,
        stream=False
    )

    return {
        "result": "Planning step complete",
        "context_delta": {
            "messages": [response],
        },
    }
