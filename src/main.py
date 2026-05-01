from agents.coffee.coffee_config import COFFEE_FLOW_CONTROLLERS, COFFEE_FLOW
from neurobios.core.agent import AgentCore
from neurobios.core.constants import StreamingEvent
from neurobios.core.deps import CoreConfig


def main():
    core_config = CoreConfig(
        base_url="http://localhost:8080",
        api_key="llama.cpp",
        model="qwen/qwen3.5-9b",
    )

    coffee_agent = AgentCore(
        states_config=COFFEE_FLOW_CONTROLLERS,
        core_config=core_config,
    )
    user_prompt = input("prompt > ")
    response_generator = coffee_agent.run(COFFEE_FLOW, user_prompt)

    for chunk in response_generator:
        event = chunk.event
        payload = chunk.payload

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
                    f"[TOOL CALL] {payload.get('name')} with content: {payload.get('content')}"
                )
            case StreamingEvent.RESPONSE_END:
                print("EOS")
    print()


if __name__ == "__main__":
    main()
