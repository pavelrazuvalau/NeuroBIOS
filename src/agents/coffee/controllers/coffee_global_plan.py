from lm.lm_service import send_messages


def plan_task(**kwargs):
    context = kwargs.get("context", [])
    
    response = send_messages(context)
    next_step_message = {"role": "user", "content": "Follow the plan. Describe the first step you perform"}

    return {
        "result": "Planning task complete",
        "context_delta": [response, next_step_message],
    }
