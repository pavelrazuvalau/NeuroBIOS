from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.controllers.coffee_execute import CoffeeExecuteController
from agents.coffee.controllers.coffee_global_plan import CoffeeGlobalPlanController
from agents.coffee.controllers.coffee_next_step_plan import CoffeeNextStepPlanController
from agents.coffee.tools.coffee_execute_tools_definition import (
    grind_coffee,
    pour_chocolate,
    pour_milk,
    pour_water,
)
from agents.coffee.tools.coffee_execute_tools_contract import (
    GRIND_COFFEE_SCHEMA,
    POUR_WATER_SCHEMA,
    POUR_MILK_SCHEMA,
    POUR_CHOCOLATE_SCHEMA,
)


COFFEE_FLOW = (
    CoffeeFlowState.GLOBAL_PLAN,
    CoffeeFlowState.NEXT_STEP_PLAN,
    CoffeeFlowState.EXECUTE,
)

COFFEE_FLOW_CONTROLLERS = {
    CoffeeFlowState.GLOBAL_PLAN: CoffeeGlobalPlanController,
    CoffeeFlowState.NEXT_STEP_PLAN: CoffeeNextStepPlanController,
    CoffeeFlowState.EXECUTE: CoffeeExecuteController,
}

COFFEE_TOOLS_REGISTRY = {
    "grind_coffee": grind_coffee,
    "pour_water": pour_water,
    "pour_milk": pour_milk,
    "pour_chocolate": pour_chocolate,
}

COFFEE_TOOLS_LIST = [
    GRIND_COFFEE_SCHEMA,
    POUR_WATER_SCHEMA,
    POUR_MILK_SCHEMA,
    POUR_CHOCOLATE_SCHEMA,
]
