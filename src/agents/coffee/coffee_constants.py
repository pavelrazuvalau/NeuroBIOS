from enum import Enum


class CoffeeState(str, Enum):
    GRIND_COFFEE = "GRIND_COFFEE"
    POUR_WATER = "POUR_WATER"
    POUR_MILK = "POUR_MILK"
    ANALYZE = "ANALYZE"
    SERVE = "SERVE"


class CoffeeFlow(str, Enum):
    BLACK_COFFEE = "BLACK_COFFEE"
    CAPUCINO = "CAPUCINO"
    FLAT_WHITE = "FLAT_WHITE"
