from agents.coffee.prompts.system.coffee_maker_system_prompt import coffee_maker_system_prompt
from lm.lm_service import send_messages
from agents.coffee.prompts.task.coffee_summarize_task_prompt import (
    summarize_task_prompt,
)


def summarize(context):
    print("\n")

    messages_history = context.get("messages", [])
    response = send_messages(f"{coffee_maker_system_prompt.strip()}\n\n{summarize_task_prompt.strip()}", messages_history)

    return {
        "result": "Summarize task complete",
        "context_delta": {
            "messages": [response],
        },
    }
