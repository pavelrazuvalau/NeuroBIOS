from enum import Enum

from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.controllers.coffee_execute import CoffeeExecuteController
from agents.coffee.controllers.coffee_global_plan import CoffeeGlobalPlanController
from agents.coffee.controllers.coffee_next_step_plan import CoffeeNextStepPlanController
from neurobios.core.controller.base_controller import ControllerClass


COFFEE_FLOW: tuple[Enum, ...] = (
    CoffeeFlowState.GLOBAL_PLAN,
    CoffeeFlowState.NEXT_STEP_PLAN,
    CoffeeFlowState.EXECUTE,
)

COFFEE_FLOW_CONTROLLERS: dict[Enum, ControllerClass] = {
    CoffeeFlowState.GLOBAL_PLAN: CoffeeGlobalPlanController,
    CoffeeFlowState.NEXT_STEP_PLAN: CoffeeNextStepPlanController,
    CoffeeFlowState.EXECUTE: CoffeeExecuteController,
}
