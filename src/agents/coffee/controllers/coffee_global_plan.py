from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt
from core.controller.base_lm_controller import BaseLMController


class CoffeeGlobalPlanController(BaseLMController):
    def _build_system_prompt(self, state, context):
        return f"{coffee_maker_system_prompt}\n\n{plan_task_prompt}"

    def _build_response(self, model_response):
        return {
            "state_delta": {"session_plan": model_response.get("content", "")},
        }
