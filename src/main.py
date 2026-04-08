from agents.coffee.coffee_agent import CoffeeAgent


def main():
    coffee_agent = CoffeeAgent()
    user_prompt = input("prompt > ")
    result = coffee_agent.run(user_prompt)

    for chunk in result:
        print(chunk, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
