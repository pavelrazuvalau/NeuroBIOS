from agents.coffee.coffee_config import (
    COFFEE_FLOW_ACTIONS,
    COFFEE_SYSTEM_STATE_ACTIONS,
    COFFEE_FLOW,
)
from core.agent import AgentCore
from core.constants import StreamingEvent


def main():
    coffee_agent = AgentCore(COFFEE_FLOW_ACTIONS | COFFEE_SYSTEM_STATE_ACTIONS)
    user_prompt = input("prompt > ")
    response_generator = coffee_agent.run(COFFEE_FLOW, user_prompt)

    for chunk in response_generator:
        event = chunk.get("event")
        payload = chunk.get("payload")

        match event:
            case StreamingEvent.EXECUTING_NEXT_STEP:
                print()
            case StreamingEvent.REASONING_STREAM:
                print(
                    f"\033[90m{payload.get("content", '')}\033[0m", end="", flush=True
                )
            case StreamingEvent.CONTENT_STREAM:
                print(payload.get("content", ""), end="", flush=True)
            case StreamingEvent.TOOL_CALL:
                print(
                    f"[TOOL CALL] {payload.get('name')} with args: {payload.get('arguments')}"
                )
            case StreamingEvent.RESPONSE_END:
                print("EOS")
    print()


if __name__ == "__main__":
    main()
