from lm.lm_service import send_messages
from agents.coffee.prompts.coffee_summarize_task_prompt import summarize_task_system_prompt

def summarize(context):
    messages_history = context.get("messages", [])
    next_step_plan_message = {"role": "user", "content": "Summarize the work done without calling any tools. Come up with a phrase like \"Enjoy your drink\""}
    history_for_inference = messages_history + [next_step_plan_message]
    response = send_messages(summarize_task_system_prompt, history_for_inference)

    return {
        "result": "Summarize task complete",
        "context_delta": {
            "messages": [response],
        },
    }
