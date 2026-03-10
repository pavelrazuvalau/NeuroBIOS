from agents.coffee.coffee_agent import CoffeeAgent
from agents.coffee.coffee_config import COFFEE_FLOW


def main():
    coffee_agent = CoffeeAgent()
    user_prompt = input("prompt > ")
    coffee_agent.run(COFFEE_FLOW, {"messages": [{"role": "user", "content": user_prompt}]})


if __name__ == "__main__":
    main()
