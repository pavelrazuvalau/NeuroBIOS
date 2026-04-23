from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt
from core.controller.base_lm_controller import BaseLMController


class CoffeeGlobalPlanController(BaseLMController):
    def __init__(self, **config):
        super().__init__(**config)
        self._are_tools_enabled = False

    def _build_system_prompt(self, state, context):
        return f"{self._system_prompt}\n\n{plan_task_prompt}"

    def _build_response(self, model_response):
        return {
            "state_delta": {"session_plan": model_response.get("content", "")},
        }
