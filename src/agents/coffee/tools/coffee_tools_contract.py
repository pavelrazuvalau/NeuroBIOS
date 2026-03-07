GRIND_COFFEE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "grind_coffee",
        "description": "Grinds coffee beans before pouring water",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

POUR_WATER_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pour_water",
        "description": "Pours hot water into the cup. Requires coffee to be ground first",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

POUR_MILK_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pour_milk",
        "description": "Pours milk into the cup. Use this only if the drink recipe requires milk (like Capucino or Flat White)",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

SERVE_DRINK_SCHEMA = {
    "type": "function",
    "function": {
        "name": "serve_drink",
        "description": "Serves the prepared drink to the user. Call this tool to finish the process when all other steps are completed",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

COFFEE_TOOLS_LIST = [
    GRIND_COFFEE_SCHEMA,
    POUR_WATER_SCHEMA,
    POUR_MILK_SCHEMA,
    SERVE_DRINK_SCHEMA
]