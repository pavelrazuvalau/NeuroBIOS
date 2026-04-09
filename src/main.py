from agents.coffee.coffee_agent import CoffeeAgent
from core.constants import StreamingEvent


def main():
    coffee_agent = CoffeeAgent()
    user_prompt = input("prompt > ")
    response_generator = coffee_agent.run(user_prompt)

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
