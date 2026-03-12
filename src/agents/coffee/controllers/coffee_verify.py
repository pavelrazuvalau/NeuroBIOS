from agents.coffee.coffee_constants import CoffeeFlowState
from lm.lm_service import predict_metric
from agents.coffee.prompts.coffee_verify_prompt import verify_task_system_prompt

def verify(context):
    messages_history = context.get("messages", [])
    # Interrupt context inertia
    analyze_message = {"role": "user", "content": "Analyze the execution history above. Is the ENTIRE recipe from the initial plan fully complete? Answer ONLY with True or False"}
    history_analysis_copy = messages_history + [analyze_message]

    response = predict_metric(verify_task_system_prompt, history_analysis_copy, ("True", "False"))
    is_session_complete = response == "True"

    return {
        "result": "Verify complete",
        "next_state": CoffeeFlowState.NEXT_STEP_PLAN if not is_session_complete else None
    }
