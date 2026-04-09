from agents.coffee.coffee_agent import CoffeeAgent


def main():
    coffee_agent = CoffeeAgent()
    user_prompt = input("prompt > ")
    result = coffee_agent.run(user_prompt)

    for chunk in result:
        if chunk.get("type") == "content":
            print(chunk.get("delta", ""), end="", flush=True)
        elif chunk.get("type") == "reasoning_content":
            print(f"\033[90m{chunk.get('delta', '')}\033[0m", end="", flush=True)
        elif chunk.get("type") == "tool_call":
            print(f"[TOOL CALL] {chunk.get('name')} with args: {chunk.get('args')}")
    print()


if __name__ == "__main__":
    main()
