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
    HOT_CHOCOLATE = "HOT_CHOCOLATE"
    MOCHA = "MOCHA"


class CoffeeStep(str, Enum):
    GRIND_COFFEE = "GRIND_COFFEE"
    POUR_WATER = "POUR_WATER"
    POUR_MILK = "POUR_MILK"
    POUR_CHOCOLATE = "POUR_CHOCOLATE"


COFFEE_MENU = {
    CoffeeBeverage.BLACK_COFFEE: (
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
    ),
    CoffeeBeverage.CAPUCINO: (
        CoffeeStep.POUR_MILK,
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
    ),
    CoffeeBeverage.FLAT_WHITE: (
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
        CoffeeStep.POUR_MILK,
    ),
    CoffeeBeverage.HOT_CHOCOLATE: (
        CoffeeStep.POUR_CHOCOLATE,
        CoffeeStep.POUR_MILK,
    ),
    CoffeeBeverage.MOCHA: (
        CoffeeStep.POUR_CHOCOLATE,
        CoffeeStep.GRIND_COFFEE,
        CoffeeStep.POUR_WATER,
        CoffeeStep.POUR_MILK,
    ),
}
