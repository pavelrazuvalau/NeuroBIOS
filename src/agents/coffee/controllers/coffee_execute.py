from neurobios.core.controller.base_tools_controller import BaseToolsController

from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.tools.coffee_execute_tools_definition import (
    grind_coffee,
    pour_chocolate,
    pour_milk,
    pour_water,
)
from neurobios.core.models import AgentStepResult
from neurobios.lm.models import Message
from neurobios.core.deps import CoreDependencies


COFFEE_TOOLS_REGISTRY = {
    "grind_coffee": grind_coffee,
    "pour_water": pour_water,
    "pour_milk": pour_milk,
    "pour_chocolate": pour_chocolate,
}


class CoffeeExecuteController(BaseToolsController):
    def __init__(self, dependencies: CoreDependencies):
        super().__init__(tools_registry=COFFEE_TOOLS_REGISTRY)

    def _build_response(self, result: list[Message]) -> AgentStepResult:
        return AgentStepResult(
            context_delta=result,
            next_state=CoffeeFlowState.NEXT_STEP_PLAN if result else None,
        )
