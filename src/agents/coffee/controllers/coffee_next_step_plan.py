from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from lm.lm_service import send_messages
from agents.coffee.prompts.coffee_plan_next_step_prompt import plan_step_system_prompt

def plan_next_step(context):
    messages_history = context.get("messages", [])
    next_step_plan_message = {"role": "user", "content": "Analyze the current history and call one tool"}
    history_for_inference = messages_history + [next_step_plan_message]
    response = send_messages(plan_step_system_prompt, history_for_inference, tools=COFFEE_TOOLS_LIST)

    return {
        "result": "Planning step complete",
        "context_delta": {
            "messages": [response],
        },
    }