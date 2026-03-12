from lm.lm_service import send_messages
from agents.coffee.prompts.coffee_plan_task_prompt import plan_task_system_prompt


def plan_task(context):
    messages_history = context.get("messages", [])
    response = send_messages(plan_task_system_prompt, messages_history)

    return {
        "result": "Planning task complete",
        "context_delta": {
            "messages": [response],
        },
    }
