from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from lm.lm_service import send_messages, predict_metric
from agents.coffee.prompts.task.coffee_verify_prompt import analyze_completion_prompt, verify_task_prompt


def verify(context):
    messages_history = context.get("messages", [])

    analysis_response = send_messages(
        f"{coffee_maker_system_prompt.strip()}\n\n{analyze_completion_prompt.strip()}",
        messages_history,
        hide_output=True
    )

    response = predict_metric(
        coffee_maker_system_prompt,
        messages_history + [analysis_response] + [{"role": "user", "content": verify_task_prompt}],
        ("True", "False"),
    )
    is_session_complete = response == "True"

    print(f"[IS COMPLETE]: {is_session_complete}")

    return {
        "result": "Verify complete",
        "next_state": (
            CoffeeFlowState.NEXT_STEP_PLAN if not is_session_complete else None
        ),
    }
