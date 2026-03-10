from agents.coffee.coffee_constants import CoffeeBeverage, CoffeeStep, CoffeeFlowState
from agents.coffee.tools.execute import coffee_execute_tools
from agents.coffee.tools.plan import coffee_plan_tools
from core.constants import SystemState


COFFEE_FLOW = (CoffeeFlowState.PLAN, CoffeeFlowState.EXECUTE)

COFFEE_FLOW_ACTIONS = {
    CoffeeFlowState.PLAN: coffee_plan_tools.plan,
    CoffeeFlowState.EXECUTE: coffee_execute_tools.execute,
}

COFFEE_SYSTEM_STATE_ACTIONS = {
    SystemState.END: coffee_execute_tools.end_flow,
    SystemState.ESCALATE: coffee_execute_tools.escalate_flow,
}
