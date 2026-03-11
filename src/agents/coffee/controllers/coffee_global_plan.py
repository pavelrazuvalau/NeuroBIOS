import json

from lm.lm_service import send_messages
from agents.coffee.prompts.coffee_macro_plan_prompt import macro_plan_system_prompt


def plan_task(context):
    messages_history = context.get("messages", [])
    response = send_messages(macro_plan_system_prompt, messages_history)

    return {
        "result": "Planning complete",
        "context_delta": {
            "messages": [{"role": "assistant", "content": response}],
        },
    }
