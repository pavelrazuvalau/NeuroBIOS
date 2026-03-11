from agents.coffee.coffee_agent import CoffeeAgent


def main():
    coffee_agent = CoffeeAgent()
    user_prompt = input("prompt > ")
    coffee_agent.run(user_prompt)


if __name__ == "__main__":
    main()
