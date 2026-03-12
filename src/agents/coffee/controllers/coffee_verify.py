from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.prompts.system.coffee_maker_system_prompt import coffee_maker_system_prompt
from lm.lm_service import predict_metric
from agents.coffee.prompts.task.coffee_verify_prompt import verify_task_prompt


def verify(context):
    messages_history = context.get("messages", [])

    response = predict_metric(
        f"{coffee_maker_system_prompt.strip()}\n\n{verify_task_prompt.strip()}", messages_history, ("True", "False")
    )
    is_session_complete = response == "True"

    return {
        "result": "Verify complete",
        "next_state": (
            CoffeeFlowState.NEXT_STEP_PLAN if not is_session_complete else None
        ),
    }
