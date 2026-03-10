import json

from lm.lm_service import send_messages
from agents.coffee.prompts.coffee_plan_prompt import plan_system_prompt


def plan(context):
    response = send_messages(
        [
            {"role": "system", "content": plan_system_prompt},
            {"role": "user", "content": json.dumps(context)},
        ]
    )

    return {
        "result": response,
        "context_update": {
            "messages": [{"role": "assistant", "content": response}],
        },
    }
