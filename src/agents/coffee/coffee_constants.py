from enum import Enum


class CoffeeFlowState(str, Enum):
    GLOBAL_PLAN = "GLOBAL_PLAN"
    NEXT_STEP_PLAN = "NEXT_STEP_PLAN"
    EXECUTE = "EXECUTE"
    VERIFY = "VERIFY"
    SUMMARIZE = "SUMMARIZE"


class CoffeeBeverage(str, Enum):
    BLACK_COFFEE = "BLACK_COFFEE"
    CAPUCINO = "CAPUCINO"
    FLAT_WHITE = "FLAT_WHITE"


class CoffeeStep(str, Enum):
    GRIND_COFFEE = "GRIND_COFFEE"
    POUR_WATER = "POUR_WATER"
    POUR_MILK = "POUR_MILK"
    ANALYZE = "ANALYZE"
    SERVE = "SERVE"


COFFEE_MENU = {
    CoffeeBeverage.BLACK_COFFEE: (
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
        CoffeeStep.SERVE,
    ),
    CoffeeBeverage.CAPUCINO: (
        CoffeeStep.POUR_MILK,
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
        CoffeeStep.SERVE,
    ),
    CoffeeBeverage.FLAT_WHITE: (
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
        CoffeeStep.POUR_MILK,
        CoffeeStep.SERVE,
    ),
}
