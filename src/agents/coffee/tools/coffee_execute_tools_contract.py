GRIND_COFFEE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "grind_coffee",
        "description": "Grinds coffee beans before pouring water",
        "parameters": {
            "type": "object",
            "properties": {
                "strength": {
                    "type": "string",
                    "description": "A string describing coffee strength or how much beans should be ground for a particular beverage",
                },
            },
            "required": ["strength"],
        },
    },
}

POUR_WATER_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pour_water",
        "description": "Pours hot water into the cup. Requires coffee to be ground first",
        "parameters": {
            "type": "object",
            "properties": {
                "volume": {
                    "type": "number",
                    "description": "Volume of water to be poured for the current beverage",
                },
            },
            "required": ["volume"],
        },
    },
}

POUR_MILK_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pour_milk",
        "description": "Pours milk into the cup. Use this only if the drink recipe requires milk (like Capucino or Flat White)",
        "parameters": {
            "type": "object",
            "properties": {
                "volume": {
                    "type": "number",
                    "description": "Volume of milk to be poured for the current beverage",
                },
            },
            "required": ["volume"],
        },
    },
}

POUR_CHOCOLATE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "pour_chocolate",
        "description": "Pours chocolate into the cup. Use this only if the drink recipe requires chocolate (like Hot Chocolate or Mocha)",
        "parameters": {
            "type": "object",
            "properties": {
                "volume": {
                    "type": "number",
                    "description": "Volume of chocolate to be poured for the current beverage",
                },
            },
            "required": ["volume"],
        },
    },
}

COFFEE_TOOLS_LIST = [
    GRIND_COFFEE_SCHEMA,
    POUR_WATER_SCHEMA,
    POUR_MILK_SCHEMA,
    POUR_CHOCOLATE_SCHEMA,
]
