from agents.coffee.coffee_constants import CoffeeFlowState
from core.controller.base_tools_controller import BaseToolsController


class CoffeeExecuteController(BaseToolsController):
    def _build_response(self, tool_responses):
        return {
            "context_delta": tool_responses,
            "next_state": CoffeeFlowState.NEXT_STEP_PLAN if tool_responses else None,
        }
