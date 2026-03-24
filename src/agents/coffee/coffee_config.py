from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.controllers import (
    coffee_global_plan,
    coffee_next_step_plan,
    coffee_execute,
    coffee_system,
)
from core.constants import SystemState


COFFEE_FLOW = (
    CoffeeFlowState.GLOBAL_PLAN,
    CoffeeFlowState.NEXT_STEP_PLAN,
    CoffeeFlowState.EXECUTE,
)

COFFEE_FLOW_ACTIONS = {
    CoffeeFlowState.GLOBAL_PLAN: coffee_global_plan.plan_task,
    CoffeeFlowState.NEXT_STEP_PLAN: coffee_next_step_plan.plan_next_step,
    CoffeeFlowState.EXECUTE: coffee_execute.execute,
}

COFFEE_SYSTEM_STATE_ACTIONS = {
    SystemState.END: coffee_system.end_flow,
    SystemState.ESCALATE: coffee_system.escalate_flow,
}
