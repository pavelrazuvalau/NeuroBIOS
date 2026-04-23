from core.controller.base_lm_controller import BaseLMController
from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_prompt,
)


class CoffeeNextStepPlanController(BaseLMController):
    def _build_system_prompt(self, state, context):
        session_plan = state.get("session_plan", "")
        plan_description_prompt = (
            f"Given tha plan below:\n{session_plan}" if session_plan else ""
        )

        return (
            f"{self._system_prompt}\n\n{plan_description_prompt}\n\n{plan_step_prompt}"
        )

    def _build_response(self, model_response):
        return {
            "context_delta": [model_response],
        }
