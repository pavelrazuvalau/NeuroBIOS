from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt
from neurobios.core.controller.base_lm_controller import BaseLMController
from neurobios.core.models import (
    ControllerState,
    AgentStepResult,
)
from neurobios.lm.models import Message


class CoffeeGlobalPlanController(BaseLMController):
    def _build_system_prompt(self, state: ControllerState) -> str:
        return f"{coffee_maker_system_prompt}\n\n{plan_task_prompt}"

    def _build_response(self, model_response: Message) -> AgentStepResult:
        return AgentStepResult(
            state_delta={"session_plan": model_response.content},
        )
