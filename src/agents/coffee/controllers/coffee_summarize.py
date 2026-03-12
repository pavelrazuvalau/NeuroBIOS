from lm.lm_service import send_messages
from agents.coffee.prompts.task.coffee_summarize_task_prompt import (
    summarize_task_prompt,
)


def summarize(context):
    print("\n")

    messages_history = context.get("messages", [])
    messages_history.append({"role": "user", "content": summarize_task_prompt.strip()})

    response = send_messages(summarize_task_prompt.strip(), messages_history)

    return {
        "result": "Summarize task complete",
        "context_delta": {
            "messages": [response],
        },
    }
