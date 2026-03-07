from agents.coffee.coffee_constants import CoffeeFlow, CoffeeState
from agents.coffee.tools import coffee_tools_definition
from core.constants import SystemState


COFFEE_STATE_ACTIONS = {
    CoffeeState.GRIND_COFFEE: coffee_tools_definition.grind_coffee,
    CoffeeState.POUR_WATER: coffee_tools_definition.pour_water,
    CoffeeState.POUR_MILK: coffee_tools_definition.pour_milk,
    CoffeeState.ANALYZE: coffee_tools_definition.analyze_quality,
    CoffeeState.SERVE: coffee_tools_definition.serve_drink
}

COFFEE_SYSTEM_STATE_ACTIONS = {
    SystemState.END: coffee_tools_definition.end_flow,
    SystemState.ESCALATE: coffee_tools_definition.escalate_flow
}

COFFEE_FLOWS = {
    CoffeeFlow.BLACK_COFFEE: (CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.ANALYZE, CoffeeState.SERVE),
    CoffeeFlow.CAPUCINO: (CoffeeState.POUR_MILK, CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.ANALYZE, CoffeeState.SERVE),
    CoffeeFlow.FLAT_WHITE: (CoffeeState.GRIND_COFFEE, CoffeeState.POUR_WATER, CoffeeState.POUR_MILK, CoffeeState.ANALYZE, CoffeeState.SERVE)    
}
