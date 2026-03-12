from lm.lm_service import send_messages
from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt


def plan_task(context):
    messages_history = context.get("messages", [])
    # avoid double "user" messages
    response = send_messages(
        f"{coffee_maker_system_prompt.strip()}\n\n{plan_task_prompt.strip()}",
        messages_history,
    )

    return {
        "result": "Planning task complete",
        "context_delta": {
            "messages": [response],
        },
    }
