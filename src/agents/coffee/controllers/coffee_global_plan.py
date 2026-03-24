from core.context_manager import ContextManager
from lm.lm_service import send_messages
from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt


def plan_task(**kwargs):
    context = kwargs.get("context", [])
    system_prompt = f"{coffee_maker_system_prompt.strip()}\n\n{plan_task_prompt.strip()}"

    context_manager = ContextManager(context)
    context_with_system_prompt = context_manager.get_history_with_system_prompt(system_prompt)

    response = send_messages(context_with_system_prompt)

    return {
        "result": "Planning task complete",
        "state_delta": {
            "session_plan": response.get("content", "")
        },
    }
