from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from core.controller.base_lm_controller import BaseLMController

from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_prompt,
)


class CoffeeNextStepPlanController(BaseLMController):
    def __init__(self):
        super().__init__(COFFEE_TOOLS_LIST)

    def _build_system_prompt(self, state, context):
        session_plan = state.get("session_plan", "")
        plan_description_prompt = (
            f"Given tha plan below:\n{session_plan}" if session_plan else ""
        )

        return f"{coffee_maker_system_prompt}\n\n{plan_description_prompt}\n\n{plan_step_prompt}"

    def _build_response(self, model_response):
        return {
            "context_delta": [model_response],
        }
