from agents.coffee.coffee_constants import CoffeeFlowState
from lm.lm_service import predict_metric
from agents.coffee.prompts.task.coffee_verify_prompt import verify_task_prompt


def verify(context):
    messages_history = context.get("messages", [])

    # Interrupt context inertia
    analyze_message = {"role": "user", "content": verify_task_prompt.strip()}
    history_analysis_copy = messages_history + [analyze_message]

    response = predict_metric(
        verify_task_prompt.strip(), history_analysis_copy, ("True", "False")
    )
    is_session_complete = response == "True"

    return {
        "result": "Verify complete",
        "next_state": (
            CoffeeFlowState.NEXT_STEP_PLAN if not is_session_complete else None
        ),
    }
