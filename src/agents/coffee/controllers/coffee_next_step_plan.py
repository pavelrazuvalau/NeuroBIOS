from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from lm.lm_service import send_messages
from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_step_prompt,
)


def plan_next_step(context):
    print("\n")

    messages_history = context.get("messages", [])
    messages_history.append({"role": "user", "content": plan_step_step_prompt.strip()})

    response = send_messages(
        plan_step_step_prompt.strip(),
        messages_history,
        tools=COFFEE_TOOLS_LIST,
    )

    return {
        "result": "Planning step complete",
        "context_delta": {
            "messages": [response],
        },
    }
