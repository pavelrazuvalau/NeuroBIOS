from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from core.context_manager import ContextManager
from lm.lm_service import send_messages
from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_prompt,
)


def plan_next_step(**kwargs):
    context = kwargs.get("context", [])
    state = kwargs.get("state", {})
    session_plan = state.get("session_plan", "")

    plan_description = f"Given tha plan below:\n{session_plan}" if session_plan else ""
    system_prompt = f"{coffee_maker_system_prompt.strip()}\n\n{plan_description.strip()}\n\n{plan_step_prompt.strip()}"

    context_manager = ContextManager(context)
    context_with_system_prompt = context_manager.get_history_with_system_prompt(system_prompt)

    response = send_messages(context_with_system_prompt, tools=COFFEE_TOOLS_LIST, stream=False)

    return {"result": "Planning step complete", "context_delta": [response]}
