from agents.coffee.tools.coffee_execute_tools_contract import COFFEE_TOOLS_LIST
from lm.lm_service import send_messages


def plan_next_step(**kwargs):
    context = kwargs.get("context", [])
    response = send_messages(context, tools=COFFEE_TOOLS_LIST, stream=False)

    return {
        "result": "Planning step complete",
        "context_delta": [response]
    }
