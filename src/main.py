from agents.coffee.coffee_agent import CoffeeAgent
from agents.coffee.coffee_config import COFFEE_FLOWS
from agents.coffee.coffee_constants import CoffeeFlow


def main():
    coffee_agent = CoffeeAgent()

    print("Making Capucino:")
    coffee_agent.run(COFFEE_FLOWS[CoffeeFlow.CAPUCINO], {"messages": [{"role": "user", "content": "Make me Capucino"}], "state": {"seeds_available": False}})

    print("\n")

    print("Making Flat White:")
    coffee_agent.run(COFFEE_FLOWS[CoffeeFlow.FLAT_WHITE], {"messages": [{"role": "user", "content": "Make me Flat White"}], "state": {"seeds_available": True}})


if __name__ == "__main__":
    main()
