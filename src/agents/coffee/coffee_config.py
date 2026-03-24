from enum import Enum

from agents.coffee.coffee_constants import CoffeeFlowState
from agents.coffee.controllers import (
    coffee_global_plan,
    coffee_next_step_plan,
    coffee_execute,
    coffee_system,
)
from agents.coffee.prompts.system.coffee_maker_system_prompt import (
    coffee_maker_system_prompt,
)
from agents.coffee.prompts.task.coffee_plan_task_prompt import plan_task_prompt
from agents.coffee.prompts.task.coffee_plan_next_step_prompt import (
    plan_step_prompt,
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

COFFEE_FLOW_SYSTEM_PROMPTS: dict[Enum, str] = {
    CoffeeFlowState.GLOBAL_PLAN: f"{coffee_maker_system_prompt.strip()}\n\n{plan_task_prompt.strip()}",
    CoffeeFlowState.NEXT_STEP_PLAN: f"{coffee_maker_system_prompt.strip()}\n\n{plan_step_prompt.strip()}",
}

COFFEE_SYSTEM_STATE_ACTIONS = {
    SystemState.END: coffee_system.end_flow,
    SystemState.ESCALATE: coffee_system.escalate_flow,
}
