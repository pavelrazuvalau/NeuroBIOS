from agents.coffee.tools.coffee_execute_tools_contract import (
    GrindCoffeeArgs,
    VolumeArgs,
)


def grind_coffee(args: str) -> str:
    parsed_args = GrindCoffeeArgs.model_validate_json(args)
    return f"OK, ground with strength: {parsed_args.strength}"


def pour_water(args: str) -> str:
    parsed_args = VolumeArgs.model_validate_json(args)
    return f"OK, poured {parsed_args.volume} units of water"


def pour_milk(args: str) -> str:
    parsed_args = VolumeArgs.model_validate_json(args)
    return f"OK, poured {parsed_args.volume} units of milk"


def pour_chocolate(args: str) -> str:
    parsed_args = VolumeArgs.model_validate_json(args)
    return f"OK, poured {parsed_args.volume} units of chocolate"
