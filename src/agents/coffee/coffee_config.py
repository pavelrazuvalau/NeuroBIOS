from agents.coffee.coffee_constants import CoffeeFlow, CoffeeState
from agents.coffee import coffee_tools
from core.constants import SystemState


COFFEE_STATE_ACTIONS = {
    CoffeeState.GRIND_COFFEE: coffee_tools.grind_coffee,
    CoffeeState.POUR_WATER: coffee_tools.pour_water,
    CoffeeState.POUR_MILK: coffee_tools.pour_milk,
    CoffeeState.SERVE: coffee_tools.serve_drink
}

COFFEE_SYSTEM_STATE_ACTIONS = {
    SystemState.END: coffee_tools.end_flow,
    SystemState.ESCALATE: coffee_tools.escalate_flow
}

COFFEE_FLOWS = {
    CoffeeFlow.BLACK_COFFEE: (CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.SERVE),
    CoffeeFlow.CAPUCINO: (CoffeeState.POUR_MILK, CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.SERVE),
    CoffeeFlow.FLAT_WHITE: (CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.POUR_MILK, CoffeeState.SERVE)    
}
